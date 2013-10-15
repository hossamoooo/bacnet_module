#/usr/bin/python

import sys
import logging
from ConfigParser import ConfigParser

from bacpypes.debugging import Logging, ModuleLogger
from bacpypes.consolelogging import ConsoleLogHandler

from bacpypes.core import run

# debug global vars
_debug = 0;
_log = ModuleLogger(globals())

# main function
def main():
try:
	_log.debug("initialiation")
	_log.debug("running")

except Exception, e:
	_log.exception("error", e)
finally:
	_log.debug("finally")

if('--buggers' in sys.argv):
	loggers = logging.Logger.manager.loggerDict.keys();
	loggers.sort();
	for loggerName in loggers:
		sys.stdout.write(lggername + '\n')
	sys.exit(0)

if('--debug' in sys.argv):
	indx = sys.argv.index('--debug')
	i = indx + 1
	while(i < len(sys.argv)) and (not sys.argv[i].startswith('--')):
		ConsoleLogHandler(sys.argv[i])
		i += 1;
	del sys.argv[indx:i]

config = ConfigParser()
if('--ini' in sys.argv):
	indx = sys.argv.index('--ini')
	ini_file = sys.argv[indx+1]
	if not config.read(ini_file):
		raise RuntimeError, "configuration file %r not found" % (ini_file,)
	del sys.argv[indx:indx+2]
elif not config.read('BACPypes.ini'):
	raise RuntimeError, "configuration file not found"

thisDevice = \
	LocalDeviceObject(objectName = config.get('BACpypes','objectName'))
	, objectIdentifier = config.getint('BACpypes','objectIdentifier')
	, maxApduLengthAccepted=config.getint('BACpypes','maxApduLengthAccepted')
	, segmentationSupported=config.get('BACpypes','segmentationSupported')
	, vendorIndentifier=config.getint('BACpypes','vendorIdentifier')
	)

SampleApplication(thisDevice, config.get('BACpypes','address'))
run() 

