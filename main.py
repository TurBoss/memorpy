import shlex, subprocess
import os

from admin import checkAdmin
import time

from memWorker import MemWorker


def runGame(path):

	rc = subprocess.Popen(path, shell=True)
		
	return rc
 
def attachToGame():
	
	time.sleep(5)
	
	mw = MemWorker("ff7")
	
	
	#addr = mw.Address("\x00DC0BE2")
	#print(addr)
	text = input("String search :> ")
	l=[x for x in mw.mem_search(text)]
	a = [x for x in l]
		
	print(l)

	val = int(input("Select Offset :> "))

	a[val].dump()

	#for x in a:
	#	x.dump()

if __name__ == "__main__":

	if checkAdmin():
		game = runGame(os.path.join("C:/", "PortableApps", "Square Soft, Inc", "Final Fantasy VII", "ff7.exe"))
	
		if game:
			attachToGame()
	else:
		print("Nseeds to be run as admin")
