from tkinter import Frame
from tkinter import Button
from tkinter import Label
# from tkinter import PhotoImage

class HomeScreen(Frame):
    """
    Home screen for the program
    """
    
    def __init__(self, parent, controller, background_col, foreground_col, font):
        """
        Initialise the home screen
        """
        Frame.__init__(self, parent, bg=background_col)
        self.controller = controller
        self.parent = parent
        
        self.intro_label = Label (self, text='Welcome to the WLLR timetable diagram program.', bg=background_col, fg=foreground_col, font=font)
        self.back_button = Button (self, text='Graph', width=19, command=lambda: self.controller.show_frame('GraphTest'))

        self.intro_label.grid(row=1, column=0, sticky='W', padx=25, pady=20, columnspan=2)
        self.back_button.grid(row=2, column=0, sticky='W', padx=25, pady = 20)