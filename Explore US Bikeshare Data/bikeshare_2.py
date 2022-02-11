#######################################
#   Name: Ibrahim Ehab Abdelmaged :)  #
#######################################


#---------------------------------------------------------------------------------------------------
# important prepartion for long time useage
# note that: I copy funcitons one by one and work on them one by one and after finishing one I copy the valid code in the 
# bikeshare_2.py  so you will find the comment that came with the project to guid my :)  :) 
#---------------------------------------------------------------------------------------------------

import pandas as pd
import time
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months=['January','February','March','April','May','June','All']
days=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All']
#---------------------------------------------------------------------------------------------------

"""
First Funciton:
input: get inputs about city, month, day to filter the given datasets :)
output: return the values of city, month, day after getting the only correct filters :)
"""

#---------------------------------------------------------------------------------------------------
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("choose name of the city to analyze (chicago, new york city, washington): ").lower()
    while city not in cities:
        print("invalid city :(")
        city=input("Please Entre valid city name to analyze: ").lower()
    # get user input for month (all, january, february, ... , june)
    month=input('Entre name of the month to filter by, or "all" to apply no month filter :').lower().title()
    while month not in months:
        print("invalid month :( Choose from ['January','February','March','April','May','June','all']")
        month=input("Please Entre valid month name to filter by or 'all' to apply no month filter :").lower().title()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Entre name of the day of week to filter by, or "all" to apply no day filter: ').lower().title()
    while day not in days:
        print("Invalid day :( Choose from ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','all']")
        day=input('Please Entre valid day name to filter by or "all" to apply no day filter :').lower().title()
    
    print('-'*40)
    return city, month, day
#---------------------------------------------------------------------------------------------------

"""
Second Function:
input: get the values or filters from first function to make a desired dataframe :)
output: return the filterd dataframe 
"""

#---------------------------------------------------------------------------------------------------
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["End Time"]=pd.to_datetime(df["End Time"])
    #if month!='All' and day!='All':
        #df["Month"]=df["Start Time"].dt.month_name()
        #df["Day"]=df["Start Time"].dt.day_name()
        #df=[(df["Day"]==day) & (df["Month"]==month)]
    if month !="All":
        df = df[df["Start Time"].dt.month_name()== month]
        
    if day !="All":
        df = df[df["Start Time"].dt.day_name() == day]

    return df
#---------------------------------------------------------------------------------------------------

"""
Third Function:
input: get the dataframe created in second funciton to do some statistics on it :)
output: print the most common (month, day of week, start hour)   :)
"""

#---------------------------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month : ",end="\t")
    print(df["Start Time"].dt.month_name().mode()[0] )
    print("                -----")     
    # display the most common day of week
    print("The most common day of week : ",end="\t")
    print(df["Start Time"].dt.day_name().mode()[0])
    print("                       ----")
    # display the most common start hour
    
    print("The most common start hour : ",end="\t")
    print(df["Start Time"].dt.hour.mode()[0])
    print("                      ----")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------

"""
Fourth Function:
input: get the dataframe created in second funciton to do some statistics on it :)
output: print most commonly ( Start and End station) and most frequently combinaton  :)
"""

#---------------------------------------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used Start Station : ',end='\t')
    print(df['Start Station'].mode()[0])
    print('                   -------------')
    
    # display most commonly used end station
    print('Most commonly used End Station :',end='\t')
    print(df['End Station'].mode()[0])
    print('                   -----------')
    # display most frequent combination of start station and end station trip
    df['trip']=df['Start Station'] + " to " +df['End Station']
    print('Most frequent combination of Start Station and End Station trip :',end='\t')
    print(df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------

"""
Fifth Function:
input: get the dataframe created in second funciton to do some statistics on it :)
output: print  (total and mean) travel time  :)
"""

#---------------------------------------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time :',end='\t')
    print((df['End Time'].dt.hour - df['Start Time'].dt.hour).sum())
    print('-----')
    # display mean travel time
    print('Mean Travel Time : ',end='\t')
    print((df['End Time'].dt.hour - df['Start Time'].dt.hour).mean())
    print('----')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------

"""
Sixth Function:
input: get the dataframe created in second funciton to do some statistics on it :)
output: print counts of ( user types, gender, [earliest, most recent, and most common] year of birth  :)
Note that: Gender and Birth Year columns are available in only ( new york city and chicago) :)
"""

#---------------------------------------------------------------------------------------------------
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types :")
    print(df['User Type'].value_counts())
    try:
        
    # Display counts of gender
        print("\nCounts of gender : ")
        print(df['Gender'].value_counts())
    # Display earliest, most recent, and most common year of birth
        print("\nEarliest year : ",end='\t')
        print(df['Birth Year'].min())
        print("Most recent year : ",end='\t')
        print(df['Birth Year'].max())
        print("Most common year : ",end='\t')
        print(df['Birth Year'].mode()[0])
    except:
        print("Opps!!! Washington not contains (Gender) and (Birth Year) columns :( ")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#---------------------------------------------------------------------------------------------------

"""
MAIN FUNCTION  :)  :)
this funciton test you entire previous functions  
have fun!  :) :) :)
"""

#---------------------------------------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
#---------------------------------------------------------------------------------------------------
# End of project
#######################################
#   Name: Ibrahim Ehab Abdelmaged :)  #
#######################################
#---------------------------------------------------------------------------------------------------
