print("deneme")
def check_temperature(temperature_data):
    min_temp, max_temp = temperature_data

    if min_temp < 0:
        return "Dondurucu"
    elif min_temp < 10:
        return "Soguk"
    elif max_temp > 30:
        return "Sicak"
    else:
        return "Hava"

temperature_range = (-5, 25)
result = check_temperature(temperature_range)
print(result)
print("deneme")