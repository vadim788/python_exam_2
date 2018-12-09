from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки грошей витратив.
data = dict()
for user_auto in list (dataset.keys()):
    for race, product_race in ( dataset[user_auto]).items():
        if user_auto in data:
            data[user_auto] += sum(product_race)
        else:
            data[user_auto] = sum(product_race)

print(data)
diagram = go.Bar(
    x=list(data.keys()),
    y=list(data.values())
)

fig = go.Figure(data=[diagram])

plotly.offline.plot(fig, filename='user expenses.html')
