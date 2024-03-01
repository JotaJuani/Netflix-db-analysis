#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import seaborn as sns


# In[4]:


df = r"C:\Users\juani\OneDrive\Desktop\power\netflixproject\Netflix_dataset.csv"


# In[5]:


df = pd.read_csv(df)
df


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.shape


# In[9]:


df.size


# In[10]:


df.columns


# In[11]:


df.dtypes


# In[12]:


df['DATE'] = pd.to_datetime(df['Release_Date'])
df.dtypes


# In[13]:


df.info()


# In[ ]:





# In[14]:


df


# In[15]:


df[df.duplicated()]


# In[16]:


df.drop_duplicates(inplace=True)


# In[17]:


df.isnull().sum()


# In[18]:


sns.heatmap(df.isnull())


# In[19]:


df[df['Title'].isin(['Peaky Blinders'])]


# In[20]:


#en que año se lanzaron mas peliculas o shows? 

df['DATE'].dt.year.value_counts()


# In[21]:


df['DATE'].dt.year.value_counts().plot(kind='bar')


# In[22]:


df.groupby('Category').Category.count()


# In[23]:


sns.countplot(df['Category'])


# In[24]:


df['Year'] = df['DATE'].dt.year


# In[25]:


df[(df['Category'] == 'Movie') & (df['Year'] == 2020)]


# In[26]:


df[(df['Category'] == 'Movie') & (df['Country'] == 'Argentina')]


# In[27]:


df[(df['Category'] == 'TV Show') & (df['Country'] == 'Argentina')]


# In[28]:


##directores
df['Director'].value_counts().head(10)


# In[29]:


df.head(1)


# In[30]:


df[(df['Category'] == 'Movie') & (df['Type'] == 'Comedies')]


# In[31]:


df[(df['Category'] == 'Movie') & (df['Type'] == 'Comedies') & (df['Country'] == 'United States')]


# In[32]:


df[df['Cast'] == ('Guillermo Francella')]


# In[33]:


data = df.dropna()


# In[34]:


data


# In[35]:


data[data['Cast'].str.contains('Guillermo Francella')]


# In[36]:


#Cuantos tipos de ranking hay?
data['Rating'].unique()


# In[37]:


#cuantas peliculas obtuvieron el rating 'TV-PG' en United Kingdom
data[(data["Rating"] == 'TV-PG') & (data["Category"] == 'Movie') & (data["Country"] == 'United Kingdom')].shape


# In[38]:


# cuantas peliculas obtiveron el rating 'r' despues de 2017 ? 
data[(data["Rating"] == 'R') & (data["Category"] == 'Movie') & (data["Year"] > 2017)].shape


# In[39]:


#que programa duro mas? 
data['Duration'].unique().max()


# In[40]:


#que programa duro mas? 
data['Duration'].dtypes


# In[41]:


data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand = True)
data


# In[42]:


#que programa duro mas? 
data['Minutes'].max()


# In[43]:


#que pais tiene el mayor numero de shows?
tv_shows = data[data['Category'] == 'TV Show']
tv_shows.head(2)


# In[44]:


tv_shows.Country.value_counts().head(10)


# In[45]:


data[(data['Country'] == 'United States')]


# In[46]:


#separar el df por años
data.sort_values(by='Year', ascending=False).head()


# In[48]:


#encontrar todas las peliculas que son categoria "drama"
data[(data["Category"] == 'Movie') & (data["Type"] == 'Dramas')].shape


# In[57]:


data[(data["Category"] == 'TV Show') & (data["Type"] == "Kids' TV")].shape


# In[56]:


data[(data["Category"] == 'TV Show') & (data["Type"] == "Kids' TV")].head()


# In[49]:


data[(data["Category"] == 'Movie') & (data["Type"] == 'Dramas')].head()


# In[53]:


data[(data["Category"] == 'TV Show') & (data["Type"] == "Kids' TV") | (data["Category"] == 'Movie') & (data["Type"] == 'Dramas') ].head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




