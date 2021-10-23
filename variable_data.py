from env_setup import env_type, main_user
from src.additional_methods.additional_methods import read_json_file
from os.path import dirname, abspath


ROOT_DIR = dirname(abspath(__file__))

user_data = read_json_file(ROOT_DIR+"/src/data_for_tests/data.json")


env = env_type()
main_user = main_user()

url_env = user_data[env]["url"]
email_main_user = user_data[env]["users"][main_user]["email"]
password_user = user_data[env]["users"][main_user]["password"]