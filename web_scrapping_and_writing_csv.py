#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[1]:


from bs4 import BeautifulSoup
import requests 


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

page = requests.get(url)

soup = BeautifulSoup (page.text, 'html')


# In[3]:


print (soup)


# In[4]:


soup.find ('table')


# In[5]:


soup.find_all('table')


# In[7]:


soup.find('table', class_= 'wikitable sortable sticky-header static-row-numbers')


# In[30]:


table = soup.find_all('table')[2]


# In[31]:


print (table)


# In[32]:


soup.find_all ('th')


# In[33]:


world_titles = table.find_all ('th')


# In[34]:


world_titles


# In[35]:


world_table_title = [title.text.strip() for title in world_titles]

print (world_table_title)


# In[36]:


import pandas as pd


# In[61]:


df1 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[62]:


df1


# In[74]:


df2 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[94]:


df3 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[99]:


df4 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[100]:


df5 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[101]:


df6 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[102]:


df7 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[103]:


df8 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[104]:


df9 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[ ]:


df10 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[ ]:


df11 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[ ]:


df12 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[ ]:


df13 = pd.DataFrame (columns = ['country/territory', 'un_region', 'imf_forecast', 'imf_year', 'wb_estimate', 'wb_year', 'un_estimate', 'un_year'])


# In[40]:


column_data = table.find_all ('tr')


# In[60]:


for row in column_data [2:24]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print (individual_row_data)
    #length = len (df)
    #df.loc[length] = individual_row_data
    


# In[63]:


for row in column_data [2:24]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len (df1)
    df1.loc[length] = individual_row_data


# In[64]:


df1


# In[67]:


for row in column_data:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print (individual_row_data)
    #length = len (df1)
    #df1.loc[length] = individual_row_data


# In[70]:


df1.loc[22] =['Taiwan', 'Asia', '751,930', '2023', '—', '—', '-', '-']


# In[71]:


df1


# In[87]:


df1 = df1.drop(-1)


# In[79]:


for row in column_data[25:65]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df2)
    df2.loc[length] = individual_row_data


# In[80]:


df2


# In[84]:


df2.duplicated()


# In[88]:


df1.duplicated ()


# In[85]:


df2[df2 ["country/territory"].duplicated() == 1]


# In[89]:


df2 = df2.drop_duplicates()


# In[90]:


df2.duplicated ()


# In[91]:


df2.loc[40] =['Cuba', 'Americas', '—', '-','633,442', '2022', '126,694', '2021']


# In[92]:


df2


# In[95]:


for row in column_data[66:74]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df3)
    df3.loc[length] = individual_row_data


# In[96]:


df3


# In[105]:


for row in column_data[75:80]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df4)
    df4.loc[length] = individual_row_data


# In[107]:


for row in column_data[81:89]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df5)
    df5.loc[length] = individual_row_data


# In[109]:


for row in column_data[90:105]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df6)
    df6.loc[length] = individual_row_data


# In[111]:


for row in column_data[106:125]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df7)
    df7.loc[length] = individual_row_data


# In[113]:


for row in column_data[126:130]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df8)
    df8.loc[length] = individual_row_data


# In[115]:


for row in column_data[131:137]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print (individual_row_data)
    length = len (df9)
    df9.loc[length] = individual_row_data


# In[119]:


df_final = pd.concat ([df1, df2, df3, df4, df5, df6, df7, df8, df9])


# In[121]:


df_final.reset_index()


# In[122]:


df_final.to_csv(r'/Users/juven/Desktop/Skills/python_tutorial/jupyter/countries_gdp.csv', index = False)


# In[ ]:




