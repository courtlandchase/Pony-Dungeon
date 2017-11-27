def help(op=0):
    ret = ""
    if not op:
        ret = "1. Rules\n"
        ret += "2. Movement\n"
        ret +=  "3. Items\n"
        ret +=  "4. Fighting\n"
    elif op == 1:
        ret = "Rules:\n"
        ret +=  "- Each second, the game \"ticks\"\n"
        ret +=  "- The player can make an action each tick\n"
        ret +=  "- At the end of each tick, enemies move, pickup items,\n\tand item effects take place in order\n"
        ret +=  "- The score is decreased by 1 each tick\n"
        ret +=  "- If a player and a enemy attempt to occupy the same tile then they fight (4)\n"
    elif op == 2:
        ret = "Movement:\n"
        ret +=  "- Move with w,s,a,d\n"
        ret +=  "- If no character is entered by the end of the tick\n\tthen the player will not move\n"
        ret +=  "- Moving ends the current tick\n"
        ret +=  "- Moving decreases score by 1 point\n"
        ret +=  "- Health does not recover while moving\n"
    elif op == 3:
        ret = "Items:\n"
        ret +=  "- $: sand\t->\tincreases score by 100.\n"
        ret +=  "- +: health\t->\trestores or increases health.\n"
        ret +=  "- w: weapon\t->\timproves attack stat.\n"
        ret +=  "- ?: mystery\t->\tobtain a random item or a trap.\n"
        ret +=  "- ~: dew\t->\tdecrease thirst.\n"
        ret +=  "- f: cheeto\t->\tdecrease hunger.\n"
        ret +=  "- X: treasure\t->\tdoubles score, EVEN IF NEGATIVE.\n"
        ret +=  "- t: trap\t->\tdo not step on this.\n"
        ret +=  "- >: stairs\t->\tgo further into the dungeon.\n"
        ret +=  "- E: enemy\t->\tthe bad guys.\n"
    elif op == 4:
        ret = "Fighting:\n"
        ret += "- Enimies may trap you such that fighting them is the only\n\toption to advance.\n"
        ret += "- Move into enemy to attack them.\n"
        ret += "- You deal damage based on your attack stat.\n"
        ret += "- Keep an eye on your hit points. If you can't win then try to find a way around.\n"
        ret += "- Enemies will chase you, and know where you are. Attacking them\n\twhen you see them will help you avoid getting flanked.\n"
        
    else:
        ret = "Invalid option!"
        
    return ret + "\n[Select an option or press 'h' to escape]"
