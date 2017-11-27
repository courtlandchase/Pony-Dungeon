import Dungeon

d = Dungeon.genDungeon()
room = d[0]
print(room.show())

room = d[room.doors[0]]
print(room.show())
