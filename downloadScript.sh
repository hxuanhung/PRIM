SECONDS=0
DATE=$1
REFERENCETIME=$DATE"T00" #reference time might be T00, T03, T06 or T18 # todo: confirm this
DATE_DU_RUN="${DATE//-}"
GRILLE="AROME_0.025"
U_="_"
SOUS_PAQUET="SP1"
TIME_DU_RUN="0000"
POSTFIX=".grib2"

GROUP_ECHEANCES=("00H06H" "07H12H" "13H18H" "19H24H" "25H30H" "31H36H" "37H42H")

#DATE_DU_RUN="20151211"
if [ $# -eq 0 ]
  then
    echo "Please input the Date as an arg. Ex: 2016-16-04"
    exit 1
fi

if [ ! -d "./data/$DATE_DU_RUN" ]; then
    # Control will enter here if $DIRECTORY doesn't exist.
    mkdir ./data/$DATE_DU_RUN
fi

for i in "${GROUP_ECHEANCES[@]}"; do   # The quotes are necessary here
    echo "$i"
    token="__5yLVTdr-sGeHoPitnFc7TZ6MhBcJxuSsoZp6y0leVHU__"
    url="http://dcpc-nwp.meteo.fr/services/PS_GetCache_DCPCPreviNum?token=$token&model=AROME&grid=0.025&package=SP1&time=$i&referencetime=$REFERENCETIME:00:00Z"
    curl -o ./data/$DATE_DU_RUN/$GRILLE$U_$SOUS_PAQUET$U_$i$U_$DATE_DU_RUN$TIME_DU_RUN$POSTFIX -L --max-filesize 100000 $url
done

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."