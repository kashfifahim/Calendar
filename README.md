# Calendar Project

## 02 6/21 Create sort method for Calendar object to sort by event deadlines
	[] create new sort method
		[] test out the sort method to display in order of ascending dates	
	[X] create an instance variable for Calendar to hold the date
	[X] create a method that will update the date

## 01 6/20 Create Entry, Calendar Classes
	[X] create new project
	[X] create venv
	[ ] create Entry class
		[x] what data will an entry hold?
			[x] Research date from datetime
				[x] each entry will need to be instantiated with
					[x] title, string type
					[x] start date, date type
					[x] end date, date type
					[x] location, string type
					[x] country, string type
					[x] talk deadline, date type
					[x] tutorial deadline, data type	
		[ ] what kind of operations will we need this class to perform with that data?
	[ ] create a Calendar class
		Calendar class will manage the Entries
			[ ] what kind of data does a Calendar need to remember to manage entries?
				[-] using a dictionary to store the Entry objects
				[x] might be better to use a list to store the Entry objects
				[x] Calendar remembers the listobjects
				[-] Current date
			[ ] what kind of methods should it have
				- I need these Calendar objects to sort the entries
				- reverse the sorting
				- I also need the Calendar to remove Entry objects that have past
				deadlines

## Backlog
	[] A calendar method that will update the list by removing the events that have past
	[] Entry attribute that calculates how many days left before the deadline
