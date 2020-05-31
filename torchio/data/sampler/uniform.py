from typing import Union, Sequence
import torch
from .weighted import WeightedSampler


class UniformSampler(WeightedSampler):
    """Randomly extract patches from a volume with uniform probability."""
    def __init__(self, patch_size: Union[int, Sequence[int]]):
        super().__init__(patch_size)

    def get_probability_map(self, sample):
        return torch.ones(sample.shape)
