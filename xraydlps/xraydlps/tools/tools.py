import pickle
import astropy.units as u
from astropy.cosmology import FlatLambdaCDM, z_at_value
import astropy.constants as c
import numpy as np
from scipy.interpolate import interp1d
from sklearn.metrics import auc

# import pkgutil
import pkg_resources
import pandas as pd

cosmo = FlatLambdaCDM(H0 = 69.6, Om0 = 0.286)
sky = (4*np.pi*u.radian**2).to(u.deg**2)

def get_z(dl):
	return z_at_value(cosmo.luminosity_distance, dl*u.Mpc, zmax = 1e6)

def get_dcom(dl):
	## bit of a roundabout way to get comoving distance, but assuming luminosity distances as input
	return cosmo.comoving_distance(get_z(dl)).value

DATA_PATH = pkg_resources.resource_filename('xraydlps', 'data/')

##########
# * * * * 
##########

def load(pkl_file = 'lcs.pkl'):
	"""
	Convenience function to load pickled files. User-facing application is to access lcs.pkl.

	Parameters:
		pkl_file (str): Path to pickled file.

	Returns:
		Unpickled file.
	"""
	pkl_path = pkg_resources.resource_filename('xraydlps', 'data/'+pkl_file)

	with open(pkl_path, 'rb') as pkl:
		pk = pickle.load(pkl)
	return pk


def n_obs(lpk, rate, sens, fov, 
	lunits = u.erg/u.s, runits = u.Gpc**-3/u.yr, 
	funits = u.erg/u.s/u.cm**2, fovunits = u.deg**2, perunits = u.yr):
	"""
	Return anticipated detection/observation rate for particular class of transients and instrument.

	Parameters:
		lpk (float): Peak x-ray magnitude of transient class. Default units erg/s.
		rate (float): Volumetric event rate for transient class. Default units Gpc**-3/yr.
		sens (float): Flux limit of instrument. Default units erg/s/cm**2.
		fov (float): Instrument field of view. Default units deg**2.

		lunits (astropy units object): Input units of lpk.
		runits (astropy units object): Input units of rate.
		funits (astropy units object): Input units of sens.
		fovunits (astropy units object): Input units of fov.
		perunits (astropy units object): Sets unit of time for returned Nobs. Default is Nobs/yr.

	Returns:
		n_obs (float): N_obs/yr (by default) or N_obs/perunits (if specified).

	"""

	lconv = lunits.to(u.erg/u.s)
	rconv = runits.to(u.Gpc**-3/u.yr)
	fconv = funits.to(u.erg/u.s/u.cm**2)
	fovconv = fovunits.to(u.deg**2)
	outconv = (1/u.yr).to(1/perunits)


	frac = fov*fovconv/sky.value
	depth = np.sqrt(lpk*lconv/(4*np.pi*sens*fconv))*u.cm.to(u.Mpc)
	if depth < 6701.2: #condition on z <= 1
		inst_depth = depth 
	else:
		inst_depth = 6701.2 #set z = 1 (Mpc, luminosity distance)

	inst_depth_com = get_dcom(inst_depth)
	inst_vol = 4/3*np.pi*(inst_depth*u.Mpc.to(u.Gpc))**3 * frac

	nobs = rate*rconv*inst_vol*outconv

	return nobs


def convert(time, lum, k = 1, tunits = u.d, lunits = u.erg/u.s):
	"""
	Generate Lpk, t_half, E_iso, dur points from light curve for plotting and classification.

	Parameters:
		time (arr-like): Input time data for light curve. Default units in days.
		lum (arr-like): Input luminosity data for light curve. Default unit in erg/s.
		k (float): K-correction from input band --> 0.3-10 keV.
		tunits (astropy units object): Input units of time.
		lunits (astropy units object): Input units of lum.

	Returns:
		lpk, thalf, eiso, dur: Peak luminosity, duration above 0.5*Lpk, isotropic equivalent
				energy, and duration. Output in erg/s, days, erg, days.

	** Note that light curves must have multiple data points for this to work properly. **
	"""

	tconv = tunits.to(u.d)
	lconv = k*lunits.to(u.erg/u.s)

	time = tconv * time
	lum = k * lconv * lum

	lpk = np.max(lum)
	dur = np.max(time)

	if len(time) < 2:
		eiso = time*lum
		thalf = np.nan

	if len(time) >= 2:
		eiso = auc(time, lum)
		time_check = np.linspace(np.min(time), np.max(time), 1000)
		check = interp1d(time, lum)
		thalf = (np.max(time) - np.min(time))*len(check(time_check)[check(time_check) >= 0.5*lpk])/1000

	return lpk, thalf, eiso, dur



def get_stat(c, sc = None, stat = 'max', axis = 'lum'):
    """
    Return basic stats (min, max, mean, median) about (sub)classes of transient.
    
    Hint: use xraydlps.tools.list_classes() to see available (sub)classes.
    
    Parameters:
        c (str): Class for which to compute the statistic.
        sc (str): Subclass for which to compute statistic, if applicable.
        stat (str): Statistic to computea across light curves -- 
            options are 'min', 'max', 'mean', and 'median'.
        axis (str): Axis over which to compute statistic -- 
            options are 'time', 'lum', 'flux', lpk', 'thalf', 'eiso', and 'tdur'
            
    Returns:
        Statistic across all light curves in a given class.
        If time, units are in days; lum, units are erg/s; flux, erg/s/cm2;
        	lpk, erg/s; thalf, days; eiso, erg; tdur, days.
    """
    lcs = load()
    
    stat_out = []
    if not sc:
        for i in lcs.loc[lcs['class'] == c].iterrows():
            stat_out.append(i[1][axis])
    if sc:
        for i in lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == sc)].iterrows():
            stat_out.append(i[1][axis])
    
    
    if stat == 'min':
        return np.nanmin(np.concatenate(stat_out).flatten())
    
    if stat == 'max':
        return np.nanmax(np.concatenate(stat_out).flatten())
    
    if stat == 'mean':
        return np.nanmean(np.concatenate(stat_out).flatten())
    
    if stat == 'median':
        return np.nanmedian(np.concatenate(stat_out).flatten())