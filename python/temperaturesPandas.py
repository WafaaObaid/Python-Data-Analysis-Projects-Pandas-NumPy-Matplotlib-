
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
 
file_path = "C:/Users/97056/Downloads/temperatures.csv"

try:
    temperatures = pd.read_csv(file_path)
    print("DataFram loaded succefully. ")
except FileNotFoundError:
    print(f"Error: the file '{file_path}' was not found")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty or contains no data.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the file '{file_path}'. It might be corrupted or not a valid CSV format.")
except Exception as e:
    print(f"An unexpected error occurred while trying to read the CSV file: {e}")

print(temperatures.head())

# Look at temperatures
print(temperatures)
# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")
# Look at temperatures_ind
print(temperatures_ind)
# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())
# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
cities = ["London", "Paris"]
# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])
# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])
# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]
# Subset for rows to keep
print(temperatures_ind.loc[[("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]])

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())
# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))
# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()
# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc["Pakistan":"Philippines"])
# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc["Lahore":"Manila"])
# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[("Pakistan", "Lahore"): ("Philippines", "Manila")])

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])
# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])
# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"]>="2010-1-1") & (temperatures["date"]<= "2011-12-31")]
print(temperatures_bool)
# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()
# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])
# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-8-1":"2011-2-1"])

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22:1])
# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])
# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])
# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])

# Add a year column to temperatures
temperatures["year"]= temperatures["date"].dt.year
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country", "city"], columns="year")
# See the result
print(temp_by_country_city_vs_year)

# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt": "India"]
# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"): ("India", "Delhi")]
# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"): ("India", "Delhi"), 2005:2010]

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis="index")
# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])
# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")
# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])



