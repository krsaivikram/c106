import plotly.express as px
import csv
import numpy as np
def DataSource(datapath):
    sizeoftv = []
    avgtime=[]
    with open(datapath) as file:
        reader = csv.DictReader(file)
        for row in reader:
            sizeoftv.append(float(row["Size of TV"]))
            avgtime.append(float(row["Average time "]))
    return{"x":sizeoftv,"y":avgtime}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath = "C:/Users/Manorama/Desktop/Size&time.csv"
    datasource = DataSource(datapath)
    findcorrelation(datasource)
setup()    
