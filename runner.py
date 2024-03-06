#!/opt/homebrew/bin/python3.12
import logging
import os
import sys

import importlib.util
import requests

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))
data_dir = os.path.join(project_root, 'data')


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
        'cookie': '_ga=GA1.2.707255201.1701140283; session=53616c7465645f5f50a9aeeee2ade75bbb28b0d47b1e7d81d3bcdee787c0d65a602f424dbabbe9e0d5549a3f7321fd1f6b3919bae00d2edec8950ab04100677d; _gid=GA1.2.1834388923.1709519036; _gat=1; _ga_MHSNPJKWC7=GS1.2.1709691961.154.1.1709695383.0.0.0',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        os.makedirs(data_dir_of(year), exist_ok=True)
        with open(day_data_file_name(year, day), 'w') as file:
            file.write(response.text)
    else:
        raise Exception(f"Failed to download the data for year:{year} day:{day}. Status code: {response.status_code}")


def raw_data(year: int, day: int) -> str:
    download_input_if_not_exist(year, day)
    file_name = day_data_file_name(year, day)
    with open(file_name, 'r') as file:
        return file.read()


import pyperclip

if __name__ == '__main__':
    year = '2017'
    day = '17'
    if len(sys.argv) == 2:
        day = sys.argv[1]
    elif len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]
    sys.path.append('/' + year)

    module_file = f'{year}/{day}.py'  # 替换为你的文件实际路径
    function_name = 'p1'

    spec = importlib.util.spec_from_file_location(day, module_file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[day] = mod
    spec.loader.exec_module(mod)
    mod = importlib.import_module(day)
    func = getattr(mod, 'p1')
    data = raw_data(int(year), int(day))
    ans = func(data)
    if ans:
        pyperclip.copy(ans)
    print(ans)
    func = getattr(mod, 'p2')
    ans = func(data)
    if ans:
        pyperclip.copy(ans)
    print(ans)
