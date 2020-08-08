import d20
import initiatebattle
def parse_command(command):
    commander=command.split()
    print(commander)
    status=''
    if commander[0]=='battlestart':
        b=start_battle()
        status='battle sucessfully started!'
    elif commander[1]=='addchar':

        return status





def start_battle():
    b=initiatebattle.battle()
    return b