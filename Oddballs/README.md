# Oddballs (or FXTs)

Unlike other light curves included in the DLPS, the yet unclassified "oddballs" are not included in `xraydlps` for plotting or classification. Instead, the light curves for these FXTs can be accessed here, with the exception of the light curves for XRT 110103 and XRT 120830, which were digitized for inclusion in the DLPS and so are not shared as data here.

*XRT_000519_0.1-7-src803-lc300s-back-an-sub.asc* and *XRT_000519_0.3-7keV-lc-src803-3.2s-reso.asc* contains light curves for XTR 000519 at two different resolutions (300s and 3.2s respectively) in two separate energy bands (0.1 - 7 keV) and (0.3 - 7 keV). To convert from the Chandra count rate to 0.3 - 10 keV flux, we use the photon index between assumed in Section 2.3 (Γ \~ 1.7, for Γ<sub>Peak 1</sub> = 1.6 and Γ<sub>Peak 2</sub> = 1.95) resulting in 2.132e-11 for the 0.1 - 7 keV -> 0.3 - 10 keV conversion and 2.171e-11 for the 0.3 - 7 keV -> 0.3 - 10 keV conversion. The first column is time (in seconds, adopting t0 = 75110614.016523 s), the second column is count rate, and the third column is count rate error. We only use the 300s-binned light curve in the DLPS, but since the data sample the evolution of the event somewhat differently, we share both here.

```python
import numpy as np
import pandas as pd
import astropy.units as u
from astropy.cosmology import FlatLambdaCDM, z_at_value

cosmo = FlatLambdaCDM(H0 = 69.6, Om0 = 0.286)

def get_z(dL):
  return z_at_value(cosmo.luminosity_distance, dL*u.Mpc, zmax = 1e6)

dl = [16.2*u.Mpc, 1.1*u.Gpc, 11.1*u.Gpc]
z = []
for i in dl:
  z.append(get_z(i.to(u.Mpc).value))

XRT519_300 = pd.read_csv('XRT_000519_0.1-7-src803-lc300s-back-an-sub.asc',
                        sep = '\s+', header = None)
XRT519_3 = pd.read_csv('XRT_000519_0.3-7keV-lc-src803-3.2s-reso.asc',
                        skiprows = [0, 1, 2, 3, 4, 5, 6, 7], header = 0, sep = '\s+')

XRT519_300_lc = XRT519_300.loc[XRT519_300[2] != 0]
XRT519_3_lc = XRT519_3.loc[XRT519_3.COUNT_RATE != 0]

t0 = 75110614.016523

for i, d in enumerate(dl):
  time_300 = (XRT519_300_lc[1] - t0)*u.s.to(u.d)/(1 + z[i])
  lum_300 = 4*np.pi*XRT519_300_lc[2]*2.132e-11*(d.to(u.cm))**2

  ## if using the 3.4s-binned light curve:
  time_3 = (XRT519_3_lc.TIME - t0)*u.s.to(u.d)/(1 + z[i])
  lum_3 = 4*np.pi*XRT519_3_lc.COUNT_RATE*2.171e-11*(d.to(u.cm))**2
```

*lightcurve5_Source1_NGC4636.txt* and *lightcurve5_Source2_NGC5128.txt* contain the light curves for Sources 1 and 2 respectively. The first column is the time since the beginning of the flare in seconds, the second column is the count rate (to convert to cgs flux, we use a factor of 2.132e-11), the second column gives the symmetric error on the time, the third column gives the error on the count rate (with the fourth column giving the error on the count rate), and the fifth column gives the background rate (with the sixth column giving the error on the background rate).

The light curve for CDF-S XT1 is in *CDF-S_XT1_xt_lc.fits*, which has the relevant data in the first extension. (See Quirola-Vásquez et al. (2022, 2023) for additional details and data.) The following code reads in the light curve (including a conversion factor of 2.673e-11 from Chandra ACIS-I count rate to 0.3 - 10 keV cgs flux) and bins it as in Bauer et al. (2017), iterating through the different distance estimates:

