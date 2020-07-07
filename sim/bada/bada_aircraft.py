from sim.bada.base_aircraft import BaseAircraft
from sim.bada.bada_coeff import get_coefficients
from sim.bada.phases import INITIAL, DEP_GND_RUN, TAKE_OFF, INITAL_CLIMB, CLIMB, CRUISE, DESCENT, APPROACH, LANDING, ARR_GND_RUN, POSSIBLE_PHASES



class BadaAircraft(BaseAircraft):
    '''
    Bada Aircraft class with coefficients from BADA
    '''
    def __init__(self, actype='A320', phase=INITIAL, lat=0, lon=0, heading=0, alt=0, tas=0, rocd=0):
        super().__init__(phase, lat, lon, heading, alt, tas, rocd)
        self._bada = get_coefficients(actype)[1]
        self._Vstall = 0

    
    ''' Aircraft phase check '''
    def is_phase(self, phase):
        assert phase in POSSIBLE_PHASES
        return phase == self._phase

    def get_phase(self):
        return self._phase

    def set_phase(self, phase)
        assert phase in POSSIBLE_PHASES
        self._phase = phase
    
    
    ''' Aircraft stall speed'''

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
    def compute_mass(self):
        pass





    


if __name__ == "__main__":
    ac = BadaAircraft()    
    print(ac.get_phase())
    print(ac.is_phase(CLIMB))
    print(ac)