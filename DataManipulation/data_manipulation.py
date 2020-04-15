import pandas as pd

class TrainData:
    '''
    Class to manipulate train data.
    '''
    
    def __init__(self):
        '''
        Instantiate the class.
        '''
        pass
    
    def import_train_data(self, filepath, column_datatypes):
        demo_data = pd.read_csv(filepath,dtype=column_datatypes)
        demo_data['Time'] = pd.to_datetime(demo_data['Time'],format='%H:%M')
        return demo_data

    def timetable_boundaries(self, data):    
        # change this into different function (min,max)
        first_time = data['Time'].iloc[0]
        last_time = data['Time'].iloc[-1]
        return first_time, last_time

    def fig_width_calc(self, first_time,last_time,scaling_factor):
        tdelta = (last_time - first_time).total_seconds()/60
        fig_width = tdelta*scaling_factor
        return fig_width

    def create_all_trains(self, trains_to_create, data):
        all_trains = []
        for train in trains_to_create:
            train_tt = data[data['Train']== train]
            t = Train(name=train, timetable=train_tt)
            all_trains.append(t)
        return all_trains



class Train:
    '''
    A class to hold information about different trains on the timetable.
    '''
    
    def __init__(self, name, timetable):
        '''
        Instantiate the class.
        '''
        self.name = name
        self.timetable = timetable
