'''Calendar class acts as an object manager for the Entry objects'''
'''written by Kashfi Fahim'''
'''kashfi.fahim@gmail.com'''

from Entry import Entry

class Calendar():
	def __init__(self):
		self.entryDict = {}
		self.nextId = 0

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
