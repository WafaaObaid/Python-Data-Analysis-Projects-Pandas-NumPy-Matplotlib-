import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt

file_path = "C:/Users/97056/Downloads/avoplotto (1).pkl"

try:
    avocados = pd.read_pickle(file_path)
    print("DataFram loaded succefully. ")
except FileNotFoundError:
    print(f"Error: the file '{file_path}' was not found")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty or contains no data.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the file '{file_path}'. It might be corrupted or not a valid CSV format.")
except Exception as e:
    print(f"An unexpected error occurred while trying to read the CSV file: {e}")


# Look at the first few rows of data
print(avocados.head())
# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()
# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar") 
# Show the plot
plt.show()

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="organic", y="conventional", kind="line")
# Show the plot
plt.show()

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")
# Show the plot
plt.show()

# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()
# Histogram of organic avg_price
avocados[avocados["type"]== "organic"]["avg_price"].hist()
# Add a legend
plt.legend(["conventional", "organic"])
# Show the plot
plt.show()

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados.isna())
# Check each column for missing values
print(avocados.isna().any())
# Bar plot of missing values by variable
avocados.isna().sum().plot(kind="bar")
# Show plot
plt.show()

# Remove rows with missing values
avocados_complete = avocados.dropna()
# Check if any columns contain missing values
print(avocados_complete.isna().any())

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
# Create histograms showing the distributions cols_with_missing
avocados[cols_with_missing].hist()
# Show the plot
plt.show()

# Creating DataFrams

# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]
# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)
# Print the new DataFrame
print(avocados_2019)


# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}
# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)
# Print the new DataFrame
print(avocados_2019)

