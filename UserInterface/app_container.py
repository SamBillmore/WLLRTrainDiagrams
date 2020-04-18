from tkinter import Tk
from tkinter import Frame
from tkinter import filedialog

from UserInterface.home_screen import HomeScreen
from UserInterface.graph_test import GraphTest

class App(Tk):
    """
    Overall container for app
    Individual screens are raised within this container
    """

    def __init__(self):
        """
        Initialise the class
        """
        Tk.__init__(self)

        self.title('WLLR timetable diagram program')
        self.geometry('850x600+250+100')
        self.frame_names_list = (HomeScreen,GraphTest)
        self.frames = {}
        self.background_col = 'black'
        self.foreground_col = 'white'
        self.font = 'courier 11'

        # the container holds the stack of frames on top of each other. The one to be visible will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create each frame instance and add to self.frames dictionary
        for frame_name in self.frame_names_list:
            page_name = frame_name.__name__
            frame_object = frame_name(parent=container, controller=self, background_col = self.background_col, foreground_col = self.foreground_col, font = self.font)
            self.frames[page_name] = frame_object
            frame_object.grid(row=0, column=0, sticky="nsew")
        self.show_frame(HomeScreen.__name__)

    def show_frame(self, page_name):
        """
        Show a frame for the given page_name
        """
        frame = self.frames[page_name]
        frame.tkraise()
        self.update()

    def browse_file(self, entry):
        """
        Browse the file system
        """
        file_path = filedialog.askopenfilename(title='Choose a file')
        if file_path != None:
            entry.delete(0, 'end')
            entry.insert(0, file_path)

    def browse_directory(self, entry):
        """
        Browse the file system and select a directory
        """
        dir_path = filedialog.askdirectory(title='Choose a folder location')
        if dir_path != None:
            entry.delete(0, 'end')
            entry.insert(0, dir_path)