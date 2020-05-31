from ..utils import TorchioTestCase
from torchio.data import LabelSampler


class TestLabelSampler(TorchioTestCase):
    """Tests for `LabelSampler` class."""

    def test_label_sampler(self):
        sampler = LabelSampler(5, 'label')
        next(iter(sampler(self.sample)))
