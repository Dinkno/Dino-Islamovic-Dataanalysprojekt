import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px
import dash


data = ["Data/Gender_data.csv", "Data/Municipality_Weekly_Data.csv","Data/National_Daily_Deaths.csv", 
"Data/Regional_Daily_Cases.csv", "Data/Regional_Totals_Data.csv"]


df_dic = {}

data_name = ["Gender", "Municipality", "National_daily_deaths", "Regional_daily", "Regional_total" ]

for i,d in enumerate(data):
    df_dic[data_name[i]] = pd.read_csv(f"{d}", encoding="ISO-8859-1", header=0)

#Visualisering 1

område = ["Blekinge", "Dalarna", "Gotland", "Gävleborg", "Halland", "Jämtland Härjedalen", "Jönköping", "Kalmar"]

smittade_regional = {}
medel = 0

storlek = len(df_dic["Regional_daily"])
 
for i,d in enumerate(område):
    smittade_regional[område[i]] = []
    for z in range(storlek):
        smittade_regional[område[i]].append(df_dic["Regional_daily"].iloc[z,i+2])

while True:
    try:
        valde = str(input("Välj ett område mellan (Blekinge, Dalarna, Gotland, Gävleborg, Halland, Jämtland Härjedalen, Jönköping, Kalmar"))
        fig = px.line(df_dic["Regional_daily"], y=valde, title="Smittade per dag")
        fig.show()
        break
    except ValueError:
            print("Kolla att du stavade rätt")

#Visualisering 2

total = ["Total_Cases", "Total_Deaths"]
titel = ["Procentuell Smittade av Kvinnor och Men", "Procentuell Döda av Kvinnor och Men"]

for i in range(2):
    fig = px.pie(df_dic["Gender"], values=total[i], names='Gender', title=titel[i], color='Gender')
    fig.show()

#Visualisering 3

ds_daily = ["Regional_daily", "National_daily_deaths"]
column1 = ["Sweden_Total_Daily_Cases", "National_Daily_Deaths"]


def daily(x):
    lista = []
    for index, row in df_dic[ds_daily[x]].iterrows():
        lista.append(row[column1[x]])
    return lista

titel = ["Smittade per dag", "Döda per dag"]

for i in range(2):
    fig = px.line(y= daily(i), x=df_dic[ds_daily[i]]["Date"], title=titel[i])
    fig.show()

#Visualisering 4

fig = px.histogram(df_dic["National_daily_deaths"], y="National_Daily_Deaths", x="Date", nbins=50)
fig.show()

#Visualisering 5

total_döda = {}

region = ["Blekinge", "Dalarna", "Gotland", "Gävleborg", "Halland", "Jämtland Härjedalen", "Jönköping", "Kalmar", "Kronoberg", "Norrbotten", "Skåne", "Stockholm", "Sörmland", "Uppsala", "Värmland", "Västerbotten", "Västernorrland", "Västmanland", "Västra Götaland", "Örebro", "Östergötland"]

for i,d in enumerate(region):
    total_döda[region[i]] = df_dic["Regional_total"].iloc[i,4]

döda_värde = sorted(total_döda.values(), reverse=True)
sorted_total_döda = {}

for z in döda_värde:
    for k in total_döda.keys():
        if total_döda[k] == z:
            sorted_total_döda[k] = total_döda[k]

    
df_dic["Regional_total"]["Region"] = sorted_total_döda.keys() 
df_dic["Regional_total"]["Total_Cases"] = sorted_total_döda.values() 

fig = px.bar(df_dic["Regional_total"].head(5), x='Region', y='Total_Cases')
fig.show()