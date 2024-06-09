from os import path, environ
import requests
import yaml

API_TOKEN_ENV: str = "UPLOAD_API_TOKEN"
BOT_ID_ENV: str = "UPLOAD_BOT_ID"
CONFIG_FILE: str = "config.yml"
MY_BOT_NAME: str = "MyBotName"
ZIPFILE_NAME: str = "bot.zip"

TOKEN: str = environ.get(API_TOKEN_ENV)
BOT_ID: str = environ.get(BOT_ID_ENV)
URL: str = f"https://aiarena.net/api/bots/{BOT_ID}/"


def get_bot_description() -> str:
    """
    Generate bot description
    REPLACE WITH OWN LOGIC HERE
    By default, attempts to get bot name from config
    and generate a basic description.
    """
    bot_name: str = "MyBot"
    __user_config_location__: str = path.abspath(".")
    user_config_path: str = path.join(__user_config_location__, CONFIG_FILE)
    # attempt to get race and bot name from config file if they exist
    if path.isfile(user_config_path):
        with open(user_config_path) as config_file:
            config: dict = yaml.safe_load(config_file)
            if MY_BOT_NAME in config:
                bot_name = config[MY_BOT_NAME]

    return (
        f"# {bot_name} <br />  "
        "This bot is designed to showcase some useful features in "
        "ares-sc2 and to serve as an example project. <br >  "
        "[Bot Repo](https://github.com/AresSC2/ares-random-example) <br/>  "
        "Made with [ares-sc2](https://github.com/AresSC2/ares-sc2)"
    )


if __name__ == "__main__":
    print("Uploading bot")
    with open(ZIPFILE_NAME, "rb") as bot_zip:
        request_headers = {
            "Authorization": f"Token {TOKEN}",
        }
        request_data = {
            "bot_zip_publicly_downloadable": True,
            "bot_data_publicly_downloadable": False,
            "bot_data_enabled": False,
            "wiki_article_content": get_bot_description(),
        }
        request_files = {
            "bot_zip": bot_zip,
        }
        print(URL)
        response = requests.patch(
            URL, headers=request_headers, data=request_data, files=request_files
        )
        print(response)
        print(response.content)
