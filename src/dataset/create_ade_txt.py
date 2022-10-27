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
"""generate train_list.txt or val_list.txt file script for ade dataset"""

import argparse
import os


def _parse_args():
    parser = argparse.ArgumentParser('dataset list generator')
    parser.add_argument("--data_dir", type=str, default='',
                        help='where dataset stored.')
    return parser.parse_args()


def main():
    args = _parse_args()
    data_dir = args.data_dir

    ade_train_img_dir = os.path.join(data_dir, 'images', 'training')
    ade_val_img_dir = os.path.join(data_dir, 'images', 'validation')

    ade_train_lst_txt = os.path.join(data_dir, 'training_list.txt')
    ade_val_lst_txt = os.path.join(data_dir, 'val_list.txt')

    with open(ade_train_lst_txt, mode='w') as f:
        for id_ in sorted(os.listdir(ade_train_img_dir)):
            name = id_.split('.')[0]
            img = os.path.join('images', 'training', id_)
            anno = os.path.join('annotations', 'training', name + '.png')
            f.write(img + ' ' + anno + '\n')
    print('generating ade20k train list success.')

    with open(ade_val_lst_txt, mode='w') as f:
        for id_ in sorted(os.listdir(ade_val_img_dir)):
            name = id_.split('.')[0]
            img = os.path.join('images', 'validation', id_)
            anno = os.path.join('annotations', 'validation', name + '.png')
            f.write(img + ' ' + anno + '\n')
    print('generating ade20k val list success.')


if __name__ == '__main__':
    main()
