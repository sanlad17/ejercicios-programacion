def celsius_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit
celsius = 25
print(f"{celsius}°C = {celsius_fahrenheit(celsius)}°F")