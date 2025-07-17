from utils import read_video,save_video
from trackers import playerTracker
from trackers import BallTracker


def main():
    input_video_path="inputvideos/input_video.mp4"
    video_frames=read_video(input_video_path)

    player_tracker = playerTracker('yolov8x')
    player_detection = player_tracker.detect_frames(video_frames,read_from_stub=True,stub_path="tracker_stubs/player_detections.pkl")
    ball_tracker = BallTracker('models/last.pt')
    ball_detection = ball_tracker.detect_frames(video_frames,read_from_stub=False,stub_path="tracker_stubs/ball_detections.pkl")



    ##DRAW BOUDNING BOX
    output_video_frames=player_tracker.draw_boxes(video_frames=video_frames,player_detections=player_detection)
    output_video_frames=ball_tracker.draw_boxes(video_frames=video_frames,balldetection=ball_detection)



    save_video(output_video_frames,"output_videos/output_video.avi")



if __name__=="__main__":
    main()