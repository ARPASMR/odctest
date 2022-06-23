#!/home/buck/anaconda3/envs/odc_env/bin/python3

import rasterio

src = rasterio.open('/home/buck/dev/odc/data/netcdf/test_no_zeta.nc')

print (src.crs)

print (src.crs.wkt)

print (src.transform)

