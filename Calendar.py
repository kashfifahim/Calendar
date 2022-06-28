'''Calendar class acts as an object manager for the Entry objects'''
'''written by Kashfi Fahim'''
'''kashfi.fahim@gmail.com'''

from datetime import datetime
from Entry import Entry
import pandas as pd

class Calendar():
	'''Calendar object will manage a list of Entry objects holding the events'''
	def __init__(self):
		self.entryList = [] 
		self.todayIs = datetime.now()

	def start_with_URL(self, url):
		data = pd.read_csv(url)
		calendar_frame = pd.DataFrame(
		{
			"Title" : data["Subject"],
			"Start date" : data["Start Date"],
			"End date" : data["End Date"],
			"Country" : data["Country"],
			"Location" : data["Location"],
			"Talk deadline" : data["Talk Deadline"],
			"Tutorial deadline" : data["Tutorial Deadline"],
		})
		self.from_calendar_frame(calendar_frame)


	'''The Calendar object needs to update todayIs attribute'''
	def updateDate(self):
		self.todayIs = datetime.now()		

	'''Create a row of an Entry object'''
	def createRow(self, title, start_date, end_date, location, country, talkDeadline, tutorialDeadline):
		anEntry = Entry(title, start_date, end_date, location, country, talkDeadline, tutorialDeadline)
		self.entryList.append(anEntry)
		# return self.entryList[-1]

	def from_calendar_frame(self, calendar_frame):
		for title, start_date, end_date, location, country, talk_deadline, tutorial_deadline in zip(calendar_frame['Title'], calendar_frame['Start date'], calendar_frame['End date'], calendar_frame['Country'], calendar_frame['Location'], calendar_frame['Talk deadline'], calendar_frame['Tutorial deadline']):
			self.createRow(title, (start_date), (end_date), location, country, (talk_deadline), (tutorial_deadline))

	'''Display the rows'''
	def show(self):
		for num, entry in enumerate(self.entryList):
			print (num, entry.show())

	def sortList(self):
		pass
