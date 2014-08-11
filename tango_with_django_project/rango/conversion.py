def encode(name):
	return name.replace(' ', '_')

def decode(url):
	return url.replace('_', ' ')