import pandas as pd


class DR400_160_data:
    """Retrieves the data for the computations of the performances for the DR400 at 180cv.
    """
    def __init__(self):
        pass
    
    def get_tabledata(self, mode):
        """Gets the data points for the performances in the minimum and maximum mass scenario.

        Args:
            runway_type (str): the type of runway between "dur" and "herbe".
            mode (str): the perfomance mode between "take_off" and "landing".

        Returns:
            tuple[dataframes]: the dataframes for the minimum and maximum mass performances.
        """
        
        columns = ['altitude','temperature','distance_roulement','distance_decollage']
        
            
        # For the landing performances
        if mode == 'landing':
            array_min = [
                [0,-5,190,435],
                [0,15,205,460],
                [0,35,215,485],
                [4000,-13,210,475],
                [4000,7,230,505],
                [4000,27,245,535],
                [8000,-21,240,520],
                [8000,-1,260,555],
                [8000,19,275,585]
            ]
            array_max = [
                [0,-5,230,510],
                [0,15,250,545],
                [0,35,270,575],
                [4000,-13,260,565],
                [4000,7,280,600],
                [4000,27,300,635],
                [8000,-21,295,620],
                [8000,-1,320,660],
                [8000,19,340,700]
            ]
        
        # For the take off performances
        elif mode == 'take_off':
            array_min = [
                [0,-5,170,340],
                [0,15,185,375],
                [0,35,205,415],
                [4000,-13,220,445],
                [4000,7,260,500],
                [4000,27,275,550],
                [8000,-21,300,605],
                [8000,-1,340,675],
                [8000,19,380,750]
            ]
            array_max = [
                [0,-5,265,530],
                [0,15,295,590],
                [0,35,330,655],
                [4000,-13,355,710],
                [4000,7,400,800],
                [4000,27,450,890],
                [8000,-21,485,980],
                [8000,-1,550,1105],
                [8000,19,620,1250]
            ]
        
        # Create dataframe for minimum mass points
        min_dataframe = pd.DataFrame(array_min, columns=columns)
        
        # Create dataframe for maximum mass points
        max_dataframe = pd.DataFrame(array_max, columns=columns)
        
        return min_dataframe, max_dataframe
    
    
    def get_wind(self):
        """Gets the wind performance points.
        
        Returns:
            dataframe: the dataframe for the wind performance.
        """
        
        columns = ['wind', 'factor']
        wind_array = [
                [-10,1.5],
                [-8,1.4],
                [-6,1.3],
                [-4,1.2],
                [-2,1.1],
                [0,1],
                [10,0.85],
                [20,0.65],
                [30,0.55]
        ]
        
        # Create dataframe with points
        wind_dataframe = pd.DataFrame(wind_array, columns=columns)
        
        return wind_dataframe