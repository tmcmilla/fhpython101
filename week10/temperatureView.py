# In file temperatureView.py contains TemperatureView class

import tkinter


class TemperatureView(tkinter.Frame):
    """
        The TemperatureView is a View that follows the Model/View/Controller architecture.
        Whern the user enters a temperature value and then select "convert",  the resulting temperture value will be determined by input temperature units and the out temperatrue units.

    """

    def __init__(self, controller):
        """
        Setup TemperatureView
        """
        tkinter.Frame.__init__(self)  # initializes the superclass
        self.pack()  # required in order for the Widgets to appear
        self.controller = controller  # saves a reference to the controller so that we can call methods
        self._addWidgets()  # Add controls

    def _addWidgets(self):
        """
            Places the controls onto the Frame.
        """
        self.temperatureToConvertLabel = tkinter.Label(self,
                                                       text='Temperature to Convert',
                                                       height=4).grid(row=0, column=0,
                                                                      sticky=tkinter.W)  # Add 'Temperature to Convert' Label
        self.temperatureBox = tkinter.Entry(self,
                                            textvariable=self.controller.temperatureToConvert,
                                            width=15).grid(row=0, column=1)  # Add 'Temperature to Convert' Entry

        self.temperatureBoxLabel = tkinter.Label(self,
                                                 textvariable=self.controller.temperatureBoxLabelVar).grid(row=0,
                                                                                                           column=2,
                                                                                                           sticky=tkinter.E)  # Add 'Temperature to Convert' Units

        self.FtoCRadioButton = tkinter.Radiobutton(self,
                                                   text=self.controller.FAHRENHEIT + ' to ' + self.controller.CELSIUS,
                                                   variable=self.controller.conversionVar,
                                                   command=self.controller.conversionDirectionChanged,
                                                   value=self.controller.FtoC).grid(row=1, column=0,
                                                                                    sticky=tkinter.W)  # Add Fahrenheit to Celsius Conversion Radio Button

        self.CtoFRadioButton = tkinter.Radiobutton(self,
                                                   text=self.controller.CELSIUS + ' to ' + self.controller.FAHRENHEIT,
                                                   variable=self.controller.conversionVar,
                                                   command=self.controller.conversionDirectionChanged,
                                                   value=self.controller.CtoF).grid(row=2, column=0,
                                                                                    sticky=tkinter.W)  # Add Celsius to Fahrenheit Conversion Radio Button

        self.convertedTemperatureLabel = tkinter.Label(self,
                                                       text='Converted Temperature',
                                                       height=4).grid(row=3, column=0,
                                                                      sticky=tkinter.W)  # Add 'Converted Temperature' Label
        self.convertedTemperatureBox = tkinter.Entry(self,
                                                     textvariable=self.controller.convertedTemperature,
                                                     width=15).grid(row=3,
                                                                    column=1)  # Add 'Converted Temperature' Entry
        self.convertedTemperatureBoxLabel = tkinter.Label(self,
                                                          textvariable=self.controller.convertedTemperatureBoxLabelVar).grid(
            row=3, column=2, sticky=tkinter.E)  # Add 'Converted Temperature' Units

        self.convertButton = tkinter.Button(self,
                                            text='Convert',
                                            command=self.controller.convertPressed).grid(row=4, column=0,
                                                                                         sticky=tkinter.E)  # Add 'Convert'Button
        self.quitButton = tkinter.Button(self,
                                         text='Quit',
                                         command=self.controller.quit).grid(row=4, column=1,
                                                                            sticky=tkinter.E)  # Add 'Quit'Button


