def convert_units(original, desired, value):

	if original == desired:
		return value
	else:
		if original == 'meters':
			if desired == 'feet':
				return value*3.28
		elif original == 'feet':
			if desired == 'meters':
				return value/3.28