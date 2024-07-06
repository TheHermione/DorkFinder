# DorkFinder
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/TheHermione/DorkFinder/issues)

Automatic tool to find Google Dorks using useful payloads with minimum false-positive checks. 

![Logo](https://github.com/TheHermione/DorkFinder/blob/main/img/main.png)

## Install

### Linux

```bash
git clone https://github.com/TheHermione/DorkFinder
cd DorkFinder
pip install -r requirements
```

### Docker

```bash
git clone https://github.com/TheHermione/DorkFinder
cd DorkFinder
sudo docker build . -t dorkfinder
sudo docker run -it --rm dorkfinder
```

## Usage

```bash
python3 dorkfinder.py -t example.com -o
```

Another way to continue a Linux script even after closing the SSH session, you can use the `nohup` command (short for "no hang up"). Here's how to do it:

```bash
nohup python3 dorkfinder.py -t example.com -o &
```

![Usage](https://github.com/TheHermione/DorkFinder/blob/main/img/usage.png)

## Flags

```bash
python3 dorkfinder.py -h
```

It will display help for the tool. Here are all the switches it supports.

| Flag           | Description                                          |
|----------------|------------------------------------------------------|
| -h/--help      | show this help message and exit                      |
| -t             | enter the target domain                              |
| -o             | print to output.txt                                  |

## Disclaimer
Use it only for educational purposes! I assume no responsibility :)
