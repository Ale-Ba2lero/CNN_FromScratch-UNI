from model.layers.layer import Layer, LayerType
import numpy as np


class Softmax(Layer):

    def __init__(self):
        super().__init__()
        self.layer_type = LayerType.SOFTMAX

    def setup(self, input_shape: tuple) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        # subtract the max (prevent overflow)
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return probabilities

    def backpropagation(self, d_score: np.ndarray) -> np.ndarray:
        # in this implementation the Categorical Cross Entropy Loss function
        # already takes into account the softmax backpropagation
        return d_score
