import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state)
    # print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('new_states.json') as ns:
    new_data = json.load(ns)

for state in new_data['states']:
    print(state)



