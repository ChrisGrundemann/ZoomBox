from O365 import Account, FileSystemTokenBackend, MSGraphProtocol
import creds

# set vars
token_backend = FileSystemTokenBackend(token_path='auth_token', token_filename='o365_auth_token.txt')
protocol = MSGraphProtocol(default_resource=creds.user)
scopes = ['User.Read', 'Calendars.Read', 'offline_access']

# test auth
account = Account(creds.credentials, token_backend=token_backend, protocol=protocol)
if account.authenticate(scopes=scopes):
   print('Authenticated!!!')