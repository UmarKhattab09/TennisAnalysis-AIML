import cv2
import os 
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames=[]
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames


def save_video(output_video,output_video_path):
    os.makedirs(os.path.dirname(output_video_path), exist_ok=True)

    fourcc=cv2.VideoWriter_fourcc(*'MJPG')
    out= cv2.VideoWriter(output_video_path,fourcc,24,(output_video[0].shape[1],output_video[0].shape[0]))
    for frame in output_video:
        out.write(frame)
    out.release()
