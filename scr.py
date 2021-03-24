import xml.etree.ElementTree as ET
import math
from array import array

class GPSPoint:
    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon

    def get_latitude(self):
        return self._lat

    def get_longitude(self):
        return self._lon

    def set_latitude(self, lat):
        self._lat = lat

    def set_longitude(self, lon):
        self._lon = lon

    latitude = property(get_latitude, set_latitude)
    longitude = property(get_longitude, set_longitude)

    def __str__(self):
        return "({}, {})".format(self._lat, self._lon)


class LocationManager():
    def __init__(self):
        self.locations = []
    
    def add_location(self, path):

        if(type(path) == 'list'):
            print("kokot")

        pass

        # ar = array('f')
        # with open(path, "rb") as f:
        #     arr = array('f')
        #     arr.frombytes(f.read())

        # for num in arr:
        #     ar.append(num)

        # for i, k in zip(ar[0::2], ar[1::2]):
        #     self.locations.append([i, k])

        # totalDistance = 0
        # count = 0
        # for i in range(len(test.locations)-1):
        #     point1 = GPSPoint(test.locations[count][0], test.locations[count][1])
        #     point2 = GPSPoint(test.locations[count+1][0], test.locations[count+1][1])
        #     totalDistance += LocationManager.get_distance(point1, point2)
        #     count += 1
        # print(f"Total distance of points from file {path} is {totalDistance} meters")

    
    def create_gpx(self, filename):

        root = ET.Element("gpx")
        root.set("version", "1.1")
        trk = ET.SubElement(root, "trk")
        path = ET.SubElement(trk, "name")
        path.text = "Path"
        trkseg = ET.SubElement(trk, "trkseg")

        for coords in self.locations:
            trkpt = ET.SubElement(trkseg, "trkpt")
            trkpt.set("lat", str(coords[0]))
            trkpt.set("lon", str(coords[1]))
            
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    @staticmethod
    def get_distance(GPS_point1, GPS_point2):
        R = 6371000
        fi1 = GPS_point1.latitude * math.pi / 180
        fi2 = GPS_point2.latitude * math.pi / 180
        deltaFi = (GPS_point2.latitude - GPS_point1.latitude) * math.pi / 180
        deltaLambda = (GPS_point2.longitude - GPS_point1.longitude) * math.pi / 180

        a = math.sin(deltaFi/2) * math.sin(deltaFi / 2) + math.cos(fi1) * math.cos(fi2) * math.sin(deltaLambda / 2) * math.sin(deltaLambda / 2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        return R * c


souradnice = [(49.8, 18.2), (49.9, 18.3)]

test = LocationManager()
test.add_location("locations.dat")
test.add_location("locations.dat")
test.create_gpx("brutalita.gpx")

# point1 = GPSPoint(49.9175043404, 18.2036630809)
# point2 = GPSPoint(49.8624285311, 18.1018678844)
# print(LocationManager.get_distance(point1, point2))




