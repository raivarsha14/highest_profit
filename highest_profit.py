# Importing pandas library needed to solve the challenge
import pandas as pd
# Importing OS library to work with directory paths
import os

# To read the data from RAW csv file, I am using pandas and putting the data into dataframe named as 'df'
df = pd.read_csv("https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv")

# Printing first answer using shape method of the dataframe. Shape returns answer in a tuple (no. of rows, no. of columns).
# Since only rows are requested, I am  accessing 0th element to retrieve the number of rows in the dataframe
print(f"Answer 1: There are {df.shape[0]} number of rows")

# For the second answer, I am supposed to eleminate the rows with non-numeric values.
# First I will convert the 'profit' column into numeric type. When the column contains non-numeric value, there would usually be an error. 
# In case of such an error, I am forcing pandas to place NaN (a valid numeric type) in the cell using the 'coerce' option.
df['Profit (in millions)'] = pd.to_numeric(df['Profit (in millions)'], errors='coerce')

# By using dropna method of the dataframe, I can remove NaN values placesd in above code from 'profit' column. Thus removing non-numeric profit rows.
df = df.dropna(axis=0, subset=['Profit (in millions)'])

# To write the JSON file with all the data where profit column contains only numeric values
df.to_json("data2.json")

# Printing second answer to screen using shape method as this now gets us the number of rows with numeric profit values.
# Also, printing the path of created JSON file which contains this data.
print(f"Answer 2: There are {df.shape[0]} number of rows are left after removing all the rows with \
	invalid non-numeric profit column data and the dataset has been saved as JSON file to {os.path.join(os.getcwd(), 'data2.json')}")


# To sort the data into decsending order based on 'profit' column
df = df.sort_values('Profit (in millions)', ascending=False)

print("Answer 3: Top 20 rows after sorting by Profit in descending order:")
# Printing the top 20 rows with highest profit values
print(df.head(20))