import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import seaborn as sns
import numpy as np
import datetime 

from citipy import citipy
import openweathermapy as owm
now = datetime.datetime.now()

url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "c8a4b6c487e97bc9f1940df7758a0f72"
units = "imperial"

