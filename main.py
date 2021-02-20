# Vk-api-shell
# Marakulin Andrey @annndruha
# 2021
# import os
#
# from shell import shell
# # from src.followers_monitor import FollowersMonitor
# from src.example import my_function
#
# if __name__ == '__main__':
#     # FM = FollowersMonitor()
#     target = my_function
#     config_path = os.path.join("secret", "config.json")
#     auth_type = "user"
#     one_run = True
#
#     shell = shell.Shell(config_path=config_path, target=target, auth_type=auth_type, one_run=one_run)
#     shell.start()
#     shell.join()


import cv2
import glob
import numpy as np

files = glob.glob("photos//*.jpg")
for file in files:
    name = file.split("\\")[1]
    img = cv2.imread(file)
    # kernel = np.ones((6,6),np.float32)/25
    dst = cv2.GaussianBlur(img,(35,35),0)

    center_coordinates = (50, 50)
    radius = 75
    color = (255, 255, 255)
    thickness = 50
    dst = cv2.circle(dst, center_coordinates, radius, color, thickness)


    cv2.imwrite(f"photos_blur//{name}", dst)

