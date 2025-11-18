import pandas as pd

#Creating Data
# DataFrame ==> A table containing an array of individual entries, each with a certain value
# Each entry corresponds to a ROW(or RECORD) and a column.
data1 = pd.DataFrame({"Yes":[53, 75], "No": [39, 82]})
print(data1)
print("="* 60)
# DataFrame() constructor
'''
Used to generate DataFrame Objects.
Syntax of declaring a new one is Dictionary whose KEYS are the COLUMN NAMES
'''
data2 = pd.DataFrame({"Name": ["Muwanguzi", "David", "Jeremiah"],
                "Age": [20, 32, 15]},
                index=['Person A', 'Person B', 'Person C'])

print(data2)
print("="* 60)

#SERIES : A sequence of data values. If a DataFrame is a table, Series is a List
# A Series is a single column of a DataFrame, u can assign row labels to the Series the same way as before, using an "index" parameter.

serie1 = pd.Series([1, 2, 3, 4, 5])
print(serie1)
print("="*60)
#If a Series does not have a column name, it only has one overall "name"
serie2 = pd.Series([24,65,25,53], index=['2020 Sales', '2021 Sales', '2022 Sales', '2023 Sales'], name='Product A')
print(serie2)