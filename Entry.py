'''Entries class'''
'''written by Kashi Fahim'''
'''kashfi.fahim@gmail.com'''

from datetime import date

class Entry():
	def __init__(self, title, start_date, end_date, location, country, talk_deadline, tutorial_deadline):
		self.title = title
		self.start_date = start_date
		self.end_date = end_date
		self.location = location
		self.country = country
		self.talk_deadline = talk_deadline
		self.tutorial_deadline = tutorial_deadline



	'''For testing, debugging purposes'''
	def show(self):
		print('Title', self.title)
		print('Start Date:', self.start_date)
		print('End Date:', self.end_date)
		print('Country:', self.country)
		print('Talk Deadline', self.talk_deadline)
		print('Tutorial Deadline', self.tutorial_deadline)
		print()

