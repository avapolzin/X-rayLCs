# X-ray light curves (0.3 - 10 keV)
[![arXiv](https://img.shields.io/badge/arXiv-2211.01232-b31b1b)](https://arxiv.org/abs/2211.01232)

Data from [Polzin et al., submitted](https://ui.adsabs.harvard.edu/abs/2022arXiv221101232P/abstract). The tables in the appendix list the original provenance of these data.

Each folder has its own README file that lists details of the included files and will have a copy of the table that offers citations (_including references therein_) for these data.

If you are going to use data found here, please cite both the original source(s) of the data listed in the relevant table and Polzin et al., submitted.

***
***
# `xraydlps`
Additionally, we offer `xraydlps`, a small python package to help with plotting/classification of X-ray light curves in the DLPS.

To download and install, 
```bash
cd ~
git clone git@github.com/avapolzin/X-rayLCs.git
cd X-rayLCs/xraydlps
sudo python3 setup.py install
```
The above includes download of all of the raw lightcurves in this repository, as well. If you are interested only in the plotting/classification functionality, you can just download the *xraydlps* directory above. Once you have a local copy, you can install the package with:
```bash
cd ~/xraydlps
sudo python3 setup.py install
```

Within `xraydlps` there are three modules, `plot`, `classify`, and `tools`. 

***
## `xraydlps.plot`
```python
from xraydlps import plot
```

***
## `xraydlps.classify`
```python
from xraydlps import classify
```

***
## `xraydlps.tools`
```python
from xraydlps import tools
```
The two front-facing functions in tools are `xraydlps.tools.n_obs` and `xraydlps.tools.convert`.

#### `xraydlps.tools.n_obs`
To determine the anticipated number of observations of a class of transients per year (within z &le; 1) for a given instrument, `n_obs` takes the peak X-ray luminosity of that class and its volumetric event rate. It also takes the field-of-view and the flux limit of that instrument.

```python
from xraydlps.tools import n_obs

n_obs(lpk, rate, fov, flim)
```

The default units for each of these inputs are erg/s, Gpc<>-3</sup>/yr, deg<sup>2</sup>, and erg/s/cm<sup>-2</sup>. To change the units, simply add the arguments *lunits*, *runits*, *fovunits*, and *funits*, specifying your input with `astropy.units`:
```python
import astropy.units as u

n_obs(lpk, rate, sens, fov, lunits = u.J/u.s, runits = u.Mpc**-3/u.yr, funits = u.J/u.s/u.m**2, fovunits = u.arcmin**2,)
```

You can also change the output units -- the default is N<sub>obs</sub>/yr -- with e.g. ```python perunits = u.d```, which will return N<sub>obs</sub>/day.

#### `xraydlps.tools.convert`
`convert` takes an input light curve and converts it to peak L<sub>x</sub>, t<sub>half</sub>, E<sub>iso</sub>, and duration points for use in plotting/classification.

```python
lpk, thalf, eiso, dur = convert(time, lum)
```
If the input light curve is not in the 0.3 - 10 keV band, the argument `k` sets a k-correction. Similarly, if the input light curve is not in the default units of days and erg/s, you can specify `tunits` and `lunits` with astropy units. The output will be in erg/s, days, erg, days.

