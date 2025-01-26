import pandas as pd


class DR400_180_data:
    """Retrieves the data for the computations of the performances for the DR400 at 180cv.
    """
    def __init__(self):
        pass
    
    def get_tabledata(self, runway_type, mode):
        """Gets the data points for the performances in the minimum and maximum mass scenario.

        Args:
            runway_type (str): the type of runway between "dur" and "herbe".
            mode (str): the perfomance mode between "take_off" and "landing".

        Returns:
            tuple[dataframes]: the dataframes for the minimum and maximum mass performances.
        """
        
        columns = ['altitude','temperature','distance_roulement','distance_decollage']
        
        # For an asphalt runway
        if runway_type == 'dur':
            
            # For the landing performances
            if mode == 'landing':
                array_min = [
                    [0,-20,190,425],
                    [0,15,200,450],
                    [0,20,215,475],
                    [4000,-20,210,465],
                    [4000,7,230,495],
                    [4000,20,240,520],
                    [8000,-20,240,510],
                    [8000,1,260,545],
                    [8000,20,275,575]
                ]
                array_max = [
                    [0,-20,230,500],
                    [0,15,250,530],
                    [0,20,270,560],
                    [4000,-20,260,550],
                    [4000,7,280,585],
                    [4000,20,300,620],
                    [8000,-20,295,610],
                    [8000,1,320,650],
                    [8000,20,340,690]
                ]
            
            # For the take off performances
            elif mode == 'take_off':
                array_min = [
                    [0,-20,180,360],
                    [0,15,200,400],
                    [0,20,225,440],
                    [4000,-20,240,475],
                    [4000,7,270,530],
                    [4000,20,300,585],
                    [8000,-20,320,635],
                    [8000,1,365,715],
                    [8000,20,410,795]
                ]
                array_max = [
                    [0,-20,280,550],
                    [0,15,315,610],
                    [0,20,350,675],
                    [4000,-20,375,735],
                    [4000,7,420,825],
                    [4000,20,475,920],
                    [8000,-20,510,1010],
                    [8000,1,580,1140],
                    [8000,20,650,1280]
                ]
        
        # For a grass runway
        elif runway_type == 'herbe':
            
            # For the landing performances
            if mode == 'landing':
                array_min = [
                    [0,-20,285,520],
                    [0,15,300,550],
                    [0,20,325,585],
                    [4000,-20,315,570],
                    [4000,7,345,610],
                    [4000,20,365,645],
                    [8000,-20,360,630],
                    [8000,1,385,670],
                    [8000,20,415,715]
                ]
                array_max = [
                    [0,-20,350,620],
                    [0,15,380,660],
                    [0,20,405,695],
                    [4000,-20,395,685],
                    [4000,7,425,730],
                    [4000,20,450,770],
                    [8000,-20,440,755],
                    [8000,1,480,810],
                    [8000,20,510,860]
                ]
                
            # For the take off performances
            elif mode == 'take_off':
                array_min = [
                    [0,-20,225,405],
                    [0,15,255,455],
                    [0,20,285,500],
                    [4000,-20,315,550],
                    [4000,7,360,620],
                    [4000,20,405,690],
                    [8000,-20,450,765],
                    [8000,1,520,870],
                    [8000,20,595,980]
                ]
                array_max = [
                    [0,-20,375,645],
                    [0,15,430,725],
                    [0,20,485,810],
                    [4000,-20,540,900],
                    [4000,7,620,1025],
                    [4000,20,710,1155],
                    [8000,-20,810,1310],
                    [8000,1,945,1505],
                    [8000,20,1100,1730]
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
            [10,0.81],
            [20,0.67],
            [30,0.56]
        ]
        
        # Create dataframe with points
        wind_dataframe = pd.DataFrame(wind_array, columns=columns)
        
        return wind_dataframe