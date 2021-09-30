import os


def env_run():
    if "URL_ENV" in os.environ:
        url = os.environ["URL_ENV"]
    else:
        url = str(os.getenv("URL_ENV"))
    return url

def env_user():
    if "URL_ENV" in os.environ:
        user = os.environ["USERNAME"]
    else:
        user = str(os.getenv("USERNAME"))
    return user

def env_user_password():
    if "URL_ENV" in os.environ:
        password = os.environ["PASSWORD"]
    else:
        password = str(os.getenv("PASSWORD"))
    return password

def env_user_email():
    if "USEREMAIL" in os.environ:
        URL = os.environ["USEREMAIL"]
    else:
        URL = str(os.getenv("USEREMAIL"))
    return URL


ENV_URL = env_run()
ENV_USER_MAIL = env_user_email()
ENV_PASSWORD = env_user_password()