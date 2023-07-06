# XRBs

Light curves are in either the HMXRB or LMXRB directory based on their classification.

The X Persei data is in *X-Per_sum_bar_tot2_1ks.qdp*. The first column is the time in seconds; the ninth column is the count rate. It can be converted to 0.3 - 10 keV cgs flux with a factor of 1.087e-11.

The IGR J01217-7257 (SXP 2.16) light curve is in *SXP2.16.txt*. The first column is time in seconds; the fourth column is the count rate, which can be converted to 0.3 - 10 keV cgs flux with a factor of 2.84-11.

The SXP 15.6 light curve is in its own subdirectory in *lc_swift.ascii*. There is information regarding the single Chandra observation of this event in the README file. (See the reference for details; we do not include this point in the DLPS.) The third column is the time in MJD, t0 = 57500 d. The fourth column is luminosity/(4.2259e37).

The subdirectory HMXRB/RXJ0209_or_SXP_9.3 hosts the light curve for RX JO209.6-7427. The column "MJD" can be corrected to time in days by subtracting t0 = 58800 d. The column "UnabsorbedFlux(0.5-10keV)" can be used to get the flux. The k-correction to 0.3 - 10 keV is ~1.0.

Important details of the Ferrigno et al. sample of HMXRBs are in *HMXB_Ferrigno.txt*. The filenames are *HMXB_Ferrigno\["name"\]+.txt*. Within the individual event files, "MJD" can be adjusted to days with "MJD" - min("MJD") + HMXB_Ferrigno\["t_offset"\], and "Flux(cgs)" is flux in cgs units.

The SMC X-2 light curve is in *SMC_X-2_2015_outburst.dat*. The first column is time in days, t0 = 57289. The fourth column is the count rate, which can be converted to 0.3 - 10 keV flux in cgs units with a factor of 7.25427e-11.

The SMC X-3 outburst data is in *SMC_X-3_2016_burst.dat*. The first column gives the time in days with t0 = 57599 d, and the fourth column gives the count rate, which can be converted to flux by multiplying by 5.96e-11.

*J0243_lc.dat* contains the light curve for Swift J0243.6+6124. The first column contains the time in days with t0 = 58029 d. The fourth column is the count rate. To get 0.3 - 10 keV cgs flux, multiply by a factor of 8.36e-11.

The first column of *RXJ0520_2013.dat* is time in days (t0 = 56305 d) and the fourth column is the count rate, which can be multiplied by 7.26e-11 to convert it to cgs flux. These data correspond to RX J0520.5-6932.

The only SFXT in our sample, XMMU J053108.3-690923, has data in *XMMU_J053108.3-690923_SFXT.dat*. The first column is the time in seconds (which should be filtered to 3e4 s < t < 11e4 s consistent with the outburst) and the fourth column gives the count rate. The conversion factor to 0.3 - 10 keV flux is 1.89e-10.

MAXI J1659-152's light curve is in *MAXI_J1659-152.txt*. The relevant columns are "MJD" (t0 = 55684.29844 d), "Flux", and "k". "k" is the k-correction on the flux, so the 0.3 - 10 keV cgs flux is "Flux" * "k".

GX 339-4 has successive outbursts; for simplicity, data can be read in as follows, making it easy to iterate through the outbursts:
```python
import numpy as np
import astropy.units as u
import pandas as pd

GX339 = pd.read_csv('../new_DLPS_data/LMXRB/GX3394.txt', header = 0, sep = '\s+', comment = '#')
GX339_time_ = GX339['MJD']
GX339_flux_ = GX339['Flux(cgs)']

refs339 = [(50750, 52300), (52300, 53150), (53150, 53700), (53700, 54000), (54000, 54200), (54200, 54600), (54600, 54850), (54850, 55150), (55150, 56000)]

for i in refs339:
    GX339_time = GX339_time_[(GX339_time_ > i[0]) & (GX339_time_ <= i[1])] - i[0]
    GX339_flux = GX339_flux_[(GX339_time_ > i[0]) & (GX339_time_ <= i[1])]
    GX339_lum = GX339_flux * 4 * np.pi* (8*u.kpc.to(u.cm))**2
```

