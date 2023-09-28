import config
from parser import scrapping

if __name__ == "__main__":
    scrapping.get_data (config.PAGE_URL, config.DATA_PATH)
