#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy,sys,os
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d 
import laspy


# In[2]:

#train_pointdata_Cloud.las is the .las file used to get pointcloud data. Its size is greater tha 25 MB and hence can't be uploaded
pc_path = '.'
pc_fn = 'train_pointdata_Cloud.las'
pcl = laspy.read(os.path.join(pc_path,pc_fn))


# In[3]:


xyz = np.vstack((pcl.x,pcl.y,pcl.z)).transpose()
xyz


# In[4]:


xyz.shape


# In[5]:


plt.plot(xyz[::1000,0],xyz[::1000,1], '.')


# In[6]:


pcl.classification


# In[7]:


print(np.unique(pc.classification))


# In[8]:


print(np.unique(pcl.classification))


# In[9]:


pcl.xyz[pcl.classification==0]


# In[10]:


pcl.xyz[pcl.claasification==0].shape


# In[11]:


pcl.intensity


# In[12]:


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
print('pcd:',pcd)


# In[ ]:


o3d.visualization.draw_geometries([pcd])


# In[ ]:


pcd.estimate_normals(
    o3d.geometry.KDTreeSearchParamHybrid(radius = 1, max_nn = 12)) 
pcd.orient_normals_to_align_with_direction([0.,0.,1.])


# In[ ]:


o3d.visualization.draw_geometries([pcd])


# In[ ]:


pcd_ln = pcd.voxel_down_sample(voxel_size = 1)
print('pcd_ln : ' pcd_ln)


# In[ ]:


o3d.visualization.draw_geometries([pcd_ln])


# 
