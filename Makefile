##This is a Makefile

target: simdat.Rout 

target pngtarget pdftarget vtarget acrtarget: simdat.Rout 

##################################################################

Sources += Makefile stuff.mk
include stuff.mk
-include $(ms)/git.def

beta.Rout: beta.R

simdat.Rout: CBsimulator.R paramsCB.R simulateCB.R
	$(run-R)

Nimble.fit.Rout:

%.fit.Rout: simdat.Rout paramsCB.R %.CB.R
	$(run-R)

Pymc.fit: PymcCB.py
	python PymcCB.py

#############
Sources += $(wildcard *.R)

-include $(ms)/git.mk
-include $(ms)/visual.mk
-include $(ms)/linux.mk
-include $(ms)/wrapR.mk
-include rmd.mk
