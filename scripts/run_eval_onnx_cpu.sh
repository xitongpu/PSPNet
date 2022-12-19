
if [ $# != 1 ]
then
    echo "=============================================================================================================="
    echo "Usage: bash /PSPNet/scripts/run_eval_onnx_cpu.sh [YAML_PATH]"
    echo "for example: bash PSPNet/scripts/run_eval_onnx_cpu.sh PSPNet/config/voc2012_pspnet50.yaml"
    echo "=============================================================================================================="
    exit 1
fi

rm -rf LOG
mkdir ./LOG
export YAML_PATH=$1
export RANK_SIZE=1
export RANK_ID=0
echo "start evaluating on CPU"
env > env.log

python3 eval_onnx_cpu.py --config="$YAML_PATH" > ./LOG/eval_onnx.txt 2>&1 &
