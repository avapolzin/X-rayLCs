# Novae

Each light curve file is named according to the event. _<event>_*.txt_ files are from Mukai et al. (2008) and have the suffix **_high** for upper limits and **_low** for lower limits. *Novae_Mukai.txt* contains a list of events, their distances, and k-corrections, which can be used to convert to 0.3-10 keV (following Mukai et al. in assuming a 5 keV bremsstrahlung spectrum where the native ROSAT luminosity is measured for the 0.2 - 2.4 keV band and all other instruments have their luminosities reported in the 2 - 10 keV band). The columns are "Day", which refers to days since outburst, and "logLum(cgs)", which gives the log of luminosity/(erg s<sup>-1</sup>) in the instrument's band.

The _*_fluxlc.qdp_ files are also named according to the event. **Novae_Page.txt** gives details of the light curve files including the distance in kpc and whether or not (isflux = YES or NO) the light curves give flux in counts or in cgs units. The relevant columns in the .qdp files are the first two: time (0th column) and observed 0.3 - 10 keV flux (1st column). If isflux = YES, then those latter values are in units of erg s<sup>-1</sup> cm<sup>-2</sup>. If isflux = NO, then those latter values are in counts per second and a uniform flux correction factor of 3.575e-11 can be applied to convert between counts/s and cgs units.

|Name | RA/Dec | Distance (kpc) | References|
| :---: | :---: | :---: | :---: |
|V838 Her |18:46:31.56 +12:14:00.7 | 3.4 | Mukai et al. 2008|
|V1974 Cyg | 20:30:31.61 +52:37:51.3 | 1.9 | Mukai et al. 2008|
|V351 Pup | 08:11:38.38 -35:07:30.4| 4.7 | Mukai et al. 2008|
|V382 Vel | 10:44:48.39 -52:25:30.7| 1.7 | Mukai et al. 2008|
|N LMC 2000 | 05:25:01.63 -70:14:17.4 | 55 | Mukai et al. 2008|
|V4633 Sgr | 18:21:40.49 -27:31:37.3| 8.9 | Mukai et al. 2008|
|N LMC 2005 | 05:10:32.68 -69:12:35.7 | 55 | Mukai et al. 2008|
|V5116 Sgr | 18:17:50.77 -30:26:31.3 | 11.3 | Mukai et al. 2008|
|V1663 Aql | 19:05:12.50 +05:14:12.0 | 5.5 | Mukai et al. 2008|
|V1188 Sco | 17:44:21.59 -34:16:35.7 | 7.5 | Mukai et al. 2008|
|V477 Sct | 18:38:42.93 -12:16:15.6 | 11 | Mukai et al. 2008|
|V476 Sct | 18:32:04.75 -06:43:34.3 | 4 | Mukai et al. 2008|
|V382 Nor | 16:19:44.74 -51:34:53.1 | 13.8 | Mukai et al. 2008|
|RS Oph | 17:50:13.2 -06:42:28.5 | 1.6 | Page et al. 2020|
|V2362 Cyg | 21:11:32.342 +44:48:03.67 | 7.2 - 15.8 | Poggiani 2009; Page et al. 2020|
|V1280 Sco | 16:57:40.91 -32:20:36.4| 1.6 | Chesneau et al. 2008; Page et al. 2020|
|V1281 Sco | 16:56:59.35 -35:21:50.2| 25.9 | Kantharia 2017; Page et al. 2020|
|V458 Vul | 19:54:24.61 +20:52:52.6 | 8.5 | Page et al. 2020|
|V597 Pup | 08:16:17.953 -34:15:25.19| 3 | Worpel et al. 2020; Page et al. 2020|
|V2468 Cyg | 19:58:33.57 +29:52:11.6| 5.6| Raj et al. 2015; Page et al. 2020|
|V2491 Cyg | 19:43:01.977 +32:19:13.55| 10.5 - 14| Darnley et al. 2011; Page et al. 2020|
|HV Cet (CSS081007) | 03:05:58.53 +05:47:15.7 | 4.45 | Page et al. 2020|
|LMC 2009a | 05:04:44.20 -66:40:11.6 | 50 | Page et al. 2020|
|V2672 Oph | 17:38:19.72 -26:44:13.7| 19 | Munari et al. 2011; Page et al. 2020|
|KT Eri | 04:47:54.201 -10:10:42.96| 6.3 | Raj et al. 2013; Page et al. 2020|
|U Sco | 16:22:30.778 -17:52:43.16| 12 | Schaefer 2010; Page et al. 2020|
|V407 Cyg | 21:02:09.8 +45:46:32.7 | 2.7 | Page et al. 2020|
|T Pyx | 09:04:41.506 -32:22:47.50| 3.185 | Schaefer 2018; Page et al. 2020|
|LMC 2012 | 04:54:56.852 -70:26:56.40| 50 | Page et al. 2020|
|V959 Mon | 06:39:38.599 +05:53:52.88 | 1.4 | Page et al. 2020; Li et al. 2020a|
|SMC 2012 | 00:32:34.384 -74:20:14.55 | 61 | Page et al. 2020|
|V339 Del | 20:23:30.686 +20:46:03.78 | 2.1 | Page et al. 2020; Li et al. 2020a|
|V1369 Cen | 13:54:45.363 -59:09:04.17 | 2.0 | Page et al. 2020; Li et al. 2020a|
|V745 Sco | 17:55:22.227 -33:14:58.56 | 7.8 | Schaefer 2010; Page et al. 2020|
|V1534 Sco | 17:15:46.83 -31:28:30.3 | 8.8 | Hachisu & Kato 2018; Page et al. 2020|
|V1535 Sco | 17:03:26.171 -35:04:17.82 | 8.5 | Linford et al. 2017; Page et al. 2020|
|V5668 Sgr | 18:37:39.9 -29:04:03 | 2.0 | Page et al. 2020; Li et al. 2020a|
|LMC 1968-12a | 05:09:58.40 -71:39:52.7 | 50 | Page et al. 2020|
|V407 Lup | 15:29:01.820 -44:49:40.89 | $\sim10$ | Aydi et al. 2018b; Page et al. 2020|
|SMCN 2016-10a | 01:06:03.27 -74:47:15.8 | 61 | Page et al. 2020|
|V549 Vel | 08:50:29.62 -47:45:28.3 | 0.560 | Page et al. 2020; Li et al. 2020a|
