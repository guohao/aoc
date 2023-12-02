import logging
import configparser
import os
import requests
from typing import List

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(current_file_path)

config = configparser.ConfigParser()
config.read(os.path.join(project_root, 'config.ini'))


def name_to_path(file_name: str) -> str:
    return os.path.join(project_root, 'data', file_name)


def day_input_file_name(day: int) -> str:
    return name_to_path(f'day{day}.txt')


def download_input_if_not_exist(day: int):
    if not os.path.exists(day_input_file_name(day)):
        download_input(day)
    else:
        logging.info(f"day{day} input data already existed,skip download")


def download_input(day: int):
    logging.info(f"Downloading day{day} input data...")
    url = f"https://adventofcode.com/2023/day/{day}/input"
    headers = {
        'authority': 'adventofcode.com',
        'cookie': config['settings']['cookie'],
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(name_to_path(f'day{day}.txt'), 'w') as file:
            file.write(response.text)
    else:
        print(f"Failed to download the data for day {day}. Status code: {response.status_code}")


def get_day_input(day: int) -> List[str]:
    download_input_if_not_exist(day)
    file_name = day_input_file_name(day)
    return read_file_to_list(file_name)


def read_file_to_list(file_name: str) -> List[str]:
    file_path = name_to_path(file_name)
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
