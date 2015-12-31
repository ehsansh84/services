__author__ = 'Ehsan'

from facebook import Facebook

api_key = '1523315421330779'
secret  = 'f2400983f41838547108ddad99fd5585'

session_key = 'your infinite Session key of user'

fb = Facebook(api_key, secret)
fb.session_key = session_key

# now use the fb object for playing around