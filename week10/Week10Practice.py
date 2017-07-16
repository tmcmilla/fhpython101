""" 
This main program creates a MyFrame object that contains two Buttons and a Label. 
"""
#import tkinter
#import myFrame                # contains class MyFrame
import controller

if __name__ == "__main__":
    c = controller.Controller()
    #try:
    #    root = tkinter.Tk()     # starts up the tkinter framework
    #    view = myFrame.MyFrame(master = root)   
    #    view.mainloop()     # starts the event loop
    #    root.destroy()
    #except Exception as ex:
    #    print(ex.args)
    #    print(ex.with_traceback)
    #except:
    #    print('Error')
    #else:
    #    print("Success")
