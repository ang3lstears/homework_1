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
pol = pd.Series({0: 'female',1: 'male',2: 'male',3: 'female',4: 'female',5: 'male',
  6: 'male',7: 'male',8: 'male',9: 'female',10: 'female',11: 'female',12: 'female',
  13: 'female',14: 'male',15: 'male',16: 'male',17: 'male',18: 'male',19: 'female',
  20: 'female',21: 'female',22: 'male',23: 'male',24: 'male',25: 'male',26: 'female',
  27: 'female',28: 'male',29: 'female',30: 'male',31: 'female',32: 'female',
  33: 'male',34: 'female'})

x = pol.value_counts().index
y = pol.value_counts().values
plt.bar(x, y, color=['pink', 'blue'])
plt.xlabel('количество учеников') 
plt.ylabel('пол учеников') 
plt.title('соотношение студентов')
plt.show()
