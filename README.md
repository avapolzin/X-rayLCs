# X-ray light curves (0.3 - 10 keV)
[![arXiv](https://img.shields.io/badge/arXiv-2211.01232-b31b1b)](https://arxiv.org/abs/2211.01232)

Light curves from [Polzin et al., submitted](https://ui.adsabs.harvard.edu/abs/2022arXiv221101232P/abstract). The tables in the appendix list the original provenance of these data.

Each folder has its own README file that lists details of the included files and will have a copy of the table that offers citations (_including references therein_) for these data.

If you are going to use data found here, please cite both the original source(s) of the data listed in the relevant table and Polzin et al., submitted. There is also a Zenodo reference to the dataset and package (link above) that we appreciate you citing.

(Within _/xraydlps/xraydlps/tools_ there is a .pkl file (lcs.pkl), which stores light curves for the major classes of transient in a dataframe. Pre-made plotting functions for this dataframe are in `xraydlps` and we urge people interested in using the data for further analysis to look at the more complete data stored in the broader repository and consult the original sources for additional details and considerations.)

***
***
# How to use `xraydlps`
Additionally, we offer `xraydlps`, a small python package to help with plotting/classification of X-ray light curves in the DLPS. If you use this package, please cite Polzin et al., submitted and the package itself (via Zenodo above).

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

Within `xraydlps` there are three modules, `plot`, `classify`, and `tools`. We walk through a handful of use cases with some example code below.

***
## `xraydlps.plot`
```python
from xraydlps import plot
```
Plotting functions are designed to be modular and allow for rapid/flexible plotting of the duration-luminosity phase space.

We include here quick plotting functions for the general DLPS, the schematic DLPS, the DFPS, and our L<sub>pk</sub> vs. t<sub>1/2</sub> and E<sub>iso</sub> and t<sub>dur</sub>.

Each of the functions allows you to specify which classes (and with the exception of the schematic DLPS, which subclasses) to show, it is useful to have a list of working keywords. To list available classes:
```python
list_classes()
```

If you would like to list the subclasses, too, the command becomes:
```python
list_classes(sub = True)
```

To directly recreate figures from Polzin et al. (2023), you can use our built in style functions + our general DLPS plotting function:
```python
from xraydlps.plot import set_mpldefaults, dlps_axes, dlps_legend, obs_dlps

set_mpldefaults() #sets general matplotlib style parameters for all plots

fig = plt.figure(figsize = (27, 25))
obs_dlps() #plots light curves, can specify which classes to include + line color/appearance
dlps_axes() #generates axes, including minor ticks + axis labels (fully customizable)
dlps_legend() #creates legend and adds it to the plot, specify labels, colors, and appearance
```
Toggling `subson = True` in `obs_dlps` shows individual (specified) subclasses of transient. Classes are specified as a list, subclasses should be specified as a nested list, where classes sans subclasses or where subclasses should be turned off should be input as *None*.

And, to generate a schematic DLPS plot:
```python
from xraydlps.plot import schematic_dlps

set_mpldefaults()

fig = plt.figure(figsize = (27, 25))
schematic_dlps() #plots general dlps regions, can specify which classes to include + line color/appearance
dlps_axes()
dlps_legend()
```

Similarly, to plot the DFPS:
```python
from xraydlps.plot import obs_dfps

set_mpldefaults()

fig = plt.figure(figsize = (27, 25))
obs_dfps() #plots dfps, can specify which classes to include + line color/appearance
dlps_axes(ylabel = r'0.3 - 10 keV X-ray Flux (erg s$^{-1}$ cm$^{-2}$)', 
            add_minoryticks = [10.**i for i in np.arange(2, 16)], 
            ylim = [1e-17, 3e-2]) #can specify new y-limit and label since default is for dlps + new minor tick positions
dlps_legend()
```

We also have quick plotting functions for the L<sub>pk</sub> vs. t<sub>1/2</sub> and E<sub>iso</sub> vs. t<sub>dur</sub> phase space. As with the other classes, these functions are flexible and you can alter the included (sub)classes among other features.
```python
from xraydlps.plot import lpk_thalf

set_mpldefaults()

fig = plt.figure(figsize = (27, 25))
lpk_thalf() #plots Lpk vs. thalf, can specify which classes to include + appearance
dlps_axes(xlabel = r'Rest Frame Time Above $\frac{1}{2}$ Peak L$_x$ (days)', 
            add_minorxticks = [10.**i for i in np.arange(-7, 4)], xlim = [1e-7, 5e4],
            ylabel = r'Peak L$_x$ (0.3 - 10 keV, erg s$^{-1}$)', 
            add_minoryticks = [10.**i for i in np.arange(26, 51)], 
            ylim = [1e26, 1e51]) #can specify new limits, labels, + minor tick positions
dlps_legend(style = 'scatter')
```

```python
from xraydlps.plot import iso_energy

set_mpldefaults()

fig = plt.figure(figsize = (27, 25))
iso_energy() #plots Eiso vs. tdur, can specify which classes to include + appearance
dlps_axes(xlabel = 'Rest Frame Duration (days)', 
            add_minorxticks = [10.**i for i in np.arange(-6, 4)], xlim = [1e-6, 5e4],
            ylabel = r'Isotropic Equivalent Energy (0.3 - 10 keV, ergs)', 
            add_minoryticks = [10.**i for i in np.arange(26, 51)], 
            ylim = [1e26, 2e51]) #can specify new limits, labels, + minor tick positions
dlps_legend(style = 'scatter')
```


***
## `xraydlps.classify`
```python
from xraydlps import classify
```
Within `xraydlps.classify` we offer some preliminary trained KNN models for classifying both light curves (using a dynamic time warping metric) and more general characteristics (L<sub>pk</sub>, t<sub>1/2</sub>, E<sub>iso</sub>, and t<sub>dur</sub>). We also layout a means of rapidly training models using other hyperparameters.

We ensure that classes with only one observation (i.e., SBOs, FRBs, magnetar flares) are included in the training set, so we urge caution in using the results of the KNN classification as anything other than preliminary guidance. The results of visual comparison to the DLPS are likely comparable.

To use a pre-trained model:
```python
from xraydlps.classify import lc_class, sum_class

lc_class([time, lum]) #to classify a light curve

sum_class([lpk, thalf, eiso, tdur]) #to classify light curve summary statistics
```

If you are starting from a light curve that is not in the 0.3-10 keV band or does not use default units, you can specify arguments in `lc_class` or in converting to the summary statistics with `xraydlps.tools.convert` (see below) to easily rectify this:

```python
lc_class([time, lum], tunits = u.s, k = 2.132)

sum_class(convert(time, lum, tunits = u.s, k = 2.132))
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

n_obs(lpk, rate, sens, fov)
```

The default units for each of these inputs are erg/s, Gpc<sup>-3</sup>/yr, deg<sup>2</sup>, and erg/s/cm<sup>-2</sup>. To change the units, simply add the arguments *lunits*, *runits*, *fovunits*, and *funits*, specifying your input with `astropy.units`:
```python
import astropy.units as u

n_obs(lpk, rate, sens, fov, lunits = u.J/u.s, runits = u.Mpc**-3/u.yr, 
      funits = u.J/u.s/u.m**2, fovunits = u.arcmin**2)
```

You can also change the output units -- the default is N<sub>obs</sub>/yr -- with e.g. `perunits = u.d`, which will return N<sub>obs</sub>/day.

#### `xraydlps.tools.convert`
`convert` takes an input light curve and converts it to peak L<sub>x</sub>, t<sub>half</sub>, E<sub>iso</sub>, and duration points for use in plotting/classification.

```python
from xraydlps.tools import convert

lpk, thalf, eiso, dur = convert(time, lum)
```
If the input light curve is not in the 0.3 - 10 keV band, the argument `k` sets a k-correction. Similarly, if the input light curve is not in the default units of days and erg/s, you can specify `tunits` and `lunits` with astropy units. The output will be in erg/s, days, erg, days.

### Dependencies
- numpy
- matplotlib
- pandas
- sklearn
- astropy
- pickle
- scipy
