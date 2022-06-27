# GRBs

GRB light curves are organized into folders by type (short, long, ultralong, and subluminous); the text files with names _Swift\_GRB\_zonly\_\*.txt_ list the included GRBs and some additional information about them (redshift, t<sub>90</sub>, etc.). Because we focus exclusively on z &le; 1 events in the paper, higher redshift GRBs are commented out (with '#') in the list files, but the light curves themselves are still available and included in the relevant directories.

The light curve files are named according to the event and the relevant columns are "Time" (time since outburst in days) and "Flux" (0.3-10 keV flux in erg s<sup>-1</sup> cm<sup>-2</sup> -- and are rest frame by default). Other columns give the positive and negative error on "Time" and "Flux". The redshift in the list files can be used to convert the duration to the rest frame.

The exception to this formatting is GRB170817A, in which the columns are "days(sincemerger)", "flux(unabsorbed,0.3-10kev)" (in erg s<sup>-1</sup> cm<sup>-2</sup>), and, like the other light curve files, positive and negative errors on the flux measurements.

See Table A1 for additional details about the individual events:

|Name | Type | t$_{90}$ (s) | RA/Dec | z | Distance (kpc) | References|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GRB980425A | subluminous | 22.0 | 19:35:03.17 -52:50.46 | 0.0085 | $2.7\times10^4$| Pian et al. 2000; Kouveliotou et al. 2004|
|GRB031203A | subluminous | 30 | 08:02:30.1 -39:51:03 | 0.105 | $4.9\times10^5$ | Sazanov et al. 2004; Watson et al. 2004|
|GRB050509B | short | 0.073 | 12:36:18.00 +29:01:24.0| 0.225 | $1.1\times10^6$ | Evans et al. 2007, 2009|
|GRB050724 | short | 3.00 | 16:24:44.400 -27:32:27.90 | 0.258 | $1.3\times10^6$ | Evans et al. 2007, 2009|
|GRB051221A | short | 1.400 | 21:54:48.626 +16:53:27.16 | 0.5465 | $3.2\times10^6$ | Evans et al. 2007, 2009|
|GRB060218A | subluminous | 2100 | 09:09:30.625 +33:08:20.16 | 0.0331 | $1.5 \times10^5$ | Evans et al. 2007, 2009|
|GRB061006 | short | 0.42 | 07:24:07.660 -79:11:55.10 | 0.438 | $2.4\times10^6$ | Evans et al. 2007, 2009|
|GRB061210 | short | 85.0 | 09:38:05.270 +15:37:17.30 | 0.4095 | $2.3\times10^6$ | Evans et al. 2007, 2009|
|GRB061217 | short | 0.210 | 10:41:39.320 -21:07:22.11 | 0.827 | $5.3\times10^6$ | Evans et al. 2007, 2009|
|GRB070714B | short | 3.0 | 03:51:22.30 +28:17:51.3 | 0.923 | $6.1\times10^6$ | Evans et al. 2007, 2009|
|GRB070724A | short | 0.4 | 01:51:14.08 -18:35:38.8 | 0.457 | $2.6\times10^6$ | Evans et al. 2007, 2009|
|GRB071227 | short | 1.8 | 03:52:31.09 -55:59:03.3 | 0.383 | $2.1\times10^6$ | Evans et al. 2007, 2009|
|GRB080905A | short | 1.0 | 19:10:39.10 -18:51:55.4 | 0.1218 | $5.7\times10^5$ | Evans et al. 2007, 2009|
|GRB090510A | short | 0.3 | 22:14:12.60 -26:35:51.1 | 0.903 | $5.9\times10^6$ | Evans et al. 2007, 2009|
|GRB100117A | short | 0.3 | 00:45:04:56 -01:35:41.7 | 0.92 | $6.0\times10^6$ | Evans et al. 2007, 2009|
|GRB100316D | subluminous | 292.8 | 07:10:30.63 -56:15:19.7| 0.059 | $2.7\times10^5$ | Evans et al. 2007, 2009|
|GRB100816A | short | 2.9 | 23:26:57.56 +26:34:42.6 | 0.8049 | $5.1\times10^6$ | Evans et al. 2007, 2009|
|GRB101219A | short | 0.6 | 04:58:20.45 -02:32:23.1 | 0.718 | $4.4\times10^6$ | Evans et al. 2007, 2009|
|GRB101225A | ultralong | 1088 | 00:00:47.48 +44:36:01.0 | 0.847 | $5.5 \times10^6$ | Evans et al. 2007, 2009|
|GRB141212AS | short | 0.30 |02:36:29.95 +18:08:49.1 | 0.596 | $3.5\times10^6$ | Evans et al. 2007, 2009|
|GRB141225A | long | 40.24 | 09:15:06.79 +33:47:30.6| 0.915 | $6.0 \times 10^6$ | Evans et al. 2007, 2009|
|GRB150101BS | short | 0.08 |12:32:04.98 -10:56:00.7 | 0.134 | $6.4\times10^5$ | Evans et al. 2007, 2009|
|GRB150323A | long | 149.6 | 08:32:42.74 +45:27:52.7| 0.593 | $3.5 \times 10^6$ | Evans et al. 2007, 2009|
|GRB150514A | long | 10.8 |04:59:30.46 -60:58:06.9 | 0.807 | $5.1 \times 10^6$ | Evans et al. 2007, 2009|
|GRB150518A | subluminous | -- | 15:36:48.25 +16:19:47.3 | 0.256 | $1.3\times10^6$ | Evans et al. 2007, 2009|
|GRB150727A | long | 88 | 13:35:52.51 -18:19:32.5| 0.313 | $1.6 \times 10^6$ | Evans et al. 2007, 2009|
|GRB150818A | long | 123.3 | 15:21:25.44 +68:20:31.3| 0.282 | $1.5 \times 10^6$ | Evans et al. 2007, 2009|
|GRB150821A | long | 172.1 | 22:47:39.13 -57:53:38.1 | 0.755 | $4.7 \times 10^6$ | Evans et al. 2007, 2009|
|GRB151027A | long | 129.69 | 18:09:56.86 +61:21:11.9| 0.81 | $5.2\times 10^6$ | Evans et al. 2007, 2009|
|GRB160131A | long | 325 | 05:12:40.32 -07:02:59.5| 0.972 | $6.5 \times 10^6$ | Evans et al. 2007, 2009|
|GRB160314A | long | 8.73 | 07:31:09.79 +16:59:57.3| 0.726 | $4.9\times 10^6$ | Evans et al. 2007, 2009|
|GRB160425A | long | 304.58 | 18:41:18.55 -54:21:36.1| 0.555 | $3.2\times 10^6$ | Evans et al. 2007, 2009|
|GRB160623A | long | 13.5 | 21:01:11.54 +42:13:15.4| 0.367 | $2.0\times 10^6$ | Evans et al. 2007, 2009|
|GRB160624AS | short | 0.2 | 22:00:46.21 +29:38:37.8 | 0.483 | $2.7\times10^6$ | Evans et al. 2007, 2009|
|GRB160804A | long | 130 | 14:46:31.20 +09:59:55.9| 0.736 | $4.6 \times 10^3$ | Evans et al. 2007, 2009|
|GRB160821BS | short | 0.48 | 18:39:54.550 +62:23:30.35 | 0.16 | $7.7\times10^5$ | Evans et al. 2007, 2009|
|GRB161219B | long | 6.94 | 06:06:51.37 -26:47:29.7| 0.1475 | $7.1 \times 10^5$ | Evans et al. 2007, 2009|
|GRB170519A | long | 216.4 | 10:53:42.50 +25:22:26.8| 0.818 | $5.2\times 10^6$ | Evans et al. 2007, 2009|
|GRB170607A | long | 23.0 | 00:29:27.82 +09:14:35.7| 0.557 | $3.3\times10^6$ | Evans et al. 2007, 2009|
|GRB170714A | ultralong | 1000 | 02:17:23.97 +01:59:29.0 | 0.793 | $5.0\times10^6$ | Evans et al. 2007, 2009|
|GRB170817A | short | 2.0 | 13:09:48.085 -23:22:53.343 | 0.0099 | $4.3\times10^4$ |  Hajela et al. 2019, 2020|
|GRB171010A | long | 70.3 |04:26:19.42 -10:27:47.7 | 0.3285 | $1.7\times 10^6$ | Evans et al. 2007, 2009|
|GRB171205A | subluminous | 189.4 | 11:09:39.49 -12:35:18.7 | 0.0368 | $1.6\times10^5$ | Evans et al. 2007, 2009|
|GRB180404A | long | 35.2 |05:34:11.74 -37:10:04.8 | 1.000 | $6.7\times10^6$ | Evans et al. 2007, 2009|
|GRB180703A | long | 20.9 |00:24:28.10 -67:18:17.9 | 0.6678 | $4.0\times10^6$ | Evans et al. 2007, 2009|
|GRB180720B | long | 51.1 | 00:02:06.86 -02:55:08.1 | 0.654 | $4.0 \times10^6$ | Evans et al. 2007, 2009|
|GRB180728A | long | 8.68 | 16:54:15.60 -54:02:40.2| 0.117 | $5.5\times10^5$ | Evans et al. 2007, 2009|
|GRB190114C | long | 361.5 | 03:38:01.18 -26:56:47.8 | 0.425 | $2.4 \times 10^6$ | Evans et al. 2007, 2009|
|GRB190829A | long | 63 | 02:58:10.50 -08:57:29.8| 0.0785 | $3.6\times10^5$ | Evans et al. 2007, 2009|
|GRB191019A | long | 64.35 |22:40:05.87 -17:19:40.8 | 0.248 | $1.3\times10^6$ | Evans et al. 2007, 2009|
