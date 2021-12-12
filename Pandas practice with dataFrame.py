#!/usr/bin/env python
# coding: utf-8

# # Imprting Pandas

# In[1]:


import pandas as pd


# # Loading the data

# In[2]:


df = pd.read_csv('pokemon_data.csv')


# # Checking the data

# In[3]:


df.info


# In[4]:


df.describe()


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df['Name'].head()


# # Reading Data

# ### 1. Reading Headers

# In[8]:


df.columns


# ### 2. Read each item in a column

# In[9]:


df.Name


# In[10]:


print(df['Name'])


# In[11]:


df[['Name', 'Type 1', 'Legendary']].head(15)


# In[12]:


# Gives of only one type
df.loc[df['Type 1'] == 'Fire'].head(10)


# In[13]:


# Gives of only one type
df.loc[df['Type 1'] == 'Water'].head(10)


# ### 3. Read each item in a row

# In[14]:


df.iloc[10]


# In[15]:


df.iloc[70:75]


# ### 4. Read a specific locations

# In[16]:


df.head()


# In[17]:


# To get Charmander
df.iloc[4,1]


# # Sorting

# In[18]:


# All names in alpabethical (Ascending) order
df.sort_values('Name')


# In[19]:


# All names in alpabethical (Descending) order
df.sort_values('Name', ascending=False)


# # Making Changes to Data

# In[20]:


df.head()


# # Creating new Column

# In[21]:


# Creates new column name Total
df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
df.head(10)


# # Deleting a Column

# In[22]:


df = df.drop(columns=['Total'])
df


# # Another way to add columns

# In[23]:


df['Total'] = df.iloc[:, 4:10].sum(axis=1)
df.head()


# # Saving the data 

# In[24]:


# Saves the file in CSV format and in the same folder
df.to_csv('modified_Pokemon.csv')
# But also includes the index numbers, if not needed add
# index=False [ df.to_csv('modified_Pokemon.csv', index=False) ]


# ![image.png](attachment:image.png)

# # Filtering Data

# In[25]:


df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]


# In[26]:


df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
df.head()


# # Reset Index

# In[27]:


new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP']>70)]
new_df


# In[28]:


# Notice the irregular index no.
# To change it use reset_index()
new_df = new_df.reset_index(drop=True)
new_df
# drop=True removes the existing index no's


# # Aggregrate Statistics (Groupby)

# Questions:<br>
# >1. Which Type of Pokemon has Highest / Lowest HP<br>
# >2. Which Type of Pokemon has Highest / Lowest Attack<br>
# >3. Which Type of Pokemon has Highest / Lowest Defence<br>
# >4. Which Type of Pokemon has Highest / Lowest Special Attack<br>
# >5. Which Type of Pokemon has Highest / Lowest Special Defence<br>
# >6. Which Type of Pokemon has Highest / Lowest Speed<br>
# >7. Which Type of Pokemon has Highest / Lowest Total

# In[63]:


df.head()


# # Highest / Lowest HP

# In[65]:


hp = df.groupby(['Type 1']).mean().sort_values('HP', ascending=False)
hp.head(1)
# Highest HP


# In[48]:


hp.tail(1)
# Lowest HP


# # Highest / Lowest Attack

# In[49]:


attack = df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
attack.head(1)
# Highest Attack


# In[51]:


attack.tail(1)
# Lowest Attack


# # Highest / Lowest Defense

# In[55]:


defense = df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
defense.head(1)
# Highest Defense


# In[57]:


defense.tail(1)
# Lowest Defense


# # Highest / Lowest Special Attack

# In[60]:


spl_attack = df.groupby(['Type 1']).mean().sort_values('Sp. Atk', ascending=False)
spl_attack.head(1)
# Highest Special Attack


# In[61]:


spl_attack.tail(1)
# Lowest Special Attack


# # Highest / Lowest Special Defence

# In[66]:


spl_def = df.groupby(['Type 1']).mean().sort_values('Sp. Def', ascending=False)
spl_def.head(1)
# Highest Special Defence


# In[67]:


spl_def.tail(1)
# Lowest Special Defence


# # Highest / Lowest Speed

# In[68]:


speed = df.groupby(['Type 1']).mean().sort_values('Speed', ascending=False)
speed.head(1)
# Highest Speed


# In[69]:


speed.tail(1)
# Lowest Speed


# # Highest / Lowest Total

# In[70]:


total = df.groupby(['Type 1']).mean().sort_values('Total', ascending=False)
total.head(1)
# Highest Total


# In[71]:


total.tail(1)
# Lowest Total


# # Total Pokemon Types

# In[89]:


total_pokemons = df.groupby(['Type 1']).count()
total_pokemons


# In[91]:


df

