import plotly.express as px
import csv 
with open("C:/Users/Manorama/Desktop/icecreamdata.csv") as file:
    df = csv.DictReader(file)
    fig = px.scatter(df,x="Temperature",y="Ice-cream Sales")
    fig.show()
