import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 

np.set_printoptions(suppress=True)

# Object points in 3D
GRID_SHAPE = (7,7)
objp = np.zeros((GRID_SHAPE[0]*GRID_SHAPE[1],3), np.float32)
objp[:,:2] = np.mgrid[0:GRID_SHAPE[0], 0:GRID_SHAPE[1]].T.reshape(-1,2)
objp *= 20 # One square on my grid has 20mm

FOLDER = "calib_images/left/"
fnames = os.listdir(FOLDER)
obj_pts = []
img_pts = []


for fname in fnames:
    print(f"processing {fname}")
    img = Image.open(FOLDER+fname)
    arr = np.array(img)
    
    flags = cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_FAST_CHECK
    ret, corners = cv2.findChessboardCorners(arr, GRID_SHAPE, flags)
    
    arr_vis = cv2.drawChessboardCorners(arr, GRID_SHAPE, corners, ret)
    #plt.imshow(arr_vis, cmap='gray')
    #plt.show()
    print("RET", ret)
    print("CORNERS", corners)


    if ret:
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        corners_subpix = cv2.cornerSubPix(arr,corners,(11,11),(-1,-1),criteria)
        obj_pts.append(objp)
        img_pts.append(corners_subpix)

# get calibration params
ret, K_l, dist_coeff_l, rvecs, tvecs = cv2.calibrateCamera(obj_pts, img_pts, (arr.shape[1], arr.shape[0]), None,None)

img = Image.open(FOLDER+"001.png")
arr = np.array(img)

arr_corr = cv2.undistort(arr, K_l, dist_coeff_l, None, K_l)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
ax1.imshow(arr, cmap='gray')
ax2.imshow(arr_corr, cmap='gray')
plt.show()

## Repeat for the right images

FOLDER = "calib_images/right/"
fnames = os.listdir(FOLDER)
obj_pts = []
img_pts = []


for fname in fnames:
    print(f"processing {fname}")
    img = Image.open(FOLDER+fname)
    arr = np.array(img)
    
    flags = cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_FAST_CHECK
    ret, corners = cv2.findChessboardCorners(arr, GRID_SHAPE, flags)
    
    arr_vis = cv2.drawChessboardCorners(arr, GRID_SHAPE, corners, ret)
    #plt.imshow(arr_vis, cmap='gray')
    #plt.show()

    if ret:
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        corners_subpix = cv2.cornerSubPix(arr,corners,(11,11),(-1,-1),criteria)
        obj_pts.append(objp)
        img_pts.append(corners_subpix)

ret, K_r, dist_coeff_r, rvecs, tvecs = cv2.calibrateCamera(obj_pts, img_pts, (arr.shape[1], arr.shape[0]), None, None)

## Save params
np.save("K_l.npy", K_l)
np.save("K_r.npy", K_r)

np.save("dist_coeff_l.npy", dist_coeff_l)
np.save("dist_coeff_r.npy", dist_coeff_r)
