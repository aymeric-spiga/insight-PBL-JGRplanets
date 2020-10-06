#! /usr/bin/env python

from ppclass import pp
import ppplot
import numpy as np


fold = "25M_LS300_W20"
#fold = "25M_LS300_W10"

fifi = fold+"/wrfout_d01_9999-01-01_05:08:20"
var = "WNSFC"

field = pp()
field.file = fifi
field.var = var
field.z = 0
ffield = field.getf()

anom = pp()
anom.file = fifi
anom.var = var
anom.z = 0
anom.t = "0,1e10" ; anom.compute = "pert_t"
anom.verbose = True
fanom = anom.getf()

wip = 100.*fanom/ffield

logfac = np.log(1.165/0.1e-2)
wip = 0.4*ffield/logfac


pl = ppplot.plot2d()
pl.f = np.max(wip,axis=0)


w = np.where(pl.f <= 1.2)
pl.f[w] = 1.0

pl.colorbar = "copper_r"
pl.vmin = 1.0
pl.vmax = 1.5
pl.fmt = "%.2f"
pl.div = 20
pl.units = "m/s"
pl.xcoeff = 0.025
pl.ycoeff = 0.025
pl.xlabel = "x-axis (km)"
pl.ylabel = "y-axis (km)"
pl.make()

ppplot.save(mode="pdf",filename="tracks_"+fold)


