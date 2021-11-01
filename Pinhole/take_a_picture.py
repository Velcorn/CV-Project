import numpy as np
import imageio
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# camera intrinsic
fx = 1066.778
fy = 1066.778
cx = 312.9869
cy = 241.3109
intrinsic_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

# transformation matrix
point_rotation = np.identity(3)
point_translation = np.array([[0.00160, -0.00181, 0.09233]])
point_pose = np.hstack([point_rotation, point_translation.T])

# 3D point
point_3D = np.loadtxt("point_3D.txt")
point_3D = point_3D[:, 0:3]
point_3D_homogeneous = np.hstack([point_3D, np.ones((point_3D.shape[0], 1))])
point_transformation = np.hstack([point_rotation, point_translation.T])

# project to 2D point
point_2D_homogeneous = np.dot(point_transformation, point_3D_homogeneous.T)
point_2D = np.dot(intrinsic_matrix, point_2D_homogeneous)

# visualization
img = imageio.imread('000001-color.png')
implot = plt.imshow(img)
plt.scatter(point_2D[0, :], point_2D[1, :], c='g', s=40)
plt.show()
