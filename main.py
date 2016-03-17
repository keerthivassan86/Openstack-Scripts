import os
import time
from ucsmsdk import *
from ucsmsdk import ucshandle
import Firmware as firm
from config import IP,USERNAME,PASSWORD
def main():
    import pdb
    pdb.set_trace()
    handle=ucshandle.UcsHandle(IP,username=USERNAME,password=PASSWORD)
    handle.login()
    
    blade=firm.BladeServer(handle,"org-root/org-Finance",version="2.2(6g)",policy_name="onecloudfirmware") # Version number for the blade to upgrade
    blade.discover_blade_server()

if __name__ == "__main__":
    main()
