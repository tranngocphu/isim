'''Define of all possible aircraft phases during a flight'''

# Flight phases
INITIAL      = 'Just initialized'
DEP_GND_RUN  = 'Departure Ground Acceleration'
TAKE_OFF     = 'Take Off'
INITAL_CLIMB = 'Initial Climb'
CLIMB        = 'Climb'
CRUISE       = 'Cruise'
DESCENT      = 'Descent'
APPROACH     = 'Approach'
LANDING      = 'Landing'
ARR_GND_RUN  = 'Arrival Ground Run'
POSSIBLE_PHASES = [INITIAL, DEP_GND_RUN, TAKE_OFF, INITAL_CLIMB, CLIMB, CRUISE, DESCENT, APPROACH, LANDING, ARR_GND_RUN]

# Vstall configurations
TO = 'Take off'
IC = 'Initial climb'
CR = 'Cruise'
AP = 'Approach'
LD = 'Landing'
POSSIBLE_CONFIGURATIONS = [TO, IC, CR, AP, LD]
VSTALL_KEYS = {
    TO: 'Vstall_to',
    IC: 'Vstall_ic',
    CR: 'Vstall_cr',
    AP: 'Vstall_ap',
    LD: 'Vstall_ld',
}