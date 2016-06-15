import shlex, subprocess
import os

from admin import check_admin
import time

from memWorker import MemWorker
from address import Address

class TurBoDebugger:
	
	def __init__(self, proc_name):
		
		self.mw = MemWorker(proc_name)
		
	def run_game(self, path):

		self.rc = subprocess.Popen(path, shell=True)
	 
		
	def options(self):
		
		print("what to do?")
		print("  1 search for text")
		print("  2 go to offset")
		self.option = int(input("1 or 2 :"))
		
		if self.option == 1:
			self.search_text()
		elif self.option == 2:
			self.go_offset()
		
		
	def search_text(self):
		
		text = input("Text search :> ")
		
		l= [x for x in self.mw.mem_search(text)]
		
		a = [x for x in l]
			
		print(l)
		print(a)

		val = int(input("Select Offset :> "))

		a[val].dump()

	def go_offset(self):
		
		print("go for it")

if __name__ == "__main__":
	
	if check_admin():
		
		tb = TurBoDebugger("ff7")
		tb.options()
		
	else:
		print("Nseeds to be run as admin")
