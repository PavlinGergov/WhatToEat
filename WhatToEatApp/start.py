import os
import sys

path = '/home/bgvladedivac/Desktop/APP/WhatToEat/WhatToEatApp'
if path not in sys.path:
    sys.path.append(path)

from main_logic import app as application