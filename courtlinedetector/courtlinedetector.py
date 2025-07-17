# import torch
# import torchvision
# import cv2
# import torchvision.models as models

# class CourtLineDetector:
#     def __init__(self,model_path):
#         self.model = models.resnet50(pretrained=False)
#         self.model.fc=torch.nn.Linear(self.model.fc.in_features,14*2)
#         self.model.load_state_dict(torch.load(model_path,map_location='cpu'))

#         self.transform=

#     def predict(self,image):
#         image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#         image_tensor=self.transform(image_rgb).unsqueeze(0) #Unsqueeze: Makes it a list
#         with torch.no_grad():
#             outputs=self.model(image_tensor)

#         keypoints = outputs.squeeze().cpu.numpy()
#         original_h = original_w = image_rgb.shape[:2]
    
#         keypoints[::2]*=original_w/244.0
#         keypoints[1::2]*=original_h/244.0

#         return keypoints
    

#     def draw_keypoints(self,image,keypoints):
#         for i in range 

