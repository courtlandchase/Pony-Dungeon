class MotionPlanner:
    def __init__(self, pos, dungeon, stimuli = []):
        self.path = []
        self.pos = pos
        self.dungeon = dungeon
        self.stimuli = stimuli
        self.plan()
        
    def canSee(self, pos):
        return self.pos.roomnum == pos.roomnum
        
    def plan(self):
        sees = []
        dists = []
        for stimulus in stimuli:
            if self.canSee(stimulus.pos):
                pass

        #todo: find shortest path and take it

    def step(self):
        return path.pop()
