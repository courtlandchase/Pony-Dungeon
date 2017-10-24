def help(op=0):
    ret = ""
    if not op:
        ret = "1. Rules.\n"
        + "2. Movement.\n"
        + "3. Items.\n"
        + "4. Fighting.\n"
    elif op == 1:
        ret = ""
        #todo: show all of these
    return ret
