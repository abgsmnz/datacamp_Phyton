"""
Line plot (1)
With matplotlib, you can create a bunch of different plots in Python. The most basic plot is the line plot. A general recipe is given here.

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()
In the video, you already saw how much the world population has grown over the past years. Will it continue to do so? 
The world bank has estimates of the world population for the years 1950 up to 2100. 
The years are loaded in your workspace as a list called year, and the corresponding populations as a list called pop.
"""
#print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. Use two print() functions.
#Before you can start, you should import matplotlib.pyplot as plt. pyplot is a sub-package of matplotlib, hence the dot.
#Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. 
#Don't forget to finish off with the plt.show() function to actually display the plot.
# Print the last item from year and pop
print(year)
print(pop)


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()


"""
Line plot (3)
Now that you've built your first line plot, let's start working on the data that professor Hans Rosling used to build his beautiful bubble chart. 
It was collected in 2007. Two lists are available for you:

life_exp which contains the life expectancy for each country and
gdp_cap, which contains the GDP per capita (i.e. per person) for each country expressed in US Dollars.
GDP stands for Gross Domestic Product. It basically represents the size of the economy of a country. 
Divide this by the population and you get the GDP per capita.

matplotlib.pyplot is already imported as plt, so you can get started straight away.
"""
#Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
#Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
#Don't forget to finish off with a plt.show() command, to actually display the plot.
# Print the last item of gdp_cap and life_exp
print(gdp_cap)
print(life_exp)


# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()


"""
Scatter Plot (1)
When you have a time scale along the horizontal axis, the line plot is your friend. 
But in many other cases, when you're trying to assess if there's a correlation between two variables, for example, the scatter plot is the better choice. 
Below is an example of how to build a scatter plot.

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()
Let's continue with the gdp_cap versus life_exp plot, the GDP and life expectancy data for different countries in 2007. 
Maybe a scatter plot will be a better alternative?

Again, the matplotlib.pyplot package is available as plt.
"""
#Change the line plot that's coded in the script to a scatter plot.
#A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').
#Finish off your script with plt.show() to display the plot.
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()


"""
Scatter plot (2)
In the previous exercise, you saw that the higher GDP usually corresponds to a higher life expectancy. In other words, there is a positive correlation.

Do you think there's a relationship between population and life expectancy of a country? 
The list life_exp from the previous exercise is already available. 
In addition, now also pop is available, listing the corresponding populations for the countries in 2007. The populations are in millions of people.
"""
#Start from scratch: import matplotlib.pyplot as plt.
#Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
#Finish the script with plt.show() to actually display the plot. Do you see a correlation?
# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()


"""
Build a histogram (1)
life_exp, the list containing data on the life expectancy for different countries in 2007, is available in your Python shell.

To see how life expectancy in different countries is distributed, let's create a histogram of life_exp.

matplotlib.pyplot is already available as plt.
"""
#Use plt.hist() to create a histogram of the values in life_exp. Do not specify the number of bins; 
#Python will set the number of bins to 10 by default for you.
#Add plt.show() to actually display the histogram. Can you tell which bin contains the most observations?
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()


"""
Build a histogram (2): bins
In the previous exercise, you didn't specify the number of bins. By default, Python sets the number of bins to 10 in that case. 
The number of bins is pretty important. Too few bins will oversimplify reality and won't show you the details. 
Too many bins will overcomplicate reality and won't show the bigger picture.

To control the number of bins to divide your data in, you can set the bins argument.

That's exactly what you'll do in this exercise. You'll be making two plots here. 
The code in the script already includes plt.show() and plt.clf() calls; 
plt.show() displays a plot; plt.clf() cleans it up again so you can start afresh.

As before, life_exp is available and matplotlib.pyplot is imported as plt.
"""
#Build a histogram of life_exp, with 5 bins. Can you tell which bin contains the most observations?
#Build another histogram of life_exp, this time with 20 bins. Is this better?
# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()


