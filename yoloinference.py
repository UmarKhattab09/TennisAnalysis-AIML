from ultralytics import YOLO

"""
model = YOLO('yolov8x')
result=model.predict('inputvideos/input_video.mp4',save=True, project='detection')
print(result)
"""
"""
model = YOLO('models/best.pt')
result=model.predict('inputvideos/input_video.mp4',save=True, project='detection')
"""
"""
model = YOLO('models/last.pt')
result=model.predict('inputvideos/input_video.mp4',conf=0.2,save=True, project='detection')
"""
"""
model = YOLO('yolov8x')
result=model.track('inputvideos/input_video.mp4',conf=0.2,save=True, project='detection')
print(result)
"""


model = YOLO('yolov8x')
result=model.predict('inputvideos/image.png',conf=0.2,save=True, project='detection')[0]

print("-----------------------------------")
for box in result:

    print(box.boxes)
    print("_________________________________")
    print(box.track_id)

