#! /usr/bin/env python
# coding: utf-8

import numpy as np
import apss_lib
import os
datatype = "pds" # read directly in PDS format
recalculate = True # recalculate everything included in soltab (could be very long)
#recalculate = False
detailed_check = False
#detailed_check = True

###########################################################
###########################################################

## single sols
##soltab = [19]
#soltab = [608]
##soltab = [65]
##soltab = [18]
#soltab = [352]
##soltab = [205]
##soltab = [319]

### all sols
lastday = 400 ; soltab = range(1,lastday+1) 


###########################################################
###########################################################

#window = 1000. ; droplim = 99.   ; winsearch = 30 ; denoise = True  ; test_cell = True  ; zefold = "outputjgr_W1000_LIMADAPT_B30_DENOISE_TESTCELL"
#window = 0500. ; droplim = -0.35 ; winsearch = 30 ; denoise = False ; test_cell = False ; zefold = "outputjgr_W0500_LIM0p35_B30"
#window = 0500. ; droplim = 99.   ; winsearch = 30 ; denoise = True  ; test_cell = True  ; zefold = "outputjgr_W0500_LIMADAPT_B30_DENOISE_TESTCELL"
#window = 1000. ; droplim = -0.30 ; winsearch = 50 ; denoise = False ; test_cell = False ; zefold = "outputjgr" ## [default] W1000_LIM0p3_B50

###########################################################
###########################################################

#window = 1000. ; droplim = -0.35 ; winsearch = 30 ; denoise = True  ; test_cell = True  ; zefold = "outputjgr_W1000_LIM0p35_B30_DENOISE_TESTCELL"
#window = 1000. ; droplim = -0.35 ; winsearch = 30 ; denoise = False ; test_cell = True  ; zefold = "outputjgr_W1000_LIM0p35_B30_TESTCELL"
#window = 1000. ; droplim = -0.35 ; winsearch = 30 ; denoise = False ; test_cell = False ; zefold = "outputjgr_W1000_LIM0p35_B30"
#window = 1000. ; droplim = -0.35 ; winsearch = 50 ; denoise = False ; test_cell = False ; zefold = "outputjgr_W1000_LIM0p35_B50"
window = 1000. ; droplim = -0.35 ; winsearch = 30 ; denoise = True  ; test_cell = False ; zefold = "outputjgr_W1000_LIM0p35_B30_DENOISE"
#window = 1000. ; droplim = -0.30 ; winsearch = 30 ; denoise = False ; test_cell = False ; zefold = "outputjgr_W1000_LIM0p30_B30" 
#zefold = "outputTRASH"

###########################################################
###########################################################

try:
  os.mkdir(zefold)
  os.mkdir(zefold+"/txt_per_sol")
  os.mkdir(zefold+"/pdf_per_sol")
  os.mkdir(zefold+"/pdf_per_sol_strongest")
except:
  pass

###########################################################
###########################################################
#### MAIN MAIN MAIN MAIN ####
apss_lib.analyze_pressure(soltab=soltab,recalculate=recalculate,datatype=datatype,\
                          detailed_check=detailed_check,test_cell=test_cell,denoise=denoise,\
                          window=window,droplim=droplim,zefold=zefold,winsearch=winsearch)
#### MAIN MAIN MAIN MAIN ####


