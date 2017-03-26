import tkinter


class MyFrame(tkinter.Frame):
    def __init__(self, controller):
        """
        Places the controls onto the Frame.
        """
        tkinter.Frame.__init__(self)  # initializes the superclass
        self.pack()  # required in order for the Buttons to show up properly
        self.controller = controller  # saves a reference to the controller so that we can call methods

        # on the controller object when the user generates events������
        # set up the increment Button
        self.incrementButton = tkinter.Button(self)
        self.incrementButton["text"] = "Increment"
        self.incrementButton["command"] = self.controller.buttonIncrementPressed
        self.incrementButton.pack({"side": "left"})

        # set up the Label
        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.labelForOutput.pack({"side": "left"})

        self.decrementButton = tkinter.Button(self)
        self.decrementButton["text"] = "Decrement"
        self.decrementButton["command"] = self.controller.buttonDecrementPressed
        self.decrementButton.pack({"side": "left"})

        # set up the quit Button
        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side": "left"})