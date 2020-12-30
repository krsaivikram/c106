import plotly.express as px 
import csv 
with open("C:/Users/Manorama/Desktop/Size&time.csv") as f:
     df= csv.DictReader(f) 
     fig= px.scatter(df,x="Size of TV",y="Average time ") 
     fig.show()