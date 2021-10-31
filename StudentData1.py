import pandas as pd
import csv
import plotly.graph_objects as go

file = pd.read_csv("StudentData.csv")
studentdf = file.loc[file["student_id"] == "TRL_987"]
print(studentdf.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x = studentdf.groupby("level")["attempt"].mean(),y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = "h"))
fig.show()
