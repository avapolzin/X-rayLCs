# ULXs

M51_ULX7_lc_AVA.qdp has 11 columns: "Time", "T_+ve", "T_-ve", "Rate", "Ratepos", "Rateneg", "FracExp", "BGrate", "BGerr", "CorrFact", "CtsInSrc". The relevant colums are "Time", which is in seconds, and "Rate", which can be converted to flux with a factor of 6.47e-11. There are multiple outbursts from M51 ULX-7 in these data. We iterate through them as follows:

```python
import numpy as np
import pandas as pd
import astropy.units as u

M51 = pd.read_csv('../new_DLPS_data/ULX/M51_ULX7_lc_AVA.qdp', header = None, sep = '\s+', comment = '#')
M51_time_ = M51[0]*u.s.to(u.d)
M51_flux_ = M51[3]*6.47e-11 #Swift XRT pc Gamma = 1
M51_lum_ = M51_flux_*4*np.pi*(8580*u.kpc.to(u.cm))**2

refsm51 = [(4650, 4710), (4710, 4750), (4750, 4790), (4790, 4835), (4835, 4870), (4870, 4900), (4900, 4950), (4950, 5000), (5000, 5025), (5025, 5075)]

for i in refsm51:
    M51_time = M51_time_[(M51_time_ > i[0]) & (M51_time_ <= i[1])] - i[0]
    M51_flux = M51_flux_[(M51_time_ > i[0]) & (M51_time_ <= i[1])]
    M51_lum = M51_lum_[(M51_time_ > i[0]) & (M51_time_ <= i[1])]
```

NGC925_ULX.txt compiles all of the light curve information from NGC925fluxes*_forAP.txt, which are broken down by instrument. The columns for the instrument-specific are: sourceID, obsID, date, rate, rate error, flux, flux error, rate upper limit, flux upper limit. Flux is calculated assuming Γ = 1.6 if no specific spectral fit is noted.
Within NGC925_ULX.txt, there are two columns, time (given as date and time) and flux, which is in cgs units. If a row lists flux = 0, this indicates an upper limit and can be ignored. The upper limit values are listed in the instrument-specific files.

There are several different outbursts from NGC 925 ULX-3 in these data, which iterate through in the following way:

```python
import numpy as np
import pandas as pd
from astropy.time import Time
import astropy.units as u

Earnshaw_dist = ((9.56*u.Mpc).to(u.cm)).value
Earnshaw = pd.read_csv('../new_DLPS_data/ULX/NGC925_ULX.txt', sep ='\s+', comment = '#', header = 0)
E_t = [str(i) for i in Earnshaw.time]
Earnshaw_t = Time(E_t, format = 'isot', scale = 'utc')

cut = [0, 15, -1]
for i in range(2):
    if i == 0:
        sub_ = 53500
    if i != 0:
        sub_ = 57770
    
    Earnshaw_MJD = Earnshaw_t.mjd[cut[i]:cut[i+1]] - sub_
    Earnshaw_flux = Earnshaw.flux[cut[i]:cut[i+1]]
    Earnshaw_lum = Earnshaw_flux*4*np.pi*Earnshaw_dist**2
    
    Earnshaw_MJD = Earnshaw_MJD[Earnshaw_flux > 0]
    Earnshaw_lum = Earnshaw_lum[Earnshaw_flux > 0]
    Earnshaw_flux = Earnshaw_flux[Earnshaw_flux > 0]
```

Qiu+2019.txt lists data from CG X-1; "lum" and "flux" are in cgs, "start_time" gives the exposure start time in date + time, and "k" is the k-correction for each observation.

XMMUJ004243.6+412519.txt has three columns, "days", "lum", and "instr". "lum" is the unabsorbed 0.3-10 keV luminosity in units of 10<sup>38</sup> erg s<sup>-1</sup>.

See Table A9 for additional details about individual events:
|Name | RA/Dec | Distance (kpc) | References|
| :---: | :---: | :---: | :---: |
| XMMU J004243.6+412519 | 00:42:43.68 +41:25:18.6 | 778 | Middleton et al. 2013 |
| CG X-1 | 14:13:12.21 -65:20:13.7 | 4200 | Qiu et al. 2019 |
| M51 ULX-7 | 13:30:01.02 +47:13:43.8 | 8580 | Vasilopoulos et al. 2020a |
| NGC 925 ULX-3 | 02:27:20.18 +33:34:12.84 | 9560 | Earnshaw et al. 2020 |
