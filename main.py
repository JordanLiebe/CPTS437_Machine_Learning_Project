import pandas as pd

# Read the csv file
datatable = pd.read_csv("Data/2022_game_data.csv")
incompleteGames = datatable[datatable.completed==False]
completedGames = datatable[datatable.completed==True]

print(datatable)

print(completedGames)