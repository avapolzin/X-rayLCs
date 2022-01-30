# SNe

SN light curves are organized into folders by type (as defined in the paper -- Type I, Type II, Interacting, Superluminous, and Ca-rich); the text files with names _SNe\_\*\_list.txt_ list the included SNe and some additional details about them (distance, k-correction, etc.).

The _Type I_, _Type II_, and _Interacting_ light curve files are named according to the event and the energy in tens of eV, so that "SN1993J_lc_30_1000.txt" is the 0.3-10 keV light curve for SN1993J and "SN2005kd_lc_50_800.txt" is the 0.5-8 keV light curve for SN2005kd. The k-correction for each event in the list files can be used to convert the light curves to 0.3-10 keV.

The relevant columns are "time(days)" and "flux(1d-15 erg/s/cm2)" (flux in units of 10<sup>-15</sup> erg s<sup>-1</sup>). Other columns give the (symmetric) error on "time" and "flux", as well as the instrument that took the observation. Additional light curve-specific information is retained at the top of some of the event files.

The _Superluminous_ and _Ca-rich_ light curve files are named according to the event. The columns for _Superluminous_ light curves are "time(days)" and "Lum(erg/s)" (in the 0.3-10 keV band). The colums for the _Ca-rich_ light curve are "Time(day)" and "Flux(erg/s/cm2)" (also 0.3-10 keV).

See Table A3 for additional details about the individual events (NOTE: will add a typeset image of the table to this README when it becomes available from the journal).
