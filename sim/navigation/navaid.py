import numpy as np
from pygeodesy.ellipsoidalVincenty import LatLon

from config import APP_NAME


class Waypoint(LatLon):
    def __init__(self, lat, lon, name=''):
        super().__init__(lat=lat, lon=lon, name=name)        
        self.cartersian = self.toCartesian()

    @property
    def xy(self):
        return np.array([self.cartersian.x, self.cartersian.y])
    
    @property
    def latlon(self):
        return np.array([self.lat, self.lon])




if __name__ == '__main__' :
    test = Waypoint(41.49008, -71.312796, 'testwp')
    test1 = test.toCartesian()
    print(test.latlon)
    print(test.xy)
    print()