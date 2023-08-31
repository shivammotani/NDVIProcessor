import numpy as np

class NDVI:
    def __init__(self, nirData, redData):
        self.ndvi = np.ma.masked_invalid((nirData - redData) / (nirData + redData))
        self.mean = None
        self.min = None
        self.max = None

    def calculateStats(self):
        self.mean = np.mean(self.ndvi)
        self.min = np.min(self.ndvi)
        self.max = np.max(self.ndvi)


