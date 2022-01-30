import pprint

import xbmc

from .bar import BAR

v = vars().copy()
for name, value in v.items():
    xbmc.log(f"FOO {name}={value}", xbmc.LOGINFO)
