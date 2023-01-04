# introduction

"""
Creating a float
Before we start looking for Bayes' kidnapper, we need to fill out a Missing Puppy Report with details of the case. 
Each piece of information will be stored as a variable.

We define a variable using an equals sign (=). For instance, we would define the variable height:

height = 24
In this exercise, we'll be defining bayes_age to be 4.0 months old. The data type for this variable will be float, meaning that it is a number.
"""
# Define a variable called bayes_age and set it equal to 4.0.
# Display the variable bayes_age.
# Fill in Bayes' age (4.0)
bayes_age = 4.0

# Display the variable bayes_age
print(bayes_age)



"""
Creating strings
Let's continue to fill out the Missing Puppy Report for Bayes. In the previous exercise, we defined bayes_age, which was a float, 
which represents a number.

In this exercise, we'll define favorite_toy and owner, which will both be strings. A string represents text. 
A string is surrounded by quotation marks (' or ") and can contain letters, numbers, and special characters. 
It doesn't matter if you use single (') or double (") quotes, but it's important to be consistent throughout your code.
"""
# Define a variable called favorite_toy whose value is "Mr. Squeaky".
# Define a variable called owner whose value is 'DataCamp'.
# Show the values assigned to these variables.
# Bayes' favorite toy
favorite_toy = "Mr. Squeaky"

# Bayes' owner
owner = "DataCamp"

# Display variables
print(favorite_toy)
print(owner)


"""
Correcting string errors
It's easy to make errors when you're trying to type strings quickly.

Don't forget to use quotes! Without quotes, you'll get a name error.
owner = DataCamp
Use the same type of quotation mark. If you start with a single quote, and end with a double quote, you'll get a syntax error.
fur_color = "blonde'
Someone at the police station made an error when filling out the final lines of Bayes' Missing Puppy Report. In this exercise, 
you will correct the errors.
"""
# Correct the mistakes in the code so that it runs without producing syntax errors.
# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors
birthday = "2017-07-14"
case_id = 'DATACAMP!123-456?'


"""
Load a DataFrame
A ransom note was left at the scene of Bayes' kidnapping. 
Eventually, we'll want to analyze the frequency with which each letter occurs in the note, to help us identify the kidnapper. 
For now, we just need to load the data from ransom.csv into Python.

We'll load the data into a DataFrame, a special data type from the pandas module. 
It represents spreadsheet-like data (something with rows and columns).

We can create a DataFrame from a CSV (comma-separated value) file by using the function pd.read_csv().
"""
#Use pd.read_csv() to load data from a CSV file called ransom.csv. This file represents the frequency of each letter in the ransom note for Bayes.
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)


"""
Correcting a function error
The code in the script editor should plot information from the DataFrame that we loaded in the previous exercise.

However, there is an error in function syntax. Remember that common function errors include:

Forgetting closing parenthesis
Forgetting commas between each argument
Note that all arguments to the functions are correct. The problem is in the function syntax.
"""
#Correct the code so that it runs without syntax errors.
# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()

"""
Snooping for suspects
We need to narrow down the list of suspects for the kidnapping of Bayes. Once we have a list of suspects, 
we'll ask them for writing samples and compare them to the ransom note.

A witness to the crime noticed a green truck leaving the scene of the crime whose license plate began with 'FRQ'. 
We'll use this information to search for some suspects.

As a detective, you have access to a special function called lookup_plate.

lookup_plate accepts one positional argument: A string representing a license plate.
"""
#Part1: Create a variable called plate that represents the observed license plate: the first three letters were FRQ, 
#but the witness couldn't see the final 4 letters. Use asterisks (*) to represent missing letters.
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

#Part2: Call lookup_plate() using the variable plate.
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

#Part3: Calling lookup_plate() with the license plate FRQ**** produced too many results. Luckily, lookup_plate() also accepts a keyword argument: 
#color. Use the color of the car ('Green') to get a smaller list.
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color='Green')


#PARTE2: LOADING DATA IN PANDAS

"""
Loading a DataFrame
We're still working hard to solve the kidnapping of Bayes, the Golden Retriever. Previously, 
we used a license plate spotted at the crime scene to narrow the list of suspects to:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We've obtained credit card records for all four suspects. Perhaps some of them made suspicious purchases before the kidnapping?

The records are in a CSV called "credit_records.csv".
"""
#Import the pandas module under the alias pd.
#Load the CSV "credit_records.csv" into a DataFrame called credit_records.
#Display the first five rows of credit_records using the .head() method.
# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())

"""
Inspecting a DataFrame
We've loaded the credit card records of our four suspects into a DataFrame called credit_records. Let's learn more about the structure of this DataFrame.

The pandas module has been imported under the alias pd. The DataFrame credit_records has already been imported.

How many rows are in credit_records?
"""
#Use the .info() method to inspect the DataFrame credit_records.
# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())


