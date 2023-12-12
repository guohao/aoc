import configparser
import logging
import os
from typing import List

import requests

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))
data_dir = os.path.join(project_root, 'data')

config = configparser.ConfigParser()
config.read(os.path.join(project_root, 'config.ini'))


def data_dir_of(year: int) -> str:
    return os.path.join(data_dir, f'{year}')


def day_data_file_name(year: int, day: int) -> str:
    return os.path.join(data_dir_of(year), f'day{day}.txt')


def download_input_if_not_exist(year: int, day: int):
    if not os.path.exists(day_data_file_name(year, day)):
        download_input(year, day)
    else:
        logging.info(f"year:{year} day{day} data already existed, skip download")


def download_input(year: int, day: int):
    logging.info(f"Downloading year:{year} day:{day} input data...")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        'authority': 'adventofcode.com',
        'cookie': config['settings']['cookie'],
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        os.makedirs(data_dir_of(year), exist_ok=True)
        with open(day_data_file_name(year, day), 'w') as file:
            file.write(response.text)
    else:
        raise Exception(f"Failed to download the data for year:{year} day:{day}. Status code: {response.status_code}")
