def save(globs):
	fd = open("save.txt", "a")
	fd.write(globs.name + "," + str(globs.score) + "\n")
