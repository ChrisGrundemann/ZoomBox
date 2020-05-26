from O365 import Account, FileSystemTokenBackend, MSGraphProtocol
import creds
import time
import datetime

# set vars
token_backend = FileSystemTokenBackend(token_path='auth_token', token_filename='o365_auth_token.txt')
protocol = MSGraphProtocol()
scopes = ['User.Read', 'Calendars.Read', 'offline_access']
account = Account(creds.credentials, token_backend=token_backend, protocol=protocol)
schedule = account.schedule()
calendar = schedule.get_default_calendar()

# find out when it is
now = float(time.time())
print(now)
today = datetime.datetime.now()
print(today)

# query the calendar
q = calendar.new_query('start').greater_equal(datetime.datetime(2020, 5, 26))
q.chain('and').on_attribute('end').less_equal(datetime.datetime(2020, 5, 27))


# print out the events
events = calendar.get_events(query=q, include_recurring=True)

for event in events:
    print(event)
    print(event.location)
