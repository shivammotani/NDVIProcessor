from src.utils import handleInputOutput,calculateNdvi

if __name__ == "__main__":
    polygon_file_name = "sample_polygon.geojson"
    polygon_object = handleInputOutput.FileReader(polygon_file_name)
    polygon_data = polygon_object.read_file()
    
    s3_path = "s3://sentinel-cogs/sentinel-s2-l2a-cogs/36/N/YF/2023/6/S2B_36NYF_20230605_0_L2A/"
    red_band_file = s3_path + "B04.tif"
    nir_band_file = s3_path + "B08.tif"

    satelliteData = handleInputOutput.LandSatPath(nir_band_file, red_band_file)
    finalNirData, finalRedData = satelliteData.readSatelliteData(polygon_data)

    processNdvi = calculateNdvi.NDVI(finalNirData, finalRedData)
    processNdvi.calculateStats()

    outputData = handleInputOutput.writeToDisk(processNdvi)
    outputData.saveData()