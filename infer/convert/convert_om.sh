
if [ $# -ne 2 ]
then
  echo "Wrong parameter format."
  echo "Usage:"
  echo "         bash $0 INPUT_AIR_PATH OUTPUT_OM_PATH_NAME"
  echo "Example: "
  echo "         bash convert_om.sh models/0-150_1251.air models/0-150_1251.om"

  exit 255
fi

input_air_path=$1
output_om_path=$2

echo "Input AIR file path: ${input_air_path}"
echo "Output OM file path: ${output_om_path}"


atc --input_format=NCHW \
--framework=1 \
--model=${input_air_path} \
--output=${output_om_path} \
--soc_version=Ascend310 \
--disable_reuse_memory=0 \
--output_type=FP32 \
--precision_mode=allow_fp32_to_fp16  \
--op_select_implmode=high_precision