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

    def ToCsvString(this):
        return this.__dict__.keys()

    def applyStats(this, stats):
        stat_dict = dict()
        
        for stat in stats:
            key = stat[4] + "_" + str(stat[5]).replace(' ', '_')
            value = stat[6]
            stat_dict[key] = value

        this.defensive_PD = getKeyOrNull(stat_dict, "defensive_PD")
        this.defensive_QB_HUR = getKeyOrNull(stat_dict, "defensive_QB_HUR")
        this.defensive_SACKS = getKeyOrNull(stat_dict, "defensive_SACKS")
        this.defensive_SOLO = getKeyOrNull(stat_dict, "defensive_SOLO")
        this.defensive_TD = getKeyOrNull(stat_dict, "defensive_TD")
        this.defensive_TFL = getKeyOrNull(stat_dict, "defensive_TFL")
        this.defensive_TOT = getKeyOrNull(stat_dict, "defensive_TOT")
        this.fumbles_FUM = getKeyOrNull(stat_dict, "fumbles_FUM")
        this.fumbles_LOST = getKeyOrNull(stat_dict, "fumbles_LOST")
        this.fumbles_REC = getKeyOrNull(stat_dict, "fumbles_REC")
        this.interceptions_AVG = getKeyOrNull(stat_dict, "interceptions_AVG")
        this.interceptions_INT = getKeyOrNull(stat_dict, "interceptions_INT")
        this.interceptions_TD = getKeyOrNull(stat_dict, "interceptions_TD")
        this.interceptions_YDS = getKeyOrNull(stat_dict, "interceptions_YDS")
        this.kicking_FGA = getKeyOrNull(stat_dict, "kicking_FGA")
        this.kicking_FGM = getKeyOrNull(stat_dict, "kicking_FGM")
        this.kicking_LONG = getKeyOrNull(stat_dict, "kicking_LONG")
        this.kicking_PCT = getKeyOrNull(stat_dict, "kicking_PCT")
        this.kicking_PTS = getKeyOrNull(stat_dict, "kicking_PTS")
        this.kicking_XPA = getKeyOrNull(stat_dict, "kicking_XPA")
        this.kicking_XPM = getKeyOrNull(stat_dict, "kicking_XPM")
        this.kickReturns_AVG = getKeyOrNull(stat_dict, "kickReturns_AVG")
        this.kickReturns_LONG = getKeyOrNull(stat_dict, "kickReturns_LONG")
        this.kickReturns_NO = getKeyOrNull(stat_dict, "kickReturns_NO")
        this.kickReturns_TD = getKeyOrNull(stat_dict, "kickReturns_TD")
        this.kickReturns_YDS = getKeyOrNull(stat_dict, "kickReturns_YDS")
        this.passing_ATT = getKeyOrNull(stat_dict, "passing_ATT")
        this.passing_COMPLETIONS = getKeyOrNull(stat_dict, "passing_COMPLETIONS")
        this.passing_INT = getKeyOrNull(stat_dict, "passing_INT")
        this.passing_PCT = getKeyOrNull(stat_dict, "passing_PCT")
        this.passing_TD = getKeyOrNull(stat_dict, "passing_TD")
        this.passing_YDS = getKeyOrNull(stat_dict, "passing_YDS")
        this.passing_YPA = getKeyOrNull(stat_dict, "passing_YPA")
        this.punting_In_Twenty = getKeyOrNull(stat_dict, "punting_In_20")
        this.punting_LONG = getKeyOrNull(stat_dict, "punting_LONG")
        this.punting_NO = getKeyOrNull(stat_dict, "punting_NO")
        this.punting_TB = getKeyOrNull(stat_dict, "punting_TB")
        this.punting_YDS = getKeyOrNull(stat_dict, "punting_YDS")
        this.punting_YPP = getKeyOrNull(stat_dict, "punting_YPP")
        this.puntReturns_AVG = getKeyOrNull(stat_dict, "puntReturns_AVG")
        this.puntReturns_LONG = getKeyOrNull(stat_dict, "puntReturns_LONG")
        this.puntReturns_NO = getKeyOrNull(stat_dict, "puntReturns_NO")
        this.puntReturns_TD = getKeyOrNull(stat_dict, "puntReturns_TD")
        this.puntReturns_YDS = getKeyOrNull(stat_dict, "puntReturns_YDS")
        this.receiving_LONG = getKeyOrNull(stat_dict, "receiving_LONG")
        this.receiving_REC = getKeyOrNull(stat_dict, "receiving_REC")
        this.receiving_TD = getKeyOrNull(stat_dict, "receiving_TD")
        this.receiving_YDS = getKeyOrNull(stat_dict, "receiving_YDS")
        this.receiving_YPR = getKeyOrNull(stat_dict, "receiving_YPR")
        this.rushing_CAR = getKeyOrNull(stat_dict, "rushing_CAR")
        this.rushing_LONG = getKeyOrNull(stat_dict, "rushing_LONG")
        this.rushing_TD = getKeyOrNull(stat_dict, "rushing_TD")
        this.rushing_YDS = getKeyOrNull(stat_dict, "rushing_YDS")
        this.rushing_YPC = getKeyOrNull(stat_dict, "rushing_YPC")

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

    playerStatRecords = compressPlayerRecords(uniquePlayerIds, playerRecords)

    playerStatRecords[0].ToCsvString()

main()