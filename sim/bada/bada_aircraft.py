from sim.bada.base_aircraft import BaseAircraft
from sim.bada.bada_coeff import get_coefficients
from sim.bada.phases import INITIAL, DEP_GND_RUN, TAKE_OFF, INITAL_CLIMB, CLIMB, CRUISE, DESCENT, APPROACH, LANDING, ARR_GND_RUN, POSSIBLE_PHASES
from sim.bada.phases import TO, IC, CR, AP, LD, POSSIBLE_CONFIGURATIONS, VSTALL_KEYS



class BadaAircraft(BaseAircraft):
    '''
    Bada Aircraft class with coefficients from BADA
    '''
    def __init__(self, actype='A320', init_mass=None, phase=INITIAL, lat=0, lon=0, heading=0, alt=0, tas=0, rocd=0):
        super().__init__(phase, lat, lon, heading, alt, tas, rocd)
        self._bada = get_coefficients(actype)[1]
        if self._bada.engtype != 'Jet':
            raise ValueError('Only aircraft with Jet engine is supported at the momement')
        self._mass = self._bada.m_ref if init_mass is None else init_mass
        self._phase = None
        self._configuration = None  # TO CL CR AP LD, for calculation of Vstall        
        self._Vstall = 0.0
        self._idle_thrust = False

    
    ''' Aircraft phase check '''
    def is_phase(self, phase):
        assert phase in POSSIBLE_PHASES
        return phase == self._phase

    def get_phase(self):
        return self._phase

    def set_phase(self, phase):
        assert phase in POSSIBLE_PHASES
        self._phase = phase
    
    
    ''' Aircraft stall speed'''
    def get_vstall(self, configuration):
        assert configuration in POSSIBLE_CONFIGURATIONS
        return getattr(self._bada, VSTALL_KEYS[configuration])


    ''' Aircraft thrust'''
    def compute_thurst(self):
        pass

    
    ''' Aircraft drag'''
    def compute_drag(self):
        pass

    
    ''' Aircraft lift'''
    def compute_lift(self):
        pass

    
    ''' Aircraft mass'''
    @property
    def mass(self):
        return self._mass
    
    @property
    def fuel_flow(self):
        if self._bada.engtype != 'Jet':            
            raise ValueError('Only Jet engine fuel flow is available for the moment.')
        if self._phase == CRUISE:
            pass
        elif self._idle_thrust or self._phase == DESCENT:
            pass
        else:
            pass
    
    def update_mass(self):
        pass   



if __name__ == "__main__":
    ac = BadaAircraft()    
    print(ac.get_phase())
    print(ac.is_phase(CLIMB))
    print(ac.get_vstall(AP))
    print(ac)