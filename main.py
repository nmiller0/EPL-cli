import datetime
import urllib.request
import csv
from prettytable import PrettyTable
import re


def main():
    date1 = datetime.date.today()
    global season
    season = str((date1.year - 1) % 2000) + str((date1.year % 2000))
    done = False
    while not done:
        print("EPL-cli \nEnter a command: ")
        print(season)
        usrInput = input()

        if usrInput == "teams" or usrInput == "Teams":
            printTeams()

        if usrInput == "season" or usrInput == "Season":
            season = changeSeason()

        if usrInput == "table" or usrInput == "Table":
            table()

        if usrInput == "exit" or usrInput == "Exit":
            done = True


def downloadRead(str):
    url = 'http://www.football-data.co.uk/mmz4281/' + season + '/E0.csv'
    urllib.request.urlretrieve(url, (season + ".csv"))
    infile = open(season + ".csv")
    reader = csv.DictReader(infile)
    return reader


def changeSeason():
    entered = False
    while (entered == False):
        print("Enter season (e.g) 16/17:")
        newSeason = input()
        seasonForm = re.compile('\d*/\d*')
        if seasonForm.match(newSeason):
            print("season set to " + newSeason)
            newSeason = newSeason.replace("/", "")
            return newSeason
            entered = True


def teams():
    reader = downloadRead(season)
    teams = []
    for row in reader:
        teams.append(row['HomeTeam'])
    tempTeams = teams[:]
    for x in teams:
        for i in range(tempTeams.count(x) - 1):
            tempTeams.remove(x)
    teams = tempTeams[:]
    teams.sort()
    return teams


def printTeams():
    teamList = teams()
    for x in teamList:
        print(x)


class Club(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def calcPoints(self):
        self.points = (self.wins * 3) + self.draws
        return self.points


def table():
    teamList = teams()
    reader = downloadRead(season)
    league = []
    for x in range(len(teamList)):
        league.append(Club(teamList[x]))
    reader = downloadRead(season)

    for row in reader:
        if row['FTR'] == 'H':
            for z in league:
                if z.name == row['HomeTeam']:
                    z.wins = z.wins + 1
                if z.name == row['AwayTeam']:
                    z.losses = z.losses + 1
    reader = downloadRead(season)
    for row2 in reader:
        if row['FTR'] == 'A':
            for y in league:
                if y.name == row2['HomeTeam']:
                    y.losses = y.losses + 1
                if y.name == row2['AwayTeam']:
                    y.wins = y.wins + 1
    reader = downloadRead(season)
    for row3 in reader:
        if row['FTR'] == 'D':
            for q in league:
                if q.name == row3['HomeTeam']:
                    q.draws = q.draws + 1
                if q.name == row3['AwayTeam']:
                    q.draws = q.draws + 1

    for i in range(len(league) - 1):
        for x in range(i):
            if league[i].calcPoints() > league[i + 1].calcPoints():
                temp = league[i]
                league[i] = league[i + 1]
                league[i + 1] = temp

    disTable = PrettyTable()
    disTable.field_names = ["#", "Club", "Wins", "Draws", "Losses", "Points"]
    for i in range(len(league)):
            disTable.add_row([str(i+1), league[i].name, league[i].wins, league[i].draws, league[i].losses, str(league[i].calcPoints())])

    print(disTable.get_string(border=True, padding_width=5))

main()
