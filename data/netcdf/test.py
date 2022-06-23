#!/home/buck/anaconda3/envs/odc_env/bin/python3

import datacube
from datacube.api.query import Query, query_group_by, query_geopolygon

dc = datacube.Datacube(app="arpa_analysis")

query = Query(product='c_o3_no_z', time=('2015-04-10T02:00:00', '2015-04-11T01:00:00'))

datasets = dc.find_datasets(**query.search_terms)
print('\n***** DATASETS for c_o3_no_z')
print(datasets)

products = dc.list_products(False, True)
print('\n***** PRODUCTS for c_o3_no_z')
print(products)

measurements = dc.list_measurements(True, False)
print('\n***** MEASUREMENTS for c_o3_no_z')
print(measurements)

result = dc.load(product='c_o3_no_z',
        measurements=['c_O3']
        )
print('\n***** RESULTS for c_o3_no_z')
print(result)

dc.close()

# dc1 = datacube.Datacube(app="isentinel_analysis")

# query1 = Query(product='sentinel_5p_NO2', time=('2022-05-05T00:00:00', '2022-05-05T23:59:59'))

# datasets1 = dc1.find_datasets(**query1.search_terms)
# print('\n***** DATASETS for sentinel_5p_NO2')
# print(datasets1)

# products1 = dc1.list_products(False, True)
# print('\n***** PRODUCTS for sentinel_5p_NO2')
# print(products1)

# measurements1 = dc1.list_measurements(True, False)
# print('\n***** MEASUREMENTS for sentinel_5p_NO2')
# print(measurements1)


# result1 = dc1.load(product='sentinel_5p_NO2',
#         measurements=['tropospheric_NO2_column_number_density', 'NO2_column_number_density', 'stratospheric_NO2_column_number_density', 'NO2_slant_column_number_density', 'cloud_fraction', 'absorbing_aerosol_index', 'tropopause_pressure'])
# print('\n***** RESULTS for sentinel_5p_NO2')
# print(result1)

# dc1.close()
