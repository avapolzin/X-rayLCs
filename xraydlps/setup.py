import setuptools

setuptools.setup(
	name = "xraydlps",
	version = "1.0.0",
	author = "Ava Polzin",
	author_email = "apolzin@uchicago.edu",
	description = "Tools to help plot the X-ray duration-luminosity phase space and use it for classification.",
	packages = ["xraydlps", "xraydlps/plot", "xraydlps/classify", "xraydlps/tools"],
	url = "https://github.com/avapolzin/X-rayLCs",
	license = "MIT",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Topic :: Scientific/Engineering :: Astronomy",
		"Topic :: Scientific/Engineering :: Physics"
		],
	python_requires = ">3",
	install_requires = ["numpy", "matplotlib", "pandas", "scikit-learn", "astropy", "scipy"],
	package_data={'xraydlps': ['data/*']}
	)
