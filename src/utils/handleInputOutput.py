import rasterio
from rasterio.features import geometry_window, geometry_mask
from rasterio.windows import transform
import geopandas as gpd
import matplotlib.pyplot as plt
import os

class FileReader:
    def __init__(self, polygon_file_name = None):
        file_paths = f'src/input/{polygon_file_name}'
        self.file_path = file_paths

    def read_file(self):
        if(self.file_path == None):
            return "Invalid File Name"
        try:
            polygon = gpd.read_file(self.file_path)
            projected_polygon = polygon.to_crs(epsg=32636)
            return projected_polygon
        except Exception as e:
            print("Could not read polygon file: " + self.file_path + str(e))
            return None

class LandSatPath:
    def __init__(self, nirBandFile, redBandFile):
        self.nirBandFile = nirBandFile
        self.redBandFile = redBandFile
        os.environ['AWS_NO_SIGN_REQUEST'] = 'YES'

    def readSatelliteData(self, polygon):
        self.polygon = polygon
        with rasterio.open(self.nirBandFile) as nir_src, rasterio.open(self.redBandFile) as red_src:
            for feature in polygon.iterfeatures():
            
                window = geometry_window(nir_src, [feature["geometry"]])
                window_transform = transform(window, nir_src.transform)
                window_shape = (window.height, window.width)

                # Read all the data in the window, masking out any NoData
                nir = nir_src.read(window=window, masked=True).astype('float32')
                red = red_src.read(window=window, masked=True).astype('float32')
                
                # Update the NoData mask to exclude anything outside the polygon
                mask = geometry_mask([feature["geometry"]], window_shape, window_transform)
                nir.mask += mask
                red.mask += mask

                return nir,red
            
class writeToDisk:

    def __init__(self, ndviObject):
        self.ndviObject = ndviObject
    
    def saveData(self):

        file_paths = f'src/output/'
        if not os.path.exists(file_paths):
            os.makedirs(file_paths)

        plt.imshow(self.ndviObject.ndvi[0])
        plt.colorbar()
        plt.title('{}'.format("NDVI"))
        plt.savefig(os.path.join(file_paths, 'ndvi.png'))
        plt.close()

        with open(os.path.join(file_paths, 'statistics.csv'), "w") as stats:
            stats.write("Statistic,Value\n") 
            stats.write(f"Mean NDVI,{self.ndviObject.mean}\n")
            stats.write(f"Min NDVI,{self.ndviObject.min}\n")
            stats.write(f"Max NDVI,{self.ndviObject.max}\n")




                

