# pip install python-dotenv
# resumo: https://github.com/theskumar/python-dotenv
# case sensitive .env
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("USUARIO"))
print(type(os.getenv("USUARIO")))
# print(os.getenv("DEBUG"))
# print(type(os.getenv("DEBUG")))
DEBUG = eval(os.getenv("DEBUG", "False"))
print(DEBUG)
print(type(DEBUG))

print(os.getenv("DATABASE_URL"))
print(os.getenv("DATABASE_URL_FIXO"))
