import datetime
import urllib.request
import csv

def main():
    print("EPL-cli \nEnter a command: ")
    date1 = datetime.date.today()
    global season
    season = str((date1.year - 1)%2000) + str((date1.year % 2000))
    print(season)
    UsrInput = input()
    if UsrInput == "teams" or "Teams":        
            teams()

def download(str):
    url = 'http://www.football-data.co.uk/mmz4281/' +season+ '/E0.csv'
    urllib.request.urlretrieve(url, (season + ".csv"))
    
def teams():
    download(season)
    infile = open(season + ".csv")
    reader = csv.DictReader(infile)
    teams = []
    for row in reader:
        teams.append(row['HomeTeam'])
    i = 0
    tempTeams = teams[:]
    for x in teams:
        for i in range(tempTeams.count(x)-1):
            tempTeams.remove(x)
    teams = tempTeams[:]
    for x in teams:
        print(x)

main()
    
