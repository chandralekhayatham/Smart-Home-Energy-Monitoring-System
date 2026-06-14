def calculate_power(voltage, current):
    return round(voltage * current, 2)

def calculate_energy(power):
    return round(power / 1000, 2)

def calculate_cost(energy):
    return round(energy * 8, 2)