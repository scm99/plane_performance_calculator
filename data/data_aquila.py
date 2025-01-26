import pandas as pd


class Aquila_data:
    """Retrieves the data for the computations of the performances for the DR400 at 180cv.
    """
    def __init__(self):
        pass
    
    def get_altitude(self, mode: str):
        """Gets the altitude performance points.
        
        Returns:
            dataframe: the dataframe for the altitude performance.
        """
        
        columns = ['altitude', 'temperature', 'value']

        if mode == 'landing':
            altitude_array = [
                    [0,-30,408],
                    [0,-10,450],
                    [0,20,510],
                    [0,40,550],
                    [380,20,525],
                    [2000,-30,452],
                    [2000,-10,500],
                    [2000,10,540],
                    [2000,40,615],
                    [4000,-30,502],
                    [4000,-10,550],
                    [4000,10,600],
                    [4000,40,680],
                    [6000,-30,558],
                    [6000,-10,612],
                    [6000,20,700],
                    [6000,40,752],
                    [8000,-30,620],
                    [8000,-20,680],
                    [8000,10,740],
                    [8000,40,840]
            ]
        elif mode == 'take_off':
            altitude_array = [
                    [0,-30,192],
                    [0,-10,218],
                    [0,20,258],
                    [0,40,291],
                    [2000,-30,219],
                    [2000,10,281],
                    [2000,20,297],
                    [2000,40,333],
                    [4000,-30,251],
                    [4000,0,305],
                    [4000,20,342],
                    [4000,40,382],
                    [6000,-30,290],
                    [6000,0,351],
                    [6000,30,420],
                    [6000,40,442],
                    [8000,-30,334],
                    [8000,-20,358],
                    [8000,10,432],
                    [8000,20,458],
                    [8000,40,512]
            ]
        
        # Create dataframe with points
        altitude_dataframe = pd.DataFrame(altitude_array, columns=columns)
        
        return altitude_dataframe
    
    def get_distances(self, mode: str):
        """Gets the distances performance points.
        
        Returns:
            dataframe: the dataframe for the distances performance.
        """
        
        columns = ['d1', 'd2']
        
        if mode == 'landing':
            d_array = [
                [218,85],
                [288,120],
                [375,160],
                [432,175],
                [508,205],
                [580,240],
                [648,270],
                [720,300],
                [788,330],
                [862,360],
                [932,390],
                [1005,420]
            ]
        elif mode == 'take_off':
            d_array = [
                [120,222],
                [150,280],
                [180,335],
                [210,392],
                [240,420],
                [270,502],
                [300,560],
                [330,615],
                [360,670],
                [390,727],
                [420,782],
                [450,840],
                [480,895],
                [510,955]
            ]
        
        # Create dataframe with points
        d_dataframe = pd.DataFrame(d_array, columns=columns)
        
        return d_dataframe
    
    
    def get_headwind(self, mode: str):
        """Gets the head wind performance points.
        
        Returns:
            dataframe: the dataframe for the head wind performance.
        """
        
        columns = ['curve', 'wind', 'value']
        
        if mode == 'landing':
            hwind_array = [
                [1,0,355],
                [1,4,325],
                [1,10,275],
                [1,14,250],
                [1,20,220],
                [2,0,518],
                [2,6,438],
                [2,10,398],
                [2,14,358],
                [2,20,315],
                [3,0,650],
                [3,6,550],
                [3,10,500],
                [3,14,450],
                [3,20,395],
                [4,0,740],
                [4,4,675],
                [4,10,575],
                [4,16,500],
                [4,20,455],
                [5,0,840],
                [5,6,725],
                [5,10,650],
                [5,14,590],
                [5,20,520]
            ]
        elif mode == 'take_off':
            hwind_array = [
                [1,0,120],
                [1,4,108],
                [1,8,96],
                [1,10,91],
                [1,16,80],
                [1,20,76],
                [2,0,205],
                [2,4,183],
                [2,10,156],
                [2,14,141],
                [2,20,124],
                [3,0,291],
                [3,4,261],
                [3,8,238],
                [3,10,223],
                [3,16,192],
                [3,20,180],
                [4,0,394],
                [4,4,358],
                [4,10,302],
                [4,16,262],
                [4,20,242],
                [5,0,513],
                [5,6,441],
                [5,10,392],
                [5,14,359],
                [5,20,316]
            ]
        
        # Create dataframe with points
        hwind_dataframe = pd.DataFrame(hwind_array, columns=columns)
        
        return hwind_dataframe
    
    
    def get_mass(self, mode:str):
        """Gets the mass performance points.
        
        Returns:
            dataframe: the dataframe for the mass performance.
        """
        
        columns = ['curve', 'mass', 'value']
        if mode == 'landing':
            mass_array = [
                    [1,750,408],
                    [1,725,400],
                    [1,600,375],
                    [1,550,360],
                    [2,750,450],
                    [2,650,425],
                    [2,550,398],
                    [3,750,500],
                    [3,650,470],
                    [3,575,450],
                    [3,550,440],
                    [4,750,554],
                    [4,650,518],
                    [4,550,482],
                    [5,750,612],
                    [5,700,595],
                    [5,600,552],
                    [5,550,538],
                    [6,750,680],
                    [6,675,650],
                    [6,625,628],
                    [6,550,595],
                    [7,750,752],
                    [7,650,705],
                    [7,550,658],
                    [8,750,840],
                    [8,675,800],
                    [8,550,735]
            ]
        elif mode == 'take_off':
            mass_array = [
                    [1,750,198],
                    [1,700,178],
                    [1,650,160],
                    [1,600,141],
                    [1,550,122],
                    [2,750,224],
                    [2,700,203],
                    [2,650,181],
                    [2,600,161],
                    [2,550,140],
                    [3,750,255],
                    [3,675,220],
                    [3,600,183],
                    [3,550,160],
                    [4,750,292],
                    [4,700,262],
                    [4,650,238],
                    [4,600,209],
                    [4,550,182],
                    [5,750,335],
                    [5,700,305],
                    [5,650,272],
                    [5,600,239],
                    [5,550,211],
                    [6,750,382],
                    [6,700,350],
                    [6,650,313],
                    [6,600,277],
                    [6,575,260],
                    [6,550,240],
                    [7,750,442],
                    [7,700,400],
                    [7,650,360],
                    [7,600,318],
                    [7,550,279],
                    [8,750,512],
                    [8,700,465],
                    [8,675,442],
                    [8,650,418],
                    [8,600,365],
                    [8,550,321]
            ]
        
        # Create dataframe with points
        mass_dataframe = pd.DataFrame(mass_array, columns=columns)
        
        return mass_dataframe
    
    
    def get_tailwind(self, mode:str):
        """Gets the tail wind performance points.
        
        Returns:
            dataframe: the dataframe for the tail wind performance.
        """
        
        columns = ['curve', 'wind', 'value']
        if mode == 'landing':
            twind_array = [
                [1,0,352],
                [1,-10,480],
                [2,0,430],
                [2,-10,575],
                [3,0,510],
                [3,-10,695],
                [4,0,595],
                [4,-10,805],
                [5,0,700],
                [5,-10,952]
            ]
        elif mode == 'take_off':
            twind_array = [
                [1,0,120],
                [1,-10,162],
                [2,0,200],
                [2,-10,270],
                [3,0,300],
                [3,-10,407],
                [4,0,395],
                [4,-10,538],
                [5,0,510],
                [5,-10,692]
            ]

        # Create dataframe with points
        twind_dataframe = pd.DataFrame(twind_array, columns=columns)
        
        return twind_dataframe