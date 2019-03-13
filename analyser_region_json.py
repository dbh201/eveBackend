from json import *
from analyser_region import AnalyserRegion

class RegionEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, AnalyserRegion):
            return vars(obj)
        return JSONEncoder.default(self,obj)