The data for Aql X-1 are stored between six files. The final times (in days) are tob1, tob2, and tob3; and the final luminosities (0.3-10 keV; cgs) are lob1, lob2, and lob3:
```python
import numpy as np
import astropy.units as u
import pandas as pd

t1_ = pd.read_csv('../new_DLPS_data/LMXRB/LopezNavas2020/info_outb1.txt', header = None, sep = '\s+')
ob1_ = pd.read_csv('../new_DLPS_data/LMXRB/LopezNavas2020/PObb_outb1_fluxes.txt', header = None, sep = '\s+')
ob1 = ob1_[1]*1.065
tob1_ = []
for i in ob1_[0].values:
    tob1_.append(t1_[1].values[t1_[0].values == i])
tob1 = np.concatenate(tob1_)   
tob1 = tob1/(24*3600) + 51910 - 56450
ob1 = ob1[np.argsort(tob1)]
tob1 = tob1[np.argsort(tob1)]
lob1 = ob1*4 * np.pi*(5*u.kpc.to(u.cm))**2

t2_ = pd.read_csv('../new_DLPS_data/LMXRB/LopezNavas2020/info_outb2.txt', header = None, sep = '\s+')
ob2_ = pd.read_csv('../new_DLPS_data/LMXRB/LopezNavas2020/PObb_outb2_fluxes_036.txt', header = None, sep = '\s+')
ob2 = ob2_[1]*1.065
tob2_ = []
for i in ob2_[0].values:
    tob2_.append(t2_[1].values[t2_[0].values == i])
tob2 = np.concatenate(tob2_)   
tob2 = tob2/(24*3600) + 51910 - 56838
ob2 = ob2[np.argsort(tob2)]
tob2 = tob2[np.argsort(tob2)]
lob2 = ob2*4 * np.pi*(5*u.kpc.to(u.cm))**2

t3_ = pd.read_csv('../new_DLPS_data/LMXRB/LopezNavas2020/info_outb3.txt', header = None, sep = '\s+')
ob3_ = pd.read_csv('../new_DLPS_data/LMXRB/LopezNavas2020/PObb_outb3_fluxes.txt', header = None, sep = '\s+')
ob3 = ob3_[1]*1.065
tob3_ = []
for i in ob3_[0].values:
    tob3_.append(t3_[1].values[t3_[0].values == i])
tob3 = np.concatenate(tob3_)   
tob3 = tob3/(24*3600) + 51910 - 57597
ob3 = ob3[np.argsort(tob3)]
tob3 = tob3[np.argsort(tob3)]
lob3 = ob3*4 * np.pi*(5*u.kpc.to(u.cm))**2
```

*The light cuve of PSR J1023+0038 is not included in this repository.*

See Table A9 for additional details about individual events:
|Name | Type | RA/Dec | Distance (kpc) | References|
| :---: | :---: | :---: | :---: | :---: |
| 4U 0352-309 (X Persei) | HMXRB | 03:55:23.077 +31:02:45.05 | 1 | La Palombara & Mereghetti 2007 |
| RX J0209.6-7427 | HMXRB | 02:09:33.85 -74:27:12.5 | 55 | Vasilopoulos et al. 2020b |
| PSR J1023+0038 | LMXRB | 10:23:47.684 +00:38:41.01 | 1.37 | Bogdanov et al. 2015 |
| IGR J01217-7257 (SXP 2.16) | HMXRB | 01:21:40.6 -72:57:21.9 | 62 | Boon et al. 2017; Vasilopoulos et al. 2017a |
| SXP 15.6 | HMXRB | 00:48:55.360 -73:49:45.70 | 62 | Vasilopoulos et al. 2017b |
| Aql X-1 | LMXRB | 19:11:16.057 +00:35:05.88 | ~5 | López-Navas et al. 2020 |
| GX 339-4 | LMXRB | 17:02:49.381 -48:47:23.16 | 8 | Kong et al. 2000; Corbel et al. 2013 |
| MAXI J1659-152 | LMXRB | 16:59:01.680 -15:15:28.73 | 6 | Jonker et al. 2012 |
| 4U J1907+09 | HMXRB | 19:09:40.8 +09:48:25 | 5 | Ferrigno et al. 2022 |
| IGR J16393-4643 | HMXRB | 16:39:05.5 -46:42:14 | 12 | Ferrigno et al. 2022 |
| IGR J17503-2636 | HMXRB | 17:50:18.06 -26:36:16.7 | 10 | Ferrigno et al. 2022 |
| IGR J19140+0951 | HMXRB | 19:14:04.23 +09:52:58.4 | 2.8 | Ferrigno et al. 2022 |
| Swift J0243.6+6124 | HMXRB | 02:43:40.43 +61:26:03.8 | 7 | Wilson-Hodge et al. 2018; Chatzis et al. 2022 |
| RX J0520.5-6932 | HMXRB | 05:20:30.90 -69:31:55.0 | 50 | Vasilopoulos et al. 2014 |
| SMC X-2 | HMXRB | 00:54:33.43 -73:41:01.3 | 62 | Lutovinov et al. 2017 |
| SMC X-3 | HMXRB | 00:52:05.63 -72:26:04.2 | 62 | Koliopanos & Vasilopoulos 2018 |
| XMMU J053108.3-690923 | HMXRB | 05:31:08.44 -69:09:23.5 | 50 | Vasilopoulos et al. 2018; Maitra et al. 2021 |
