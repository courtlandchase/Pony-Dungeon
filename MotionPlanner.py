import Dungeon
from copy import copy, deepcopy

class MotionPlanner:
    def __init__(self):
        self.paths = None
        
    def plan(self, globs):
        dim = len(globs.dungeon)

        self.paths = Dungeon.adjMatrix(globs.dungeon)
        dists = deepcopy(self.paths)
        for i in range(len(dists)):
            for j in range(len(dists)):
                if dists[i][j] == 0:
                    dists[i][j] = 1E1000
                    self.paths[i][j] = None
                    
        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    edgeNum = dists[j][i] + dists[i][k]
                    if dists[j][k] > edgeNum:
                        dists[j][k] = edgeNum
                        self.paths[j][k] = self.paths[j][i]

    def nextStep(self, globs, pos):
        if not self.paths:
            self.plan(globs)
            
        nextRoom = None
        ret = copy(pos)
        croom = globs.dungeon[pos.roomnum]
        if globs.player.pos.roomnum != pos.roomnum:
            nextRoom = self.paths[pos.roomnum][globs.player.pos.roomnum]
            
            for i in range(len(croom.doors)):
                if nextRoom == croom.doors[i]:
                    break
                    
            if i == 0:
                if pos.x > 2:
                    ret.x -= 1
                elif pos.y > 1:
                    ret.y -= 1
                else:
                    ret.roomnum = nextRoom
            elif i == 1:
                if pos.x < croom.width - 3:
                    ret.x += 1
                elif pos.y > 1:
                    ret.y -= 1
                else:
                    ret.roomnum = nextRoom
            elif i == 2:
                if pos.x > 2:
                    ret.x -= 1
                elif pos.y < croom.height:
                    ret.y += 1
                else:
                    ret.roomnum = nextRoom
            else:
                if pos.x < croom.width - 2:
                    ret.x += 1
                elif pos.y < croom.height:
                    ret.y += 1
                else:
                    ret.roomnum = nextRoom
        else:
            pp = globs.player.pos
            dy = abs(pos.y - pp.y)
            dx = abs(pos.x - pp.x)

            if pos.y > pp.y and dx or pos.y - 1 > pp.y:
                ret.y -= 1
            elif pos.y < pp.y and dx or pos.y + 1 < pp.y:
                ret.y += 1
            else:
                if pos.x > pp.x and dy or pos.x - 1 > pp.x:
                    ret.x -= 1
                elif pos.x < pp.x and dx or pos.x + 1 < pp.x:
                    ret.x += 1

        if ret.roomnum == nextRoom:
            nrooms = globs.dungeon[nextRoom].doors
            for i in range(len(nrooms)):
                if nrooms[i] == croom:
                    break

            if i == 0:
                ret.x = 2
                ret.y = 1
            elif i == 1:
                ret.x = globs.dungeon[nextRoom].width - 2
                ret.y = 1
            elif i == 2:
                ret.x = 2
                ret.y = globs.dungeon[nextRoom].height
            else:
                ret.x = globs.dungeon[nextRoom].width - 2
                ret.y = globs.dungeon[nextRoom].height

        return ret
