from O365 import Account
credentials = ('1dc00ae0-9a5e-4fed-9e59-b3328cf35dff', 'q1vg_F_aq94p2KTiRjPVD9E89Bx-.DXsuV')

account = Account(credentials)
if account.authenticate(scopes=['User.Read', 'Calendars.Read', 'offline_access']):
   print('Authenticated!!!')

