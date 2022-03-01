import numpy as np
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv")
theme = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv")

''' Remove invalid data from lego_sets.csv'''
invalid_data_index = df[df["set_num"].isnull()].index
df = df.drop(invalid_data_index)
licensed_parent_themes = list(theme[theme["is_licensed"]==True]["name"])
licensed_legosets = df[df["parent_theme"].isin(licensed_parent_themes)]

''' What percentage of all licensed sets ever released were Star Wars themed?'''
licensed_legosets_starwars = licensed_legosets[licensed_legosets["parent_theme"]=="Star Wars"]
the_force = len(licensed_legosets_starwars)/len(licensed_legosets)
print("{:.2f}%".format(100*the_force))

''' In which year was Star Wars not the most popular licensed theme
(In terms of number of sets released that year)?'''
licensed_sorted = licensed_legosets.sort_values("year")
licensed_sorted["count"] = 1
summed_df = licensed_sorted.groupby(["year","parent_theme"]).sum().reset_index()
max_df = summed_df.sort_values("count",ascending=False).drop_duplicates(["year"])
max_df.sort_values("year")

''' numbers of sets Released every year for Star Wars'''
starwars_data = licensed_legosets[licensed_legosets["parent_theme"]=="Star Wars"]
starwars_yearly_sales = starwars_data.groupby("year")["year"].count()
new_era = starwars_yearly_sales.idxmin()
print(new_era)