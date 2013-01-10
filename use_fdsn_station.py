import time
from fdsn_station import *

doc = FDSNStationXML(source='Test Agency', schema_version=1.0, created=round(time.time()))

net = Network(code='NE')

sta = Station(code='STA', 
        latitude = Latitude(value=0.0), 
        longitude = Longitude(value=0.0),
        elevation = Distance(value=0.0),
        site = Site(name='Testsite'),
        creation_date = round(time.time()))


net.station_list.append(sta)
doc.network_list.append(net)

print doc.dump_xml()


