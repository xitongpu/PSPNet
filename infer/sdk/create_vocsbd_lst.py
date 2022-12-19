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
    voc_img_dir = os.path.join(data_dir, 'img')
    voc_anno_gray_dir = os.path.join(data_dir, 'gray')
    voc_train_txt = os.path.join(data_dir, 'train.txt')
    voc_val_txt = os.path.join(data_dir, 'val.txt')
    voc_train_lst_txt = os.path.join(data_dir, 'voc_train_lst.txt')
    voc_val_lst_txt = os.path.join(data_dir, 'voc_val_lst.txt')

    voc_train_data_lst = _get_data_list(voc_train_txt)
    with open(voc_train_lst_txt, mode='w') as f:
        for id_ in voc_train_data_lst:
            id_ = id_.strip()
            img_ = os.path.join(voc_img_dir, id_ + '.jpg')
            anno_ = os.path.join(voc_anno_gray_dir, id_ + '.png')
            f.write(img_ + ' ' + anno_ + '\n')
    print('generating voc train list success.')

    voc_val_data_lst = _get_data_list(voc_val_txt)
    with open(voc_val_lst_txt, mode='w') as f:
        for id_ in voc_val_data_lst:
            id_ = id_.strip()
            img_ = os.path.join(voc_img_dir, id_ + '.jpg')
            anno_ = os.path.join(voc_anno_gray_dir, id_ + '.png')
            f.write(img_ + ' ' + anno_ + '\n')
    print('generating voc val list success.')


if __name__ == '__main__':
    main()
