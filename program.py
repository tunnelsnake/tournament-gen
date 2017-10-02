import csv
import random
import sys

def load_teams(filename):
    """
    Reads teams from a CSV file,
    returns a multi-dimensional array of teams.
    Expects the CSV file to omit the header.
    """
    teams = [] 
    with open(filename) as f: 
        reader = csv.reader(f)
        for row in reader:
            teams.append(row)
    return teams

def make_game(teams, a, b, game_num, bye=False):
    team_a = "/".join(x.strip() for x in a)
    team_b = "/".join(x.strip() for x in b) if len(b) >= 1 else ""
    return {
        "num": game_num,
        "a": team_a,
        "b": team_b,
        "bye": bye
    }

def first_round(teams):
    games = []

    random.shuffle(teams)

    game_num = 1
    scheduled_teams = 0  #iterator
    while True:

        if (len(teams) % 2 != 0) and (len(teams) - scheduled_teams == 1):
            games.append(make_game(teams, teams[scheduled_teams], [], game_num, True))
            break

        a = teams[scheduled_teams]
        b = teams[scheduled_teams+1]
        scheduled_teams += 2
        games.append(make_game(teams, a, b, game_num))
        game_num += 1

    return games

def print_games(games):
    for game in games:
        print "Game %d" % game["num"]
        if len(game["b"]) == 0:
            print "%s vs. --bye--" % game["a"]
        else:
            print "%s vs. %s" % (game["a"], game["b"])
        print '\t'

def main():
    if len(sys.argv) < 2:
        print "Please provide a CSV file as a CLI argument"
        exit(1)

    teams = load_teams(sys.argv[1])
    if teams < 3:
        raise "Need at least 3 teams to use this tool."
    print "Generating first round elimination tournament for %d teams..." % len(teams)
    print "========================================================"
    games = first_round(teams)

    print_games(games)

if __name__ == '__main__':
    main()
