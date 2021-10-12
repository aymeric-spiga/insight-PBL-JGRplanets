#! /usr/bin/env python
# coding: utf-8

import numpy as np
import apss_lib

###########################################################
###########################################################
recalculate = False # recalculate only when txt is missing
window = 1000 # optimum
datatype = "pds" # read directly in PDS format
###
soltab = range(335,351)
soltab = [248]
soltab = range(1,20)
#soltab = [341] ; recalculate = True ; window = 1000 

###########################################################
###########################################################
#####################
### RECOMPUTE ALL ###
#####################
recalculate = True # recalculate everything included in soltab (could be very long)
lastday = 807
soltab = range(1,lastday+1) 
recalculate = False  # recalculate only when txt is missing

###########################################################
window = 1000. ; droplim = -0.35 ; winsearch = 30 ; denoise = True
###########################################################

#### MAIN MAIN MAIN MAIN ####
apss_lib.analyze_pressure(soltab=soltab,recalculate=recalculate,datatype=datatype,\
                          window=window,droplim=droplim,winsearch=winsearch,denoise=denoise)
#### MAIN MAIN MAIN MAIN ####
try:
    dafile = open("./sol_.txt","a")
    fisol,firatio = np.loadtxt("./sol_.txt",unpack=True)    
except:
    dafile = open("./sol_.txt","w")
    fisol = []
for sol in soltab:
    if sol not in fisol:
       ratio = apss_lib.ratioddsol(sol,reload=False,var="PRE",distant=True)
       dafile.write( '%03d %5.3f\n' % (sol,ratio))
       print "added ratio %03d for sol %i" % (ratio,sol)
dafile.close()


