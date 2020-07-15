import numpy as np

from sim.bada.base_aircraft import BaseAircraft
from sim.bada.bada_coeff import get_coefficients
from sim.bada.phases import INITIAL, DEP_GND_RUN, TAKE_OFF, INITAL_CLIMB, CLIMB, CRUISE, DESCENT, APPROACH, LANDING, ARR_GND_RUN
from sim.bada.phases import TO, IC, CR, AP, LD, POSSIBLE_CONFIGURATIONS, VSTALL_KEYS
from sim.units import MS2KNOTS, M2FT



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
        self._configuration = None  # TO CL CR AP LD, for calculation of Vstall        
        self._Vstall = None
        self._idle_thrust = False
    
    
    # ####################################################################
    # Aircraft type query
    # ####################################################################      
    def engine_is_jet(self): return self._bada.engtype == 'Jet'
    def engine__turboprop(self): return self._bada.engtype == 'Turboprop'
    def engine_piston(self): return self._bada.engtype == 'Piston'

    
    # ####################################################################
    # STALL SPEED
    # ####################################################################  
    def get_vstall(self, configuration):
        assert configuration in POSSIBLE_CONFIGURATIONS
        return getattr(self._bada, VSTALL_KEYS[configuration]) * np.sqrt(self._mass/self._bada.m_ref)


    # ####################################################################
    # THRUST
    # ####################################################################
    def compute_thurst(self):
        if self.engine_is_jet():
            if self._phase in [DEP_GND_RUN, TAKE_OFF, INITAL_CLIMB, CLIMB]:
                pass
            elif self._phase == CRUISE:
                pass
            elif self._phase == DESCENT:
                pass
            elif self._phase == APPROACH:
                pass
            elif self._phase == LANDING:
                pass
            elif self._phase == ARR_GND_RUN:
                pass
            else:
                raise ValueError('Invalid aircraft phase!')

        else:
            raise ValueError('Only Jet is supported at the moment.')

   
    # ####################################################################
    # DRAG
    # ####################################################################
    def compute_drag(self):
        pass

    
    # ####################################################################
    # LIFT
    # ####################################################################
    def compute_lift(self):
        pass

    
    ''' MASS '''
    @property
    def mass(self):
        return self._mass

    def update_mass(self):
        self._mass -= self.fuel_flow

    ''' FUEL '''
    @property
    def fuel_flow(self):
        '''Calculate fuel flow consumed after a time step'''
        if self._bada.engtype != 'Jet':            
            raise ValueError('Only Jet engine fuel flow is available for the moment.')        
        if self._idle_thrust or self._phase == DESCENT:
            '''calculate minimum fuel flow, 3.9-5'''
            rate = self._bada.Cf3 * (1 - self._alt * M2FT * (1/self._bada.Cf4))
        else:
            '''Not minimum fuel flow'''            
            eta = self._bada.Cf1 * (1 + self._tas * MS2KNOTS * (1/self._bada.Cf2))  # Equation 3.9-1
            if self._phase == CRUISE:
                '''calculate cruise fuel flow, 3.9-6
                   devide _thrust by 1000.0 to get thrust in kN'''
                rate = eta * (self._thrust/1000.0) * self._bada.Cf_cruise 
            else:
                '''calculate nominal fuel flow, 3.9-[1-4]'''
                rate = eta * (self._thrust/1000.0)
        return rate * (self._d_time / 60.0)       



if __name__ == "__main__":
    ac = BadaAircraft()    
    print(ac.get_phase())
    print(ac.is_phase(CLIMB))
    print(ac.get_vstall(AP))
    print(ac.fuel_flow)
    print(ac.__dict__)
    print(ac.get_vstall(CR))
    print(ac.fuel_flow)
    print(ac)