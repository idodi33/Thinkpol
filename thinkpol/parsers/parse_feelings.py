import json
from parsers.parser_utils import extract_metadata


def parse_feelings(snapshot, data_dir=None):
	"""
	Gets a json dict with snapshot data including feelings, 
	and returns another json with differently formatted data.

	:param snapshot: the snapshot we're parsing
	:type snapshot: json
	:returns: a json containing information about the snapshot.
	:rtype: json
	"""
	js = json.loads(snapshot)
	json_parsed = extract_metadata(js)
	json_parsed['hunger'] = js['hunger']
	json_parsed['thirst'] = js['thirst']
	json_parsed['exhaustion'] = js['exhaustion']
	json_parsed['happiness'] = js['happiness']
	json_parsed = json.dumps(json_parsed)
	return json_parsed

parse_feelings.field = 'feelings'
