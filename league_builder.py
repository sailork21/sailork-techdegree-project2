import csv
#from collections import defaultdict

teams = ['Sharks', 'Dragons', 'Raptors']

league = {teams[0]:[], teams[1]:[], teams[2]:[]}

def dict_create():
    """Opens the CSV file and turns each row into a list."""
    with open('soccer_players.csv', newline = '') as soccer_players:
        player_reader = csv.reader(soccer_players, delimiter=',')
        rows = list(player_reader)
        del rows[0]
        """ This part counts players and divides them into teams. It
        also makes sure the players with experience are equally divided.
        """
        player_count = 0
        exp_count = 0
        for row in rows:
            player_count += 1
            if row[2] == 'YES':
                exp_count += 1
        team_size = player_count // len(teams)
        exp_per_team = exp_count // len(teams)
        """This part first assigns all players with experience evenly to the
        three teams, it then goes back and fills in with non-experienced
        players until each team is full."""
        for team in teams:
            team_exp = 0
            for row in rows:
                if row[2] == 'YES' and team_exp < exp_per_team and row[0] != False:
                    team_exp += 1
                    league[team].append([row[0], row[2], row[3]])
                    row.insert(0, False)
        for team in teams:
            for row in rows:
                if row[2] == 'NO' and len(league[team]) < team_size and row[0] != False:
                    league[team].append([row[0], row[2], row[3]])
                    row.insert(0, False)
    return league
    soccer_players.close()

def print_file(league):
    """This function takes the dictionary made in dict_create and prints them to
    one text file.
    """
    team_list = open("teams.txt", "+w")
    for team in league.keys():
        team_list.write(f"{team}" + "\n")
        for players in league[team]:
            team_list.write(", ".join(players) + "\n")
        team_list.write("\n")

    letters(league)


def letters(league):
    """This function takes the dictionary from dict_create and creates new text
    files with the names of the players and writes a note to the guardians
    in the text file.
    """
    for team in league.keys():
        for player in league[team]:
            kid_name = player[0].split(" ")
            new_file = open(f"{kid_name[0].lower()}_{kid_name[1].lower()}.txt", "w+")
            new_file.write(f"Dear {player[2]},\n\n{player[0]} will be a member of the {team} team. Our first practice will be next Monday at 6 pm.")
            new_file.close()


if __name__ == '__main__':
    dict_create()
    print_file(league)
