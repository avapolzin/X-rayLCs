# SNe

SN light curves are organized into folders by type (as defined in the paper -- Type I, Type II, Interacting, Superluminous, and Ca-rich); the text files with names _SNe\_\*\_list.txt_ list the included SNe and some additional details about them (distance, k-correction, etc.).

The _Type I_, _Type II_, and _Interacting_ light curve files are named according to the event and the energy in tens of eV, so that "SN1993J_lc_30_1000.txt" is the 0.3-10 keV light curve for SN1993J and "SN2005kd_lc_50_800.txt" is the 0.5-8 keV light curve for SN2005kd. The k-correction for each event in the list files can be used to convert the light curves to 0.3-10 keV.

The relevant columns are "time(days)" and "flux(1d-15 erg/s/cm2)" (flux in units of 10<sup>-15</sup> erg s<sup>-1</sup> cm<sup>-2</sup>). Other columns give the (symmetric) error on "time" and "flux", as well as the instrument that took the observation. Additional light curve-specific information is retained at the top of some of the event files.

The _Superluminous_ and _Ca-rich_ light curve files are named according to the event. The columns for _Superluminous_ light curves are "time(days)" and "Lum(erg/s)" (in the 0.3-10 keV band). The colums for the _Ca-rich_ light curve are "Time(day)" and "Flux(erg/s/cm2)" (also 0.3-10 keV).

See Table A3 for additional details about the individual events:

|Name | Type | RA/Dec | Distance (kpc) | References|
| :---: | :---: | :---: | :---: | :---: |
|SN1978K | II |03:17:38.620 -66:33:03.40 | $4.5 \times 10^3$ | Raf's data reduction|
|SN1980K | IIL |20:35:30.07 +60:06:23.7 | $5.1 \times 10^3$ | Soria & Perna 2008|
|SN1981K | II | 12:18:59.42 +47:19:31.0| $7.2 \times 10^3$ | Immler et al. 2007b|
|SN1986J | IIn |02:22:31.33 +42:19:56.4 | $9.6 \times 10^3$ | Raf's data reduction|
|SN1987A | IIpec | 05:35:28.020 -69:16:11.07|50 | Haberl et al. 2006; Heng et al. 2008; Sturm et al. 2010|
|SN1993J | IIb |09:55:24.77 +69:01:13.7 | $2.6 \times 10^3$ | Chandra et al. 2009 + Raf's data reduction|
|SN1995N | IIn | 14:49:28.29 -10:10:14.0| $2.4 \times 10^4$ | Zampieri et al. 2005|
|SN1996cr | IIn |14:13:10.05 -65:20:44.8 | $3.8 \times10^3$ | Bauer et al. 2008 + Raf's data reduction|
|SN1998bw | Ib/c | 19:35:03.17 -52:50:46.1| $3.8 \times 10^4$ | Kouvelioutou et al. 2004|
|SN1999em | IIP | 04:41:27.04 -02:51:45.2| $7.8  \times  10^3$ | Pooley et al. 2002|
|SN1999gi | IIP | 10:18:16.66 +41:26:28.2| $8.7 \times 10^3$ | Schlegel 2001|
|SN2001em | Ib/c |21:42:23.61 +12:29:50.3 | $8.0 \times 10^4$ | Pooley & Lewin 2004a + Raf's data reduction|
|SN2001ig | II | 22:57:30.69 -41:02:25.9 | $1.1 \times 10^4$ | Schlegel & Ryder 2002|
|SN2002ap | Ib/c | 01:36:23.85 +15:45:13.2 | $1.0 \times 10^4$ | Soria et al. 2004|
|SN2002hh | II | 20:34:44.29 +60:07:19.0| $5.1 \times 10^3$ | Pooley & Lewin 2002|
|SN2002hi | IIn | 07:19:54.08 +17:58:18.8| $1.8 \times 10^5$ | Pooley & Lewin 2003|
|SN2003bg | Ic/pec | 04:10:59.42 -31:24:50.3| $1.9 \times 10^4$ | Soderberg et al. 2006|
|SN2004dj | IIP | 07:37:17.04 +65:35:57.8| $3.2 \times 10^3$ | Pooley & Lewin 2004b|
|SN2004et | II |20 35 25.33 +60 07 17.7 | $5.5 \times  10^3$ | Misra et al. 2007|
|SN2005ip | IIn |09:32:06.42 +08:26:44.4 | $3.0 \times 10^4$ | Pooley et al. 2007|
|SN2005kd | IIn | 04:03:16.88 +71:43:18.9| $6.4 \times 10^4$ | Immler et al. 2007c; Pooley et al. 2007|
|SN2006aj | Ib/c | 03 21 39.670 +16 52 02.27| $1.5 \times 10^5$ | "Margutti GRB catalog"|
|SN2006bp | IIP | 11:53:55.74 +52:21:09.4| $1.5 \times 10^4$ | Immler et al. 2007e|
|SN2006jc | Ibc | 09:17:20.78 +41:54:32.7| $2.4 \times 10^4$ | Immler et al. 2008|
|SN2006jd | IIb/IIn | 08:02:07.43 +00:48:31.5| $7.9 \times 10^4$ | Immler et al. 2007a|
|SN2007pk | IIn | 01:31:47.07 +33:36:54.1| $7.1 \times 10^4$ | Immler et al. 2007d|
|SN2008M | II | 06:21:41.28 -59:43:45.4| $3.7 \times 10^4$ | Immler 2010|
|SN2008ax | IIb | 12:30:40.80 +41:38:16.1| $8.0 \times 10^3$ | Roming et al. 2009|
|SN2008ij | II |18:19:51.81 +74:33:54.9| $2.1 \times 10^4$ | Immler et al. 2009|
|SN2009gj | IIb | 00:30:28.56 -33:12:56.0| $1.8 \times 10^4$ | Immler & Russell 2009|
|SN2009mk | IIb | 00:06:21.37 -41:28:59.8| $2.1 \times 10^4$ | Russell & Immler 2010|
|SN2010F | II | 10:05:21.05 -34:13:21.0| $3.9 \times 10^4$ | Russell et al. 2010|
|SN2010jl | IIn | 09:42:53.33 +09:29:41.8 | $4.9 \times 10^4$ | Immler et al. 2010; Chandra et al. 2015|
|SN2011dh | IIb | 13:30:05.106 +47:10:10.92| $7.3 \times 10^3$ | Soderberg et al. 2012|
|SN2011ja | IIP | 13:05:11.12 -49:31:27.0| $3.0 \times 10^3$ | Chakraborti et al. 2013|
|PTF12dam | Ic/SL | 14:24:46.20 +46:13:48.3| $4.98 \times 10^5$ | Margutti et al. 2018|
|SN2013by | IIL/IIn | 16:59:02.43 -60:11:41.8| $1.5 \times 10^5$ | Margutti et al. 2013|
|SN2013ej | IIP/IIL | 01:36:48.16 +15:45:31.0| $9.6 \times 10^3$ | Chakraborti et al. 2016|
|SN2014C | Ib/IIn | 22:37:05.60 +34:24:31.9|  $1.5\times10^4$ | Brethauer et al. 2022|
|SN2015L (ASASSN-15lh) | I/SL | 22:02:15.45 -61:39:34.6| $1.2 \times 10^6$ | Margutti et al. 2017|
|SN2018gk | IIb/SL | 16:35:53.908 +40:01:58.31 | $5.0 \times 10^5$ | Bose et al. 2020|
|SN2019ehk | Ca-rich | 12:22:56.130 +15:49:33.60 | $1.6 \times 10^4$ | Jacobson-Galán et al. 2020|
