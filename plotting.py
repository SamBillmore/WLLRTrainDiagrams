


# TO DO:
# Write doc strings for all methods and functions
# Update first/last time function in data manipulation TrainData
# User interface



from Plotter.plotter import Plotter
from DataManipulation.data_manipulation import TrainData
from config import column_datatypes,filepath,scaling_factor

def main_function(filepath,column_datatypes,scaling_factor):
    train_data = TrainData()
    data = train_data.import_train_data(filepath,column_datatypes)
    first_time,last_time = train_data.timetable_boundaries(data)
    fig_width = train_data.fig_width_calc(first_time,last_time,scaling_factor)
    trains_to_create = set(data['Train'])
    all_trains = train_data.create_all_trains(trains_to_create, data)
    plotter = Plotter()
    plotter.train_diagram_plotter(fig_width,all_trains)

if __name__ =='__main__':
    main_function(filepath,column_datatypes,scaling_factor)