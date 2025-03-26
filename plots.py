import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# Simple plot
ages = df['Age']
names = df['Name']
plt.bar(names, ages)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of Individuals')
plt.show()