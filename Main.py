'''Main Class'''
'''written by Kashfi Fahim'''
'''kashfi.fahim@gmail.com'''

from calendar import calendar
from Calendar import Calendar

'''2020 Conference Calendar'''
url = "https://raw.githubusercontent.com/python-organizers/conferences/master/2020.csv"
pycon2020 = Calendar()
pycon2020.start_with_URL(url)
pycon2020.show()

'''2021 Conference Calendar'''
url = "https://raw.githubusercontent.com/python-organizers/conferences/master/2021.csv"
pycon2020 = Calendar()
pycon2020.start_with_URL(url)
pycon2020.show()

'''2022 Conference Calendar'''
url = "https://raw.githubusercontent.com/python-organizers/conferences/master/2022.csv"
pycon2020 = Calendar()
pycon2020.start_with_URL(url)
pycon2020.show()










# '''Testing instantiation of a Calendar object'''
# pycon2022 = Calendar()
# pycon2022.createRow('KashfiCon', '2022-05-22', '2022-05-23', 'New York', 'USA', '2022-04-04', '2022-04-01')
# pycon2022.show()

# def start_With_Url(url):
#     data = pd.read_csv(url)
#     calendar_frame = pd.DataFrame(
#     {
#         "Title" : data["Subject"],
#         "Start date" : data["Start Date"],
#         "End date" : data["End Date"],
#         "Country" : data["Country"],
#         "Location" : data["Location"],
#         "Talk deadline" : data["Talk Deadline"],
#         "Tutorial deadline" : data["Tutorial Deadline"],
#     })
#     return calendar_frame

# '''Testing feeding csv to Calendar'''

# '''2020 Conference Calendar'''
#url = "https://raw.githubusercontent.com/python-organizers/conferences/master/2020.csv"
# calendar_frame = start_With_Url(url)
#pycon2020 = Calendar()
#pycon2020.start_with_URL(url)
# pycon2020.from_calendar_frame(calendar_frame)
#pycon2020.show()


# url = "https://raw.githubusercontent.com/python-organizers/conferences/master/2022.csv"
# # https://raw.githubusercontent.com/python-organizers/conferences/master/2022.csv

# data = pd.read_csv(url)
# # create calendar table from selected columns from data found in github 
# calendar_frame = pd.DataFrame(
#     {
#         "Title" : data["Subject"],
#         "Start date" : data["Start Date"],
#         "End date" : data["End Date"],
#         "Country" : data["Country"],
#         "Location" : data["Location"],
#         "Talk deadline" : data["Talk Deadline"],
#         "Tutorial deadline" : data["Tutorial Deadline"],
#     }
# )

# pycon2022 = Calendar()
# for title, start_date, end_date, location, country, talk_deadline, tutorial_deadline in zip(calendar_frame['Title'], calendar_frame['Start date'], calendar_frame['End date'], calendar_frame['Country'], calendar_frame['Location'], calendar_frame['Talk deadline'], calendar_frame['Tutorial deadline']):
#     pycon2022.createRow(title, (start_date), (end_date), location, country, (talk_deadline), (tutorial_deadline))

# pycon2022.show()

