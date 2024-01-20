# DorkFinder
Automatic tool to find Google Dorks using useful payloads with minimum false-positive checks. 

![Logo](https://github.com/glavstroy/DorkFinder/blob/main/img/logo.png)

## Install

```bash
git clone https://github.com/glavstroy/DorkFinder
cd DorkFinder
pip install -r requirements
```

## Usage

```bash
python3 dorkfinder.py -t example.com -o
```

![Usage](https://github.com/glavstroy/DorkFinder/blob/main/img/usage.png)

## Flags

```bash
python3 dorkfinder.py -h
```

This will display help for the tool. Here are all the switches it supports.

| Flag           | Description                                          |
|----------------|------------------------------------------------------|
| -h/--help      | show this help message and exit                      |
| -t             | enter the target domain                              |
| -o             | print to output.txt                                  |

### Warning
Use it only for educational purposes! I assume no responsibility :)
