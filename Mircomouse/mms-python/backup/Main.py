import API
import sys

def log(string):
	sys.stderr.write("{}\n".format(string))
	sys.stderr.flush()

def leftHand():
	if not API.wallLeft():
		API.turnLeft()
	while API.wallFront():
		API.turnRight()
	API.moveForward()

def rightHand():
	if not API.wallRight():
		API.turnRight()
	while API.wallFront():
		API.turnLeft()
	API.moveForward()

def centralLeft():
	while not API.wallFront():
		API.moveForward()
	if not API.wallLeft():
		API.turnLeft()
	else:
		API.turnRight()

def centralRight():
	while not API.wallFront():
		API.moveForward()
	if not API.wallRight():
		API.turnRight()
	else:
		API.turnLeft()

def main():
	log("Running...")
	API.setColor(0, 0, "G")
	API.setText(0, 0, "abc")
	API.setColor(15, 15, "G")
	API.setWall(15,15,'n')
	API.setWall(15,15,'e')
	API.moveForward()
	while True:
		centralRight()

if __name__ == "__main__":
	main()
