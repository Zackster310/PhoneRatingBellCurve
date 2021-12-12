import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("phone.csv")

rating = df["Avg Rating"].tolist()

fig = ff.create_distplot([rating], ["Rating"], show_hist = False)

fig.show()