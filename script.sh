#!/usr/bin/env bash

#DATE_DU_RUN="20151211"
SECONDS=0

if [ $# -eq 0 ]
  then
    echo "Please input Date_du_run as an arg. Ex: 2015-12-28"
    exit 1
fi

DATE=$1
DATE_DU_RUN="${DATE//-}"
GRILLE="AROME_0.025"
U_="_"
SOUS_PAQUET="SP1"
TIME_DU_RUN="0000"
POSTFIX=".grib2"
#PATH="./data/processed/"
echo $GRILLE$U_$SOUS_PAQUET$U_$DATE_DU_RUN$TIME_DU_RUN$POSTFIX

#cat files
GRIB_FILES=$GRILLE$U_$SOUS_PAQUET$U_*$DATE_DU_RUN$TIME_DU_RUN$POSTFIX
MERGED_FILE=$GRILLE$U_$SOUS_PAQUET$U_$DATE_DU_RUN$TIME_DU_RUN$POSTFIX

if [ ! -d "tmp" ]; then
    # Control will enter here if $DIRECTORY doesn't exist.
    mkdir tmp #different with /tmp/ folder of Linux
fi

cat ./data/$DATE_DU_RUN/$GRIB_FILES > ./tmp/$MERGED_FILE

echo ./tmp/$MERGED_FILE


FC_TIME_LIST=("00" "01" "02" "03" "04" "05" "06" "07" "08" "09" "10" 
    "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" 
    "21" "22" "23")
SHORT_PARA=("WIND" "TCDC")
LONG_PARA=(":WIND:10 m above ground:" ":TCDC:atmos col:")
DB=$U_$DATE_DU_RUN

#CREATE DATABASE && TABLES
python pythonScript.py $U_$DATE_DU_RUN

#EXTRACT DATA AND IMPORT TO MYSQL
for i in "${FC_TIME_LIST[@]}"; do   # The quotes are necessary here
    echo "$i"
    date_fc_time=$DATE_DU_RUN$i
    grib_file=$U_$DATE_DU_RUN$i$POSTFIX
    echo $date_fc_time
    echo $grib_file

    #Extract to separate files by forecast time and store them in /tmp folder
    wgrib2 ./tmp/$MERGED_FILE -vt -s | awk -v var="$date_fc_time" '{d=substr($3,4); if (d == var) print $0}' FS=':' |
    wgrib2 ./tmp/$MERGED_FILE -i -grib ./tmp/$grib_file

    #For each file, extract messages and then import to mysql
    for ((j=0;j<${#SHORT_PARA[@]};++j)); do
        printf "%s is in %s\n" "${SHORT_PARA[j]}" "${LONG_PARA[j]}"
        find /tmp/ -type f -name "wgrib2*" -exec rm {} \;
        wgrib2 ./tmp/$grib_file -match "${LONG_PARA[j]}" -mysql localhost root root $DB ${SHORT_PARA[j]}
        file=( $(readlink -f /tmp/wgrib2*) )
        table="${SHORT_PARA[j]}"
        mysql -h localhost -u root -proot $DB -e \
        "LOAD DATA LOCAL INFILE '${file}' INTO TABLE ${table} FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"
    done
done

#delete folder ./tmp after each run of this script
rm -r ./tmp

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."

