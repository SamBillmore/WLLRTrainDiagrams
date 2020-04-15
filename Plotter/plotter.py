import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class Plotter:
    '''
    Class to plot the train diagram.
    '''
    
    def __init__(self):
        '''
        Instantiate the class.
        '''
        pass
    
    def train_diagram_plotter(self, fig_width, all_trains):
        fig, ax = plt.subplots(1,1, figsize=(fig_width,6))
        for train in all_trains:
            ax.plot_date(train.timetable['Time'],train.timetable['Distance'],linestyle='solid',marker=',')
        ax.set_ylim((-0.5, 8.5))
        myFmt = mdates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(myFmt)
        plt.show()  