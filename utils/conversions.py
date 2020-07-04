#conversion function checks what conversion needs to take place
def convert_units(original, desired, value):
	if original == desired:
		return value
	else:
		if original == 'meters':
			if desired == 'feet':
				return meters_to_feet(value)
		elif original == 'feet':
			if desired == 'meters':
				return feet_to_meters(value)


#unit conversions
def feet_to_meters(value):
	return value/3.28084

def meters_to_feet(value):
	return value*3.28084