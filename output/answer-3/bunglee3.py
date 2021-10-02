import os
import pandas as pd

cwd = os.getcwd()
print(cwd)

df = pd.read_csv(cwd + '/input/question-3/main.csv')
df = df[['Team', 'Yellow Cards', 'Red Cards']]
result = df.sort_values('Yellow Cards', ascending=False).sort_values('Red Cards', ascending=False)

result.to_csv(cwd + '/output/answer-3/main.csv')
