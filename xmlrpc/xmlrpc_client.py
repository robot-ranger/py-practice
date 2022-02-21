import logging
import xmlrpc.client


# setup logging
FORMAT = ('%(asctime)-15s %(threadName)-20s '
		  '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(filename=str(__file__) + '.log', format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
logstream = logging.StreamHandler()
logstream.setLevel(logging.DEBUG)
log.addHandler(logstream)

# setup client
PORT = 7077
c = xmlrpc.client.ServerProxy('http://localhost:%i'%PORT)
print(c.system.listMethods())
def getMethods():
	for method_name in c.system.listMethods():
		print('=' * 60)
		print(method_name)
		print('-' * 60)
		print(c.system.methodHelp(method_name))

getMethods()