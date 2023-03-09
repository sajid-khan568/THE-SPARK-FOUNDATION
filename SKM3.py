#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Author-Sajid khan 

The Sparks Foundation - Data Science & Business Analytics Internship

TASK 3: Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’

In this task we will try to find out the weak areas where we can work to make more profit.

Steps to be followed:

1.) Importing the libraries

2.) Reading the dataset

3.) Data Preprocessing

4.) EDA

5.) Data Visualization

-----------------------
IMPORT LIBRARIES


# In[2]:


# In this step we will import the required libarries 
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')

# To ignore the warnings 
import warnings as wg
wg.filterwarnings("ignore")


# In[ ]:


*Reading the dataset*


# In[3]:


df = pd.read_csv('https://github.com/ashishverma5218/Data-Science-Projects/blob/main/Datasets/SampleSuperstore.csv?raw=true')


# In[ ]:





# In[4]:


df.head()


# In[ ]:


*data processing*


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.isnull().sum()


# In[8]:


df.info()
     


# In[9]:


df.describe()


# In[10]:


# checking for duplicate values
df.duplicated().sum()


# In[11]:


# dropping the duplicates
df.drop_duplicates()
df.head()


# In[ ]:


#removing the unnecessary columns such as postal code
df=df.drop(['Postal Code'],axis=1)


# In[25]:


df.head()


# In[ ]:


*EXPLORATORY DATA ANALYSIS*


# In[26]:


# visualizing the dataset as a whole using the pair plot
import seaborn as sns 
sns.pairplot(df)
     


# In[27]:


# finding the pairwise correlations between the columns and visualising using heatmaps
df.corr()
plt.figure(figsize=(10,5))
sns.heatmap(df.corr(), annot=True)
plt.show()


# In[28]:


plt.figure(figsize = (6,6))
textprops = {"fontsize":15}
plt.title('Category')
plt.pie(df['Category'].value_counts(), labels=df['Category'].value_counts().index,autopct='%1.1f%%',textprops = textprops)
plt.show()
     


# In[30]:


plt.figure(figsize= (10,16))
df.groupby('Category')['Profit','Sales'].agg(['sum']).plot.bar()
plt.ylabel('Profit')
plt.show()


# In[31]:


# computing top categories in terms of sales from first 100 observations
top_category_s = df.groupby("Category").Sales.sum().nlargest(n=100)
# computing top categories in terms of profit from first 100 observations
top_category_p = df.groupby("Category").Profit.sum().nlargest(n=100)

# plotting to see it visually
plt.style.use('seaborn')
top_category_s.plot(kind = 'bar',figsize = (10,5),fontsize = 14)
top_category_p.plot(kind = 'bar',figsize = (10,5),fontsize = 14,color='red')
plt.xlabel('Category',fontsize = 15)
plt.ylabel('Total Sales/Profits',fontsize = 15)
plt.title("Top Category Sales vs Profit",fontsize = 15)
plt.show()
     


# In[ ]:


*Visualising the sub categories*


# In[32]:


# computing top sub-categories in terms of sales from first 100 observations
top_subcategory_s = df.groupby("Sub-Category").Sales.sum().nlargest(n = 100)
# computing top sub-categories in terms of profit from first 100 observations
top_subcategory_p = df.groupby("Sub-Category").Profit.sum().nlargest(n = 100)

# plotting to see it visually
plt.style.use('seaborn')
top_subcategory_s.plot(kind = 'bar',figsize = (10,5),fontsize = 14)
top_subcategory_p.plot(kind = 'bar',figsize = (10,5),fontsize = 14, color = 'red')
plt.xlabel('Sub-Category',fontsize = 15)
plt.ylabel('Total Sales/Profits',fontsize = 15)
plt.title("Top Sub-Category Sales vs Profit",fontsize = 15)
plt.show()


# In[33]:


# A more detailed view
plt.figure(figsize=(14,12))
statewise = df.groupby(['Sub-Category'])['Profit'].sum().nlargest(50)
statewise.plot.barh() # h for horizontal
     


# In[ ]:


The above graph clearly shows that Copiers and Phones have the highest sales and profit and tables has negative profit

Visualising the discount


# In[34]:


plt.figure(figsize=(8,7))
sns.lineplot(df['Discount'], df['Profit'], data=df)


# In[35]:


plt.figure(figsize = (6,6))
plt.title('Region')
plt.pie(df['Region'].value_counts(), labels=df['Region'].value_counts().index,autopct='%1.1f%%')
plt.show()


# In[ ]:


from locale import D_T_FMT
# computing top states in terms of sales from first 10 observations
top_states_s = df.groupby("State").Sales.sum().nlargest(n=10)

# computing top states in terms of profit from first 10 observations
top_states_p = df.groupby("State").Profit.sum().nlargest(n = 10)

plt.style.use('seaborn')
top_states_s.plot(kind = 'bar',figsize = (10,5),fontsize = 14)
top_states_p.plot(kind = 'bar',figsize = (10,5),fontsize = 14, color = 'red')
plt.xlabel('States',fontsize = 15)
plt.ylabel('Total sales',fontsize = 15)
plt.title("Top 10 states Sales vs Profit",fontsize = 15)
plt.show()


# In[ ]:


*Visualizing the Sales vs Profits in different Regions*


# In[37]:


plt.style.use('seaborn')
df.plot(kind = "scatter",figsize = (10,5), x = "Sales", y= "Profit", c = "Discount", s = 20,fontsize = 16, colormap = "viridis")
plt.ylabel('Total Profits',fontsize = 16)
plt.title("Interdependency of Sales,Profits and Discounts",fontsize = 16)

plt.show()

     


# In[ ]:


The graph clearly shows that if we give more Discount on our products sales increases but profit decreases.

*Conclusion :*

1.The weak areas where one can work to make more profit are :

2. We should limit sales of furniture and increase that of technology and office suppliers as
furniture has very less profit as compared to sales.

3.Considering the sub-categories sales of tables should be minimized.

4.Increase sales more in the east as profit is more.

5.We should concentrate on the states like 'New York' and 'California' to make more profits.

