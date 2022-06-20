# Calendar Project

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
				- using a dictionary to store the Entry objects
				- Calendar remembers the dictionary object and remembers an integer
				value to use as a key for the next Entry object added to the dict
			[ ] what kind of methods should it have
				- I need these Calendar objects to sort the entries
				- I also need the Calendar to remove Entry objects that have past
				deadlines
