#!/bin/bash
# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

if [ $# != 2 ]
then
    echo "=============================================================================================================="
    echo "Usage: bash /PSPNet/scripts/run_eval.sh [YAML_PATH] [DEVICE_ID]"
    echo "Warning: before cpu infer, you need check device_target in config file."
    echo "for gpu example: bash PSPNet/scripts/run_eval.sh PSPNet/config/voc2012_pspnet50.yaml 0"
    echo "for cpu example: bash PSPNet/scripts/run_eval.sh PSPNet/config/voc2012_pspnet50.yaml cpu"
    echo "=============================================================================================================="
    exit 1
fi

rm -rf LOG
mkdir ./LOG
export YAML_PATH=$1
export RANK_SIZE=1
export RANK_ID=0
export DEVICE_ID=$2
echo "start evaluating for device $DEVICE_ID"
env > env.log
if [ "$2" == "cpu" ]
then
    python3 eval_cpu.py --config="$YAML_PATH" > ./LOG/eval_log.txt 2>&1 &
fi
if [ "$2" != "cpu" ]
then
    python3 eval.py --config="$YAML_PATH" > ./LOG/eval_log.txt 2>&1 &
fi
