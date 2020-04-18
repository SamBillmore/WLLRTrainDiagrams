import pandas as pd

class TrainData:
    """
    Class to manipulate train data.
    """
    
    def __init__(self, filepath, column_datatypes):
        """
        Instantiate the class.
        """
        self.filepath = filepath
        self.column_datatypes = column_datatypes

        self.controller()

    def controller(self):
        """
        Method to call all other methods in class in order.
        """
        self.import_train_data()
        self.timetable_boundaries()
        self.create_all_trains()

    def import_train_data(self):
        """
        Import data from filepath using column data types defined as column_datatypes
        """
        self.data = pd.read_csv(self.filepath,dtype=self.column_datatypes)
        self.data['Time'] = pd.to_datetime(self.data['Time'],format='%H:%M')

    def timetable_boundaries(self):
        """
        Determine earliest and latest scheduled station stop.
        """
        self.first_time = min(self.data['Time'])
        self.last_time = max(self.data['Time'])

    def create_all_trains(self):
        """
        Creates a separate object for each train in the data and allocates 
        the relevant data to it.
        """
        self.all_trains = []
        trains_to_create = set(self.data['Train'])
        for train in trains_to_create:
            train_tt = self.data[self.data['Train']== train]
            t = Train(name=train, timetable=train_tt)
            self.all_trains.append(t)

class Train:
    """
    A class to hold information about different trains on the timetable.
    """
    
    def __init__(self, name, timetable):
        """
        Instantiate the class.
        """
        self.name = name
        self.timetable = timetable
