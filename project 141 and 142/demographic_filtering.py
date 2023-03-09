import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')
df = df.sort_values('score', ascending=True)
output = df[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()