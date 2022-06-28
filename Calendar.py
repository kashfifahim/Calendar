'''Calendar class acts as an object manager for the Entry objects'''
'''written by Kashfi Fahim'''
'''kashfi.fahim@gmail.com'''

from datetime import datetime
from Entry import Entry

class Calendar():
	'''Calendar object will manage a list of Entry objects holding the events'''
	def __init__(self):
		self.entryList = [] 
		self.todayIs = datetime.now()

	'''The Calendar object needs to update todayIs attribute'''
	def updateDate(self):
		self.todayIs = datetime.now()		

	'''Create a row of an Entry object'''
	def createRow(self, title, start_date, end_date, location, country, talkDeadline, tutorialDeadline):
		anEntry = Entry(title, start_date, end_date, location, country, talkDeadline, tutorialDeadline)
		self.entryList.append(anEntry)
		return self.entryList[-1]

	'''Display the rows'''
	def show(self):
		for num, entry in enumerate(self.entryList):
			print (num, entry.show())

	def sortList(self):
		pass