"""
Build a histogram (3): compare
In the video, you saw population pyramids for the present day and for the future. 
Because we were using a histogram, it was very easy to make a comparison.

Let's do a similar comparison. life_exp contains life expectancy data for different countries in 2007. 
You also have access to a second list now, life_exp1950, containing similar data for 1950. Can you make a histogram for both datasets?

You'll again be making two plots. The plt.show() and plt.clf() commands to render everything nicely are already included. 
Also matplotlib.pyplot is imported for you, as plt.
"""
#Build a histogram of life_exp with 15 bins.
#Build a histogram of life_exp1950, also with 15 bins. Is there a big difference with the histogram for the 2007 data?
# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins=15)


# Show and clear plot again
plt.show()
plt.clf()


"""
Labels
It's time to customize your own plot. This is the fun part, you will see your plot come to life!

You're going to work on the scatter plot with world development data: GDP per capita on the x-axis (logarithmic scale), life expectancy on the y-axis. 
The code for this plot is available in the script.

As a first step, let's add axis labels and a title to the plot. 
You can do this with the xlabel(), ylabel() and title() functions, available in matplotlib.pyplot. This sub-package is already imported as plt
"""
#The strings xlab and ylab are already set for you. Use these variables to set the label of the x- and y-axis.
#The string title is also coded for you. Use it to add a title to the plot.
#After these customizations, finish the script with plt.show() to actually display the plot.
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')

# Add title
plt.title('World Development in 2007')

# After customizing, display the plot
plt.show()
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

"""
Ticks
The customizations you've coded up to now are available in the script, in a more concise form.

In the video, Hugo has demonstrated how you could control the y-ticks by specifying two arguments:

plt.yticks([0,1,2], ["one","two","three"])
In this example, the ticks corresponding to the numbers 0, 1 and 2 will be replaced by one, two and three, respectively.

Let's do a similar thing for the x-axis of your world development chart, with the xticks() function. 
The tick values 1000, 10000 and 100000 should be replaced by 1k, 10k and 100k. 
To this end, two lists have already been created for you: tick_val and tick_lab.
"""
#Use tick_val and tick_lab as inputs to the xticks() function to make the the plot more readable.
#As usual, display the plot with plt.show() after you've added the customizations.
# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()


"""
Sizes
Right now, the scatter plot is just a cloud of blue dots, indistinguishable from each other. 
Let's change this. Wouldn't it be nice if the size of the dots corresponds to the population?

To accomplish this, there is a list pop loaded in your workspace. It contains population numbers for each country expressed in millions. 
You can see that this list is added to the scatter method, as the argument s, for size.
"""
#Run the script to see how the plot changes.
#Looks good, but increasing the size of the bubbles will make things stand out more.
#Import the numpy package as np.
#Use np.array() to create a numpy array from the list pop. Call this NumPy array np_pop.
#Double the values in np_pop setting the value of np_pop equal to np_pop * 2. Because np_pop is a NumPy array, each array element will be doubled.
#Change the s argument inside plt.scatter() to be np_pop instead of pop.
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


"""
Colors
The code you've written up to now is available in the script.

The next step is making the plot more colorful! To do this, a list col has been created for you. 
It's a list with a color for each corresponding country, depending on the continent the country is part of.

How did we make the list col you ask? The Gapminder data contains a list continent with the continent each country belongs to. 
A dictionary is constructed that maps continents onto colors:

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
Nothing to worry about now; you will learn about dictionaries in the next chapter.
"""
#Add c = col to the arguments of the plt.scatter() function.
#Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). 
#Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c= col, alpha=0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()


"""
Additional Customizations
If you have another look at the script, under # Additional Customizations, you'll see that there are two plt.text() functions now. 
They add the words "India" and "China" in the plot.
"""
#Add plt.grid(True) after the plt.text() calls so that gridlines are drawn on the plot.
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()



