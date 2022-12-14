# MIT License
#
# Copyright (c) 2022  Dr. Magnus Christ (mc0110)
#
# This is part of the inetbox2mqtt package
# 
# 
# After reboot the port starts with boot.py and main.py
#
# This code-segment needs to be named "main.py"
#
#
#
#
# Use this commands to connect to the network 
#
# import network
# s = network.WLAN(network.STA_IF)
# s.active(True)
# s.connect("<yourSSID>","<YourWifiPW>")
# print('network config:', s.ifconfig())
# import mip
# mip.install("github:mc0110/wifimanager/bootloader/main.py","/")
# 
# import main
#
# The last command starts the download-process of the whole suite
# The download overwrites the main-program, so you see this process only once



import time, os
import mip
#sleep to give some boards time to initialize, for example Rpi Pico W
time.sleep(3)

# bootloader for the whole suite
tree = "github:mc0110/wifimanager"

env = [       
    ["/lib/", "ccrypto_keys.py", "/lib"],
    ["/lib/", "connect.py", "/lib"],
    ["/src/", "cred.py", "/"],
    ]

for i in range(len(env)):
    mip.install(tree+env[i][0]+env[i][1], target= env[i][2])


import cred
cred.set_cred_json()
cred.update_repo()

import main