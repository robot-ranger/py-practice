import logging
from xmlrpc.server import SimpleXMLRPCServer, list_public_methods
import inspect

# setup logging
FORMAT = ('%(asctime)-15s %(threadName)-20s '
		  '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(filename=str(__file__) + '.log', format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
logstream = logging.StreamHandler()
logstream.setLevel(logging.DEBUG)
log.addHandler(logstream)

# setup server
PORT = 7077
log.info("Initiallizing server at locahost:%i"%PORT)
s = SimpleXMLRPCServer(('localhost',PORT), logRequests=True)
s.register_introspection_functions()

# define functions
class funcs():
	def _listMethods(self):
		return list_public_methods(self)
	
	def _methodHelp(self, method):
		f = getattr(self, method)
		return inspect.getdoc(f)

	def add(self,a,b):
		"""Returns sum of a and b"""
		return a + b

	def mult(self,a,b):
		"""Returns product of a and b"""
		return a*b

s.register_instance(funcs())

try:
	print('Use Ctl+C to exit')
	s.serve_forever()
except KeyboardInterrupt:
	print('Exiting')