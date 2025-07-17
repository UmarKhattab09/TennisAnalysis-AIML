


# import numpy as np
# import cv2
# import sys
# def MiniCourt():
#     def __init__(self,frame):
#         self.draw_rectangle_width= 250
#         self.draw_rectangle_height = 450
#         self.buffer=50
#         self.padding_court=20

#         self.boxposition(frame)
#         self.set_mini_position()


#     def boxposition(self,frame):
#         frame = frame.copy()
#         self.end_x = frame.shape[1] - self.buffer
#         self.end_y = self.draw_rectangle_height + self.buffer
#         self.start_x = self.end_x - self.drawing_rectangle_width
#         self.start_y = self.end_y - self.drawing_rectangle_height

#     def set_court_lines(self):
#         self.lines = [
#             (0, 2),
#             (4, 5),
#             (6,7),
#             (1,3),
            
#             (0,1),
#             (8,9),
#             (10,11),
#             (10,11),
#             (2,3)

#         ]

#     def set_mini_position(self):
#         self.court_start_x = self.start_x + self.padding_court
#         self.court_start_y = self.start_y + self.padding_court
#         self.court_end_x = self.end_x - self.padding_court
#         self.court_end_y = self.end_y - self.padding_court
#         self.court_drawing_width = self.court_end_x - self.court_start_y


#     def draw_court(self,frame):
#         shape = np.zeros_like(frame,np.unint8)
        

