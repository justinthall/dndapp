import d20
import initiatebattle


class commandParam():
    def __init__(self, command, room, headers):
        self.id = command['base'][0]
        self.base = command['base']
        self.flags = command['optionals']
        self.room = room
        self.characters = headers['characters']
        self.nickname = headers['nickname']
        cutTime = headers['datetime'].split()[1]
        self.time = str(cutTime.split(".")[0])


def parseCommand(command, room, headers):
    command = commandParam(skinCommand(command), room, headers)
    msg = ""
    if command.id == "roll":
        msg = roll(command)
    elif command.id == "startbattle":
        msg = commandStartBattle(command)
    elif command.id == "initiative":
        msg = commandListInitiative(command)
    elif command.id == "addchar":
        msg = AddCharacter(command)
    else:
        msg = "Command not found!"
    return finalizeMsg(msg, command.time)


def skinCommand(command):
    command = command.replace("/", "")
    command = command.split('-')
    addons = []
    for i in range(len(command)):
        if i == 0:
            base = command[i].split()
        else:
            try:
                addons.append(command[i].split())
            except:
                break
    return {'base': base, 'optionals': addons}


def finalizeMsg(msg, time):
    return time + ": " + msg


def commandStartBattle(command):
    returnMessage = ""
    try:
        initiatebattle.start_battle(command.room)
        returnMessage = "Battle {0} has been started in room {1}".format(
            command.base[1], command.room)
    except IndexError:
        returnMessage = "A name is needed to begin the encounter, input the command like this: /startbattle [name]"
    return returnMessage


def roll(command):
    result = str(d20.roll(command.base[1]).total)
    nickname = command.nickname
    return "{} has rolled a {}!".format(nickname, result)


def commandListInitiative(command):
    returnMessage = ""
    try:
        battle = initiatebattle.find_battle(command.room)['initiative']
        returnMessage = "->".join(battle)
    except:
        returnMessage = "battle not found"
    return returnMessage


def AddCharacter(command):
    try:
        character = command.characters[command.base[1]]
        characterinit = d20.roll(
            '1d20+{}'.format(character['initiative'])).total
        returnMessage = "{} has rolled a {} and will be added to initiative!".format(
            character['charactername'], str(characterinit))

    except:
        returnMessage = "This character was not found"
    return returnMessage
