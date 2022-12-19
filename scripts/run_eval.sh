
if [ $# != 2 ]
then
    echo "=============================================================================================================="
    echo "Usage: bash /PSPNet/scripts/run_eval.sh [YAML_PATH] [DEVICE_ID]"
    echo "Warning: before cpu infer, you need check device_target in config file."
    echo "for gpu example: bash PSPNet/scripts/run_eval.sh PSPNet/config/voc2012_pspnet50.yaml 0"
    echo "=============================================================================================================="
    exit 1
fi

if [ ! -d "LOG/" ];then
    mkdir LOG
    else
    echo "The LOG folder already exists."
fi

i=1
file="eval_log.txt"
while [ -e "LOG/$file" ]
do
    file="eval_log${i}.txt"
    let "i++"
done

export YAML_PATH=$1
export RANK_SIZE=1
export RANK_ID=0
export DEVICE_ID=$2
echo "start evaluating for device $DEVICE_ID"
env > env.log

python3 eval.py --config="$YAML_PATH" > ./LOG/$file 2>&1 &
