# TDEs

All light curves from Auchettl et al. (2017) are in TDEs_Auchettl.txt, where a single light curve can be constructed from the set of rows with the same "Name". Given that the time resolution is ~0.01 yr, we take the first datapoint in each light curve to be +0.01 yr from the detection of the outburst.

For ASASSN-19bt from Holoien et al. (2019), the "Time" is MJD - 58504.6, to align with the first detection light of the outburst, "Luminosity" is the 0.3-10 keV X-ray luminosity in cgs units. 

ASASSN-14li_XRT_Brown2016.txt (Brown et al. 2017) has two columns, "Days" and "Count-rate(0.01)" -- to get flux (cgs) from the later simply multiply by the "Count-rate(0.01)" x 0.01 x 3.5e-11.

ASASSN15oi_Xray.txt (Holoien et al. 2018) also has two columns, "Timesincediscovery(days)" and "X-rayflux(1e-14)". The later can be converted to flux in cgs units by "X-rayflux(1e-14)" x 1e-14.

The relevant columns of Swift1644_XRT_phil.txt (Mangano et al. 2016) are "timeobs", which is in seconds, and "flux", which is in cgs units. The "terr" and "ferr" columns give the error on time and flux respectively. To correct the flux for absorption (which, with the exception of GRBs, we only do explicitly in cases where the column density is exceedingly high and the correction is well-constrained), we use a factor of 8.91/4.83.

|Name | Type | RA/Dec | Distance (kpc) | References|
| :---: | :---: | :---: | :---: | :---: |
|PS10jh | thermal | 16:09:28.296 +53:40:23.52 | $8.2\times10^5$ | Gezari et al. 2012; Auchettl et al. 2017|
|ASASSN-14ae | thermal | 11:08:40.11 +34:05:52.4 | $2.0\times10^5$ | Holoien et al. 2014; Auchettl et al. 2017|
|ASASSN-14li | thermal | 12:48:15.22 +17:46:26.5 | $9.0\times10^4$ | Miller et al. 2015; Brown et al. 2017; Auchettl et al. 2017; Bright et al. 2018|
|ASASSN-15oi | thermal | 20:39:09.096 -30:45:20.71 | $2.2\times10^5$ | Auchettl et al. 2017; Holoien et al. 2018|
|Swift 1644+57 | non-thermal | 16:44:49.3 +57:34:51 | $1.9\times10^6$ | Mangano et al. 2016; Auchettl et al. 2017|
|ASASSN-19bt | non-thermal | 07:00:11.410 -66:02:25.16 | $1.15\times10^5$ | Holoien et al. 2019|
|Swift J2058.4+0516a | non-thermal | 20:58:19.898 +05:13:32.25 | $1\times10^7$ | Auchettl et al. 2017|
|SDSS J131122.15-012345.6 | thermal | 13:11:22.154 -01:23:45.61 | $9.0\times10^5$ | Auchettl et al. 2017|
|SDSS J132341.97+482701.3 | thermal | 13:23:41.973 +48:27:01.26 | $4.0\times10^5$ | Auchettl et al. 2017|
|SDSS J1201+3003 | thermal | 12:01:36.028 +30:03:05.52 | $7.1\times10^5$ | Auchettl et al. 2017|
|WINGS J1348 | thermal | 13:48:51.1 +26:35:05.7 | $2.8\times10^5$ | Auchettl et al. 2017|
|RBS 1032 | thermal | 11:47:26.73 +49:42:57.3 | $1.1\times10^5$ | Auchettl et al. 2017|
|3XMM J1521+0749 | thermal | 11:47:26.70 +49:42:57.8 | $8.9\times10^5$ | Auchettl et al. 2017|
|2MASX J0249 | thermal | 02:49:17.32 -04:12:52.20 | $8.0\times10^4$ | Auchettl et al. 2017|
|IGR J17361-4441 | thermal | 17:36:17.42 -44:44:05.98 | $1.8\times10^5$ | Auchettl et al. 2017|
|NGC 247 | thermal | 00:47:08.55 -20:45:37.44 | $2240$ | Auchettl et al. 2017|
|OGLE 16aaa | thermal | 01:07:20.88 -64:16:20.70 | $8.1\times10^5$ | Auchettl et al. 2017|
|PTF-10iya | thermal | 14:38:40.98 +37:39:33.45 | $1.2\times10^6$ | Auchettl et al. 2017|
|XMMSL1 J0740-85 | therma | 07:40:08.09 -85:39:31.30 | $7.4\times10^5$ | Auchettl et al. 2017|

