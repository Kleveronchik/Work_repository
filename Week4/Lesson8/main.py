from logging import *
from logger import Logger
'''
from Week4.Lesson7.decorator import Checker
basicConfig(level=CRITICAL,#DEBUG
            filename='loggingFile.log',
            filemode='a',#'w'
            format='Logging message: %(asctime)s : %(levelname)s - %(message)s')
'''
'''
debug("debug message")
info("info message")
warning("warning message")
error("error message")
critical("critical message")
'''
logger = Logger(DEBUG, 'loggingFile.log', 'a')
try:
    checker = Checker()
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    operation = input("Select operation[/*-+]: ")
    checker.Calculate(f'{digit1}{operation}{digit2}')
except Exception as ex:
    logger.Log(ERROR, ex)