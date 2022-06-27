# FBOTs

GRB light curves are organized into folders by type (short, long, ultralong, and subluminous); the text files with names Swift_GRB_zonly_*.txt list the included GRBs and some additional information about them (redshift, t90, etc.). Because we focus exclusively on z ≤ 1 events in the paper, higher redshift GRBs are commented out in the list files, but the light curves themselves are still available and included in the relevant directories.

The light curve files are named according to the event and the relevant columns are "Time" (time since outburst in days) and "Flux" (0.3-10 keV flux in erg s-1 cm-2 -- and are rest frame by default). Other columns give the positive and negative error on "Time" and "Flux". The redshift in the list files can be used to convert the duration to the rest frame.

The exception to this formatting is GRB170817A, in which the columns are "days(sincemerger)", "flux(unabsorbed,0.3-10kev)" (in erg s-1 cm-2), and, like the other light curve files, positive and negative errors on the flux measurements.

See Table A1 for additional details about the individual events (NOTE: will add a typeset image of the table to this README when it becomes available from the journal).
