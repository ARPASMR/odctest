#!/bin/bash
echo 'Drop datacube db'
dropdb datacube
echo 'Create datacube db'
createdb -h localhost -U buck datacube
echo 'System init'
datacube -v system init

echo 'Add product c_O3'
datacube product add c_O3_product.odc-metadata.yaml 
echo 'Add dataset c_O3'
datacube dataset add c_O3_dataset.odc-metadata.yaml

# echo 'Change dir to rodrigo'
# cd rodrigo
# echo 'Add product sentinel_5p_NO2'
# datacube product add rodrigop.yaml 
# echo 'Add dataset sentinel_5p_NO2'
# datacube dataset add rodrigo.yaml
# echo 'Go back'
# cd ..

