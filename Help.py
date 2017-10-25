#todo: check to see if fit in screen
def help(op=0):
    ret = ""
    if not op:
        ret = "1. Rules\n"
        ret += "2. Movement\n"
        ret +=  "3. Items\n"
        ret +=  "4. Fighting\n"
    elif op == 1:
        ret = "Rules:\n"
        ret +=  "- each second, the game \"ticks\"\n"
        ret +=  "- the player can make an action each tick\n"
        ret +=  "- at the end of each tick, enemies move, pickup items,\n\tand item effects take place in order\n"
        ret +=  "- the score is decreased by 1 each tick\n"
        ret +=  "- if a player and a enemy occupy a same tile then they fight (4)\n"
    elif op == 2:
        ret = "Movement:\n"
        ret +=  "- move with w,s,a,d\n"
        ret +=  "- if no character is entered by the end of the tick\n\tthen the player will not move"
        ret +=  "- moving ends the current tick\n"
        ret +=  "- moving decreases score by 1 point\n"
        ret +=  "- health does not recover while moving\n"
    elif op == 3:
        #todo
        ret = ""
    elif op == 4:
        #todo
        ret = ""
    else:
        ret = "Invalid option!"
        
    return ret + "\n[Select an option or press 'h' to escape]"
