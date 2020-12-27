import json
import os

dataset = 'dataset_dates.json'
original = 'dataset_colours.json'
destination = 'dataset_complete.json'

data_dates = []
data_cols = []

with open(dataset, 'r') as d:
	d = json.loads(d.read())
	data_dates = d['albums']

n_albums = len(data_dates)

with open(original, 'r') as o:
	new_data = []
	o = json.loads(o.read())
	data_cols = o['albums']
	
for i, datum in enumerate(data_dates):
	name = datum['album_name']
	artist = datum['artist_name']
	album = None

	for o_datum in data_cols:
		if type(o_datum) is list:
			o_datum = o_datum[0]
		try:
			if o_datum['album_name'] == name and o_datum['artist_name'] == artist:
				album = orig[j]
				print(i, 'found')
				break
		except:
			continue

	if album is not None:
		album['date'] = datum['date']
		new_data.append(album)
		print(i, '- found')
	else:
		continue
		print(i, '- not found')

	if len(new_data) == 25:
		print('saving 25 data')
		to_app = {'albums' : new_data}
		new_data = []
		if not os.path.isfile(destination):
			with open(destination, 'w') as dest:
				dest.write(json.dumps(to_app, indent=4))
		else:
			old = {}
			with open(destination, 'r') as dest:
				old = json.loads(dest.read())
			with open(destination, 'w') as dest:
				for new_datum in to_app['albums']:
					old['albums'].append(new_datum)
				dest.write(json.dumps(old, indent=4))

	if i == n_albums-1 and os.path.isfile(destination):
		print('saving last data')
		to_app = {'albums' : new_data}
		new_data = []
		old = {}
		with open(destination, 'r') as dest:
			old = json.loads(dest.read())
		with open(destination, 'w') as dest:
			for new_datum in to_app['albums']:
				old['albums'].append(new_datum)
			dest.write(json.dumps(old, indent=4))







