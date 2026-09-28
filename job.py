import os

a = 2
print("coucou", a)

token = os.environ.get("SECRET_API_TOKEN")
print("Secret présent :", token is not None)
print("Secret correct :", token == "42")
