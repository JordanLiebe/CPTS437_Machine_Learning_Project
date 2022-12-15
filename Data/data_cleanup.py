def getKeyOrNull(dictionary, key):
    if key in dictionary.keys():
        return dictionary[key]
    else:
        return ''


class PlayerStatRecord:
    id = "-1"
    name = "Unknown"
    team = "Unknown"
    conference = "Unknown"
    defensive_PD = -1
    defensive_QB_HUR = -1
    defensive_SACKS = -1
    defensive_SOLO = -1
    defensive_TD = -1
    defensive_TFL = -1
    defensive_TOT = -1
    fumbles_FUM = -1
    fumbles_LOST = -1
    fumbles_REC = -1
    interceptions_AVG = -1
    interceptions_INT = -1
    interceptions_TD = -1
    interceptions_YDS = -1
    kicking_FGA = -1
    kicking_FGM = -1
    kicking_LONG = -1
    kicking_PCT = -1
    kicking_PTS = -1
    kicking_XPA = -1
    kicking_XPM = -1
    kickReturns_AVG = -1
    kickReturns_LONG = -1
    kickReturns_NO = -1
    kickReturns_TD = -1
    kickReturns_YDS = -1
    passing_ATT = -1
    passing_COMPLETIONS = -1
    passing_INT = -1
    passing_PCT = -1
    passing_TD = -1
    passing_YDS = -1
    passing_YPA = -1
    punting_In_Twenty = -1
    punting_LONG = -1
    punting_NO = -1
    punting_TB = -1
    punting_YDS = -1
    punting_YPP = -1
    puntReturns_AVG = -1
    puntReturns_LONG = -1
    puntReturns_NO = -1
    puntReturns_TD = -1
    puntReturns_YDS = -1
    receiving_LONG = -1
    receiving_REC = -1
    receiving_TD = -1
    receiving_YDS = -1
    receiving_YPR = -1
    rushing_CAR = -1
    rushing_LONG = -1
    rushing_TD = -1
    rushing_YDS = -1
    rushing_YPC = -1

    def __init__(Id, Name, Team, Conference):
        id = Id
        name = Name
        team = Team
        confernece = Conference

    def applyStats(this, stats):
        stat_dict = dict()
        
        for stat in stats:
            key = stat[4] + "_" + str(stat[5]).replace(' ', '_')
            value = stat[6]
            stat_dict[key] = value

        defensive_PD = getKeyOrNull(stat_dict, "defensive_PD")
        defensive_QB_HUR = getKeyOrNull(stat_dict, "defensive_QB_HUR")
        defensive_SACKS = getKeyOrNull(stat_dict, "defensive_SACKS")
        defensive_SOLO = getKeyOrNull(stat_dict, "defensive_SOLO")
        defensive_TD = getKeyOrNull(stat_dict, "defensive_TD")
        defensive_TFL = -1
        defensive_TOT = -1
        fumbles_FUM = -1
        fumbles_LOST = -1
        fumbles_REC = -1
        interceptions_AVG = -1
        interceptions_INT = -1
        interceptions_TD = -1
        interceptions_YDS = -1
        kicking_FGA = -1
        kicking_FGM = -1
        kicking_LONG = -1
        kicking_PCT = -1
        kicking_PTS = -1
        kicking_XPA = -1
        kicking_XPM = -1
        kickReturns_AVG = -1
        kickReturns_LONG = -1
        kickReturns_NO = -1
        kickReturns_TD = -1
        kickReturns_YDS = -1
        passing_ATT = -1
        passing_COMPLETIONS = -1
        passing_INT = -1
        passing_PCT = -1
        passing_TD = -1
        passing_YDS = -1
        passing_YPA = -1
        punting_In_Twenty = -1
        punting_LONG = -1
        punting_NO = -1
        punting_TB = -1
        punting_YDS = -1
        punting_YPP = -1
        puntReturns_AVG = -1
        puntReturns_LONG = -1
        puntReturns_NO = -1
        puntReturns_TD = -1
        puntReturns_YDS = -1
        receiving_LONG = -1
        receiving_REC = -1
        receiving_TD = -1
        receiving_YDS = -1
        receiving_YPR = -1
        rushing_CAR = -1
        rushing_LONG = -1
        rushing_TD = -1
        rushing_YDS = -1
        rushing_YPC = -1

def getUniquePlayers(filename):
    playerFile = open(filename, 'r')
    Lines = playerFile.readlines()

    allPlayerIds = []
    uniquePlayerIds = []

    firstline = True
    for line in Lines:
        if(firstline):
            firstline = False
            continue

        splitLine = line.strip().split(',')
        allPlayerIds.append(splitLine[0])

    uniquePlayerIds = list(set(allPlayerIds))
    return uniquePlayerIds

def getPlayerRecords(filename):
    playerFile = open(filename, 'r')
    Lines = playerFile.readlines()

    allPlayerRecords = []

    firstline = True
    for line in Lines:
        if(firstline):
            firstline = False
            continue

        splitLine = line.strip().split(',')
        allPlayerRecords.append(splitLine)

    return allPlayerRecords

def compressPlayerRecords(playerIds, allPlayerRecords):
    playerStatArray = []

    for id in playerIds:
        playerRecords = [pr for pr in allPlayerRecords if pr[0] == id]
        playerName = playerRecords[0][1]
        playerTeam = playerRecords[0][2]
        playerConference = playerRecords[0][3]

        playerStats = PlayerStatRecord(playerName, playerTeam, playerConference)
        playerStats.applyStats(playerRecords)
        playerStatArray.append(playerStats)
        
    return playerStatArray


def main():
    playerStatFile = 'Data/2022_player_stat_data.csv'

    uniquePlayerIds = getUniquePlayers(playerStatFile)
    playerRecords = getPlayerRecords(playerStatFile)

    compressPlayerRecords(uniquePlayerIds, playerRecords)

main()