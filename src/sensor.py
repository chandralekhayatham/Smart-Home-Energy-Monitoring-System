import random

def get_voltage():
    return random.randint(220, 240)

def get_current():
    return round(random.uniform(0.5, 5.0), 2)