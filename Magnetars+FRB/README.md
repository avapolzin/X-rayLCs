# Magnetar Flares/Outbursts & Fast Radio Bursts

For the FRB, FRB 200428, the HXMT data are in SGR1935+2154_FRB200428.fits. To go from counts ('RATE' column) to flux, we use a factor of 1.4e-8 (8.76 keV -> erg; from the HXMT ground calibration paper), and an additional k-correction factor of 1.067. Time (in days) can be calculated from the 'TIME' column. Since 'TIME' is natively in seconds and does not start exactly at t0 (taken to be 58967.60722222 based on the radio burst), we have to subtract off (t0 - dat.header['MJDREFI']) - 3, keeping in mind that 'MJDREFI' will need to be converted to seconds.

Since that's not entirely straightforward as an explanation, here is a code snippet to guide:

```python
from astropy.io import fits
import numpy as np
import astropy.units as u

FRB200428_dat = fits.open('../1s_LE_0.005s_lc_afterSatCor_ch106-1170.fits')[1]
dist_FRB = 4.4*u.kpc.to(u.cm)
conv = 1*u.keV.to(u.erg) * 8.76
Luminosity = (FRB200428_dat.data['RATE']*conv*1.067)*4*np.pi*dist_FRB**2
Duration = (FRB200428_dat.data['TIME'] - (58967.60722222 - FRB200428_dat.header['MJDREFI'])*u.d.to(u.s) - 3)*u.s.to(u.d)
Flux = FRB200428_dat.data['RATE']*conv*1.067

Duration = Duration[Luminosity > 0]
Luminosity = Luminosity[Luminosity > 0]
Flux = Flux[Flux > 0]
```


See Table A8 for additional details about individual events:
|Name | Type | RA/Dec | Distance (kpc) | References|
| :---: | :---: | :---: | :---: | :---: |
|1E161348-5055 | Outburst | 16:17:33.000 -51:02:00.00 | 3.3 | Rea et al. 2016; Esposito et al. 2019|
|SGR 1900+14 | IF/SB | 19:07:13.0 +09:19:34| 10.4 | Case & Bhattacharya 1998; Israel et al. 2008|
|SGR 1627-41 | Outburst | 16:35:52.0 -0.47:35:12 | 11 | Coti Zelati et al. 2018|
|1E2259+586 | Outburst | 23:01:08.14 +58:52:44.5| 3.2 | Coti Zelati et al. 2018|
|XTE J1810-197 | Outburst | 18:09:51.07 -19:43:51.8| 3.5 | Coti Zelati et al. 2018|
|SGR 1806-20 | Outburst |18:08:39.32 -20:24:40.1 | 8.7 | Coti Zelati et al. 2018|
|CXOU J1647-4552 | Outburst | 16:47:10.18 -45:52:16.7 | 4 | Coti Zelati et al. 2018|
|SGR 0501+4516 | Outburst |05:01:08.0 +45:16:31 | 1.5 | Coti Zelati et al. 2018|
|1E1547.0-5408 | Outburst | 15:50:54.18 -54:18:23.9| 4.5 | Coti Zelati et al. 2018|
|SGR 0418+5729 | Outburst | 04:18:33.867 +57:32:22.91| 2 | Coti Zelati et al. 2018|
|SGR 1833-0832 | Outburst | 18:33:46.0 -08:32:13| 10 | Coti Zelati et al. 2018|
|Swift J1822.3-1606 | Outburst | 18:22:18.32 -16:04:27.2| 1.6 | Coti Zelati et al. 2018|
|Swift J1834.9-0846 | Outburst |18:34:52.768 -08:45:40.83 | 4.2 | Coti Zelati et al. 2018|
|1E1048.1-5937 | Outburst | 10:50:08.93 -59:53:19.9| 9 | Coti Zelati et al. 2018|
|SGR J1745-2900 | Outburst |17:45:40.1640 -29:00:29.818 | 8.3 | Coti Zelati et al. 2018|
|SGR 1935+2154 (FRB 200428) | FRB | 19:34:55.68 +21:53:48.2| 4.4 | Li et al. 2021|
|SGR 1935+2154 | IF/SB | | | Matsuoka et al. 2009; Sugawara et al. 2020|
