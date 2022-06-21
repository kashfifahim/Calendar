'''Calendar class acts as an object manager for the Entry objects'''
'''written by Kashfi Fahim'''
'''kashfi.fahim@gmail.com'''

import datetime
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
		newId = self.nextId
		self.entryDict[newId] = anEntry
		self.nextId += 1
		return newId

	'''Display the rows'''
	def show(self):
		for entryId in self.entryDict:
			anEntry = self.entryDict[entryId]
			print('Row:', entryId)
			anEntry.show() 

	def sortList(self):
		self.entryList.sort()
		return None
