
if [ $# != 2 ]
then
    echo "=============================================================================================================="
    echo "Usage: bash scripts/run_distribute_train_ascend.sh [RANK_TABLE_FILE] [YAML_PATH]"
    echo "Please run the script as: "
    echo "bash /PSPNet/scripts/run_distribute_train_ascend.sh [RANK_TABLE_FILE] [YAML_PATH]"
    echo "for example: bash scripts/run_distribute_train_ascend.sh /PSPNet/scripts/config/RANK_TABLE_FILE PSPNet/config/voc2012_pspnet50.yaml"
    echo "=============================================================================================================="
    exit 1
fi

export RANK_SIZE=8
export RANK_TABLE_FILE=$1
export YAML_PATH=$2
export HCCL_CONNECT_TIMEOUT=6000

for((i=0;i<RANK_SIZE;i++))
do
    export DEVICE_ID=$i
    rm -rf LOG$i
    mkdir ./LOG$i
    cp ./*.py ./LOG$i
    cp -r ./src ./LOG$i
    cd ./LOG$i || exit
    export RANK_ID=$i
    echo "start training for rank $i, device $DEVICE_ID"
    env > env.log
    python3 train.py --config="$YAML_PATH"> ./log.txt 2>&1 &

    cd ../
done