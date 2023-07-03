# Dwarf Novae

The GW Lib detection time is 198171032.2006 s - 0.545184 days. The first column gives time in seconds, and needs to have t0 subtracted off. The fourth column gives the count rate, which can be converted to flux with a factor of 2.84e-11. Like other sets of Swift observations, upper limits can be filtered out by ensuring that the Rateerr columns are non-zero.

The SSSJ122222 light curve has two columns HJD and count rate. t0 in this case is 6300 and as in the case of GW Lib, one can convert from the count rate to the flux by a factor of 2.84e-11.

SS Cyg has five fits files that contain data for four distinct outbursts. For ease, I will include here a code snippet, showing how to read in those data:
```python
from astropy.io import fits
import astropy.units as u
import numpy as np

rxte_flux = 1.918e-11 #pca
xte_flux = 5.688e-10 #asm

SSCygdist = 114.6*u.pc.to(u.cm) 
SSCyg_asm = fits.open('../DNe/SSCyg/xa_sscyg_d1.lc')
SSCyg_asmTime_ = np.array(SSCyg_asm[1].data['TIME']+ (SSCyg_asm[0].header['MJDREFI'] + SSCyg_asm[0].header['MJDREFF']))
SSCyg_asmFlux_ = np.array(SSCyg_asm[1].data['RATE'] * xte_flux)
SSCyg_asmLum_ = SSCyg_asmFlux_*4*np.pi*SSCygdist**2
SSCyg_1 = fits.open('../DNe/SSCyg/xp1004001_e3_n2a.lc')
SSCyg_1Time_ = np.array((SSCyg_1[1].data['TIME'])*u.s.to(u.d)+ (SSCyg_1[0].header['MJDREFI'] + SSCyg_1[0].header['MJDREFF']))
SSCyg_1Flux_ = np.array(SSCyg_1[1].data['RATE'] * rxte_flux)
SSCyg_1Lum_ = SSCyg_1Flux_*4*np.pi*SSCygdist**2
SSCyg_2 = fits.open('../DNe/SSCyg/xp2003301_e3_n2a.lc')
SSCyg_2Time_ = np.array((SSCyg_2[1].data['TIME'])*u.s.to(u.d)+ (SSCyg_2[0].header['MJDREFI'] + SSCyg_2[0].header['MJDREFF']))
SSCyg_2Flux_ = np.array(SSCyg_2[1].data['RATE'] * rxte_flux)
SSCyg_2Lum_ = SSCyg_2Flux_*4*np.pi*SSCygdist**2
SSCyg_4 = fits.open('../DNe/SSCyg/xp4001201_e4_n2a.lc')
SSCyg_4Time_ = np.array((SSCyg_4[1].data['TIME'])*u.s.to(u.d)+ (SSCyg_4[0].header['MJDREFI'] + SSCyg_4[0].header['MJDREFF']))
SSCyg_4Flux_ = np.array(SSCyg_4[1].data['RATE'] * rxte_flux)
SSCyg_4Lum_ = SSCyg_4Flux_*4*np.pi*SSCygdist**2
SSCyg_5 = fits.open('../DNe/SSCyg/xp5001101_e5_n2a.lc')
SSCyg_5Time_ = np.array((SSCyg_5[1].data['TIME'])*u.s.to(u.d)+ (SSCyg_5[0].header['MJDREFI'] + SSCyg_5[0].header['MJDREFF']))
SSCyg_5Flux_ = np.array(SSCyg_5[1].data['RATE'] * rxte_flux)
SSCyg_5Lum_ = SSCyg_5Flux_*4*np.pi*SSCygdist**2

SSCyg_refs = [(50365, 50380), (51335, 51355), (51600, 51660), (51660, 51700)]

    for i in SSCyg_refs:
        SSCyg_asmTime = SSCyg_asmTime_[(SSCyg_asmTime_ >= i[0]) & (SSCyg_asmTime_ <= i[1])] - i[0]
        SSCyg_asmFlux = SSCyg_asmFlux_[(SSCyg_asmTime_ >= i[0]) & (SSCyg_asmTime_ <= i[1])]
        SSCyg_asmLum = SSCyg_asmLum_[(SSCyg_asmTime_ >= i[0]) & (SSCyg_asmTime_ <= i[1])]

        SSCyg_1Time = SSCyg_1Time_[(SSCyg_1Time_ >= i[0]) & (SSCyg_1Time_ <= i[1])] - i[0]
        SSCyg_1Flux = SSCyg_1Flux_[(SSCyg_1Time_ >= i[0]) & (SSCyg_1Time_ <= i[1])]
        SSCyg_1Lum = SSCyg_1Lum_[(SSCyg_1Time_ >= i[0]) & (SSCyg_1Time_ <= i[1])]

        SSCyg_2Time = SSCyg_2Time_[(SSCyg_2Time_ >= i[0]) & (SSCyg_2Time_ <= i[1])] - i[0]
        SSCyg_2Flux = SSCyg_2Flux_[(SSCyg_2Time_ >= i[0]) & (SSCyg_2Time_ <= i[1])]
        SSCyg_2Lum = SSCyg_2Lum_[(SSCyg_2Time_ >= i[0]) & (SSCyg_2Time_ <= i[1])]

        SSCyg_4Time = SSCyg_4Time_[(SSCyg_4Time_ >= i[0]) & (SSCyg_4Time_ <= i[1])] - i[0]
        SSCyg_4Flux = SSCyg_4Flux_[(SSCyg_4Time_ >= i[0]) & (SSCyg_4Time_ <= i[1])]
        SSCyg_4Lum = SSCyg_4Lum_[(SSCyg_4Time_ >= i[0]) & (SSCyg_4Time_ <= i[1])]

        SSCyg_5Time = SSCyg_5Time_[(SSCyg_5Time_ >= i[0]) & (SSCyg_5Time_ <= i[1])] - i[0]
        SSCyg_5Flux = SSCyg_5Flux_[(SSCyg_5Time_ >= i[0]) & (SSCyg_5Time_ <= i[1])]
        SSCyg_5Lum = SSCyg_5Lum_[(SSCyg_5Time_ >= i[0]) & (SSCyg_5Time_ <= i[1])]
```
All plotting and analysis can then happen in that for loop on a by-outburst basis.


See Table A6 for additional details about individual events:
|Name | RA/Dec | Distance (kpc) | References|
| :---: | :---: | :---: | :---: |
| SS Cyg | 21:42:42.80 +43:35:09.9 | 0.115 | Wheatley et al. 2003; McGowan et al. 2004; Pala et al. 2020 |
| GW Lib | 1%:19:55.33 -25:00:24.6 | 0.113 | Byckling et al. 2009; Neustroev et al. 2018; Pala et al. 2020 |
| SSS J122221.7-311525 | 12:22:21.67 -31:15:23.8 | 0.275 | Neustroev et al. 2018 |