```python
import numpy as np
import astropy.units as u
from astropy.io import fits

from astropy.cosmology import FlatLambdaCDM, z_at_value

cosmo = FlatLambdaCDM(H0 = 69.6, Om0 = 0.286)

def get_z(dL):
  return z_at_value(cosmo.luminosity_distance, dL*u.Mpc, zmax = 1e6)

cdfs = fits.open('CDF-S_XT1_xt_lc.fits')

dl = [1.6*u.Gpc, 18.1*u.Gpc]
z = []
for i in dl:
    z.append(get_z(i.to(u.Mpc).value))

t0 = 56931.29487269 - cdfs[1].header['MJDREF']
conv = 2.673e-11

t = cdfs[1].data['TIME'][(cdfs[1].data['COUNT_RATE'] != 0) & (cdfs[1].data['TIME'] > t0)]
cts = cdfs[1].data['COUNTS'][(cdfs[1].data['COUNT_RATE'] != 0) & (cdfs[1].data['TIME'] > t0)]

for i, d in enumerate(dl):
  ## to read in the light curve as is
  # time = (t*u.s.to(u.d) - t0)/(1 + z[i])
  # lum = 4*np.pi*cts*conv*(d.to(u.cm))**2

  ## to bin the light curve (as in Bauer et al. (2017) or however else):
  bbins =  [0, 32, 96, 224, 480, 1184, 2144, 4992, 31008, 150816] # from Table 1 of Bauer et al.
  n, bins = np.histogram(t - t0*u.d.to(u.s), weights = cts, bins = bbins)
  time = (bins[:-1] + bins[1:])/2 * u.s.to(u.d)
  deltat = bins[1:] - bins[:-1]
  lum = 4*np.pi*(n/deltat)*conv*(d.to(u.cm))**2
```
Alternatively, you can simply use the times and fluxes from Table 1 of Bauer et al. (2017), which is what we plot in the DLPS. That light curve is saved in *CDF-S_XT1_BauerTable1.txt* -- the columns are "time(s)" and "flux(cgs)", which is in the 0.3 - 10 keV band.

*CDF-S_XT2.txt* is the light curve for CDF-S XT2 -- the two columns are "time(s)" and "lum(cgs)".

The light curve for EXMM 023135.0-603743 is in *Novara_SBO_candidate_lc_SN_100_GAUSS.qdp*. The first column is time in seconds (t0 = 2e4 s) and the third column is the count rate. To convert to 0.3 - 10 keV flux, multiply by a factor of 7.316e-12.


The light curves for XRT 110103 and XRT 120830 were digitized for inclusion in the DLPS and so are not shared as data here.

See Table A10 for additional details about the individual events:
|Name | Type | RA/Dec | z | Distance (kpc) | References|
| :---: | :---: | :---: | :---: | :---: | :---: |
|XRT 000519 | 12:25:31.64 +13:03:58.8 | 0.23 - 1.5 | $$1.62 \times 10^4$$ | Jonker et al. 2013|
| | | | $$1.1 \times 10^6$$| | 
| | | | $$1.11 \times 10^7$$| |
|XRT 110103 | 14:08:28.89 -27:03:29.4 | - | $$9.49 \times 10^4$$ | Glennie et al. 2015|
|XRT 120830 | 23:52:12.19 -46:43:43.3 | - | 0.08 | Glennie et al. 2015|
| Source 1 | 12:42:51.4 +02:38:35 | - | $$1.43 \times 10^4$$ | Irwin et al. 2016|
| Source 2 | 13:25:52.7 -43:05:46 | - | $$3.8 \times 10^3$$ | Irwin et al. 2016|
| CDF-S XT1 | 03:32:38.77 −27:51:33.67 | 0.3 - 2.23 | $$1.6 \times 10^6$$ | Bauer et al. 2017|
| | | | $$1.81 \times 10^7$$ | |
|CDF-S XT2 | 03:32:18.38 -27:52:24.2 | 0.738 | $$4.68 \times 10^6$$ | Xue et al. 2019|
|EXMM 023135.0-603743 | 02:31:34.9 -60:37:43.3 | 0.092 | $$4.35 \times 10^5$$ | Novara et al. 2020|
