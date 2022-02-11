#importing necessary liberaries for analysis :) 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#load dataset
df=pd.read_csv('tmdb-movies.csv')


#check that dataset is loaded and show columns of datasest :)
df.head(2)

# know the dimensions of our dataset
df.shape

# check if there are columns have a Null valuse of not 
df.info()

# we need to determine the object columns which will be string data types :( 
df.dtypes[df.dtypes=='object']


def obj_type(colname):
    return type(df[colname][0])

# verify that all object types are string 
obj_type('imdb_id')

#check that function work correctly :)
if type(df['imdb_id'][0])==obj_type('imdb_id'):
    print("yeeees! function works well :) ")

obj_type('original_title')

obj_type('cast')

obj_type('release_date')

#check duplicated rows
df.duplicated().sum()

# get the duplicated row
df[df.duplicated()]

# drop duplicate row :)
df.drop_duplicates(inplace=True)

# check again for duplicates
if not df.duplicated().sum():
    print("Awesome, there are no duplicates :)")

#chek for null values 
df.isnull().sum()

#drop all null values :)
df.dropna(inplace =True)

# check again for nulls 
df.isnull().sum()


print("Awesome, there are no nulls :)")

# look at some useful statistice about dataset to prepare some good questions :) 
df.describe()

# show relationships in data using plots to imagine first impresion about it
pd.plotting.scatter_matrix(df,figsize=(18,12))
plt.show()

# histograms for more details
df.hist(figsize=(17,13));

# after filtering dataset by genres i sort the value descending and get first 5
df[df['revenue']!=0].groupby('genres')['revenue'].sum().sort_values(ascending=False).head(5).plot(kind='pie',figsize=(12,10),autopct='%1.0f%%')
plt.title("generes VS revenue",fontsize=30)
plt.ylabel(' ');

# after filtering dataset by runtime i sort them descending and get first 10 to know best run time :) 
df[df['revenue']!=0].groupby('runtime')['revenue'].sum().sort_values(ascending=False).head(10).plot(kind='bar',figsize=(12,10)).set_yscale('log')
plt.title("Runtime VS Revenue",fontsize=25)
plt.xlabel('runtime',fontsize=20)
plt.ylabel('revenue',fontsize=20);

#pie chart for top five 
df[df['revenue']>0].groupby('production_companies')['revenue'].sum().sort_values(ascending=False).head(5).plot(kind='pie',figsize=(12,10),autopct='%1.0f%%')
plt.title('Top 5 production Companies')
plt.ylabel(' ');

this pie chart shows that best companies to follow thier steps  :)

# bar chart for top five
df[df['revenue']>0].groupby('production_companies')['revenue'].sum().sort_values(ascending=False).head(5).plot(kind='bar',figsize=(12,10))
plt.title('Top 5 production Companies',fontsize=20)
plt.xlabel('Production Companies',fontsize=15)
plt.ylabel('revenue',fontsize=15);

# to help us know about the runtime of movies and correct range 
plt.scatter(df['vote_average'],df['runtime'])
plt.title('Vote_average VS Runtime',fontsize=20)
plt.xlabel('vote_average',fontsize=15)
plt.ylabel('runtime',fontsize=15);

f100 = df.sort_values(by='popularity', ascending=False).head(100)
f100cast = pd.Series(f100['cast'].str.cat(sep='|').split('|'))
frequent_cast_in_f100cast = f100cast.value_counts(ascending=False).head(10)
frequent_cast_in_f100cast.plot(kind='bar', figsize=(12, 6))
plt.title('Top popular actors',fontsize=20)
plt.xlabel('actor name',fontsize=15)
plt.ylabel('popularity',fontsize=15);

#need to verify that the popular movies get good revenue and what is the relationship between them
plt.scatter(df['revenue'],df['popularity'])
plt.title('Revenue VS Popularity',fontsize=20)
plt.xlabel('revenue',fontsize=15)
plt.ylabel('popularity',fontsize=15);

#if i invieste more in production of movie can it increase revenue ?
plt.scatter(df['revenue'],df['budget'])
plt.title("Revenue VS Budget",fontsize=20)
plt.xlabel('revenue',fontsize=15)
plt.ylabel('budget',fontsize=15)
plt.show;

#knowing the highs year in movies numbers to analyze it
df.groupby('release_year')['original_title'].count().plot(kind='bar',figsize=(17,14))
plt.title('Movies per year',fontsize=26)
plt.xlabel('Number of movies',fontsize=20)
plt.ylabel('Year of release',fontsize=20);

# arrange them to know the most year in production movies
df.groupby('release_year')['original_title'].count().sort_values(ascending=False).plot(kind='bar',figsize=(17,14))
plt.title('Movies per year',fontsize=26)
plt.xlabel('Number of movies',fontsize=20)
plt.ylabel('Year of release',fontsize=20);

#
df[df['release_year']==2011].groupby('genres')['revenue'].count().sort_values(ascending=False).head(10).plot(kind='bar',figsize=(17,14))
plt.title('Sort Movies genres with high revenue in 2011 ',fontsize=25)
plt.xlabel('Genres',fontsize=20)
plt.ylabel('Revenue',fontsize=20);

# determine the best months for choose the date of release :)
df['release_date']=pd.to_datetime(df['release_date'])
months=df['release_date'].dt.month

# show graph to know the best two months 
df.groupby(months)['revenue_adj'].sum().plot(kind='bar',figsize=(13,10))
plt.title('Month released VS Revenue ',fontsize=20)
plt.xlabel('Months',fontsize=15)
plt.ylabel('Revenue',fontsize=15);