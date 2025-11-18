import pandas as pd

data = pd.DataFrame({"Name": ["Muwanguzi", "David", "Jeremiah"],
                "Age": [20, 32, 15]},
                index=['Person A', 'Person B', 'Person C'])

print(data)