"""
Motivation for dictionaries
To see why dictionaries are useful, have a look at the two lists defined in the script. 
countries contains the names of some European countries. capitals lists the corresponding names of their capital.
"""
#Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
#Use ind_ger to access the capital of Germany from the capitals list. Print it out.
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger=countries.index("germany")

# Use ind_ger to print out capital of Germany
ind_ger
print(capitals[ind_ger])


"""
Create dictionary
The countries and capitals lists are again available in the script. 
It's your job to convert this data to a dictionary where the country names are the keys and the capitals are the corresponding values. 
As a refresher, here is a recipe for creating a dictionary:

my_dict = {
   "key1":"value1",
   "key2":"value2",
}
In this recipe, both the keys and the values are strings. This will also be the case for this exercise.
"""
#With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. 
#Beware of capitalization! Make sure you use lowercase characters everywhere.
#Print out europe to see if the result is what you expected.
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)


"""
Access dictionary
If the keys of a dictionary are chosen wisely, accessing the values in a dictionary is easy and intuitive. 
For example, to get the capital for France from europe you can use:

europe['france']
Here, 'france' is the key and 'paris' the value is returned.
"""
#Check out which keys are in europe by calling the keys() method on europe. Print out the result.
#Print out the value that belongs to the key 'norway'.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])


"""
Dictionary Manipulation (1)
If you know how to access a dictionary, you can also assign a new value to it. 
To add a new key-value pair to europe you can use something like this:

europe['iceland'] = 'reykjavik'
"""
#Add the key 'italy' with the value 'rome' to europe.
#To assert that 'italy' is now a key in europe, print out 'italy' in europe.
#Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
#Print out europe.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland']='warsaw'

# Print europe
print(europe)


"""
Dictionary Manipulation (2)
Somebody thought it would be funny to mess with your accurately generated dictionary. 
An adapted version of the europe dictionary is available in the script.

Can you clean up? Do not do this by adapting the definition of europe, but by adding Python commands to the script to update and remove key:value pairs.
"""
#The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
#Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
#Print out europe to see if your cleaning work paid off.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany']='berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

"""
Dictionariception
Remember lists? They could contain anything, even other lists. Well, for dictionaries the same holds. 
Dictionaries can contain key:value pairs where the values are again dictionaries.

As an example, have a look at the script where another version of europe - the dictionary you've been working with all along - is coded. 
The keys are still the country names, but the values are dictionaries that contain more information than just the capital.

It's perfectly possible to chain square brackets to select elements. To fetch the population for Spain from europe, for example, you need:

europe['spain']['population']
"""
#Use chained square brackets to select and print out the capital of France.
#Create a dictionary, named data, with the keys 'capital' and 'population'. Set them to 'rome' and 59.83, respectively.
#Add a new key-value pair to europe; the key is 'italy' and the value is data, the dictionary you just built.
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy']=data

# Print europe
print(europe)



"""
Dictionary to DataFrame (1)
Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. 
One way to build a DataFrame is from a dictionary.

In the exercises that follow you will be working with vehicle data from different countries. 
Each observation corresponds to a country and the columns give information about the number of vehicles per capita, 
whether people drive left or right, and so on.

Three lists are defined in the script:

names, containing the country names for which data is available.
dr, a list with booleans that tells whether people drive left or right in the corresponding country.
cpc, the number of motor vehicles per 1000 people in the corresponding country.
Each dictionary key is a column label and each value is a list which contains the column elements.
"""
#Import pandas as pd.
#Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
#key 'country' and value names.
#key 'drives_right' and value dr.
#key 'cars_per_cap' and value cpc.
#Use pd.DataFrame() to turn your dict into a DataFrame called cars.
#Print out cars and see how beautiful it is.
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
    }

# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

# Print cars
print(cars)


