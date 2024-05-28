#!/usr/bin/python3

import random

weather = {
    'sunny': {'sunny':0.7, 'rainy':0.1, 'cloudy':0.2},
    'rainy': {'sunny':0.1, 'rainy':0.6, 'cloudy':0.3},
    'cloudy': {'sunny':0.2, 'rainy':0.5, 'cloudy':0.3}
    }

def get_next_day(model, today):
    day_chance = random.random()
    today_chance = model[today]
    probability = 0
    for e in today_chance:
        probability+=today_chance[e]
        if day_chance<=probability:
            return e

print(get_next_day(weather, 'rainy'))

def get_forecast(model, days, start):
    n = 0
    day_current = start
    day_list = []
    while n < days:
        day_current = get_next_day(model, day_current)
        day_list.append(day_current)
        n+=1
    return day_list

print(get_forecast(weather, 10, 'sunny'))
