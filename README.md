# X-ray light curves (0.3 - 10 keV)
[![arXiv](https://img.shields.io/badge/arXiv-2211.01232-b31b1b)](https://arxiv.org/abs/2211.01232) [![DOI](https://zenodo.org/badge/332685529.svg)](https://zenodo.org/badge/latestdoi/332685529) [![Documentation Status](https://readthedocs.org/projects/xraydlps/badge/?version=latest)](https://xraydlps.readthedocs.io/en/latest/?badge=latest) [![Downloads](https://static.pepy.tech/badge/xraydlps)](https://pepy.tech/project/xraydlps)

Light curves from [Polzin et al. (2023)](https://ui.adsabs.harvard.edu/abs/2022arXiv221101232P/abstract). The tables in the appendix list the original provenance of these data.

Data are organized into folders by class of transient. Each folder has its own README file that lists details of the included files (as a rule, unless it is specifically stated otherwise, included light curves are not corrected for absorption or corrected to the rest frame) and will have a copy of the table that offers citations (_including references therein_) for these data.

If you are going to use data found here, please cite both the original source(s) of the data listed in the relevant table and Polzin et al. (2023). There is also a Zenodo reference to the dataset and package (link above) that we appreciate you citing.

<details>
  <summary>Click for BibTeX</summary>
  
  ```tex
@ARTICLE{2023ApJ...959...75P,
       author = {{Polzin}, Ava and {Margutti}, Raffaella and {Coppejans}, Deanne L. and {Auchettl}, Katie and {Page}, Kim L. and {Vasilopoulos}, Georgios and {Bright}, Joe S. and {Esposito}, Paolo and {Williams}, Peter K.~G. and {Mukai}, Koji and {Berger}, Edo},
        title = {The Luminosity Phase Space of Galactic and Extragalactic X-Ray Transients Out to Intermediate Redshifts},
      journal = {\apj},
     keywords = {X-ray astronomy, X-ray telescopes, X-ray transient sources, High energy astrophysics, Transient sources, Time domain astronomy, 1810, 1825, 1852, 739, 1851, 2109, Astrophysics - High Energy Astrophysical Phenomena},
         year = 2023,
        month = dec,
       volume = {959},
       number = {2},
          eid = {75},
        pages = {75},
          doi = {10.3847/1538-4357/acf765},
archivePrefix = {arXiv},
       eprint = {2211.01232},
 primaryClass = {astro-ph.HE},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2023ApJ...959...75P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}


@misc{polzin_2023_8319602,
  author       = {Polzin, Ava and
                  Margutti, Rafaella and
                  Coppejans, Deanne L. and
                  Auchettl, Katie and
                  Page, Kim L. and
                  Vasilopoulos, Georgios and
                  Bright, Joe S. and
                  Esposito, Paolo and
                  Williams, Peter K. G. and
                  Mukai, Koji and
                  Berger, Edo},
  title        = {X-rayLCs: Data and code from Polzin et al. (2023)},
  month        = sep,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v1.0},
  doi          = {10.5281/zenodo.8319602},
  url          = {https://doi.org/10.5281/zenodo.8319602}
}
```
</details>


(If for some reason any of the data that should be here are not or do not open, feel free to reach out via email or open an issue. Please note that a handful of light curves from the paper -- namely the superluminous SN 2018bsz, LMXRB PSR J1023+0038, and the two FXTs XRT 110103 and XRT 120830 -- are not available here.)

Interactive plots facilitating exploration of the data/DLPS are available [here](https://avapolzin.github.io/projects/xraydlps/).

(Within _/xraydlps/xraydlps/tools_ there is a .pkl file (lcs.pkl), which stores light curves for the major classes of transient in a dataframe. Pre-made plotting functions for this dataframe are in `xraydlps` and are used for our [interactive plots](https://avapolzin.github.io/projects/xraydlps/), but we urge people interested in using the data for further analysis to look at the more complete data stored in the broader repository and consult the original sources for additional details and considerations.)

We also include some additional versions of figures in the paper that may be edifying in *extra_figures*.

***
***
# How to use `xraydlps`
Additionally, we offer `xraydlps`, a small python package to help with plotting/classification of X-ray light curves in the DLPS. If you use this package, please cite Polzin et al. (2023) and the package itself (via Zenodo above).

Full code documentation: [xraydlps.readthedocs.io](https://xraydlps.readthedocs.io)

To download and install, 
```bash
cd ~
git clone git@github.com/avapolzin/X-rayLCs.git
cd X-rayLCs/xraydlps
sudo python3 setup.py install
```
OR
```bash
pip install xraydlps
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
plot.list_classes()
```

If you would like to list the subclasses, too, the command becomes:
```python
plot.list_classes(subs = True)
```
Similarly, `colors = True` will return the default colors for the (sub)classes.

To directly recreate figures from Polzin et al. (2023), you can use our built in style functions + our general DLPS plotting function:
```python
from xraydlps.plot import set_mpldefaults, dlps_axes, dlps_legend, obs_dlps
import matplotlib.pyplot as plt

set_mpldefaults() #sets general matplotlib style parameters for all plots

fig = plt.figure(figsize = (27, 25))
obs_dlps() #plots light curves, can specify which classes to include + line color/appearance
dlps_axes() #generates axes, including minor ticks + axis labels (fully customizable)
dlps_legend() #creates legend and adds it to the plot, specify labels, colors, and appearance
```
For whatever reason, you may have to run `set_mpldefaults` twice before the font changes propagate. Additionally, we recommend changing the font size in the legend with the `fontsize` key word argument to be 0.5 - 0.8 times the selected fontsize -- this is purely aesthetic, though, so we don't enforce this with hardcoding. Toggling `subson = True` in `obs_dlps` shows individual (specified) subclasses of transient. Classes are specified as a list, subclasses should be specified as a nested list, where classes sans subclasses or where subclasses should be turned off should be input as *None*.

And, to generate a schematic DLPS plot:
```python
from xraydlps.plot import schematic_dlps
import matplotlib.pyplot as plt

set_mpldefaults()

fig = plt.figure(figsize = (27, 25))
schematic_dlps() #plots general dlps regions, can specify which classes to include + line color/appearance
dlps_axes()
dlps_legend()
```

Similarly, to plot the DFPS:
```python
from xraydlps.plot import obs_dfps
import numpy as np

set_mpldefaults()

fig = plt.figure(figsize = (27, 25))
obs_dfps() #plots dfps, can specify which classes to include + line color/appearance
dlps_axes(xlabel = r'Observed Time Since Identification (days)', 
            ylabel = r'0.3 - 10 keV X-ray Flux (erg s$^{-1}$ cm$^{-2}$)', 
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
            add_minoryticks = [10.**i for i in np.arange(32, 56)], 
            ylim = [1e32, 2e55]) #can specify new limits, labels, + minor tick positions
dlps_legend(style = 'scatter')
```


***
## `xraydlps.classify`
```python
from xraydlps import classify
```
Within `xraydlps.classify` we offer some preliminary trained KNN models for classifying both light curves (using a dynamic time warping metric) and more general characteristics (L<sub>pk</sub>, t<sub>1/2</sub>, E<sub>iso</sub>, and t<sub>dur</sub>). We also offer a means of breaking up the existing light curves into training/test sets that default to including especially sparsely populated classes (i.e., SBOs, FRBs, ...) only in the training set, which is consistent with the models included here.

We ensure that classes with only one observation (i.e., SBOs, FRBs, magnetar flares) are included in the training set, so we urge caution in using the results of the KNN classification as anything other than preliminary guidance. (The pre-trained classifiers we provide are at best ~60-70% accurate based on testing.) The results of visual comparison to the DLPS are likely comparable.

To use a pre-trained model:
```python
from xraydlps.classify import lc_class, sum_class, dtw_dist

labels, probabilities = lc_class(time, lum) #to classify a light curve

labels, probabilities = sum_class(time, lum) #to classify light curve summary statistics
```
You will have to import `dtw_dist` so that the classifier can access it.

If you are starting from a light curve that is not in the 0.3-10 keV band or does not use default units, you can specify arguments in `lc_class` or in converting to the summary statistics with `xraydlps.tools.convert` (see below) to easily rectify this:

```python
labels, probabilities = lc_class(time, lum, tunits = u.s, k = 2.132)

labels, probabilities = sum_class(time, lum, tunits = u.s, k = 2.132)
```

There are some other arguments that are meant to allow further customization of the pre-trained models -- `verbose = True` (the default) has the classifier output all possible classes + assigned probabilities (`skip_zero = True` to only show classes with non-zero probabilities) and `full = True` will use the classifier trained on **all** of the available light curves rather than a subset.

<!--- For those who want to try other hyperparameters, metrics, or classifiers, we include a convenience function to break up the training set, so that classes with a paucity of observations (like SBOs or FRBs) are included in the training set. `split` has two arguments -- a dataframe, which should be formatted like the one in lcs.pkl (default is lcs.pkl here) and minlen, which sets the minimum length of the included light curves. If the model is for time-series classification, then we *strongly recommend* setting minlen ≥ 2.

```python
from xraydlps.classify import split

xtrain, xtest, ytrain, ytest = split(minlen = 2)
``` --->
For those who want to try other hyperparameters, metrics, or datasets with the KNeighborsClassifier, we include a couple of convenience functions to facilitate training -- `xraydlps.classify.train_lcmodel` and `xraydlps.classify.train_summodel`. We encourage users who are interested in using the classifier for more than preliminary guidance to train and validate their own models this way.


Our own implementation of dynamic time warping is available as `dtw_dist` (`xraydlps.classify.dtw_dist`) and can be used by a classifier by setting metric = `dtw_dist` or equivalent.

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
- scikit-learn
- astropy
- pickle
- scipy
