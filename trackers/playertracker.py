from ultralytics import YOLO
import cv2
import pickle
class playerTracker:
    def __init__(self,model_path):
        self.model = YOLO(model_path)


    def detect_frames(self,frames,read_from_stub=False,stub_path=None):

        if read_from_stub and stub_path is not None:
            with open(stub_path,'rb') as f:
                player_detection = pickle.load(f)
            return player_detection



        player_detection=[]
        for frame in frames:
            playerdict = self.detect_frame(frame)
            player_detection.append(playerdict)

        if stub_path is not None:
            with open(stub_path,'wb') as f:
                pickle.dump(player_detection,f)
        return player_detection
    

        


    def detect_frame(self,frame): # Persist continues or memorize the old frames
        results= self.model.track(frame,persist=True)[0]
        id_names_dict = results.names

        player_dict={}
        for box in results.boxes:
            track_id = int(box.id.tolist()[0])
            result = box.xyxy.tolist()[0]
            object_cls_id=box.cls.tolist()[0]
            object_cls_name = id_names_dict[object_cls_id]
            if object_cls_name=="person":
                player_dict[track_id]=result
        
        return player_dict
    
    def draw_boxes(self,video_frames,player_detections):
        output_video_frames = []
        for frame,player_dict in zip(video_frames,player_detections):
            #Draw Boxes
            for track_id,bbox in player_dict.items():
                x1,y1,x2,y2=bbox
                cv2.putText(frame,f"Player ID:{track_id}",(int(bbox[0]),int(bbox[1] -10)),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
                frame = cv2.rectangle(frame,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),2)
            output_video_frames.append(frame)
        return output_video_frames