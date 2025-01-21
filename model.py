from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d, LinearNDInterpolator, CloughTocher2DInterpolator
import logging
from pathlib import Path
import glob

class AbstractPerformanceGenerator(ABC):
    """Abstract Class to Calculate Performances for TakeOff.
    """

    def __init__(self, plane_type: str, subtype: str):
        """Initializes Abstract Class for Take Off Performances

        Args:
            plane_type (str): type of plane, DR400 or Aquila.
            subtype (str): subtype of plane in case of DR400, 160cv or 180cv.
        """
        self.type = plane_type
        self.subtype = subtype
        self.distance_take_off = 0
        self.distance_ground_roll = 0
        self.min_mass = 0
        self.max_mass = 0

        # Configure the logging system 
        logging.basicConfig(filename ='PerformancesAvion.log', 
                        level = logging.DEBUG,
                        format = '%(levelname)s: %(asctime)s: %(message)s') 
       
    @abstractmethod 
    def calculate_distances(self, *args) -> tuple[float, float]:
        """Abstract method to calculate ground roll and take off distances.

        Returns:
            Tuple[float, float]: ground roll and take off distances
        """
        pass
    
    
class PerformanceGeneratorDR400(AbstractPerformanceGenerator):
    """
    Implements Take Off Performance Calculation Class for DR400
    """
    
    def __init__(self, subtype):
        """Initializes Class for calculating Take Off Performances for a DR400.

        Args:
            subtype (str): subtype of plane in case of DR400, 160cv or 180cv.
        """
        super().__init__('DR400', subtype)
        if subtype == '160':
            self.min_mass = 620
            self.max_mass = 1050
            self.max_landing = 1045
            self.min_landing = 850
            self.max_take_off = 1050
            self.min_take_off = 850
        if subtype == '180':
            self.min_mass = 570
            self.max_mass = 1100
            self.max_landing = 1045
            self.min_landing = 845
            self.max_take_off = 1100
            self.min_take_off = 900
            
        
    def calculate_distances(self, mode, altitude, temperature, mass, herbe: bool = False, wind: float = 0) -> tuple[float, float]:
        """Calculates ground roll and take off distances for a DR400 depending on the power subtype.

        Returns:
            Tuple[float, float]: ground roll and take off distances
        """
        
        # Get folder for selected subtype
        folder = f"{self.type}_{self.subtype}"
        
        # Get performance files
        pathHard = Path('data', folder, 'dur', mode)
        performance_files = list(pathHard.glob('*.txt'))
        files_herbe = False
        if herbe:
            pathGrass = Path('data', folder, 'herbe', mode)
            files_aux = list(pathGrass.glob('*.txt'))
            if files_aux:
                performance_files = files_aux
                files_herbe = True
        
        # Get Dataframes
        dataframes_performance = []
        for performance_file in performance_files:
            dataframes_performance.append(pd.read_csv(performance_file))

            
        if mode == 'landing':
            masses = [self.min_landing, self.max_landing]
        else:
            masses = [self.min_take_off, self.max_take_off]
            
        # Collect data from interpolation purposes
        x = np.array([])
        y = np.array([])
        z = np.array([])
        d1 = np.array([])
        d2 = np.array([])
        for i, dataframe in enumerate(dataframes_performance):
            x = np.append(x, dataframe.altitude.to_numpy())
            y = np.append(y, dataframe.temperature.to_numpy())
            z = np.append(z, np.array([masses[i]]*len(dataframe)))
            d1 = np.append(d1, dataframe.distance_decollage.to_numpy())
            d2 = np.append(d2, dataframe.distance_roulement.to_numpy())
            
        # Error if mass is above maximum mass
        max_mass = np.amax(masses)
        if mass > max_mass:
            return '-', '-'
        
        # 3D Interpolator
        f_take_off = LinearNDInterpolator((x, y, z), d1)
        f_ground_roll = LinearNDInterpolator((x, y, z), d2)
        
        # Calculate distances using 3D interpolator
        distance_take_off = f_take_off(altitude, temperature, mass)
        distance_ground_roll = f_ground_roll(altitude, temperature, mass)
        
        # Add wind contribution
        if wind != 0:
            
            # Read Wind Factors
            dataframe_wind = pd.read_csv(Path('data', folder, 'wind.txt'))
            
            # Create Interpolator
            f_wind = interp1d(dataframe_wind.wind, dataframe_wind.factor, fill_value="extrapolate")
            
            # Calculate multiplication factor for wind
            wind_factor = f_wind(wind)
            
            # Calculate New Take Off Distance taking into account Wind
            distance_take_off = distance_take_off * wind_factor
            
            # Calculate New Ground Roll Distance taking into account Wind
            distance_ground_roll = distance_ground_roll * wind_factor
            
        # Add Runway type contribution
        if herbe and not files_herbe:
            distance_take_off *= 1.15
            distance_ground_roll *= 1.15
    
        if np.isnan(distance_ground_roll) or np.isnan(distance_take_off):
            return '-', '-'
            
        return int(distance_ground_roll), int(distance_take_off)
    
    
