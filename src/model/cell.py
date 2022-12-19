""" PSPNet loss function """
from mindspore import nn
from src.utils.aux_loss import SoftmaxCrossEntropyLoss


class Aux_CELoss_Cell(nn.Cell):
    """ loss """
    def __init__(self, num_classes=21, ignore_label=255):
        super(Aux_CELoss_Cell, self).__init__()
        self.num_classes = num_classes
        self.loss = SoftmaxCrossEntropyLoss(self.num_classes, ignore_label)

    def construct(self, net_out, target):
        """ the process of calculate loss """
        if len(net_out) == 2:
            predict_aux, predict = net_out
            CE_loss = self.loss(predict, target)
            CE_loss_aux = self.loss(predict_aux, target)
            loss = CE_loss + (0.4 * CE_loss_aux)
            return loss
        return self.loss(net_out, target)
