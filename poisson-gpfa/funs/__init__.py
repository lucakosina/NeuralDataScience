'''Main engine module for Poisson-GPFA model.

.. moduleauthor:: Hooram Nam <hooram.nam@tuebingen.mpg.de>

'''

import sys
import os
sys.path.append(os.getcwd()+'/funs/')
from . import engine 
from . import learning
from . import inference
from . import util
