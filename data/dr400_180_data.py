import pandas as pd


class DR400_180_data:
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
                [0,-5,190,425],
                [0,15,200,450],
                [0,35,215,475],
                [4000,-13,210,465],
                [4000,7,230,495],
                [4000,27,240,520],
                [8000,-21,240,510],
                [8000,-1,260,545],
                [8000,19,275,575]
            ]
            array_max = [
                [0,-5,230,500],
                [0,15,250,530],
                [0,35,270,560],
                [4000,-13,260,550],
                [4000,7,280,585],
                [4000,27,300,620],
                [8000,-21,295,610],
                [8000,-1,320,650],
                [8000,19,340,690]
            ]
            
        # For the take off performances
        elif mode == 'take_off':
            array_min = [
                [0,-5,120,250],
                [0,15,140,290],
                [0,35,165,340],
                [2500,-10,150,310],
                [2500,10,175,360],
                [2500,30,200,415],
                [5000,-15,185,385],
                [5000,5,215,450],
                [5000,25,250,520],
                [8000,-21,245,505],
                [8000,-1,285,590],
                [8000,19,335,695]
            ]
            array_max = [
                [0,-5,215,445],
                [0,15,250,515],
                [0,35,290,600],
                [2500,-10,260,540],
                [2500,10,305,635],
                [2500,30,355,735],
                [5000,-15,330,680],
                [5000,5,385,795],
                [5000,25,445,925],
                [8000,-21,430,890],
                [8000,-1,505,1050],
                [8000,19,590,1225]
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