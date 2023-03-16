from torchbenchmark.tasks import NLP
from torchbenchmark.util.framework.huggingface.model_factory import HuggingFaceModel

class Model(HuggingFaceModel):
    task = NLP.LANGUAGE_MODELING
    # Original train batch size per device: 8
    # Source: https://github.com/huggingface/transformers/blob/master/examples/flax/language-modeling/run_t5_mlm_flax.py#L83
    # Downscale to 4 because 8 doesn't fit on a single A100 40GB
    DEFAULT_TRAIN_BSIZE = 4
    # Original eval batch size per device: 8
    # Downscale to 1 to fit in Nvidia T4 of the infra
    DEFAULT_EVAL_BSIZE = 1
    
    def __init__(self, test, device, jit=False, batch_size=None, extra_args=[]):
        super().__init__(name="hf_T5_base", test=test, device=device, jit=jit, batch_size=batch_size, extra_args=extra_args)
