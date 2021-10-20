import os
from scr.additional_methods.additional_methods import read_json_file
from os.path import dirname, abspath
from dotenv import load_dotenv
load_dotenv()

def env_type():
    url = os.environ["ENV_TYPE"]
    return url

def main_user():
    user = os.environ["MAIN_USER"]
    return user


# ENV_TYPE = env_type()
# MAIN_USER = main_user()
# PASSWORD_USER = env_user_password()

ROOT_DIR = dirname(abspath(__file__))