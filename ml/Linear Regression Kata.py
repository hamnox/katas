
# coding: utf-8

# In[1]:

# err couldn't do this in katas folder because graphlab localized
import graphlab

graphlab.canvas.set_target('ipynb')


# In[2]:

# err had to go back to look at mtgox
mtgox_data = graphlab.SFrame('mtgox usd-btc exchange.csv')


# In[4]:

mtgox_data.head()


# In[11]:

mtgox_data['Date', 'Weighted Price'].show(view='Scatter Plot')
# err couldn't remember view=
# err misspelled Scatter Plot
# err date is a string, can't scatter plot
# err couldn't remember how to format datetime
# err timer went off


# In[ ]:




# In[ ]:




# In[ ]:



