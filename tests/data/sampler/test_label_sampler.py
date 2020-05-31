from torchio.data import LabelSampler
from ...utils import TorchioTestCase


class TestLabelSampler(TorchioTestCase):
    """Tests for `LabelSampler` class."""

    def test_label_sampler(self):
        sampler = LabelSampler(5, 'label')
        next(iter(sampler(self.sample)))
