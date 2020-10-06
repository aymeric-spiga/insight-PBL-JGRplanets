#! /bin/bash

int=10
int=20

all=`ls -d 25M*`
all=`ls -d 25M_LS0*`
all=`ls -d 25M_LS0_W20`
echo $all

#ncrcat -D 1 -O -v PSFC $1/wrfout* PSFC_LMD_LES_$1.nc
#ncrcat -D 1 -O -d Time,1,,1 -d south_north,,,$int -d west_east,,,$int PSFC_LMD_LES_$1.nc PSFC_LMD_LES_$1_every${int}.nc

for fold in ${all[*]}
do
  echo "PROCESSING: "$fold

  #ncrcat -D 1 -O -v PSFC $fold/wrfout* PSFC_LMD_LES_$fold.nc
  #ncrcat -D 1 -O -d Time,1,,1 -d south_north,,,$int -d west_east,,,$int PSFC_LMD_LES_$fold.nc PSFC_LMD_LES_$fold_every${int}.nc

  fifi=`ls ${fold}/wrfout_d01_9999-??-??_????????`
  echo $fifi

  for mot in ${fifi[*]}
  do
    echo "PROCESSING: "$mot;
    ncrcat -O -d south_north,,,$int -d west_east,,,$int $mot ${mot}_every${int}.nc
  done

  ncrcat -O -d Time,1,,1 ${fold}/wrfout*_every${int}.nc PSFC_LMD_LES_${fold}_every${int}.nc

done