"""
Two methods for selecting columns
Once again, we've loaded the credit card records of our four suspects into a DataFrame called credit_records. 
Let's examine the items that they've purchased.

The pandas module has been imported under the alias pd. The DataFrame credit_records has already been imported.
"""
#Part1: Select the column item from credit_records using brackets and string notation.
# Select the column item from credit_records
# Use brackets and string notation
items = credit_records['item']

# Display the results
print(items)

#Part2: Select the column item from credit_records using dot notation.
# Select the column item from credit_records
# Use dot notation
items = credit_records.item

# Display the results
print(items)


"""
Correcting column selection errors
A junior detective tried to access the location columns of credit_records, but he made some mistakes. 
Help correct his code so that we can search for suspicious purchases.

In all exercises going forward, pandas will be imported as pd. The DataFrame credit_records has already been imported.
"""
#Correct the code so that it runs without errors.
# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records['location']

# Select the item column in credit_records
items = credit_records.item

# Display results
print(location)


"""
More column selection mistakes
Another junior detective is examining a DataFrame of Missing Puppy Reports. He's made some mistakes that cause the code to fail.

The pandas module has been loaded under the alias pd, and the DataFrame is called mpr.
"""
#Part1: Inspect the DataFrame mpr using info().
# Use info() to inspect mpr
print(mpr.info())

#Part2: Correct the mistakes in the code so that it runs without errors.
# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr ['Dog Name']

# Select column "Missing?" from mpr
is_missing = mpr ['Missing?']

# Display the columns
print(name)
print(is_missing)

"""
Logical testing
Let's practice writing logical statements and displaying the output.

Recall that we use the following operators:

== tests that two values are equal.
!= tests that two values are not equal.
> and < test that greater than or less than, respectively.
>= and <= test greater than or equal to or less than or equal to, respectively.
"""
#Parte1: The variable height_inches represents the height of a suspect. Is height_inches greater than 70 inches?
# Is height_inches greater than 70 inches?
print(height_inches > 70)
#False

#Part2: The variable plate1 represents a license plate number of a suspect. Is it equal to FRQ123?
# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")
#True

#Part3: The variable fur_color represents the color of Bayes' fur. Check that fur_color is not equal to "brown".
# Is fur_color not equal to "brown"?
print(fur_color != "brown")


"""
Selecting missing puppies
Let's return to our DataFrame of missing puppies, which is loaded as mpr. Let's select a few different rows to learn more about the other missing dogs.
"""
#Select the dogs where Age is greater than 2.
#Select the dogs whose Status is equal to Still Missing.
#Select all dogs whose Dog Breed is not equal to Poodle.
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == "Still Missing"]
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != "Poodle"]
print(not_poodle)


"""
Narrowing the list of suspects
In Chapter 1, we found a list of people whose cars matched the description of the one that kidnapped Bayes:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We'd like to narrow this list down, so we obtained credit card records for each suspect. 
We'd like to know if any of them recently purchased dog treats to use in the kidnapping. If they did, they would have visited 'Pet Paradise'.

The credit records have been loaded into a DataFrame called credit_records.
"""
#Select rows of credit_records such that the column location is equal to 'Pet Paradise'.
# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)


"""
Working hard
Several police officers have been working hard to help us solve the mystery of Bayes, the kidnapped Golden Retriever. 
Their commanding officer wants to know exactly how hard each officer has been working on this case. 
Officer Deshaun has created DataFrames called deshaun to track the amount of time he spent working on this case. The DataFrame contains two columns:

day_of_week: a string representing the day of the week
hours_worked: the number of hours that a particular officer worked on the Bayes case'
"""
#Part1: From matplotlib, import the module pyplot under the alias plt
#Part2: Plot Officer Deshaun's hours worked using the columns day_of_week and hours_worked from deshaun.
#Part3: Display the plot.
# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Display Deshaun's plot
plt.show()


"""
Or hardly working?
Two other officers have been working with Deshaun to help find Bayes. Their names are Officer Mengfei and Officer Aditya. 
Deshaun used their time cards to create two more DataFrames: mengfei and aditya. 
  In this exercise, we'll plot all three lines together to see who was working hard each day.

We've already loaded matplotlib under the alias plt.
"""
#Part1: Plot Officer Aditya's time worked with day_of_week on the x-axis and hours_worked on the y-axis.
#Plot Officer Mengfei's time worked with day_of_week on the x-axis and hours_worked on the y-axis.
# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Plot Officer Aditya's hours_worked vs. day_of_week
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display all three line plots
plt.show()


