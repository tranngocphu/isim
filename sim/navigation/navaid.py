''' 
This file contains abstract classes of NavAid such as Waypoints, Airways, Runways
'''

import numpy as np
from pygeodesy.ellipsoidalVincenty import LatLon

from sim.units import M2NM


from config import APP_NAME, SI, GEO


class NavAid(LatLon):
    '''
    The base class for all posiible navigation aids 
    that have lat, lon as geograhical location
    Args:
        lat: latitude in degrees
        lon: longitude in degrees
        name: name of the nav aid (optional)
    '''
    def __init__(self, lat, lon, name=''):
        super().__init__(lat=lat, lon=lon, name=name)
        self._cartersian = self.toCartesian()
        self._x = self._cartersian.x
        self._y = self._cartersian.y

    @property
    def xy(self):
        return np.array([self._x, self._y])

    @property
    def latlon(self):
        return np.array([self.lat, self.lon])
    
    def distance_to(self, other, unit=SI):
        assert isinstance(other, NavAid)
        distance = self.distanceTo(other)
        if unit is GEO:
            distance *= M2NM
        return distance
    
    def euclid_distance_to(self, other, unit=SI):
        assert isinstance(other, NavAid)
        distance = self.euclideanTo(other)        
        if unit is GEO:
            distance *= M2NM
        return distance   

    def caterisan_distance_to(self, other, unit=SI):
        assert isinstance(other, NavAid)
        p1 = np.array(self._cartersian.xyz)
        p2 = np.array(other._cartersian.xyz)
        distance = np.linalg.norm(p1-p2)
        return distance

    

class Waypoint(NavAid):
    def __init__(self, lat, lon, name=''):
        super().__init__(lat=lat, lon=lon, name=name)



if __name__ == '__main__' :
    p1 = Waypoint(3.2568, -50.6598, 'P1')    
    p2 = Waypoint(2.2365, -52.312796, 'P2')    
    print(p1.distance_to(p2))
    print(p1.euclid_distance_to(p2))
    print(p1.caterisan_distance_to(p2))
