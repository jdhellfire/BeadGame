#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
from distutils.core import setup   
import py2exe                            
  

Pkt = ['graphics']
exclude = ['tkinter']            
options = {"py2exe":   
            {   "compressed": 1,           
                "optimize": 2,   
                "packages": Pkt,
		    "excludes" : exclude  
                  
            }   
          }   
  
setup(       
    version =       "1.0",   
    description =   "BeadGame",   
    name   =        "BeadGame",   
    options =       options,   
    zipfile=None,  

    console=[{"script": "BeadGame.py", "icon_resources": [(1, "BeadGame.ico")] }], requires=['graphics']
    )  