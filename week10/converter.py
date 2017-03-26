# In File converter.py contains Converter class


class Converter:
    """
        Converter (Model) coverts temperature from fahrenheit to celsius or from celsius to fahrenheit

    """

    def __init__(self):
        """
          Sets the converted temperature NAN
        """
        self.convertedTemperature = float('nan')

    def convert(self, temperature, fahrenheitToCelsius):
        """
            Convert "temperature" from  fahrenheit to celsius or from celsius to fahrenheit
        """
        self.convertedTemperature = temperature
        if fahrenheitToCelsius == True:
            self.convertedTemperature = (temperature - 32) * 5 / 9
        else:
            self.convertedTemperature = temperature * (9 / 5) + 32

    def __str__(self):
        """
            Returns the converted Temperature
        """
        return str(self.convertedTemperature)