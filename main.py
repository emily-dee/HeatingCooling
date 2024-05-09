def heating_cooling(actual_temp: int, desired_temp: int) -> str:
    print(f'Current Temp {actual_temp}')
    print(f'Desired Temp {desired_temp}')
    if actual_temp > desired_temp:
        thermostat_action = 'Run A/C'
    elif actual_temp < desired_temp:
        thermostat_action = 'Run heat'
    else:
        thermostat_action = 'Standby'
    return thermostat_action


print(heating_cooling(60, 70))
print()
print(heating_cooling(68, 65))
print()
print(heating_cooling(100, 2))
print()
print(heating_cooling(72, 72))
print()

# Gather user input
user_current_temp = int(input('Enter the current temperature: '))
user_desired_temp = int(input('Enter the desired temperature: '))

# calling function with user inputs
print(heating_cooling(user_current_temp, user_desired_temp))
print()


# convert temp unit
def convert_temp(temp_celsius: int, target_unit: str) -> int:
    if target_unit == 'F':
        target_temp = temp_celsius * 1.8 + 32
        print(f'{temp_celsius}\N{DEGREE SIGN}C in Fahrenheit is {target_temp}\N{DEGREE SIGN}F')
    elif target_unit == 'K':
        target_temp = temp_celsius + 273.15
        print(f'{temp_celsius}\N{DEGREE SIGN}C in Kelvin is {target_temp}\N{DEGREE SIGN}K')
    else:
        target_temp = temp_celsius
        print(f'No conversion for {temp_celsius}\N{DEGREE SIGN}C')
    return target_temp


convert_temp(30, 'F')
print()
convert_temp(30, 'C')
print()
convert_temp(2, 'K')
print()

# gathering user preferences
user_current_celsius = int(input('What is your current temp in celsius? '))
user_target_unit = input('What unit would you like to convert to? C, F, or K: ')

# calling function with user inputs
convert_temp(user_current_celsius, user_target_unit)
