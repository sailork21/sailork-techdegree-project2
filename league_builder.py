import csv

sharks = []
dragons = []
raptors = []

def dict_create():
    """Opens the CSV file and turns each row into a list."""
    with open('soccer_players.csv', newline = '') as soccer_players:
        player_reader = csv.DictReader(soccer_players, delimiter=',')
        rows = list(player_reader)
        """ This part counts players and divides them into 3 equal teams. It
        also makes sure the players with experience are equally divided.
        """
        player_count = 0
        exp_count = 0
        for row in rows:
            player_count += 1
            if row['Soccer Experience'] == 'YES':
                exp_count += 1
        team_size = player_count // 3
        exp_per_team = exp_count // 3
        """This part first assigns all players with experience evenly to the
        three teams, it then goes back and fills in with non-experienced
        players until each team is full."""
        shark_exp = 0
        dragon_exp = 0
        raptor_exp = 0
        for row in rows:
            if row['Soccer Experience'] == 'YES' and shark_exp < exp_per_team:
                shark_exp += 1
                sharks.append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])
            elif row['Soccer Experience'] == 'YES' and dragon_exp < exp_per_team:
                dragon_exp += 1
                dragons.append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])
            elif row['Soccer Experience'] == 'YES' and raptor_exp < exp_per_team:
                raptor_exp += 1
                raptors.append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])
        for row in rows:
            if row['Soccer Experience'] == 'NO' and len(sharks) < team_size:
                sharks.append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])
            elif row['Soccer Experience'] == 'NO' and len(dragons) < team_size:
                dragons.append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])
            elif row['Soccer Experience'] == 'NO' and len(raptors) < team_size:
                raptors.append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])
    return sharks, dragons, raptors
    soccer_players.close()

def print_file(sharks, dragons, raptors):
    """This function takes the lists made in dict_create and prints them to
    # one text file.
    """
    team_list = open("teams.txt", "+w")
    team_list.write("SHARKS" + "\n")
    for kid in sharks:
        team_list.write(", ".join(kid) + "\n")
    team_list.write("\n" + "DRAGONS" + "\n")
    for kid in dragons:
        team_list.write(", ".join(kid) + "\n")
    team_list.write("\n" + "RAPTORS" + "\n")
    for kid in raptors:
        team_list.write(", ".join(kid) + "\n")
    team_list.close()
    letters(sharks, "Sharks")
    letters(dragons, "Dragons")
    letters(raptors, "Raptors")


def letters(team_list, team):
    """This function takes the lists from dict_create and creates new text
    files with the names of the players and writes a note to the guardians
    in the text file.
    """
    for kid in team_list:
        kid_name = kid[0].split(" ")
        new_file = open(f"{kid_name[0].lower()}_{kid_name[1].lower()}.txt", "w+")
        new_file.write(f"Dear {kid[2]},\n\n{kid[0]} will be a member of the {team} team. Our first practice will be next Monday at 6 pm.")
        new_file.close()


if __name__ == '__main__':
    dict_create()
    print_file(sharks, dragons, raptors)
