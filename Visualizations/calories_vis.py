import plotly.express as px
import pandas as pd

all_calories = []
current_count = 0

with open('Data/input_d01') as f:
    for line in f:
        if line == '\n':
            all_calories.append(current_count)
            current_count = 0
        else:
            current_count = current_count + int(line)

df = pd.DataFrame(all_calories,columns=["Calories"])
fig = px.histogram(df,x="Calories")
fig.show()