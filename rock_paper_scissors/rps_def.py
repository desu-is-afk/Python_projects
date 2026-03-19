
# 1 Rock
# 2 Paper
# 3 Scissors

def userrock(mchn):
    if mchn == 1:
        return print('\nWe choose rock!\nDraw!\n')
    elif mchn == 2:
        return print('\nYou choose Rock, I choose Paper!\nI win!\n')
    elif mchn == 3:
        return print('\nYou choose Rock, I choose Scissors!\nYou win!\n')
    else:
        return print("Could you try again please?\n")

    
def userpaper(mchn):
    if mchn == 1:
        return print('\nYou choose Paper, I choose Rock!\nYou win!\n')
    elif mchn == 2:
        return print('\nWe choose paper!\nDraw!\n')
    elif mchn == 3:
        return print('\nYou choose Paper, I choose Scissors!\nI win!\n') 
    else:
        return print("Could you try again please?\n")

def userscissors(mchn):
    if mchn == 1:
        return print('\nYou choose Scissors, I chosse Rock!\nI win!\n')
    elif mchn == 2:
        return print('\nYou choose Scissors, I choose Paper!\nYou win!\n')
    elif mchn == 3:
        return print('\nWe choose scissors!\nDraw!\n')
    else:
       return print("Could you try again please?\n")