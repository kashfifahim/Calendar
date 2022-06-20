'''Entries class'''
'''written by Kashi Fahim'''
'''kashfi.fahim@gmail.com'''

from datetime import date

class Entry():
	def __init__(self, title, start_date, end_date, location, country, talk_deadline, tutorial_deadline):
	self.title = title
	self.start_date = date.fromisoformat(start_date)
	self.end_date = date.fromisoformat(end_date)
	self.country = country
	self.talk_deadline = date.fromisoformat(talk_deadline)
	self.tutorial_deadline = date.fromisoformat(tutorial_deadline)



	'''For testing, debugging purposes'''
	def show(self):
		print('Title', self.title)
		print('Start Date:', self.start_date)
		print('End Date:', self.end_date)
		print('Country:', self.country)
		print('Talk Deadline', self.talk_deadline)
		print('Tutorial Deadline', self.tutorial_deadline)
		print()

