from tkinter import Frame
from tkinter import Button
from tkinter import Label
# from tkinter import PhotoImage
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates

from config import COLUMN_DATATYPES,FILEPATH,SCALING_FACTOR
from DataManipulation.data_manipulation import TrainData

class GraphTest(Frame):
    """
    Home screen for the program
    """
    
    def __init__(self, parent, controller, background_col, foreground_col, font):
        """
        Initialise the graph screen
        """
        Frame.__init__(self, parent, bg=background_col)
        self.controller = controller
        self.parent = parent
        
        self.intro_label = Label (self, text='Welcome to the graph test page.', bg=background_col, fg=foreground_col, font=font)
        self.back_button = Button (self, text='Back', width=19, command=lambda: self.controller.show_frame('HomeScreen'))
        self.graph = self.graph_plot()

        self.intro_label.grid(row=1, column=0, sticky='W', padx=25, pady=20, columnspan=2)
        self.back_button.grid(row=4, column=0, sticky='W', padx=25, pady = 20)
        self.graph.grid(row=6, column=0, sticky='W', padx=25, pady = 20)

    def graph_plot(self):
        """
        Use TrainData to obtain data from FILEPATH.
        Returns a graph from the data that can be rendered in Tkinter.
        """
        data = TrainData(FILEPATH,COLUMN_DATATYPES)
        tdelta = (data.last_time - data.first_time).total_seconds()/60
        fig_width = tdelta*SCALING_FACTOR
        fig = Figure(figsize=(fig_width,5), dpi=100)
        ax = fig.add_subplot(111)
        for train in data.all_trains:
            ax.plot_date(train.timetable['Time'],train.timetable['Distance'],linestyle='solid',marker=',')
        ax.set_ylim((-0.5, 8.5))
        myFmt = mdates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(myFmt)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        plotted_graph = canvas.get_tk_widget()
        return plotted_graph