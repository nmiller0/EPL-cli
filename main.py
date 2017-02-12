import datetime
import urllib.request

def main():
    print("EPL-cli \nEnter a command: ")
    date1 = datetime.date.today()
    global season
    season = str((date1.year - 1)) + "-" + str((date1.year % 2000))
    print(season)
    UsrInput = input()
    if UsrInput == "teams" or "Teams":        
            teams()

    

def download(str):
    url = 'https://raw.githubusercontent.com/openfootball/eng-england/master/'+ str + '/1-premierleague.conf.txt'
    urllib.request.urlretrieve(url, "teams.txt")
    
def teams():
    download(season)
    print("Current Teams: ")
    infile = open("teams.txt", "r")
    teams = infile.read()
    print(teams)

main()
    
