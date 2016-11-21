from itty import *
from tropo import Tropo, Session

TO_NUMBER = '16478760704'
FROM_NUMBER = '16474929924'


@post('/index.json')
def index(request):
        t = Tropo()
        t.message("Hello World", TO_NUMBER, channel='VOICE', _from='tel:+' + FROM_NUMBER)
	json = t.RenderJson()
	print json
	return json
#retest


run_itty()