import os
import pandas as pd

cwd = os.getcwd()
print(cwd)

df = pd.read_csv(cwd + '/input/question-1/main.csv')
df= df.groupby((df.Year//10)*10).sum()
df.__delitem__('Year')

df.to_csv(cwd + '/output/answer-1/main.csv')