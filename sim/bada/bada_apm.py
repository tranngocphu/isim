'''
Implementation of functions in the Airline Precedure Models
'''

from sim.constants import REAL_GAS_CONTANT, ISA_SPEED_OF_SOUND, ISA_T0, ISA_TEMP_GRAD, GRAVITY, AIR_GAMMA
from sim.units import FT2M

def transition_altitude_feet(Vcas, Mach, unit='feet'):
    '''
    Implementation for equations 4.1-9 - 4.1-11 in the BADA 3.6 Manual
    Args:
        Vcas : calibrated speed of the aircraft in m/s
        Mach : considered Mach number
    '''
    
    '''Eq. 4.1-11'''
    delta_trans = 1 + ((AIR_GAMMA-1)/2.0)*(Vcas/ISA_SPEED_OF_SOUND)**2
    delta_trans = delta_trans**((AIR_GAMMA)/(AIR_GAMMA-1))
    delta_trans = delta_trans - 1
    delta_trans = delta_trans / ((1 + ((AIR_GAMMA-1)/2.0)*(Mach**2))**((AIR_GAMMA/(AIR_GAMMA-1))) - 1)

    '''Eq. 4.1-10'''
    theta_trans = delta_trans**(-ISA_TEMP_GRAD*REAL_GAS_CONTANT/GRAVITY)
    h_trans = (1000/0.3048/6.5)*ISA_T0*(1 - theta_trans)
    if unit=='meter':
        h_trans = h_trans*FT2M




if __name__ == "__main__":
    from sim.units import KNOTS2MS
    # From A320__.APF:
    Vcas = 310 # V_cl2
    Vcas_ms  = Vcas * KNOTS2MS
    Mach = 0.80 # M_cl
    print("Vcas: {} m/s; Mach: {}; Calculated Transition Altitude: {} feet.".format(Vcas_ms, Mach, transition_altitude_feet(Vcas_ms, Mach)))
