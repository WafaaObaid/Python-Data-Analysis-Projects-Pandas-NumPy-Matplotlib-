
import pandas as pd
file_path = "C:/Users/97056/Downloads/homelessness.csv"

try:
    df = pd.read_csv(file_path)
    print("DataFram loaded succefully. ")
except FileNotFoundError:
    print(f"Error: the file '{file_path}' was not found")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty or contains no data.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the file '{file_path}'. It might be corrupted or not a valid CSV format.")
except Exception as e:
    print(f"An unexpected error occurred while trying to read the CSV file: {e}")


# Chapter 1 Introducing DataFrames
print(df.head())

print(df.info())

print(df.shape)

print(df.describe())

print(df.values)

print(df.columns)

print(df.index)

print(df.sort_values("state"))

region = df["region"].isin(["South Atlantic", "East North Central"])
print(region)

state_fam = df[["state", "family_members"]]
print(state_fam.head())

# Filter for rows where individuals is greater than 10000
ind_10k = df[df["individuals"]>10000]
print(ind_10k)

# Filter for rows where region is Mountain
mountain_reg = df[df["region"]== "Mountain"]
print(mountain_reg)

# Filter for rows where family_members is less than 1000 and region is Pacific
fam_lt_1k_pac =df[(df["family_members"]<1000) & (df["region"] == "Pacific")]
print(fam_lt_1k_pac)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]
# Filter for rows in the Mojave Desert states
mojave_homelessness = df["state"].isin(canu)
# See the result
print(mojave_homelessness)

# Add total col as sum of individuals and family_members
df["total"] = df["individuals"] + df["family_members"]
# Add p_homeless col as proportion of total homeless population to the state population
df["p_homeless"] = df["total"] / df["state_pop"]
# See the result
print(df)


# Create indiv_per_10k col as homeless individuals per 10k state pop
df["indiv_per_10k"] = 10000 * df["individuals"] /df["state_pop"]
# Subset rows for indiv_per_10k greater than 20
high_homelessness = df[df["indiv_per_10k"] >20]
# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k",ascending=False)
# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]
# See the result
print(result)

