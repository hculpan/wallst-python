__author__ = 'usucuha'

import sys, \
    os, \
    game, \
    company, \
    json

def jdefault(o):
    return o.__dict__

def writeToJson(game_obj, game_name, file_name):
    with open('./' + game_name + '/' + file_name + '.json', 'w') as outfile:
        obj = json.dumps(game_obj, default=jdefault)
        outfile.write(obj)

if __name__ == "__main__":
    print "WALLST v1.0"
    print "Create New Game script"

    if len(sys.argv) == 2:
        game_name = sys.argv[0]
    else:
        game_name = raw_input("Name of game: ")

    print ("Game name: " + game_name)

    if os.path.exists("./" + game_name) and os.path.isdir("./" + game_name):
        print (game_name + " exists; please delete directory and retry")
        sys.exit(-1)

    os.mkdir("./" + game_name)

    game = game.Game(game_name)
    writeToJson(game, game_name, 'game')

    c = company.Company("Seattle First National Bank", 35, 10000, 2.5, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    c = company.Company("Rainier National Bank", 100, 10000, 4, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    c = company.Company("Weyerhauser Corp.", 50, 10000, 3, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    c = company.Company("Georgia-Pacific", 65, 10000, 3.5, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    c = company.Company("Bellevue Square", 25, 10000, 1.5, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    c = company.Company("Northgate Mall", 65, 10000, 1.5, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    c = company.Company("Boeing Aerospace", 70, 10000, 4.5, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    c = company.Company("Pacific Car & Foundry", 125, 10000, 5.5, 2.5)
    c.nextPrice()
    writeToJson(c, game_name, c.name)

    print ("Game '" + game_name + "' created")