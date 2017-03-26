# Assignment 10
# File Name temperatureController.py contains TemperatureController

import tkinter
import week10.converter as converter            # the MODEL
import week10.temperatureView as temperatureView    # the View


class TemperatureController:
    """
    TemperatureController (Controller)  creates and holds a reference to TemperatureView object (View) and Converter Object (Model)
    When the User executes an action on View, the Controller handles the action and if required calls the appropriate method in the Model
    The Controller handles all communication between the Model and the View.
    """

    CtoF = 'CtoF'  # Conversion direction C to F
    FtoC = 'FtoC'  # Conversion direction F to C
    DEGREE_SYMBOL = u'\u00b0'  # Degree Symbol
    FAHRENHEIT = DEGREE_SYMBOL + 'F'  # Degree F
    CELSIUS = DEGREE_SYMBOL + 'C'  # Degree C

    def __init__(self):

        """
        This starts the Tk framework up, instantiates the Model (a Converter object),
        instantiates the View (a TemperatureView object), and starts the event loop that waits for the users actions.
        """

        self.root = tkinter.Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.quit)  # Handles the Window Close
        self.root.title("Temperature Conversion")  # Window Title
        self.model = converter.Converter()  # create the Model Object

        self.temperatureBoxLabelVar = tkinter.StringVar()  # Temperature Unit Label
        self.temperatureBoxLabelVar.set(
            TemperatureController.FAHRENHEIT)  # Set Inital Input Temperature Unit Label
        self.convertedTemperatureBoxLabelVar = tkinter.StringVar()  # Converted Temperature Unit Label
        self.convertedTemperatureBoxLabelVar.set(
            TemperatureController.CELSIUS)  # Set Inital Converted Temperature Unit Label

        self.temperatureToConvert = tkinter.StringVar()  # Temperature to Converted Value
        self.temperatureToConvert.set('')  # Temperature to Converted initial value
        self.temperatureToConvert.trace("w", self.temperatureBoxUpdate)  # Temperature to Converted write handler
        self.convertedTemperature = tkinter.StringVar()  # Converted Temperature
        self.convertedTemperature.set('')  # Converted Temperature initial value

        self.conversionVar = tkinter.StringVar()  # Temperature convertion direction
        self.conversionVar.set(TemperatureController.FtoC)  # Temperature convertion initial direction

        self.view = temperatureView.TemperatureView(self)  # Create TemperatureView (View)
        self.view.mainloop()  # Start Main Loop

    def convertPressed(self):

        """
            Python calls this method when the user presses the convert Buttoon in the View.
        """
        temperatureStringInput = self.temperatureToConvert.get()  # Get conversion temperature
        if temperatureStringInput == '':
            return  # conversion Temperature is empty
        try:
            temperature = float(temperatureStringInput)  # type cast conversion temperature to float
            direction = self.conversionVar.get()  # Get conversion direction
            if direction == TemperatureController.FtoC:  # Convert Temperature
                self.model.convert(temperature, True)
            elif direction == TemperatureController.CtoF:
                self.model.convert(temperature, False)
            else:
                return  # Unknown Direction ... Do nothing
            self.convertedTemperature.set(str(self.model))  # Set the converted temperature
        except ValueError:
            self.convertedTemperature.set('Invalid Input')

    def conversionDirectionChanged(self):
        """
            Python calls this method when the user changes the conversion direction
        """
        direction = self.conversionVar.get()  # Get conversion direction
        if direction == TemperatureController.FtoC:  # Update Unit Labels ( Temperature to convert and converted temperature)
            self.temperatureBoxLabelVar.set(TemperatureController.FAHRENHEIT)
            self.convertedTemperatureBoxLabelVar.set(TemperatureController.CELSIUS)
        elif direction == TemperatureController.CtoF:
            self.temperatureBoxLabelVar.set(TemperatureController.CELSIUS)
            self.convertedTemperatureBoxLabelVar.set(TemperatureController.FAHRENHEIT)

        if self.temperatureToConvert.get() != '' and self.convertedTemperature.get() != '':  # Update the conversion
            self.convertPressed()

    def temperatureBoxUpdate(self, *args):
        """
           Python calls this method when the user changes the input temperature
       """
        self.convertedTemperature.set('')  # Clears the converted temperature

    def quit(self):
        """
            Python calls this method when the user changes the input temperature
        """
        self.root.destroy()  # destroys the window... cleanup


if __name__ == "__main__":
    """
            Creates a TemperatureContoller (Controller) object
    """
    tc = TemperatureController()
