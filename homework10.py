import pandas as pd
print("number 1")
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})
res = pd.concat([df1, df2], axis=0, ignore_index=True)
print(res)
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'A': [4, 5, 6]
})
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'B': [7, 8, 9]
})
res = pd.merge(df1, df2, on='ID')
print(res)
print("number 2")
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'C': [1, 1.5, 2, 2.5, 3]
})
plt.figure(figsize=(8, 6))
plt.plot(df['A'], df['B'], label='A vs B', color='b', marker='o')
plt.xlabel('A')
plt.ylabel('B')
plt.title('График зависимости A от B')
plt.legend()
plt.grid(True)
plt.show()