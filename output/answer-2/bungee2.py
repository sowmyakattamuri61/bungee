import os
import pandas as pd

cwd = os.getcwd()
print(cwd)

df = pd.read_csv(cwd + '/input/question-2/main.csv')
result = df.groupby('occupation').agg({'age': ['min', 'max']})
result.to_csv(cwd + '/output/answer-2/main.csv')
