# JSON MENU IDS
# CHALLENGE DESCRIPTION:
# You have JSON string which describes a menu. Calculate the SUM of IDs of all
# "items" in the case a "label" exists for an item.

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Input
# example is the following

# {"menu": {"header": "menu", "items": [{"id": 27}, {"id": 0, "label": "Label 0"}, null, {"id": 93}, {"id": 85}, {"id": 54}, null, {"id": 46, "label": "Label 46"}]}}
# {"menu": {"header": "menu", "items": [{"id": 81}]}}
# {"menu": {"header": "menu", "items": [{"id": 70, "label": "Label 70"}, {"id": 85, "label": "Label 85"}, {"id": 93, "label": "Label 93"}, {"id": 2}]}}

# All IDs are integers between 0 and 100. It can be 10 items maximum for a menu.

# OUTPUT SAMPLE:
# Print results in the following way.

# 46
# 0
# 248

def jsonMenuIDs(test):
	import json
	
	line = test.strip()
	j = json.loads(line)['menu']['items']
	
	total = 0
	for x in j:
		if x and 'id' in x and 'label' in x:
			total += x['id']

	return(total)


test_cases = open('jsonMenuIDs.txt', 'r')
for test in test_cases:
	print(jsonMenuIDs(test))


test_cases.close()