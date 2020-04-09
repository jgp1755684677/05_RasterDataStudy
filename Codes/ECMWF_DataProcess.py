import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import os
from mpl_toolkits.basemap import Basemap


# process the NetCDF data.
def get_NetCDF_data(filename):
    # get the dataset.
    f = nc.Dataset(filename)
    # get all variable.
    all_vars = f.variables.keys()
    # export the variable.
    print(all_vars)
    # get the information of all variable.
    all_vars_info = f.variables.items()
    # transfer the variable to a list.
    all_vars_info = list(all_vars_info)
    # get the longitude value.
    lons = f.variables['longitude'][:]
    # get the latitude value.
    lats = f.variables['latitude'][:]
    # get the temperature value.
    t2m = f.variables['t2m'][:]
    # get the time.
    time = f.variables['time'][:]
    # get the unit of latitude
    t2m_units = f.variables['t2m'].units
    # export the unit.
    print(t2m_units)
    # calculate the mean of longitude.
    lon_0 = lons.mean()
    # calculate the mean of latitude.
    lat_0 = lats.mean()
    # define the base map.
    m = Basemap(lat_0=lat_0, lon_0=lon_0)
    # define the gird.
    lon, lat = np.meshgrid(lons, lats)
    # define the axes.
    xi, yi = m(lon, lat)
    # get the first our temperature.
    t2m_0 = t2m[0:1:, ::, ::]
    # export the temperature.
    print(t2m_0)
    # get the second hour temperature.
    t2m_1 = t2m[1:2:, ::, ::]
    # export the temperature.
    print(t2m_1)
    # create gird
    cs = m.pcolor(xi, yi, np.squeeze(t2m_0))

    # Add Grid Lines
    m.drawparallels(np.arange(-90., 91., 20.), labels=[1, 0, 0, 0], fontsize=10)
    m.drawmeridians(np.arange(-180., 181., 40.), labels=[0, 0, 0, 1], fontsize=10)

    # Add Coastlines, and Country Boundaries
    m.drawcoastlines()
    m.drawcountries()

    # Add Colorbar
    cbar = m.colorbar(cs, location='bottom', pad="10%")
    cbar.set_label(t2m_units)

    # Add Title
    plt.title('Surface 2m Air Temperature')
    plt.show()

    f.close()


# 主函数
if __name__ == '__main__':
    # get path of the project.
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # export project path.
    print("Root path:" + root_path)
    # define the path of data.
    data_path = os.path.abspath(root_path + r"\RasterData")
    # export data path.
    print("Data path:" + data_path)
    # change the path.
    os.chdir(data_path)
    # define the name of operated file.
    filename = "201908ECMWF_TPE.nc"
    # call the function.
    get_NetCDF_data(filename)
