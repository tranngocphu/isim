''' This file contains calculation of atmospheric properties at ISA condition '''

from config import DELTA_TEMP_ISA

class Atmosphere(object):
    GRAVITY            = 9.81    # gravitional acceleration, m/s2
    ISA_TROPOPAUSE     = 11000.0 # tropopause height in meters at ISA condition
    REAL_GAS_CONTANT   = 287.04  # real gas contant for air, m2/(K*s2)
    ISA_K_T            = -0.0065 # k_T: ISA temperature gradient with altitude below tropopause, K/m
    ISA_SPEED_OF_SOUND = 340.29  # ISA speed of sound at sea level, m/s    
    ISA_T0             = 288.15  # ISA temperature at sea level
    ISA_T_TROPOPAUSE   = 216.65  # ISA temperature at tropopause, in Kelvins
    ISA_RHO_0          = 1.225   # ρ, ISA density of air at sea level, kg/m3
    AIR_GAMMA          = 1.4     # Air isentropic expansion coefficient
    EPSILON            = 2.718281828459 # base of the natural logarithm
    DELTA_TEMP         = DELTA_TEMP_ISA
    
    
    @classmethod
    def T0(cls):
        ''' Return temperature at sea level given temperature deviation from ISA condition. '''
        return cls.ISA_T0 + cls.DELTA_TEMP
    
    
    @classmethod
    def tropopause(cls):
        ''' Return the altitude of the tropopause in meters. Eq. 3.2-1 
            Arguments:
                delta_temp_isa: temperature different from ISA (at sea level, in Kelvin), default value = 0.0
        '''
        return cls.ISA_TROPOPAUSE + 1000.0*cls.DELTA_TEMP/6.5

    
    @classmethod
    def temperature(cls, altitude):
        ''' Return the temperature above and below the tropopause (in Kelvin). Eq. 3.2-4, 3.2-5
            Arguments:
                altitude: Altitude in meters
                delta_temp_isa: temperature different from ISA (at sea level, in Kelvin), default value = 0.0 
        '''
        if altitude >= cls.tropopause():
            return 216.65
        else:
            cls.T0(delta_temp_isa) - 6.5*altitude/1000.0    
    
    
    @classmethod
    def rho_tropopause(cls):
        ''' Return the air density at the tropopause '''
        T0 = cls.T0()
        power_term = - cls.GRAVITY / (cls.ISA_K_T * cls.REAL_GAS_CONTANT) - 1
        return ISA_RHO_0 * (cls.ISA_T_TROPOPAUSE/T0)**power_term


    @classmethod
    def air_density(cls, altitude):
        tropopause = cls.tropopause()
        if altitude <= tropopause:
            ''' Below the tropopause: rho is calculated as function of temperature, which in turn a function of altitude '''
            T0 = cls.T0()
            T = cls.temperature(altitude)
            power_term = - cls.GRAVITY / (cls.ISA_K_T * cls.REAL_GAS_CONTANT) - 1
            return cls.ISA_RHO_0 * (T/T0)**power_term
        else:
            ''' Above the tropopause: rho directly depends on the altitude. (Temperature is constant above the tropopause) '''
            rho_tropopause = cls.rho_tropopause()
            power_term = - cls.GRAVITY / (cls.REAL_GAS_CONTANT * cls.ISA_T_TROPOPAUSE) * (altitude - tropopause)
            return rho_tropopause * cls.EPSILON**power_term


    @classmethod
    def sound_speed(cls):
        pass


    @classmethod
    def cas_to_tas(cls, cas):
        pass
    

    @classmethod
    def tas_to_cas(cls, tas):
        pass



if __name__ == "__main__":
    ''' Testing atmosphere class '''
    pass