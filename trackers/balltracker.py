from ultralytics import YOLO
import cv2
import pickle
class BallTracker:
    def __init__(self,model_path):
        self.model = YOLO(model_path)


    def detect_frames(self,frames,read_from_stub=False,stub_path=None):

        if read_from_stub and stub_path is not None:
            with open(stub_path,'rb') as f:
                ball_detection = pickle.load(f)
            return ball_detection



        ball_detection=[]
        for frame in frames:
            balldict = self.detect_frame(frame)
            ball_detection.append(balldict)

        if stub_path is not None:
            with open(stub_path,'wb') as f:
                pickle.dump(ball_detection,f)
        return ball_detection
    

        


    def detect_frame(self,frame): # Persist continues or memorize the old frames
        results= self.model.predict(frame,conf=0.15)[0] #Persist is for Tracking


        ball_dict={}
        for box in results.boxes:
 
            result = box.xyxy.tolist()[0]
            ball_dict[1]=result

        return ball_dict
    
    def draw_boxes(self,video_frames,balldetection):
        output_video_frames = []
        for frame,ball_dict in zip(video_frames,balldetection):
            #Draw Boxes
            for track_id,bbox in ball_dict.items():
                x1,y1,x2,y2=bbox
                cv2.putText(frame,f"Ball ID:{track_id}",(int(bbox[0]),int(bbox[1] -10)),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
                frame = cv2.rectangle(frame,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),2)
            output_video_frames.append(frame)
        return output_video_frames