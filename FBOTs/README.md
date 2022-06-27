# FBOTs

FBOT light curves are organized into folders by type (short, long, ultralong, and subluminous); the text files with names Swift_GRB_zonly_*.txt list the included GRBs and some additional information about them (redshift, t90, etc.). Because we focus exclusively on z ≤ 1 events in the paper, higher redshift GRBs are commented out in the list files, but the light curves themselves are still available and included in the relevant directories.

The light curve files are named according to the event and the relevant columns are "Time" (time since outburst in days) and "Flux" (0.3-10 keV flux in erg s-1 cm-2 -- and are rest frame by default). Other columns give the positive and negative error on "Time" and "Flux". The redshift in the list files can be used to convert the duration to the rest frame.

The exception to this formatting is GRB170817A, in which the columns are "days(sincemerger)", "flux(unabsorbed,0.3-10kev)" (in erg s-1 cm-2), and, like the other light curve files, positive and negative errors on the flux measurements.

See Table A5 for additional details about the individual events:

|Name | RA/Dec | Distance (kpc) | Reference|
| :---: | :---: | :---: | :---: |
|CSS161010 | 04:58:34.396 -08:18:03.95 | $1.5 \times 10^5$ | Coppejans et al. 2020|
|AT2018cow | 16:16:00.2242 +22:16:04.890 | $6.0 \times 10^4$ | Margutti et al. 2019|
|AT2020xnd | 22:20:02.04 -02:50:25.1 | $1.2 \times 10^6$ | Bright et al. 2021|
|AT2020mrf | 15:47:54.18 +44:29:07.16 | $6.37\times 10^5$ | Yao et al. 2021|
