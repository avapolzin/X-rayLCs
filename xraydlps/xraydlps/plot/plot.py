import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import astropy.units as u
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import pickle
import pandas as pd
from xraydlps.tools import load, convert

cs = ['grbs', 'sbo', 'sne', 'tdes', 'agn', 
			'fbots', 'novae', 'dne', 'magnetars', 
			'frb', 'coolstellar', 'xrbs', 'ulxs']

sc = [['long', 'short', 'ultralong', 'subluminous'], None, 
			['cc-I', 'cc-II', 'interacting', 'Ca-rich', 'superluminous'], 
			['nonthermal', 'thermal'], None, None, None, None, 
			['outburst', 'flare'], None, None, ['highmass', 'lowmass'], None]

defaultc_colors = ['#2ca02c', '#17becf', '#d62728', '#ff7f0e', 
		'#cc5f00', '#8c564b', 'xkcd:burnt yellow', 'xkcd:wheat', '#e377c2', 
		'gray', '#9467bd', '#1f77b4', '#004481'] #defined for major classes of transient

defaultsc_colors = [['#2ca02c', '#79ED79', '#1f701f', '#124012'], '#1298a6', 
		['#d62728', '#ff8b8c', '#8A0000', '#400b0c', '#f2bebe'], 
		['#ff7f0e', '#FFB241'], '#cc5f00', '#8c564b',  'xkcd:burnt yellow', 'xkcd:wheat', 
		['#e377c2', '#FFAAF5'], 'gray', '#9467bd', ['#1f77b4', '#52AAE7'], 
		'#004481'] #defined for subclasses of transient


def list_classes(subs = False, colors = False):
	"""
	List available classes of transients.

	Parameters:
		subs (bool): If subs = True, return tuples with classes + subclasses of transients.
		colors (bool): If colors = True, return tuple that includes default plotting colors.
	"""
	if not subs:
		if not colors:
			for c in cs:
				print(c)
		if colors:
			for z in zip(cs, defaultc_colors):
				print(z)
	if subs:
		if not colors:
			for z in zip(cs, sc):
				print(z)
		if colors:
			for z in zip(cs, sc, defaultsc_colors):
				print(z)

##########
# * * * * 
##########

def set_mpldefaults(fontfamily = 'serif',
					fontsize = 45,
					majortick_width = 3, 
					majortick_size = 15,
					minorticks = False,
					minortick_width = 3,
					minortick_size = 10,
					rightticks = True,
					hatch_width = 3,
					linewidth = 8,
					markersize = 20):
	"""
	Set matplotlib.rc defaults for DLPS.

	Not necessary for plots, but uses style Polzin et al. (2023).

	Parameters:
		fontfamily (str): Font family to use.
		fontsize (int): Fontsize to use.
		majortick_width (int): Width of major ticks.
		majortick_size (int): Length of major ticks.
		minorticks (bool): If True, include minor ticks.
		minortick_width (int): Width of minor ticks.
		minortick_size (int): Length of minor ticks.
		rightticks (bool): If True, include right ticks.
		hatch_width (int): Width of hatches.
		linewidth (int): Default line width.
		markersize (int): Default marker size.
	"""
	matplotlib.rcParams['font.family'] = fontfamily
	# matplotlib.rcParams['font.size'] = fontsize
	matplotlib.rcParams['xtick.major.size'] = majortick_size
	matplotlib.rcParams['ytick.major.size'] = majortick_size
	matplotlib.rcParams['xtick.major.width'] = majortick_width
	matplotlib.rcParams['ytick.major.width'] = majortick_width
	matplotlib.rcParams['xtick.minor.visible'] = minorticks
	matplotlib.rcParams['xtick.minor.visible'] = minorticks
	if minorticks:
		matplotlib.rcParams['xtick.minor.size'] = minortick_size
		matplotlib.rcParams['ytick.minor.size'] = minortick_size
		matplotlib.rcParams['xtick.minor.width'] = minortick_width
		matplotlib.rcParams['ytick.minor.width'] = minortick_width
	matplotlib.rcParams['ytick.right'] = rightticks
	matplotlib.rc('hatch', linewidth = hatch_width)
	matplotlib.rcParams['lines.linewidth'] = linewidth
	matplotlib.rcParams['lines.markersize'] = markersize
	matplotlib.rc('font', size = fontsize)






def dlps_axes(xlabel = 'Rest Frame Time Since Identification (days)', 
			  ylabel = r'0.3 - 10 keV X-ray Luminosity (erg s$^{-1}$)', 
			  add_minorxticks = [10.**i for i in np.arange(-8, 4)],
			  add_minoryticks = [10.**i for i in np.arange(26, 51)],
			  ax = plt, xlim = [3e-9, 5e4], ylim = [1e26, 1e51],
			  rightticks = True, tickwidth = [3, 3],
			  xscale = 'log', yscale = 'log'):
	"""
	Quickly set up axes for X-ray DLPS plots. For most full DLPS plots, should not need to change defaults.

	Parameters:
		xlabel (str): Label for x-axis of DLPS plot.
		ylabel (str): Label for y-axis of DLPS plot.
		add_minorxticks (arr-like): If None, will not add ticks. Otherwise, list of x-values for which to add minor tick.
		add_minoryticks (arr-like): If None, will not add ticks. Otherwise, list of y-values for which to add minor tick.
		ax (axis object): Axis on which to add ticks/labels; e.g., set plt.xlabel or ax.set_xlabel.
		xlim (arr-like): Lower and upper limit of x-axis.
		ylim (arr-like): Lower and upper limit of y-axis.
		rightticks (bool): If True, plot minor ticks on right y-axis. 
							(Looks best if major ticks are enabled for the rightside, too.)
		tickwidth (list): Width of major and minor ticks to be added respectively. Best if this matches set_mpldefaults(). 
		xscale (str): Set scaling of x-axis.
		yscale (str): Set scaling of y-axis.

	(Can hard code changes to minor tick lengths to suit personal preference.)
	"""

	xtick_len = (ylim[1] - ylim[0])/(1e51 - 1e26) * (1e26 - 6.5e25) #can hard code changes to suit preferences
	ytick_len_left = (xlim[1] - xlim[0])/(5e4 - 3e-9) * (3e-9 - 2.6e-9)
	ytick_len_right = (xlim[1] - xlim[0])/(5e4 - 3e-9) * (6e4 - 5e4)

	if add_minorxticks:
		for i in add_minorxticks:
			ax.vlines(x = i, ymin = ylim[0] - xtick_len, ymax = ylim[0], clip_on = False, color = 'k', lw = tickwidth[1])
		for j in add_minoryticks:
			ax.vlines(x = i, ymin = xlim[0] - ytick_len_left, ymax = xlim[0], clip_on = False, color = 'k', lw = tickwidth[1])
			if rightticks:
				ax.vlines(x = i, ymin = xlim[1], ymax = xlim[1] + ytick_len_right, clip_on = False, color = 'k', lw = tickwidth[0])

	if ax == plt:
		ax.xlabel(xlabel)
		ax.ylabel(ylabel)
		ax.xlim(xlim)
		ax.ylim(ylim)
		ax.xscale(xscale)
		ax.yscale(yscale)

	else:
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel)
		ax.set_xlim(xlim)
		ax.set_ylim(ylim)
		ax.set_xscale(xscale)
		ax.set_yscale(yscale)


def dlps_legend(labels = [cs, sc], colors = [defaultc_colors, defaultsc_colors], 
				ax = plt, style = 'patch', marker = None, subson = False, **kwargs):
	"""
	Easily enerate custom legend for plots.

	Parameters:
		labels (arr-like): List of strings that serve as labels in legend.
		colors (arr-like): List of colors corresponding to labels.
		ax (axis object): Axis on which to add legend, e.g., ax.legend().
		style (str or arr-like): 'Patch', 'line', or 'scatter' -- 
				if 'scatter', have to specify marker. Case insensitive.
		marker (str or arr-like): Marker to be used in legend.
		subson (bool): Default is False. If true, use subclass legend.
		**kwargs modify ax.legend(), see matplotlib documentation.


	"""
	if not subson:
		labels = labels[0]
		colors = colors[0]
	if subson:
		labels_ = []
		for i, s in enumerate(sc):
			if s:
				for s_ in s:
					if cs[i] == 'magnetars':
						labels_.append(s_+', '+cs[i])
					else:
						labels_.append(s_+' '+cs[i])
			if not s:
				labels_.append(cs[i])
			
		colors_ = []
		for c in defaultsc_colors:
			if type(c) == list:
				for i in c:
					colors_.append(i)
			if type(c) == str:
				colors_.append(c)
		labels = labels_
		colors = colors_


	if type(style) == str:
		style = [style]*len(labels)
	if type(marker) == str:
		marker = [marker]*len(labels)
	handles = []
	for i, l in enumerate(labels):
		if style[i].lower() == 'patch':
			handles.append(mpatches.Patch(color = colors[i], label = l))
		if style[i].lower() == 'line':
			handles.append(mlines.Line2D([], [], color = colors[i], label = l))
		if style[i].lower() == 'scatter':
			handles.append(mlines.Line2D([], [], color = colors[i], label = l, 
				linestyle = '', marker = 'o'))

	ax.legend(handles = handles, **kwargs)

	
	
def obs_dlps(classes = cs, subclasses = sc, subson = False,
			 colors = [defaultc_colors, defaultsc_colors], 
			 xunit = u.d, yunit = u.erg/u.s, k = 1., ax = plt, **kwargs):

	"""
	Plot the observational DLPS.

	Parameters:
		classes (arr-like): List of classes to plot.
		subclasses (arr-like): If subson = True, plot these subclasses. Should be a nested list, 
			with subclasses grouped in sub-list by class.
		subson (bool): Plot subclasses instead of classes -- if subson = True, must specify subclasses.
		xunit (astropy units object): Units of time for observational DLPS. Default is days.
		yunit (astropy units object): Units of luminosity for observational DLPS. Default is erg/s
		k (float or arr-like): Value of k-correction if plotting outside of 0.3-10 keV band. 
			Should be the length of classes.
		ax (axis object): Axis on which to plot, e.g., ax.plot().
		**kwargs modify ax.plot(), see matplotlib documentation.
	"""
	lcs = load()

	xconv = u.d.to(xunit)
	yconv = (u.erg/u.s).to(yunit)
	if (type(k) == float) or (type(k) == int):
		k = [k]*len(classes)

	if colors == [defaultc_colors, defaultsc_colors]: # hacky test for default parameters (might be temporary if I find a better way)
		if subson:
			colors = colors[1]
		if not subson:
			colors = colors[0]

	if subson:
		for i, c in enumerate(classes):
			ki = k[i]
			if subclasses[i]:
				if sc[i]:
					for k_, s in enumerate(sc[i]):
						col = colors[i][k_]
						for j, obj in enumerate(lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == s)].iterrows()):
							# for obj in lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == s)]:
							time = obj[1]['time'] * xconv
							lum = obj[1]['lum'] * yconv * ki
							ax.plot(time, lum, color = col)

							if len(time) == 1:
								ax.scatter(time, lum, color = col) #s = lw^2

			if not subclasses[i]:
				col = colors[i]
				for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
					time = obj[1]['time'] * xconv
					lum = obj[1]['lum'] * yconv * ki
					ax.plot(time, lum, color = col)

					if len(time) == 1:
						ax.scatter(time, lum, color = col)

	if not subson:
		for i, c in enumerate(classes):
			ki = k[i]
			col = colors[i]
			for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
				time = obj[1]['time'] * xconv
				lum = obj[1]['lum'] * yconv * ki
				ax.plot(time, lum, color = col)

				if len(time) == 1:
					ax.scatter(time, lum, color = col)




def schematic_dlps(classes = np.concatenate((cs, ['sgrbs'])), expecton = False,
				colors = np.concatenate((defaultc_colors, ['#79ED79'])), k = 1, ax = plt,
				xunit = u.d, yunit = u.erg/u.s, **kwargs):

	"""
	Plot the schematic DLPS.

	Parameters:
		classes (arr-like): List of classes to plot. In addition to other classes, 'sgrbs' is a valid option.
		expecton (bool): Plot region where we would expect SBOs + magnetars (if included in classes).
		xunit (astropy units object): Units of time for observational DLPS. Default is days.
		yunit (astropy units object): Units of luminosity for observational DFPS. Default is erg/s
		k (float or arr-like): Value of k-correction if plotting outside of 0.3-10 keV band. 
			Should be the length of classes.
		ax (axis object): Axis on which to plot, e.g., ax.plot().
		**kwargs modify ax.plot(), see matplotlib documentation.
	"""
	carr = np.array(classes)
	colarr = np.array(colors)
	if (type(k) == float) or (type(k) == int):
		k = [k]*len(classes)
	karr = np.array(k)

	xconv = u.d.to(xunit)
	yconv = (u.erg/u.s).to(yunit)

	if expecton:
		if 'sbo' in classes:
			plt.fill_between([3e-5*xconv, 1*xconv], 
				[1e40*yconv*karr[carr == 'sbo'][0], 1e35*yconv*karr[carr == 'sbo'][0]], 
				[1e49*yconv*karr[carr == 'sbo'][0], 1e44*yconv*karr[carr == 'sbo'][0]], 
				edgecolor = colarr[carr == 'sbo'][0], facecolor = 'none', hatch = 'X', 
				linewidth = 0) #SS SBO

		if 'magnetars' in classes:
			plt.fill_between([10**-5.3*xconv, 10**0.3*xconv], 
				[10**41.5*yconv*karr[carr == 'magnetars'][0], 10**36.5*yconv*karr[carr == 'magnetars'][0]], 
				[10**38.5*yconv*karr[carr == 'magnetars'][0], 10**33.5*yconv*karr[carr == 'magnetars'][0]], 
				edgecolor = colarr[carr == 'magnetars'][0], hatch = '+', facecolor = 'none', 
				linewidth = 0) #magnetar exp

	if 'agn' in classes:
		plt.fill_between([8e-2*xconv, 5e3*xconv], 
			[2e38*yconv*karr[carr == 'agn'][0], 2e38*yconv*karr[carr == 'agn'][0]], 
			[3e46*yconv*karr[carr == 'agn'][0], 3e46*yconv*karr[carr == 'agn'][0]], 
			color = colarr[carr == 'agn'][0]) #AGN - 1
		plt.fill_between([2.5e-3*xconv, 8e-2*xconv], 
			[1e41*yconv*karr[carr == 'agn'][0]], 
			[3e42*yconv*karr[carr == 'agn'][0], 3e42*yconv*karr[carr == 'agn'][0]], 
			color = colarr[carr == 'agn'][0]) #AGN - 2, QPEs

	if 'grbs' in classes:
		plt.fill_between([3e-4*xconv, 2e3*xconv], 
			[1e46*yconv*karr[carr == 'grbs'][0], 3e38*yconv*karr[carr == 'grbs'][0]], 
			[6e50*yconv*karr[carr == 'grbs'][0], 3e43*yconv*karr[carr == 'grbs'][0]], 
			color = colarr[carr == 'grbs'][0]) #GRBs - 1
		plt.fill_between([5e-5*xconv, 3*xconv], 
			[3e45*yconv*karr[carr == 'grbs'][0], 1e40*yconv*karr[carr == 'grbs'][0]], 
			[3e47*yconv*karr[carr == 'grbs'][0], 1e42*yconv*karr[carr == 'grbs'][0]], 
			color = colarr[carr == 'grbs'][0]) #GRBs - 2
		if 'sgrbs' in classes:
			scol = colarr[carr == 'sgrbs'][0]
			sk = karr[carr == 'sgrbs'][0]
		if 'sgrbs' not in classes:
			scol = colarr[carr == 'grbs'][0]
			sk = karr[carr == 'grbs'][0]
		plt.fill_between([3e-4*xconv, 7e2*xconv], 
			[4.2e44*yconv*sk, 3e36*yconv*sk], 
			[7e49*yconv*sk, 5e41*yconv*sk], 
			color = scol)#sGRBs

	if 'tdes' in classes:
		plt.fill_between([1e-2*xconv, 1e4*xconv], 
			[3e46*yconv*karr[carr == 'tdes'][0], 3e42*yconv*karr[carr == 'tdes'][0]], 
			[1e50*yconv*karr[carr == 'tdes'][0], 1e46*yconv*karr[carr == 'tdes'][0]], 
			color = colarr[carr == 'tdes'][0]) #TDEs - 1
		plt.fill_between([3e0*xconv, 1e4*xconv], 
			[3e37*yconv*karr[carr == 'tdes'][0], 3e37*yconv*karr[carr == 'tdes'][0]], 
			[1e45*yconv*karr[carr == 'tdes'][0], 1e45*yconv*karr[carr == 'tdes'][0]], 
			color = colarr[carr == 'tdes'][0]) #TDEs - 2

	if 'sne' in classes:
		plt.fill_between([2.5e-1*xconv, 1.5e4*xconv], 
			[1e39*yconv*karr[carr == 'sne'][0], 1e34*yconv*karr[carr == 'sne'][0]], 
			[1e42*yconv*karr[carr == 'sne'][0], 1e42*yconv*karr[carr == 'sne'][0]], 
			color = colarr[carr == 'sne'][0])

	if 'sbo' in classes:
		plt.fill_between([2e-4*xconv, 1e-2*xconv], 
			[1e43*yconv*karr[carr == 'sbo'][0], 2e41*yconv*karr[carr == 'sbo'][0]], 
			[5e44*yconv*karr[carr == 'sbo'][0], 1e43*yconv*karr[carr == 'sbo'][0]], 
			color = colarr[carr == 'sbo'][0]) #wind SBO

	if 'xrbs' in classes:
		plt.fill_between([1e-6*xconv, 3e3*xconv], 
			[1e31*yconv*karr[carr == 'xrbs'][0], 1e31*yconv*karr[carr == 'xrbs'][0]], 
			[2e35*yconv*karr[carr == 'xrbs'][0], 2e35*yconv*karr[carr == 'xrbs'][0]], 
			color = colarr[carr == 'xrbs'][0]) #XRBs - 1
		plt.fill_between([1.5e-1*xconv, 3e3*xconv], 
			[2e35*yconv*karr[carr == 'xrbs'][0], 2e35*yconv*karr[carr == 'xrbs'][0]], 
			[3e39*yconv*karr[carr == 'xrbs'][0], 3e39*yconv*karr[carr == 'xrbs'][0]], 
			color = colarr[carr == 'xrbs'][0]) #XRBs - 2

	if 'dne' in classes:
		plt.fill_between([7e-4*xconv, 2e3*xconv], 
			[4e29*yconv*karr[carr == 'dne'][0], 4e29*yconv*karr[carr == 'dne'][0]], 
			[1e34*yconv*karr[carr == 'dne'][0], 1e34*yconv*karr[carr == 'dne'][0]], 
			color = colarr[carr == 'dne'][0]) #DNe

	if 'novae' in classes:
		plt.fill_between([1.5e-1*xconv, 6e3*xconv], 
			[1.5e30*yconv*karr[carr == 'novae'][0], 1.5e30*yconv*karr[carr == 'novae'][0]], 
			[7e36*yconv*karr[carr == 'novae'][0], 7e36*yconv*karr[carr == 'novae'][0]], 
			color = colarr[carr == 'novae'][0]) #Novae

	if 'coolstellar' in classes:
		plt.fill_between([2e-3*xconv, 1.2e0*xconv], 
			[1.5e28*yconv*karr[carr == 'coolstellar'][0], 1.5e28*yconv*karr[carr == 'coolstellar'][0]], 
			[6e32*yconv*karr[carr == 'coolstellar'][0], 6e32*yconv*karr[carr == 'coolstellar'][0]], 
			color = colarr[carr == 'coolstellar'][0]) #cool stellar flares

	if 'frb' in classes:
		plt.fill_between([2.5e-8*xconv, 1.5e-5*xconv], 
			[5e39*yconv*karr[carr == 'frb'][0], 5e39*yconv*karr[carr == 'frb'][0]], 
			[1e42*yconv*karr[carr == 'frb'][0], 1e42*yconv*karr[carr == 'frb'][0]], 
			color = colarr[carr == 'frb'][0]) #FRB

	if 'magnetars' in classes:
		plt.fill_between([1e-6*xconv, 3e-5*xconv], 
			[2e39*yconv*karr[carr == 'magnetars'][0], 2e39*yconv*karr[carr == 'magnetars'][0]], 
			[9e40*yconv*karr[carr == 'magnetars'][0], 9e40*yconv*karr[carr == 'magnetars'][0]], 
			color = colarr[carr == 'magnetars'][0]) #magnetar - 1
		plt.fill_between([2e-1*xconv, 8e3*xconv], 
			[4e33*yconv*karr[carr == 'magnetars'][0], 9e29*yconv*karr[carr == 'magnetars'][0]], 
			[1e36*yconv*karr[carr == 'magnetars'][0], 1e36*yconv*karr[carr == 'magnetars'][0]], 
			color = colarr[carr == 'magnetars'][0]) #magnetar - 2

	if 'ulxs' in classes:
		plt.fill_between([0.6*xconv, 9e3*xconv], 
			[3e38*yconv*karr[carr == 'ulxs'][0], 3e38*yconv*karr[carr == 'ulxs'][0]], 
			[3e40*yconv*karr[carr == 'ulxs'][0], 3e40*yconv*karr[carr == 'ulxs'][0]], 
			color = colarr[carr == 'ulxs'][0]) #ULX

	if 'fbots' in classes:
		plt.fill_between([2.5*xconv, 400*xconv], 
			[1e42*yconv*karr[carr == 'fbots'][0], 1e38*yconv*karr[carr == 'fbots'][0]], 
			[2e44*yconv*karr[carr == 'fbots'][0], 2e44*yconv*karr[carr == 'fbots'][0]], 
			color = colarr[carr == 'fbots'][0]) #FBOT



def obs_dfps(classes = cs, subclasses = sc, subson = False,
			 colors = [defaultc_colors, defaultsc_colors], 
			 xunit = u.d, yunit = u.erg/u.s/u.cm**2, k = 1., ax = plt, **kwargs):

	"""
	Plot the observational DFPS.

	Parameters:
		classes (arr-like): List of classes to plot.
		subclasses (arr-like): If subson = True, plot these subclasses. Should be a nested list, 
			with subclasses grouped in sub-list by class.
		subson (bool): Plot subclasses instead of classes -- if subson = True, must specify subclasses.
		xunit (astropy units object): Units of time for observational DLPS. Default is days.
		yunit (astropy units object): Units of flux for observational DFPS. Default is erg/s/cm**2
		k (float or arr-like): Value of k-correction if plotting outside of 0.3-10 keV band. 
			Should be the length of classes.
		ax (axis object): Axis on which to plot, e.g., ax.plot().
		**kwargs modify ax.plot(), see matplotlib documentation.
	"""
	lcs = load()

	xconv = u.d.to(xunit)
	yconv = (u.erg/u.s/u.cm**2).to(yunit)
	if (type(k) == float) or (type(k) == int):
		k = [k]*len(classes)

	if colors == [defaultc_colors, defaultsc_colors]: # hacky test for default parameters (might be temporary if I find a better way)
		if subson:
			colors = colors[1]
		if not subson:
			colors = colors[0]

	if subson:
		for i, c in enumerate(classes):
			ki = k[i]
			if subclasses[i]:
				if sc[i]:
					for k_, s in enumerate(sc[i]):
						col = colors[i][k_]
						for j, obj in enumerate(lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == s)].iterrows()):
							if np.isfinite(obj[1]['z']):
								time = obj[1]['time'] * (1 + obj[1]['z']) * xconv
							if not np.isfinite(obj[1]['z']):
								time = obj[1]['time'] * xconv
							flux = obj[1]['flux'] * yconv * ki
							ax.plot(time, flux, color = col)

							if len(time) == 1:
								ax.scatter(time, flux, color = col) #s = lw^2

			if not subclasses[i]:
				col = colors[i]
				for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
					if np.isfinite(obj[1]['z']):
						time = obj[1]['time'] * (1 + obj[1]['z']) * xconv
					if not np.isfinite(obj[1]['z']):
						time = obj[1]['time'] * xconv
					flux = obj[1]['flux'] * yconv * ki
					ax.plot(time, flux, color = col)

					if len(time) == 1:
						ax.scatter(time, flux, color = col)

	if not subson:
		for i, c in enumerate(classes):
			ki = k[i]
			col = colors[i]
			for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
				if np.isfinite(obj[1]['z']):
					time = obj[1]['time'] * (1 + obj[1]['z']) * xconv
				if not np.isfinite(obj[1]['z']):
					time = obj[1]['time'] * xconv
				flux = obj[1]['flux'] * yconv * ki
				ax.plot(time, flux, color = col)

				if len(time) == 1:
					ax.scatter(time, flux, color = col)

def iso_energy(classes = cs, subclasses = sc, subson = False,
			 colors = [defaultc_colors, defaultsc_colors], 
			 xunit = u.d, yunit = u.erg, k = 1, ax = plt, **kwargs):

	lcs = load()

	xconv = u.d.to(xunit)
	yconv = (u.erg).to(yunit)
	if (type(k) == float) or (type(k) == int):
		k = [k]*len(classes)

	if colors == [defaultc_colors, defaultsc_colors]: # hacky test for default parameters (might be temporary if I find a better way)
		if subson:
			colors = colors[1]
		if not subson:
			colors = colors[0]

	if subson:
		for i, c in enumerate(classes):
			ki = k[i]
			if subclasses[i]:
				if sc[i]:
					for k_, s in enumerate(sc[i]):
						col = colors[i][k_]
						for j, obj in enumerate(lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == s)].iterrows()):
							for obj in lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == sc)]:
								time = obj[1]['tdur'] * xconv
								eiso = obj[1]['eiso'] * yconv * ki
								ax.scatter(time, eiso, color = col) #s = lw^2

			if not subclasses[i]:
				col = colors[i]
				for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
					time = obj[1]['tdur'] * xconv
					eiso = obj[1]['eiso'] * yconv * ki
					ax.scatter(time, eiso, color = col)

	if not subson:
		for i, c in enumerate(classes):
			ki = k[i]
			col = colors[i]
			for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
				time = obj[1]['tdur'] * xconv
				eiso = obj[1]['eiso'] * yconv * ki
				ax.scatter(time, eiso, color = col)

