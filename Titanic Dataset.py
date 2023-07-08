#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


### Task One : Load the dataset into a Pandas DataFrame and display the first 5 rows.

tt = pd.read_csv('C:/Users/User pc/Downloads/archive/Titanic.csv')


# In[5]:


tt

print(tt.head(5))


# In[13]:




### Task Two : Calculate and print the basic statistics (mean, median, standard deviation) for numerical columns such
## as age and fare.

statistics = tt[['Age', 'Fare']].agg(['mean', 'median', 'std'])

# Print the statistics
print("Basic Statistics for Age and Fare:")
print(statistics)


# In[15]:



##Task Three (a)

# Assuming you have already loaded the Titanic dataset into a DataFrame named 'tt'

# Count the number of passengers who survived
survived_count = tt['Survived'].sum()

# Calculate the percentage of passengers who survived
survived_percentage = (survived_count / len(tt)) * 100

# Print the count and percentage
print("Number of passengers who survived:", survived_count)
print("Percentage of passengers who survived:", survived_percentage)


# In[16]:


##Task Three (b)

## What is the average age of passengers on board? Print the result.

average_age = tt['Age'].mean()

# Print the result
print("Average age of passengers:", average_age)


# In[17]:



## Task Three (c)

##How many passengers travelled in each passenger class (Pclass)? Print the count for each class

passenger_class_count = tt['Pclass'].value_counts()

# Print the count for each class
print("Passenger Count by Class:")
print(passenger_class_count)


# In[18]:


### Task Three (d)

##What is the survival rate for male and female passengers separately? Print the survival rate for each
##gender.


survival_rate_gender = tt.groupby('Sex')['Survived'].mean()

# Print the survival rate for each gender
print("Survival Rate by Gender:")
print(survival_rate_gender)


# In[ ]:




