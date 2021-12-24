#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/va/projects/python/FlaskApp/")

from FlaskApp import app as application