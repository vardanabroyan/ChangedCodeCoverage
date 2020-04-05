
import inspect
import os.path
from xml.etree import ElementTree

import coverage
from coverage import env
from coverage.backward import StringIO, import_local_file
from coverage.data import line_counts
from coverage.control import Plugins
from coverage.misc import CoverageException

import coverage.plugin

#from tests.coveragetest import CoverageTest
#from tests.helpers import CheckUniqueFilenames

class Utils:
    def open(self, filename, mode="r"):
        """Be just like `open`, but write written file names to `self.written`."""
        if mode.startswith("w"):
            self.written.add(filename.replace('\\', '/'))
        return open(filename, mode)



    def run_all_functions(self, cov, suite_name):           # pragma: nested
        """Run all functions in `suite_name` under coverage."""
        cov.start()
        suite = import_local_file(suite_name)
        #print(dir(suite))
        try:
            # Call all functions in this module
            for name in dir(suite):
                variable = getattr(suite, name)
                
                if inspect.isclass(variable):
                    obj = variable()
                    
                    memberNames = inspect.getmembers(variable,inspect.isfunction)
                    
                    for member in memberNames:
                        if member[0].startswith('test_'):
                            getattr(obj, member[0])()
                #if inspect.isfunction(variable):
                #    variable()
        finally:
            cov.stop()


 
