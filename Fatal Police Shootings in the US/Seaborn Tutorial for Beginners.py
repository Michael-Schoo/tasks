# https://www.kaggle.com/code/kanncaa1/seaborn-tutorial-for-beginners/data
# https://www.kaggle.com/code/kanncaa1/seaborn-tutorial-for-beginners/notebook

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
# %matplotlib inline
# Input data files are available in the "../archive/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import warnings
warnings.filterwarnings('ignore') 

# from subprocess import check_output
# print(check_output(["ls", "../archive"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

# Read datas
median_house_hold_in_come = pd.read_csv(
    './archive/MedianHouseholdIncome2015.csv', encoding="windows-1252")
percentage_people_below_poverty_level = pd.read_csv(
    './archive/PercentagePeopleBelowPovertyLevel.csv', encoding="windows-1252")
percent_over_25_completed_highSchool = pd.read_csv(
    './archive/PercentOver25CompletedHighSchool.csv', encoding="windows-1252")
share_race_city = pd.read_csv(
    './archive/ShareRaceByCity.csv', encoding="windows-1252")
kill = pd.read_csv('./archive/PoliceKillingsUS.csv', encoding="windows-1252")

print("percentage_people_below_poverty_level.head(): ")
print(percentage_people_below_poverty_level.head())
print()

print("percentage_people_below_poverty_level.info(): ")
print(percentage_people_below_poverty_level.info())
print()


print("percentage_people_below_poverty_level['Geographic Area'].unique():")
print(percentage_people_below_poverty_level['Geographic Area'].unique())
print()

# Poverty rate of each state
percentage_people_below_poverty_level.poverty_rate.replace(['-'],0.0,inplace = True)
percentage_people_below_poverty_level.poverty_rate = percentage_people_below_poverty_level.poverty_rate.astype(float)
area_list = list(percentage_people_below_poverty_level['Geographic Area'].unique())
area_poverty_ratio = []
for i in area_list:
    x = percentage_people_below_poverty_level[percentage_people_below_poverty_level['Geographic Area']==i]
    area_poverty_rate = sum(x.poverty_rate)/len(x)
    area_poverty_ratio.append(area_poverty_rate)
data = pd.DataFrame({'area_list': area_list,'area_poverty_ratio':area_poverty_ratio})
new_index = (data['area_poverty_ratio'].sort_values(ascending=False)).index.values
sorted_data = data.reindex(new_index)

# visualization
plt.figure(figsize=(15,10))
sns.barplot(x=sorted_data['area_list'], y=sorted_data['area_poverty_ratio'])
plt.xticks(rotation= 45)
plt.xlabel('States')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate Given States')
print("Bar Plot (shown in external window)\n")
plt.show()

print("kill.head(): ")
print(kill.head())
print()

print("kill.name.value_counts():")
print(kill.name.value_counts())
print()


# Most common 15 Name or Surname of killed people
separate = kill.name[kill.name != 'TK TK'].str.split()
a, b = zip(*separate)
name_list = a+b
name_count = Counter(name_list)
most_common_names = name_count.most_common(15)
x, y = zip(*most_common_names)
x, y = list(x), list(y)
#
plt.figure(figsize=(15, 10))
ax = sns.barplot(x=x, y=y, palette=sns.cubehelix_palette(len(x)))
plt.xlabel('Name or Surname of killed people')
plt.ylabel('Frequency')
plt.title('Most common 15 Name or Surname of killed people')
print("Most common 15 Name or Surname of killed people (shown in external window)\n")
plt.show()


print("percent_over_25_completed_highSchool.head():")
print(percent_over_25_completed_highSchool.head())
print()


print("percent_over_25_completed_highSchool.info():")
print(percent_over_25_completed_highSchool.info())
print()


print("percent_over_25_completed_highSchool.percent_completed_hs.value_counts():")
print(percent_over_25_completed_highSchool.percent_completed_hs.value_counts())
print()


# High school graduation rate of the population that is older than 25 in states
percent_over_25_completed_highSchool.percent_completed_hs.replace(['-'],0.0,inplace = True)
percent_over_25_completed_highSchool.percent_completed_hs = percent_over_25_completed_highSchool.percent_completed_hs.astype(float)
area_list = list(percent_over_25_completed_highSchool['Geographic Area'].unique())
area_highschool = []
for i in area_list:
    x = percent_over_25_completed_highSchool[percent_over_25_completed_highSchool['Geographic Area']==i]
    area_highschool_rate = sum(x.percent_completed_hs)/len(x)
    area_highschool.append(area_highschool_rate)
# sorting
data = pd.DataFrame({'area_list': area_list,'area_highschool_ratio':area_highschool})
new_index = (data['area_highschool_ratio'].sort_values(ascending=True)).index.values
sorted_data2 = data.reindex(new_index)
# visualization
plt.figure(figsize=(15,10))
sns.barplot(x=sorted_data2['area_list'], y=sorted_data2['area_highschool_ratio'])
plt.xticks(rotation= 90)
plt.xlabel('States')
plt.ylabel('High School Graduate Rate')
plt.title("Percentage of Given State's Population Above 25 that Has Graduated High School")
print("Percentage of Given State's Population Above 25 that Has Graduated High School (shown in external window)\n")
plt.show()


print("share_race_city.head():")
print(share_race_city.head())
print()


thing = []
aaa = [a for a in thing if a["author"] == "author"][0]