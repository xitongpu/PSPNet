# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 3.0 (the "License");
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
"""generate train_list.txt or val_list.txt file script for voc dataset"""

import argparse
import os


def _parse_args():
    parser = argparse.ArgumentParser('dataset list generator')
    parser.add_argument("--data_dir", type=str, default='',
                        help='where dataset stored.')
    return parser.parse_args()


def _get_data_list(data_list_file):
    with open(data_list_file, mode='r') as f:
        return f.readlines()


def main():
    args = _parse_args()
    data_dir = args.data_dir

    voc_train_txt = os.path.join(data_dir, 'train.txt')
    voc_train_lst_txt = os.path.join(data_dir, 'train_list.txt')

    voc_val_txt = os.path.join(data_dir, 'val.txt')
    voc_val_lst_txt = os.path.join(data_dir, 'val_list.txt')

    voc_train_data_lst = _get_data_list(voc_train_txt)
    with open(voc_train_lst_txt, mode='w') as f:
        for id_ in voc_train_data_lst:
            id_ = id_.strip()
            img_ = os.path.join('img', id_ + '.jpg')
            anno_ = os.path.join('cls_png', id_ + '.png')
            f.write(img_ + ' ' + anno_ + '\n')
    print('generating voc train list success.')

    voc_val_data_lst = _get_data_list(voc_val_txt)
    with open(voc_val_lst_txt, mode='w') as f:
        for id_ in voc_val_data_lst:
            id_ = id_.strip()
            img_ = os.path.join('img', id_ + '.jpg')
            anno_ = os.path.join('cls_png', id_ + '.png')
            f.write(img_ + ' ' + anno_ + '\n')
    print('generating voc val list success.')

if __name__ == '__main__':
    main()
