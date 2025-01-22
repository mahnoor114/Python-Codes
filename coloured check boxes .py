#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
from IPython.display import display
img = Image.open("C:/Users/hp/Downloads/test.jpg")
# img = Image.open('test.jpg')
display(img)
img_array_white = np.array(img)
img_array_black = np.array(img)
for i in range (0,548):
    for j in range (0,549):
        if(list(img_array_white[i][j])==[0,0,0]):
            img_array_white[i][j]=[255,255,0]
img_white_yellow = Image.fromarray(img_array_white)
display(img_white_yellow)
print(img_array_black)

img_black_yellow = Image.fromarray(img_array_black)
display(img_black_yellow)


# In[ ]:




