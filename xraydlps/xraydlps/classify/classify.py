import numpy as np
import astropy.units as u
import pandas as pd
from scipy.interpolate import interp1d
from sklearn.neighbors import KNeighborsClassifier
from xraydlps.tools import load, convert
import warnings

def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
	return '%s:%s: %s: %s\n' % (filename, lineno, category.__name__, message)

warnings.formatwarning = warning_on_one_line

### internal functions -- callable, but generally not necessary to call explicitly ###

def get_interp(time, lum, t = np.logspace(-8, 4, 100), returns = 'df'):
	"""
	Generate *evenly* sampled light curves for DTW via interpolation.
	
	Run automatically within train_lcmodel.
	
	Parameters:
		time (arr): Time (days) for individual light curve.
		lum (arr): Luminosity (cgs) for individual light curve.
		t (arr): Time (days) used for sampling interpolated light curves.
		returns (str): 'df' to return dataframe for sklearn, 'arr' generates an array
		
	Returns:
		Luminosity (cgs) sampled by t (days) -- dataframe if "df", array if "arr".
	"""
	
	if len(t) >= 10**4:
		warnings.warn('Increased sampling may make prediction slow. Try ~1000 points or fewer.')
		
	if len(time) < 2: #filter for single data points
		if returns == 'arr':
			return np.array([np.nan])
		if returns == 'df':
			lcdict = {}
			for i in range(len(t)):
				lcdict[str(i)] = np.nan
			lcdf = pd.DataFrame(lcdict, index = [0])
			return lcdf
		
	interp = interp1d(time, lum)

	lc = np.zeros_like(t, dtype = float) # so that sklearn will work
	lc[(t >= np.min(time)) & (t <= np.max(time))] = interp(t[(t >= np.min(time)) & (t <= np.max(time))])
	
	if returns == 'arr':
		return lc
	
	if returns == 'df':
		lcdict = {}
		for i in range(len(t)):
			lcdict[str(i)] = lc[i]
		
		lcdf = pd.DataFrame(lcdict, index = [0])
		return lcdf


def dtw_dist(lc1, lc2):
	"""
	Implementation of dynamic time warping for time series classification.

	Only necessary if training a new model.

	Parameters:
		lc1 (series): first light curve Lx
		lc2 (series): second light curve Lx

	Returns:
		Dynamic time warping distance metric for use in classification.
	"""

	n, m = len(lc1), len(lc2)

	dtw = np.full((n + 1, m + 1), np.inf)
	dtw[0, 0] = 0

	for i in range(1, n + 1):
		for j in range (1, m + 1):
			cost = abs(lc1[i - 1] - lc2[j - 1]) 
			dtw[i, j] = cost + np.min([dtw[i - 1, j], dtw[i, j - 1], dtw[i - 1, j - 1]])

	return dtw[n, m]


##########
# * * * * 
##########


def lc_class(time, lum, tunits = u.d, lunits = u.erg/u.s, k = 1, verbose = True, skip_zero = True, full = False):
	"""
	Classify light curve based on default pre-trained KNN using dynamic time warping on time-series data.

	At best ~70% accurate based on testing for correct *primary* classification. Use with caution!

	Parameters:
		time (arr): Input luminosity data for light curve. Default unit in days.
		lum (arr): Input luminosity data for light curve. Default unit in erg/s.
		tunits (astropy units object): Input units of time.
		lunits (astropy units object): Input units of luminosity.
		k (float): K-correction to 0.3 - 10 keV band if input light curve in different band.
		verbose (bool): If verbose, print all possible classes + classification probability.
		skip_zero (bool): If verbose and skip_zero = True, only show classes with probability > 0.
		full (bool): Use model trained on full available dataset rather than 70/30 training/test split.
			Accuracy comes from testing model used when full = False. Ultimate accuracy may vary.

	Returns:
		If verbose, returns class + classification probability. If not verbose, returns class.
	"""

	warnings.warn("Model is ~70\% accurate based on testing. Use with caution!!")

	if not full:
		mod = load('lc_mod.pkl')
	if full:
		mod = load('lc_mod_full.pkl')
	tconv = tunits.to(u.d)
	lconv = k*lunits.to(u.erg/u.s)
	lx = get_interp(time*tconv, lum*lconv)

	if not verbose:
		out = mod.predict(lx)
		print(out[0])
		return out

	if verbose:
		labels_ = mod.classes_

		out_ = mod.predict_proba(lx)

		out = np.sort(out_)[::-1]
		labels = labels_[np.argsort(out_)][::-1]

		if not skip_zero:
			df = pd.DataFrame.from_dict({'class': labels, 'classification probability':out})

		if skip_zero:
			df = pd.DataFrame.from_dict({'class': labels[out > 0], 'classification probability':out[out > 0]})

		print(df.to_string(index=False))
		return labels_, out_



def sum_class(time, lum, tunits = u.d, lunits = u.erg/u.s, k = 1, verbose = True, skip_zero = True, full = False):
	"""
	Classify light curve based on default pre-trained KNN using summary values.

	At best ~60% accurate based on testing for correct *primary* classification. Use with caution!!

	If you would like to train your own model, use xraydlps.classify.train_summodel().

	Parameters:
		time (arr): Input luminosity data for light curve. Default unit in days.
		lum (arr): Input luminosity data for light curve. Default unit in erg/s.
		tunits (astropy units object): Input units of time.
		lunits (astropy units object): Input units of luminosity.
		k (float): K-correction to 0.3 - 10 keV band if input light curve in different band.
		verbose (bool): If verbose, print all possible classes + classification probability.
		skip_zero (bool): If verbose and skip_zero = True, only show classes with probability > 0.
		full (bool): Use model trained on full available dataset rather than 70/30 training/test split.
			Accuracy comes from testing model used when full = False. Ultimate accuracy may vary.

	Returns:
		If verbose, returns class + classification probability. If not verbose, returns class.
	"""

	warnings.warn("Model is ~60\% accurate based on testing. Use with caution!!")

	if not full:
		mod = load('sum_mod.pkl')
	if full:
		mod = load('sum_mod_full.pkl')
	tconv = tunits.to(u.d)
	lconv = k*lunits.to(u.erg/u.s)
	lpk, thalf, eiso, dur = convert(time*tconv, lum*lconv)

	pred = {'lpk':lpk, 'eiso':eiso, 'tdur':dur}
	# preddf = pd.DataFrame.from_dict(pred) 
	preddf = pd.DataFrame(pred, index = [0]) 

	if not verbose:
		out = mod.predict(preddf)
		print(out[0])
		return out

	if verbose:
		labels_ = mod.classes_

		out_ = mod.predict_proba(preddf)

		out = np.sort(out_)[::-1]
		labels = labels_[np.argsort(out_)][::-1]

		if not skip_zero:
			df = pd.DataFrame.from_dict({'class': labels, 'classification probability':out})
		if skip_zero:
			df = pd.DataFrame.from_dict({'class': labels[out > 0], 'classification probability':out[out > 0]})

		print(df.to_string(index=False))
		return labels_, out_



def train_lcmodel(dataframe = load(), n_neighbors = 1, include_singles = True, frb_as_magnetar = False, 
				verbose = True, t = np.logspace(-8, 4, 100), weights = 'uniform', test = 0.3, train = 0.7, **kwargs):
	"""
	Train model that classifies based on matching light curves.
	
	Defaults are representative of training for models in xraydlps.classify.lc_class.
	
	Parameters:
		dataframe (df): Dataframe that contains data and labels. Labels column 'class', data column 'lc'.
		n_neighbors (int): Number of neighbors used by KNN. If include_singles, n_neighbors = 1.
		include_singles (bool): Include SBO (SN2008D) and FRB (FRB200428) in classifier.
		frb_as_magnetar (bool): If include_singles = False, re-assign FRB to magnetar label. Otherwise ignored.
		verbose (bool): If verbose, print information about training and return test set.
		t (arr): Time (days) used for sampling interpolated light curves.
		weights (str): 'uniform' or 'distance' -- weights used when k neighbors > 1.
		test (float): Fraction of sample to be allocated to test set.
		train (float): Fraction of sample to be allocated to training set.
		**kwargs: Other keyword arguments for sklearn.neighbors.KNeighborsClassifier().
		
	Returns:
		Trained model to classify input light curve.
		
		If verbose, also return the training and test sets (data, labels) - dtrain, dtest, ltrain, ltest. 
	"""
	dataframe['lc'] = [get_interp(i[1].time, i[1].lum, t = t) for i in dataframe.iterrows()]
	
	labels = [] #Labels to be used for classification.
	data = [] #Consistently sampled light curve data for KNN with DTW.
	for i in dataframe.iterrows():
		if len(i[1].lc) > 1: #filter for light curves of length 1
			labels.append(i[1]['class'])
			data.append(i[1].lc)
			
	labels = np.array(labels)
	data = np.array(data)
	
	if include_singles:
		if n_neighbors != 1:
			warnings.warn("Warning: Since include_singles = True, setting n_neighbors = 1.")
		n_neighbors = 1 #since single light curve for each of SBO and FRB
		
		## split test-train so that train includes SBO and FRB
		labels_ = labels[(labels != 'sbo') & (labels != 'frb')]
		data_ = data[(labels != 'sbo') & (labels != 'frb')]
		
		if (test > 0) and (train < 1):
			dtrain, dtest, ltrain, ltest = train_test_split(data_, labels_, test_size = test, train_size = train)

			dtrain = np.concatenate((dtrain, data[(labels == 'sbo') | (labels == 'frb')]))
			ltrain = np.concatenate((ltrain, labels[(labels == 'sbo') | (labels == 'frb')]))
		
		
	if not include_singles:
		if frb_as_magnetar:
			labels[labels == 'frb'] = 'magnetars'
			
		## filter to skip SBO and FRB from test + training
		labels_ = labels[(labels != 'sbo') & (labels != 'frb')]
		data_ = data[(labels != 'sbo') & (labels != 'frb')]
		
		if (test > 0) and (train < 1):
			dtrain, dtest, ltrain, ltest = train_test_split(data_, labels_, test_size = 0.3, train_size = 0.7)
	
	knn = KNeighborsClassifier(metric = dtw_dist, n_neighbors = n_neighbors, weights = weights, **kwargs)
	
	if (test > 0) and (train < 1):
		if not verbose:
			return knn.fit(X = dtrain, y = ltrain)
		if verbose:
			return knn.fit(X = dtrain, y = ltrain), dtrain, dtest, ltrain, ltest
	
	if (test == 0) and (train == 1):
		if not verbose:
			return knn.fit(X = data_, y = labels_)
		if verbose:
			return knn.fit(X = data_, y = labels_), data_, [], labels_, []
	
def train_summodel(dataframe = load(), n_neighbors = 1, use_thalf = False, min_len = 1, 
				   include_singles = True, frb_as_magnetar = False, verbose = True, 
				   weights = 'uniform', p = 1, test = 0.3, train = 0.7, **kwargs):
	"""
	Train model that classifies based on matching summary statistics.
	
	Defaults are representative of training for models in xraydlps.classify.sum_class.
	
	Parameters:
		dataframe (df): Dataframe that contains data and labels. Labels column 'class', data column 'lc'.
		n_neighbors (int): Number of neighbors used by KNN. If include_singles, n_neighbors = 1.
		use_thalf (bool): If True, include thalf (time above 1/2 Lpk) in classification. Requires len(lc) > 1.
		min_len (int): Minimum length of included light curve -- if use_thalf = True, min_len becomes 2.
		include_singles (bool): Include SBO (SN2008D) and FRB (FRB200428) in classifier.
		frb_as_magnetar (bool): If include_singles = False, re-assign FRB to magnetar label. Otherwise ignored.
		verbose (bool): If verbose, return training and test sets.
		weights (str): 'uniform' or 'distance' -- weights used when k neighbors > 1.
		p (int): 1 or 2 -- determines power parameter for Minkowski distance metric.
		test (float): Fraction of sample to be allocated to test set.
		train (float): Fraction of sample to be allocated to training set.
		**kwargs: Other keyword arguments for sklearn.neighbors.KNeighborsClassifier().
		
	Returns:
		Trained model to classify input light curve via summary statistics.
		
		If verbose, also return the training and test sets (data, labels) - drain, dtest, ltrain, ltest.
	"""
	
	if not use_thalf:
		data = dataframe[['lpk', 'eiso', 'tdur']].copy()
		labels = dataframe[['class']].copy()
		
		data = data.loc[dataframe.time.map(len) >= min_len]
		labels = labels.loc[dataframe.time.map(len) >= min_len]
	
	if use_thalf:
		warnings.warn("Use caution; thalf is a less robust derived quantity dependent on time-sampling and other factors.")
		data = dataframe[['lpk', 'thalf', 'eiso', 'tdur']].copy()
		labels = dataframe[['class']].copy()
		
		data = data.loc[(dataframe.time.map(len) >= min_len) & (dataframe.thalf.notnull())]
		labels = labels.loc[(dataframe.time.map(len) >= min_len) & (dataframe.thalf.notnull())]
	
	
	if include_singles:
		if n_neighbors != 1:
			warnings.warn("Warning: Since include_singles = True, setting n_neighbors = 1.")
		n_neighbors = 1 #since single light curve for each of SBO and FRB
		
		## split test-train so that train includes SBO and FRB
		labels_ = labels.loc[(labels['class'] != 'sbo') & (labels['class'] != 'frb')]
		data_ = data.loc[(labels['class'] != 'sbo') & (labels['class'] != 'frb')]
		
		if (test > 0) and (train < 1):
			dtrain, dtest, ltrain, ltest = train_test_split(data_, labels_, test_size = test, train_size = train)

			dtrain = dtrain.append(data.loc[(labels['class'] == 'sbo') | (labels['class'] == 'frb')])
			ltrain = ltrain.append(labels.loc[(labels['class'] == 'sbo') | (labels['class'] == 'frb')])

		
	if not include_singles:
		if frb_as_magnetar:
			labels[labels == 'frb'] = 'magnetars'
			
		## filter to skip SBO and FRB from test + training
		labels_ = labels.loc[(labels['class'] != 'sbo') & (labels['class'] != 'frb')]
		data_ = data.loc[(labels['class'] != 'sbo') & (labels['class'] != 'frb')]
		
		if (test > 0) and (train < 1):
			dtrain, dtest, ltrain, ltest = train_test_split(data_, labels_, test_size = test, train_size = train)
	
	knn = KNeighborsClassifier(n_neighbors = n_neighbors, weights = weights, p = p, **kwargs)
	
	if (test > 0) and (train < 1):
		if not verbose: 
			return knn.fit(X = dtrain, y = ltrain)
		if verbose:
			return knn.fit(X = dtrain, y = ltrain), dtrain, dtest, ltrain, ltest
		
	if (test == 0) and (train == 1):
		if not verbose:
			return knn.fit(X = data_, y = labels_)
		if verbose:
			return knn.fit(X = data_, y = labels_), data_, [], labels_, []