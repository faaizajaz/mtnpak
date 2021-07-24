from djgeojson.fields import PointField

def calculate_distance(point1: PointField, point2: PointField):
	"""Return the distance between two points, passed in as PointField objects"""
	import math

	LON1, LAT1 = point1['coordinates']
	LON2, LAT2 = point2['coordinates']

	# earths radius in km
	RADIUS = 6371
	LAT1_RADIANS = LAT1 * (math.pi/180)
	LAT2_RADIANS = LAT2 * (math.pi/180)

	DELTA_LAT_RADIANS = (LAT2 - LAT1) * (math.pi/180)
	DELTA_LON_RADIANS = (LON2 - LON1) * (math.pi/180)

	A = math.sin(DELTA_LAT_RADIANS/2) * math.sin(DELTA_LAT_RADIANS/2) + math.cos(LAT1_RADIANS) * math.cos(LAT2_RADIANS) * math.sin(DELTA_LON_RADIANS/2) * math.sin(DELTA_LON_RADIANS/2)
	C = 2 * math.atan2(math.sqrt(A), math.sqrt(1-A))

	distance = RADIUS * C

	return distance






