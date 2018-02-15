# nexudus-python-api

Usage:

nexudus = AccessToken('username', 'password')
api_call = nexudus.update_access_token(
    Id=1,
    BusinessId=1243,
    AccessCode='1234',
    MinutesIncluded=20,
    MinutesLeft=0)