def getKeyOrNull(dictionary, key):
    if key in dictionary.keys():
        return dictionary[key]
    else:
        return ''

def joinArray(valueArray):
    joinedValue = ''
    for value in valueArray:
        if joinedValue == '':
            joinedValue = joinedValue + value
        else:
            joinedValue = joinedValue + ',' + value
    return joinedValue

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

    def __init__(self, Id, Name, Team, Conference):
        self.id = Id
        self.name = Name
        self.team = Team
        self.conference = Conference

    def ToCsvString(self):
        csvString = joinArray([self.id, self.name, self.team, self.conference, self.defensive_PD, self.defensive_QB_HUR, self.defensive_SACKS, self.defensive_SOLO, self.defensive_TD, self.defensive_TFL, 
        self.defensive_TOT, self.fumbles_FUM, self.fumbles_LOST, self.fumbles_REC, self.interceptions_AVG, self.interceptions_INT, self.interceptions_TD, self.interceptions_YDS, self.kicking_FGA, 
        self.kicking_FGM, self.kicking_LONG, self.kicking_PCT, self.kicking_PTS, self.kicking_XPA, self.kicking_XPM, self.kickReturns_AVG, self.kickReturns_LONG, self.kickReturns_NO, self.kickReturns_TD, 
        self.kickReturns_YDS, self.passing_ATT, self.passing_COMPLETIONS, self.passing_INT, self.passing_PCT, self.passing_TD, self.passing_YDS, self.passing_YPA, self.punting_In_Twenty, self.punting_LONG,
        self.punting_NO, self.punting_TB, self.punting_YDS, self.punting_YPP, self.puntReturns_AVG, self.puntReturns_LONG, self.puntReturns_NO, self.puntReturns_TD, self.puntReturns_YDS, self.receiving_LONG, 
        self.receiving_REC, self.receiving_TD, self.receiving_YDS, self.receiving_YPR, self.rushing_CAR, self.rushing_LONG, self.rushing_TD, self.rushing_YDS, self.rushing_YPC])
        return csvString + '\n'
        
        

    def applyStats(self, stats):
        stat_dict = dict()
        
        for stat in stats:
            key = stat[4] + "_" + str(stat[5]).replace(' ', '_')
            value = stat[6]
            stat_dict[key] = value

        self.defensive_PD = getKeyOrNull(stat_dict, "defensive_PD")
        self.defensive_QB_HUR = getKeyOrNull(stat_dict, "defensive_QB_HUR")
        self.defensive_SACKS = getKeyOrNull(stat_dict, "defensive_SACKS")
        self.defensive_SOLO = getKeyOrNull(stat_dict, "defensive_SOLO")
        self.defensive_TD = getKeyOrNull(stat_dict, "defensive_TD")
        self.defensive_TFL = getKeyOrNull(stat_dict, "defensive_TFL")
        self.defensive_TOT = getKeyOrNull(stat_dict, "defensive_TOT")
        self.fumbles_FUM = getKeyOrNull(stat_dict, "fumbles_FUM")
        self.fumbles_LOST = getKeyOrNull(stat_dict, "fumbles_LOST")
        self.fumbles_REC = getKeyOrNull(stat_dict, "fumbles_REC")
        self.interceptions_AVG = getKeyOrNull(stat_dict, "interceptions_AVG")
        self.interceptions_INT = getKeyOrNull(stat_dict, "interceptions_INT")
        self.interceptions_TD = getKeyOrNull(stat_dict, "interceptions_TD")
        self.interceptions_YDS = getKeyOrNull(stat_dict, "interceptions_YDS")
        self.kicking_FGA = getKeyOrNull(stat_dict, "kicking_FGA")
        self.kicking_FGM = getKeyOrNull(stat_dict, "kicking_FGM")
        self.kicking_LONG = getKeyOrNull(stat_dict, "kicking_LONG")
        self.kicking_PCT = getKeyOrNull(stat_dict, "kicking_PCT")
        self.kicking_PTS = getKeyOrNull(stat_dict, "kicking_PTS")
        self.kicking_XPA = getKeyOrNull(stat_dict, "kicking_XPA")
        self.kicking_XPM = getKeyOrNull(stat_dict, "kicking_XPM")
        self.kickReturns_AVG = getKeyOrNull(stat_dict, "kickReturns_AVG")
        self.kickReturns_LONG = getKeyOrNull(stat_dict, "kickReturns_LONG")
        self.kickReturns_NO = getKeyOrNull(stat_dict, "kickReturns_NO")
        self.kickReturns_TD = getKeyOrNull(stat_dict, "kickReturns_TD")
        self.kickReturns_YDS = getKeyOrNull(stat_dict, "kickReturns_YDS")
        self.passing_ATT = getKeyOrNull(stat_dict, "passing_ATT")
        self.passing_COMPLETIONS = getKeyOrNull(stat_dict, "passing_COMPLETIONS")
        self.passing_INT = getKeyOrNull(stat_dict, "passing_INT")
        self.passing_PCT = getKeyOrNull(stat_dict, "passing_PCT")
        self.passing_TD = getKeyOrNull(stat_dict, "passing_TD")
        self.passing_YDS = getKeyOrNull(stat_dict, "passing_YDS")
        self.passing_YPA = getKeyOrNull(stat_dict, "passing_YPA")
        self.punting_In_Twenty = getKeyOrNull(stat_dict, "punting_In_20")
        self.punting_LONG = getKeyOrNull(stat_dict, "punting_LONG")
        self.punting_NO = getKeyOrNull(stat_dict, "punting_NO")
        self.punting_TB = getKeyOrNull(stat_dict, "punting_TB")
        self.punting_YDS = getKeyOrNull(stat_dict, "punting_YDS")
        self.punting_YPP = getKeyOrNull(stat_dict, "punting_YPP")
        self.puntReturns_AVG = getKeyOrNull(stat_dict, "puntReturns_AVG")
        self.puntReturns_LONG = getKeyOrNull(stat_dict, "puntReturns_LONG")
        self.puntReturns_NO = getKeyOrNull(stat_dict, "puntReturns_NO")
        self.puntReturns_TD = getKeyOrNull(stat_dict, "puntReturns_TD")
        self.puntReturns_YDS = getKeyOrNull(stat_dict, "puntReturns_YDS")
        self.receiving_LONG = getKeyOrNull(stat_dict, "receiving_LONG")
        self.receiving_REC = getKeyOrNull(stat_dict, "receiving_REC")
        self.receiving_TD = getKeyOrNull(stat_dict, "receiving_TD")
        self.receiving_YDS = getKeyOrNull(stat_dict, "receiving_YDS")
        self.receiving_YPR = getKeyOrNull(stat_dict, "receiving_YPR")
        self.rushing_CAR = getKeyOrNull(stat_dict, "rushing_CAR")
        self.rushing_LONG = getKeyOrNull(stat_dict, "rushing_LONG")
        self.rushing_TD = getKeyOrNull(stat_dict, "rushing_TD")
        self.rushing_YDS = getKeyOrNull(stat_dict, "rushing_YDS")
        self.rushing_YPC = getKeyOrNull(stat_dict, "rushing_YPC")

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

        playerStats = PlayerStatRecord(id, playerName, playerTeam, playerConference)
        playerStats.applyStats(playerRecords)
        playerStatArray.append(playerStats)
        
    return playerStatArray

def writeRecordsToCsvFile(file, statRecords):
    outputLines = []
    for record in statRecords:
        line = record.ToCsvString()
        outputLines.append(line)

    playerFile = open(file, 'w+')
    Lines = playerFile.writelines(outputLines)

def main():
    playerStatFile = 'Data/2022_player_stat_data.csv'

    uniquePlayerIds = getUniquePlayers(playerStatFile)
    playerRecords = getPlayerRecords(playerStatFile)

    playerStatRecords = compressPlayerRecords(uniquePlayerIds, playerRecords)

    writeRecordsToCsvFile('Data/2022_player_stat_data_compressed.csv', playerStatRecords)

main()