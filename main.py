from decouple import config
from compoments.dcbot import Bot


def main():
    dcbot = Bot()
    dcbot.run(config('dc_token'))

if __name__ == "__main__":
    main()
