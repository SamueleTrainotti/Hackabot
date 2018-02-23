# -*- coding: utf-8 -*-

import csv
import io
import json
from time import sleep

import telegram
from telegram.error import NetworkError, Unauthorized

import requests

myToken = '501102931:AAH8ZGgJ_C4u0RYLyvpDoEDDX-0uxo1ZyUs'


if __name__ == '__main__':
    start_bot()    
