from .weighted import WeightedSampler


class LabelSampler(WeightedSampler):
    r"""Extract random patches containing labeled voxels.

    This iterable dataset yields patches whose center value is greater than 0
    in the :py:attr:`label_name`.

    Args:
        patch_size: Tuple of integers :math:`(d, h, w)` to generate patches
            of size :math:`d \times h \times w`.
            If a single number :math:`n` is provided,
            :math:`d = h = w = n`.
        label_name: Name of the label image in the sample that will be used to
            generate the sampling probability map.
    """
    def __init__(self, patch_size, label_name):
        super().__init__(patch_size, label_name)

    def get_probability_map(self, sample, probability_map_name):
        """Return binarized image."""
        if probability_map_name in sample:
            data = sample[probability_map_name].data > 0.5
        else:
            message = (
                f'Image "{probability_map_name}"'
                f' not found in subject sample: {sample}'
            )
            raise KeyError(message)
        return data
