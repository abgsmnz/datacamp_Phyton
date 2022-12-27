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










