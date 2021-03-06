import numpy as np
from model.layers.layer import LayerType


def xavier_initialization(units, shape=None):
    if shape is None:
        shape = units
    stddev = np.sqrt(1 / np.prod(units))
    return np.random.normal(loc=0, scale=stddev, size=shape)


def he_initialization(units, shape=None):
    if shape is None:
        shape = units
    stddev = np.sqrt(2 / np.prod(units))
    return np.random.normal(loc=0, scale=stddev, size=shape)


class Metrics:
    def __init__(self):
        self.history = {}

    def update(self, loss, acc, dataset="train"):
        key = dataset + "_loss"
        if key not in self.history:
            self.history[key] = []
        self.history[key].append(loss)

        key = dataset + "_acc"
        if key not in self.history:
            self.history[key] = []
        self.history[key].append(acc)

    @staticmethod
    def metrics_log(loss, acc, text=None):
        print_loss = "{:.2}".format(loss)
        print_acc = "{:.2%}".format(acc)
        print(f"\n{text}: loss {print_loss} |  acc {print_acc}")

    @staticmethod
    def evaluate_model(dataset, labels, layers, loss_function):
        output = dataset
        for layer in layers:
            if layer.layer_type is not LayerType.DROPOUT:
                output = layer.forward(output)
            else:
                output = layer.forward(output, train=False)

        loss, acc, _ = loss_function.calculate(output, labels)

        return loss, acc

    @staticmethod
    def normalize_meanstd(a, axis=None):
        mean = np.mean(a, axis=axis, keepdims=True)
        std = np.sqrt(((a - mean) ** 2).mean(axis=axis, keepdims=True))
        return (a - mean) / std
