
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
year = [2009, 2012, 2015, 2016, 2017, 2019] #year variable feeded with x-axis yearwise data
world_pop = [2, 5.1, 5.5, 6.1, 6.9, 8] #World population variable feeded with y-axis population segmented data

plt.plot(year, world_pop, color='purple') #Chart plotting with x-axis, y-axis and other fancy attributes

plt.xlabel('Year', color='Green', fontsize = '14') #Naming x-label
plt.ylabel('Population (in billion)', color = 'Green', fontsize = '14') #Naming y-label

plt.title('World Population Growth', color='Blue') #Naming Title

plt.yticks([0,2,4,6,8,10], ['0', '2B', '4B', '6B', '8B', '10B' ]) #Y-scale enhancement
plt.xticks([2009, 2011, 2013, 2015, 2017, 2019]) #x-scale enhancement

plt.show() #displays the chart
