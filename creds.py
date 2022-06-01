import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred():
    BOT_TOKEN = os.getenv("5427244127:AAGj7pGJSX5jg26yje-FdkWGGrfOqHH0LT8") #From botfather
    API_ID = os.getenv("8822241")       #"Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv("8f3ec71ce143e1091908837896e567c3")   #"Get this value from my.telegram.org! Please do not steal"
    DB_URL = os.getenv("https://userinfo-84a02-default-rtdb.asia-southeast1.firebasedatabase.app

")       #From Firebase database

    ####From Truecaller and Eyecon app request headers respectively########

    T_AUTH = os.getenv("T_AUTH")      # Truecaller auth id CA
    E_AUTH = os.getenv("E_AUTH")      # Eyecon auth id
    E_AUTH_V=os.getenv("E_AUTH_V")    # Eyecon auth_v
    E_AUTH_C=os.getenv("E_AUTH_C")    # Eyecon auth_c