class PerformanceGeneratorAquila(AbstractPerformanceGenerator):
    """
    Implements Take Off Performance Calculation Class for Aquila
    """
    
    def __init__(self):
        """Initializes Class for calculating Take Off Performances for an Aquila.
        """
        super().__init__('Aquila', None)
        self.min_mass = 490
        self.max_mass = 750
        
    def calculate_distances(self, mode, altitude, temperature, mass, herbe: bool = False, wind: float = 0) -> tuple[float, float]:
        """Calculates Take Off Distance for an Aquila.

        Returns:
            Tuple[float, float]: ground roll and take off distances
        """
        
        folder = 'aquila'
        
        # Maximum Take-Off and Landing Mass
        if mass > 750:
            return '-', '-'
        
        # Get performance files
        data_altitude = pd.read_csv(Path("data", folder, mode, "altitude.txt"))
        data_mass = pd.read_csv(Path("data", folder, mode, "mass.txt"))
        data_headwind = pd.read_csv(Path("data", folder, mode, "headwind.txt"))
        data_tailwind = pd.read_csv(Path("data", folder, mode, "tailwind.txt"))
        data_distances = pd.read_csv(Path("data", folder, mode, "distances.txt"))
        
        # Fist Interpolation - Altitude and Temperature
        f1 = CloughTocher2DInterpolator(list(zip(data_altitude.altitude, data_altitude.temperature)), data_altitude.value)
        value1 = f1(altitude, temperature)
        
        # Second Interpolation - Value 1 to Take Off Mass
        faux =  CloughTocher2DInterpolator(list(zip(data_mass.mass, data_mass.value)), data_mass.curve)
        f2 =  CloughTocher2DInterpolator(list(zip(data_mass.curve, data_mass.mass)), data_mass.value)
        value_aux = faux(750, value1)
        value2 = f2(value_aux, mass)
        
        # Third Interpolation - Value 2 to Wind
        if wind >= 0:
            f_temp =  CloughTocher2DInterpolator(list(zip(data_headwind.wind, data_headwind.value)), data_headwind.curve)
            f_wind =  CloughTocher2DInterpolator(list(zip(data_headwind.curve, data_headwind.wind)), data_headwind.value)
        else:
            f_temp =  CloughTocher2DInterpolator(list(zip(data_tailwind.wind, data_tailwind.value)), data_tailwind.curve)
            f_wind =  CloughTocher2DInterpolator(list(zip(data_tailwind.curve, data_tailwind.wind)), data_tailwind.value)
        curve_temp = f_temp(0, value2)
        value3 = f_wind(curve_temp, wind)
        
        # Last interpolation for computing the partial and total distances
        f_distances =  interp1d(data_distances.d1, data_distances.d2)
        
        # Mode related distance interpolation
        if mode == 'take_off':
            partial_distance = value3
            total_distance = f_distances(value3)
        else:
            total_distance = value3
            partial_distance = f_distances(value3)
        
        # Add influence of grass runway to distance
        if herbe:
            partial_distance *= 1.25
            total_distance *= 1.25
        
        return int(partial_distance), int(total_distance)