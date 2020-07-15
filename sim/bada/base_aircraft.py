from config import SI, NAUTIC
from sim.navigation.navaid import Waypoint
from sim.bada.phases import INITIAL, POSSIBLE_PHASES


class BaseAircraft(object):
    ''' 
    Abstract class of an aircraft to inlcude kinematic state properties.
    Other aircraft classes (e.g. BadaAircraft) should directly or indirectly sub-classs this class.
    All units are SI by default, except angles and lat, lon are in degrees.
    '''
    def __init__(self, phase=INITIAL, lat=0, lon=0, heading=0, alt=0, tas=0, rocd=0):
        self.init_state(phase, lat, lon, heading, alt, tas, rocd)
    
    # #####################
    # State of the aircraft
    # #####################    
    def init_state(self, phase, lat, lon, heading, alt, tas, rocd):
        '''
        Initialize state of an aircraft at creation.
        This initial state describes an aircraft parking at lat, lon, alt, heading.
        All forces are zeros at the beginning.
        '''
        self._phase      = phase
        self._position   = Waypoint(lat=lat, lon=lon)
        self._alt        = alt
        self._heading    = heading
        self._tas        = tas        
        self._rocd       = rocd
        self._thrust     = 0
        self._lift       = 0
        self._drag       = 0
        self._path_angle = 0        
        self._mass       = 0
        self._d_time = 1  # time step for calculation of 4D trajectory
        self._elapsed_time   = 0
        self._distance_to_go = 0
        self._along_path_position = 0

    def reset_state(self):
        '''reset state of the aircraft'''
        pass

    def get_state(self, format='dict', unit=SI):
        '''get current state of the aircraft, as a list or a dict'''
        pass

    # ####################################################################
    # Simulation time interval
    # ####################################################################    
    @property
    def delta_time(self):
        return self._d_time
    
    def set_delta_time(self, d_t):
        self._d_time = d_t
        return d_t


    # ####################################################################
    # Aircraft phase
    # ####################################################################    
    ''' Aircraft phase check '''
    def is_phase(self, phase):
        assert phase in POSSIBLE_PHASES
        return phase == self._phase

    @property
    def phase(self):
        return self._phase

    def set_phase(self, phase):
        assert phase in POSSIBLE_PHASES
        self._phase = phase

    
    # ####################################################################
    # Kinematic properties: lat, lon, alt, true air speed, vertical speed
    # ####################################################################    
    def get_latlon(self):
        '''read current location lat lon of the aircraft'''
        pass
    
    def get_position(self):
        '''read current position of the aircraft as a Fix object'''
        pass

    def set_position(self):
        '''update position of the aircraft to a Fix/Waypoint object'''
        pass

    def get_alt(self):
        '''read currrent altitude of the aircraf, in meters'''
        pass

    def set_alt(self):
        '''update altitude of the aircraft, in meters'''
        pass

    def get_heading(self):
        '''read currrent heading of the aircraf, in degree'''
        pass

    def set_heading(self):
        '''update heading of the aircraft, in degree'''
        pass

    def get_path_angle(self):
        '''read current path angle (gamma) of the aircraft, in degree'''
        pass

    def set_path_angle(self):
        '''update path angle (gamma) of the aircraft, in degree'''
        pass

    def get_tas(self):
        '''read current true air speed of the aircraft, in m/s'''
        pass

    def set_tas(self):
        '''update true air speed of the aircraft, in m/s'''
        pass

    def get_rocd(self):
        '''read current vertical speed of the aircraft, in m/s'''
        pass

    def set_rocd(self):
        '''update vertical speed of the aircraft, in m/s'''
        pass
    
    # #############################################
    # Dynamic properties: mass, lift, drag, thrust
    # #############################################

    @property
    def mass(self):
        '''read current mass of the aircraft, in kg'''
        pass

    def update_mass(self): 
        '''update the mass of the aircraft, in kg'''
        pass

    @property
    def thrust(self):
        '''read current thrust of the aircraft, in N'''
        return self._thrust

    def compute_thrust(self):
        '''update thrust of the aircraft, in N'''
        pass
    
    @property
    def drag(self):
        '''read current drag of the aircraft, in N'''
        return self._drag

    def compute_drag(self):
        '''update drag of the aircraft, in N'''
        pass

    @property
    def lift(self):
        '''read current lift of the aircraft, in N'''
        return self._lift

    def compute_lift(self):
        '''update lift of the aircraft, in N'''
        pass

    # #############
    # Other methods
    # #############

    def some_method(self):
        pass


if __name__ == "__main__":
    '''Test the AircraftBase class'''
    base_aircraft = AircraftBase()
    print(base_aircraft)
