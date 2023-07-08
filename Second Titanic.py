#!/usr/bin/env python
# coding: utf-8

# In[5]:


## 1. Load the dataset into a panda dataframe and display the first five rows. 

import pandas as pd 
tt= pd.read_csv('C:/Users/User pc/Downloads/archive/Titanic.csv')


# In[9]:


tt.head(5)


# In[13]:


## 2. Calculate and print the basic statistics (mean, median, standard deviation)  for numerical columns such as age and fare 


tt[['PassengerId', 'Name', 'Age', 'Fare']].head()


# In[29]:


Age_mean= tt.Age.mean() 


# In[31]:


Age_mean


# In[26]:


Fare_Mean=tt.Fare.mean()


# In[27]:


Fare_Mean


# In[32]:


Age_Std= tt.Age.std


# In[34]:


Age_Std()


# In[35]:


Fare_Std= tt.Fare.std


# In[37]:


Fare_Std()


# In[38]:


Age_Median= tt.Age.median


# In[40]:


Age_Median()


# In[41]:


Fare_Median = tt.Fare.median


# In[43]:


Fare_Median()


# In[45]:


### Option TWO for basic statistics using describe

Basic_stat= tt.describe()


# In[50]:


#### I am going to exclude other columns aside age and fare

interested_columns = tt[['Age', 'Fare']]


# In[54]:


Basic_Stat= interested_columns.describe()


# In[95]:


#### HOW MANY PASSENGERS SURVIVED THE TITANIC DISASTER 

People_survive= tt[tt.Survived == 1]


# In[99]:


x= People_survive.Survived.count()
x


# In[83]:


###percentage of survived
total_ppl= tt.Survived.count()


# In[84]:


total_ppl


# In[100]:


percentage_survived = (x/total_ppl)*100


# In[101]:


percentage_survived


# In[105]:


###What is the average of pasengers on board ?

Average_age = tt.Age.sum()/tt.Age.count()


# In[106]:


Average_age


# In[108]:


###. How many passengers travelled in each passenger class "pclass"

tt

tt.Pclass.value_counts()


# In[125]:



##### What is the survival rate for male and female passengers separately? Print the survival rate for each
##gender.

tt

no_male= tt[tt.Sex == 'male']

count_male= no_male.Sex.count()
count_male


# In[126]:


male_survival_rate = (x/count_male)* 100


# In[130]:


male_survival_rate 


# In[128]:


## Female survival rate 

no_female= tt[tt.Sex == 'female']

count_female= no_female.Sex.count()
count_female


# In[131]:


female_survival_rate = (x/count_female)*100
female_survival_rate


# In[155]:


tt.isnull().sum()


# In[166]:



##Drop Parch as an empty column.

tt.drop('Parch', axis =1)


# In[168]:


### Create an histogram showijng distribution of age.

import matplotlib.pyplot as plt


# In[175]:


tt.Age.plot(kind = 'hist')

plt.title('Distribution of Age')
plt.xlabel('Age')


# In[179]:


###use bar  chart to present the survial count for each pclass

tt

grp= tt[[ 'Survived', 'Pclass']]


# In[185]:


grp.groupby('Pclass').count().plot(kind = 'bar')


# In[189]:


tt.Sex.value_counts().plot(kind='pie')


# In[ ]:




