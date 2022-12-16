import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

def retrieveStatsFromFiles():
    # Retrieve data from csv files #
    playerStats21 = pd.read_csv("Data/2021_player_stat_data_compressed.csv", index_col = 0)
    playerStats22 = pd.read_csv("Data/2022_player_stat_data_compressed.csv", index_col = 0)

    return playerStats21, playerStats22

def normalizedStats(stats):
    # Create two scalers to normalize the dataframes #
    scaler = StandardScaler()
    scaler.fit(stats.drop(['drafted'], axis = 1))
    scaled_features = scaler.transform(stats.drop(['drafted'], axis = 1))
    normalized_features = pd.DataFrame(scaled_features, columns = stats.columns[:-1])

    return normalized_features

def main():
    # number of clusters to generate
    numOfNeighbors = 3

    # retrieve player stats from compressed files #
    playerStats21, playerStats22 = retrieveStatsFromFiles()

    # normalize stats and return #
    normalizedStats21 = normalizedStats(playerStats21)
    normalizedStats22 = normalizedStats(playerStats22)

    # split 2021 data set into test and training and return in pieces #
    X_train21, X_test21, Y_train21, Y_test21 = train_test_split(normalizedStats21, playerStats21['drafted'], test_size = 0.5)

    # Instantiate classifier and fit it to the training data #
    trained_classifier = KNeighborsClassifier(n_neighbors = numOfNeighbors)
    trained_classifier.fit(X_train21, Y_train21)

    # Make predictions on test data #
    pred21 = trained_classifier.predict(X_test21)
    
    # Printing confusion matrix from 2021 data #
    print(confusion_matrix(Y_test21, pred21))
    print('\n')
    # Printing classification report from 2021 data #
    print(classification_report(Y_test21, pred21))

    # Loading test data from 2022 data #
    _, X_test22, _, _ = train_test_split(
        normalizedStats22, playerStats22['drafted'], test_size = 1)

    # make another set of predictions based of 2022 data to see who might be a possible nfl draft candidate #
    pred22 = trained_classifier.predict(X_test22)
    print(pred22)

    # From here I need to take the predictions for 2022 and form a report on which players are candidates from the drafts

main()