"""
Dictionary to DataFrame (2)
The Python code that solves the previous exercise is included in the script. 
Have you noticed that the row labels (i.e. the labels for the different observations) were automatically set to integers from 0 up to 6?

To solve this a list row_labels has been created. You can use it to specify the row labels of the cars DataFrame. 
You do this by setting the index attribute of cars, that you can access as cars.index.
"""
#Hit Run Code to see that, indeed, the row labels are not correctly set.
#Specify the row labels by setting cars.index equal to row_labels.
#Print out cars again and check if the row labels are correct this time.
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index=row_labels

# Print cars again
print(cars)


"""
CSV to DataFrame (1)
Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. 
What if you're dealing with millions of observations? In those cases, the data is typically available as files with a regular structure. 
One of those file types is the CSV file, which is short for "comma-separated values".

To import CSV data into Python as a Pandas DataFrame you can use read_csv().

Let's explore this function with the same cars data from the previous exercises. This time, however, the data is available in a CSV file, named cars.csv. 
It is available in your current working directory, so the path to the file is simply 'cars.csv'.
"""
#To import CSV files you still need the pandas package: import it as pd.
#Use pd.read_csv() to import cars.csv data as a DataFrame. Store this DataFrame as cars.
#Print out cars. Does everything look OK?
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars=pd.read_csv("cars.csv")

# Print out cars
print(cars)


"""
CSV to DataFrame (2)
Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what we wanted. 
The row labels were imported as another column without a name.

Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used as a row label? 
Well, that's exactly what you need here!

Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?
"""
#Run the code with Run Code and assert that the first column should actually be used as row labels.
#Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
#Has the printout of cars improved now?
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)


"""
Square Brackets (1)
In the video, you saw that you can index and select Pandas DataFrames in many different ways. 
The simplest, but not the most powerful way, is to use square brackets.

In the sample code, the same cars data is imported from a CSV files as a Pandas DataFrame. 
To select only the cars_per_cap column from cars, you can use:

cars['cars_per_cap']
cars[['cars_per_cap']]
The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.
"""
#Use single square brackets to print out the country column of cars as a Pandas Series.
#Use double square brackets to print out the country column of cars as a Pandas DataFrame.
#Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])


"""
Square Brackets (2)
Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. 
The following call selects the first five rows from the cars DataFrame:

cars[0:5]
The result is another DataFrame containing only the rows you specified.

Pay attention: You can only select rows using square brackets if you specify a slice, like 0:4. 
Also, you're using the integer indexes of the rows here, not the row labels!
"""
#Select the first 3 observations from cars and print them out.
#Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])


"""
loc and iloc (1)
With loc and iloc you can do practically any data selection operation on DataFrames you can think of. 
loc is label-based, which means that you have to specify rows and columns based on their row and column labels. 
iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

Try out the following commands in the IPython Shell to experiment with loc and iloc to select observations. 
Each pair of commands here gives the same result.

cars.loc['RU']
cars.iloc[4]

cars.loc[['RU']]
cars.iloc[[4]]

cars.loc[['RU', 'AUS']]
cars.iloc[[4, 1]]
As before, code is included that imports the cars data as a Pandas DataFrame.
"""
#Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JPN, the index is 2. 
#Make sure to print the resulting Series.
#Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. 
#You can find out about the labels/indexes of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc["JPN"])

# Print out observations for Australia and Egypt
print(cars.iloc[[1,6]])


"""
loc and iloc (2)
loc and iloc also allow you to select both rows and columns from a DataFrame. To experiment, try out the following commands in the IPython Shell. 
Again, paired commands produce the same result.

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]
"""
#Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
#Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc["MOR"])

# Print sub-DataFrame
print(cars.loc[["RU","MOR"],["country", "drives_right"]])
#or iloc: cars.iloc[[4,5], [1,2]]


"""
loc and iloc (3)
It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from beginning to end in front of the comma:

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]
"""
#Print out the drives_right column as a Series using loc or iloc.
#Print out the drives_right column as a DataFrame using loc or iloc.
#Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,"drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:,["drives_right"]])


# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,["cars_per_cap","drives_right"]])















