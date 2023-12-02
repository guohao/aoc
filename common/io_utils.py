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


def day_data_file_name(day: int) -> str:
    return os.path.join(data_dir, f'day{day}.txt')


def download_input_if_not_exist(day: int):
    if not os.path.exists(day_data_file_name(day)):
        download_input(day)
    else:
        logging.info(f"day{day} input data already existed, skip download")


def raw_str_to_lines(input: str) -> List[str]:
    lines = input.splitlines()
    return [line.strip() for line in lines if line and len(line.strip()) > 0]


def download_input(day: int):
    logging.info(f"Downloading day{day} input data...")
    url = f"https://adventofcode.com/2023/day/{day}/input"
    headers = {
        'authority': 'adventofcode.com',
        'cookie': config['settings']['cookie'],
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        with open(day_data_file_name(day), 'w') as file:
            file.write(response.text)
    else:
        raise Exception(f"Failed to download the data for day {day}. Status code: {response.status_code}")


def get_day_input(day: int) -> List[str]:
    download_input_if_not_exist(day)
    file_name = day_data_file_name(day)
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]
