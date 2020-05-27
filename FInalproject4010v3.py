#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcdefaults()
fig, ax = plt.subplots()


stats = ('Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma')

#below is the code responsible for new character creation, or loading a preexisiting character done mainly by conditionals
initialmenu=int(input("would you like to make a new character?(1)\n would you like to load a character? (2)"))

if initialmenu == 1:
 stat1=int(input ("enter your characters hp stat "))
 stat2=int(input("enter your characters dexterity stat "))
 stat3=int(input("enter your characters constitution stat "))
 stat4=int(input("enter you characters intelligence stat "))
 stat5=int(input("enter your characters Wisdom stat "))
 stat6=int(input("enter your characters charisma statistic "))

#grouping all stat inputs to a variable to make final csv save easier
statgrouping=([stat1, stat2, stat3, stat4, stat5, stat6])

#graph portion
plt.bar(stats, statgrouping)
plt.xlabel('dnd stats')
plt.ylabel('stat weight')
plt.title('DnD Character Vizualizer')
plt.show()

finalprompt= int(input("would you like to exit? (1)\nwould you like to save? (2)"))
if finalprompt==1:
   exit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




