"""
Equations:
F = ( C * 1.8 ) + 32
C = ( F - 32 ) / 1.8
C = K - 273.15
K = C + 273.15
F = (( K - 273.15 ) * 1.8 ) + 32
K = (( F - 32 ) / 1.8 ) + 273.15

Options:
1 and 3 from Celsius
2 and 5 from Fahrenheit
4 and 6 from Kelvin
"""

# CELSIUS FROM/TO FAHRENHEIT SECTION


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    t_celsius = float((fahrenheit - 32) / 1.8)
    return t_celsius


def celsius_to_fahrenheit(celsius: float) -> float:
    t_fahrenheit = float((celsius * 1.8) + 32)
    return t_fahrenheit


# KELVIN FROM/TO CELSIUS SECTION


def celsius_to_kelvin(celsius: float) -> float:
    t_kelvin = float(celsius + 273.15)
    return t_kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    t_celsius = float(kelvin - 273.15)
    return t_celsius


# KELVIN FROM/TO FAHRENHEIT SECTION


def kelvin_to_fahrenheit(kelvin: float) -> float:
    t_celsius = float(((kelvin - 273.15) * 1.8) + 32)
    return t_celsius


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    t_kelvin = float(((fahrenheit - 32) / 1.8) + 273.15)
    return t_kelvin


def get_temperature(option: str) -> float:
    str_temperature = ""
    """
    based on user option,  print the converted-from temperature
    in case user forgot what temperature its converting from
    """
    if option in ["1", "3"]:
        str_temperature = "Celsius"

    elif option in ["2", "5"]:
        str_temperature = "Fahrenheit"

    elif option in ["4", "6"]:
        str_temperature = "Kelvin"
    """
    in case user entered an invalid value and
    don't want to start again from the start menu
    so keep asking for value until it is valid
    """
    while True:
        try:
            temperature = float(
                input(f"Enter a temperature in {str_temperature}: "))
        except ValueError:
            print("\nPlease, enter a valid temperature")
            continue
        else:
            return temperature


def convert(option: str) -> str:
    """
    execute the right function based on user input
    get_temperatur to print right converted-from temperature and get its value
    """
    match option:
        case "1":
            return "\nFahrenheit: " + str(
                "%0.2f" % celsius_to_fahrenheit(get_temperature(option))
            )
        case "2":
            return "\nCelsius: " + str(
                "%0.2f" % fahrenheit_to_celsius(get_temperature(option))
            )
        case "3":
            return "\nKelvin: " + str(
                "%0.2f" % celsius_to_kelvin(get_temperature(option))
            )
        case "4":
            return "\nCelsius: " + str(
                "%0.2f" % kelvin_to_celsius(get_temperature(option))
            )
        case "5":
            return "\nFahrenheit: " + str(
                "%0.2f" % fahrenheit_to_kelvin(get_temperature(option))
            )
        case "6":
            return "\nKelvin: " + str(
                "%0.2f" % kelvin_to_fahrenheit(get_temperature(option))
            )
        case _:
            return "\nInvalid input!"


if __name__ == "__main__":

    while True:
        option = str(
            input(
                """
(1) Celsius to Fahrenheit
(2) Fahrenheit to Celsius
(3) Celsius to Kelvin
(4) Kelvin to Celsius
(5) Fahrenheit to Kelvin
(6) Kelvin to Fahrenheit
(q) Quit

Choose an option: """
            )
        )

        """
        for quitting.
        in case user entered capital (q).
        """
        if option.lower() == "q":
            print("\nQuitting..\n")
            break
        print(convert(option))
