# Importing pandas library needed to solve the challange
import pandas as pd
import os

# To read the data from csv file I am using pandas and putting the data into dataframe named as 'df'
df = pd.read_csv("https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv")

# Printing first answer using shape function. Shape returns answer in tuple (no. of rows, no. of columns), since only rows are requested therefore accessing 0th element 
print(f"Answer 1: There are {df.shape[0]} number of rows")

#For the second answer, I was supposed to eleminate the rows with non-numeric values
#First I will convert the 'profit' column into numeric values, where there is not numeric value the error will 
#reflect and that will be coerced and that will result into 'null' value
df['Profit (in millions)'] = pd.to_numeric(df['Profit (in millions)'], errors='coerce')

#By using dropna function I can remove NaN values placesd in above code from 'profit' column
df = df.dropna(axis=0, subset=['Profit (in millions)'])

# To write the JSON file with only valid numeric profit
df.to_json("data2.json")

#Printing second answer using shape function displaying numeric rows only
print(f"Answer 2: There are {df.shape[0]} number of rows are left after removing all the rows with invalid non-numeric profit column data and the dataset has been saved as JSON file to {os.path.join(os.getcwd(), 'data2.json')}")


# To order the data into decsending order based on 'profit' column
df = df.sort_values('Profit (in millions)', ascending=False)

print("Answer 3: Top 20 rows after sorting by Profit in descending order:")
# Printing the top 20 rows with highest profit values
print(df.head(20))