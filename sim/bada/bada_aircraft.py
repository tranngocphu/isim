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
    def __init__(self, actype='A320', init_mass=None, phase=DEP_GND_RUN, lat=0, lon=0, heading=0, alt=0, tas=0, rocd=0):
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
    @property
    def engine_is_jet(self):
        return self._bada.engtype == 'Jet'
    
    @property
    def engine_is_turboprop(self):
        return self._bada.engtype == 'Turboprop'
    
    @property
    def engine_piston(self):
        return self._bada.engtype == 'Piston'

    
    # ####################################################################
    # STALL SPEED
    # ####################################################################  
    def get_vstall(self, configuration):
        assert configuration in POSSIBLE_CONFIGURATIONS
        return getattr(self._bada, VSTALL_KEYS[configuration]) * np.sqrt(self._mass/self._bada.m_ref)


    # ####################################################################
    # THRUST
    # ####################################################################
    def compute_thrust(self):
        CTc1, CTc2, CTc3, CTc4, CTc5 = self._bada.CTC        
        CTcr = 0.95 # Max cruise thrust factor, see 5.5 in BADA Manual
        thrust = 0.0        
        if self.engine_is_jet:
            thrust_max_climb = CTc1 * ( 1 - (self._alt*M2FT/CTc2) + CTc3*(self._alt*M2FT)**2) # Eq. 3.7-1

            if self._phase in [DEP_GND_RUN, TAKE_OFF, INITAL_CLIMB, CLIMB]:                
                self._thrust = 1.0 * T_max_climb # Eq. 3.7-1
            
            elif self._phase == CRUISE:
                self._thrust = CTcr * T_max_climb # Eq. 3.7-8
            
            elif self._phase == DESCENT:
                ''' Descent thrust is determined in 2 phases: high altitude descent and low altitude descent.
                    High altitude descent: h > h_des
                    Low altitude descent : h <= h_des
                    See Eq. 3.7-9 and 3.7-10
                '''
                self._thrust = self._bada.CTdes_high * thrust_max_climb if self._alt*M2FT > self._bada.h_des else self._bada.CTdes_low * thrust_max_climb
            
            elif self._phase == APPROACH:
                self._thrust = self._bada.CTdes_app * thrust_max_climb # Eq. 3.7-11
            
            elif self._phase == LANDING:
                self._thrust = self._bada.CTdes_land * thrust_max_climb # Eq. 3.7-12
            
            elif self._phase in [INITIAL, ARR_GND_RUN]:
                self._thrust = 0.0
            
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
    @property
    def lift_coeff(self):
        

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
    print(ac.phase)
    print(ac.is_phase(CLIMB))
    print(ac.get_vstall(AP))
    print(ac.fuel_flow)
    print(ac.__dict__)
    print(ac.get_vstall(CR))
    print(ac.fuel_flow)
    print(ac.compute_thrust())
    print(ac)