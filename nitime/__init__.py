"""
Timeseries Package: XXX: put some short description here

The module has several sub-modules: 

- ``timeseries``: contains the constructors for the two kinds of time-series

- ``algorithms``: contains algorithms

- ``utils``: I am not so sure what this will contain, but I am pretty sure that a
   need for this might arise along the way.

All of the sub-modules will be imported as part of ``__init__``, so that users
have all of these things at their fingertips.
"""

__docformat__ = 'restructuredtext'

from version import version as __version__
__status__   = 'alpha'
__url__     = 'http://neuroimaging.scipy.org'

#The order of the following is important - make sure to import according to the
#order of dependency (for example, timeseries depends on descriptors, so
#descriptors needs to be imported first): 
import utils, algorithms, descriptors, timeseries, vista_utils, viz

from timeseries import *

from numpy.testing import Tester
test = Tester().test
bench = Tester().bench