def lpk_thalf(classes = cs, subclasses = sc, subson = False,
			 colors = [defaultc_colors, defaultsc_colors], 
			 xunit = u.d, yunit = u.erg/u.s, k = 1, ax = plt, **kwargs):

	lcs = load()

	xconv = u.d.to(xunit)
	yconv = (u.erg/u.s).to(yunit)
	if (type(k) == float) or (type(k) == int):
		k = [k]*len(classes)

	if colors == [defaultc_colors, defaultsc_colors]: # hacky test for default parameters (might be temporary if I find a better way)
		if subson:
			colors = colors[1]
		if not subson:
			colors = colors[0]

	if subson:
		for i, c in enumerate(classes):
			ki = k[i]
			if subclasses[i]:
				if sc[i]:
					for k_, s in enumerate(sc[i]):
						col = colors[i][k_]
						for j, obj in enumerate(lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == s)].iterrows()):
							for obj in lcs.loc[(lcs['class'] == c) & (lcs['subclass'] == sc)]:
								time = obj[1]['thalf'] * xconv
								lum = obj[1]['lpk'] * yconv * ki
								ax.scatter(time, lum, color = col) #s = lw^2

			if not subclasses[i]:
				col = colors[i]
				for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
					time = obj[1]['thalf'] * xconv
					lum = obj[1]['lpk'] * yconv * ki
					ax.scatter(time, lum, color = col)

	if not subson:
		for i, c in enumerate(classes):
			ki = k[i]
			col = colors[i]
			for j, obj in enumerate(lcs.loc[lcs['class'].values == c].iterrows()):
				time = obj[1]['thalf'] * xconv
				lum = obj[1]['lpk'] * yconv * ki
				ax.scatter(time, lum, color = col)








	