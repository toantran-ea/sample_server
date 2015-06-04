
import json
from pprint import pprint
import mock_responses


class MessageHandler():
	def __init__(self):
		pass

	def handle(self, message):
		try:
			request = json.loads(message)
			command_id = request.get("id", 0)
			if request.get('method','') == 'SetGroupID':
				return mock_responses.SETGROUPID % command_id
			elif request.get('method','') == 'SetGroupManual':
				return mock_responses.SETGROUPMANUAL % command_id
			elif request.get('method','') == 'SetGroupScence':
				return mock_responses.SETGROUPSCENE % command_id
			return "{}"
		except:
			print "handle --> error parsing json"