"""
Adding a legend
Officers Deshaun, Mengfei, and Aditya have all been working with you to solve the kidnapping of Bayes. 
Their supervisor wants to know how much time each officer has spent working on the case.

Deshaun created a plot of data from the DataFrames deshaun, mengfei, and aditya in the previous exercise. 
Now he wants to add a legend to distinguish the three lines.
"""
#PART1: Using the keyword label, label Deshaun's plot as "Deshaun".
#Part2: Add labels to Mengfei's ("Mengfei") and Aditya's ("Aditya") plots.
#Part3: Nothing is displaying yet! Add a command to make the legend display.
# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()

"""
Adding labels
If we give a chart with no labels to Officer Deshaun's supervisor, she won't know what the lines represent.

We need to add labels to Officer Deshaun's plot of hours worked.
"""
#Add a descriptive title to the chart.
#Add a label for the y-axis.
# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title('Hours Worked')

# Add y-axis label
plt.ylabel('Hours Worked')

# Legend
plt.legend()
# Display plot
plt.show()


"""
Adding floating text
Officer Deshaun is examining the number of hours that he worked over the past six months. 
The number for June is low because he only had data for the first week. Help Deshaun add an annotation to the graph to explain this.
"""
#Place the annotation "Missing June data" at the point (2.5, 80).
# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, 'Missing June data')

# Display graph
plt.show()


"""
Tracking crime statistics
Sergeant Laura wants to do some background research to help her better understand the cultural context for Bayes' kidnapping. 
She has plotted Burglary rates in three U.S. cities using data from the Uniform Crime Reporting Statistics.

She wants to present this data to her officers, and she wants the image to be as beautiful as possible to effectively tell her data story.

Recall:

You can change linestyle to dotted (':'), dashed('--'), or no line ('').
You can change the marker to circle ('o'), diamond('d'), or square ('s').
"""
#Change the color of Phoenix to "DarkCyan".
#Make the Los Angeles line dotted.
#Add square markers to Philadelphia.
# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=':')

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker='s')

# Add a legend
plt.legend()

# Display the plot
plt.show()

"""
Playing with styles
Help Sergeant Laura try out a few different style options. 
Changing the plotting style is a fast way to change the entire look of your plot without having to update individual colors or line styles. 
Some popular styles include:

'fivethirtyeight' - Based on the color scheme of the popular website
'grayscale' - Great for when you don't have a color printer!
'seaborn' - Based on another Python visualization library
'classic' - The default color scheme for Matplotlib
"""
#Part1: Change the plotting style to "fivethirtyeight".
# Change the style to fivethirtyeight
plt.style.use('fivethirtyeight')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

#Part2:Change the plotting style to "ggplot".
# Change the style to ggplot
plt.style.use('ggplot')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

#Part3: View all styles by typing print(plt.style.available) in the console.
#Pick one of those styles and see what it looks like.
# Choose any of the styles
plt.style.use('bmh')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()


"""
Identifying Bayes' kidnapper
We've narrowed the possible kidnappers down to two suspects:

Fred Frequentist (suspect1)
Gertrude Cox (suspect2)
The kidnapper left a long ransom note containing several unusual phrases. 
Help DataCamp by using a line plot to compare the frequency of letters in the ransom note to samples from the two main suspects.

Three DataFrames have been loaded:

ransom contains the letter frequencies for the ransom note.
suspect1 contains the letter frequencies for the sample from Fred Frequentist.
suspect2 contains the letter frequencies for the sample from Gertrude Cox.
Each DataFrame contain two columns letter and frequency.
"""
#Part1: Plot the letter frequencies from the ransom note. The x-values should be ransom.letter. The y-values should be ransom.frequency. 
#The label should be the string 'Ransom'. The line should be dotted and gray.
# x should be ransom.letter and y should be ransom.frequency
plt.plot(ransom.letter, ransom.frequency,
         # Label should be "Ransom"
         label="Ransom",
         # Plot the ransom letter as a dotted gray line
         linestyle=':', color='gray')
# Display the plot
plt.show()

#Part2: Plot a line for the data in suspect1. Use a keyword argument to label that line 'Fred Frequentist').
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
# X-values should be suspect1.letter
# Y-values should be suspect1.frequency
# Label should be "Fred Frequentist"
plt.plot(suspect1.letter, suspect1.frequency, label="Fred Frequentist")
# Display the plot
plt.show()

#Part3: Plot a line for the data in suspect2 (labeled 'Gertrude Cox').
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency,
         label='Fred Frequentist')

# X-values should be suspect2.letter
# Y-values should be suspect2.frequency
# Label should be "Gertrude Cox"
plt.plot(suspect2.letter, suspect2.frequency, label="Gertrude Cox")

# Display plot
plt.show()

#Part4: Label the x-axis (Letter) and the y-axis (Frequency), and add a legend.
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()












