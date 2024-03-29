# coding=utf-8
# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Yixtral model configuration"""

from transformers.configuration_utils import PretrainedConfig
from transformers.utils import logging


logger = logging.get_logger(__name__)

YIXTRAL_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "Crystalcareai/Yixtral-Test": "https://huggingface.co/Crystalcareai/Yixtral-Test/resolve/main/config.json",
}


class YixtralConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`YixtralModel`]. It is used to instantiate a Yixtral
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the Yixtral-Test.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 64000):
            Vocabulary size of the Yixtral model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`YixtralModel`]
        hidden_size (`int`, *optional*, defaults to 4096):
            Dimension of the hidden representations.
        intermediate_size (`int`, *optional*, defaults to 11008):
            Dimension of the MLP representations. 
        num_hidden_layers (`int`, *optional*, defaults to 48):
            Number of hidden layers in the Transformer decoder.
        num_attention_heads (`int`, *optional*, defaults to 32):
            Number of attention heads for each attention layer in the Transformer decoder.
        num_key_value_heads (`int`, *optional*, defaults to 4):
            This is the number of key_value heads that should be used to implement Grouped Query Attention. If
            `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if 
            `num_key_value_heads=1 the model will use Multi Query Attention (MQA) otherwise GQA is used.
        hidden_act (`str` or `function`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the decoder.
        max_position_embeddings (`int`, *optional*, defaults to 262144):
            The maximum sequence length that this model might ever be used with. 
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        rms_norm_eps (`float`, *optional*, defaults to 1e-6):
            The epsilon used by the rms normalization layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        pad_token_id (`int`, *optional*, defaults to 0):
            Padding token id.
        eos_token_id (`int`, *optional*, defaults to 2):
            End of stream token id.
        bos_token_id (`int`, *optional*, defaults to 1):
            Beginning of stream token id.  
        tie_word_embeddings (`bool`, *optional*, defaults to `False`):
            Whether to tie weight embeddings
        rope_theta (`float`, *optional*, defaults to 10000000.0):
            The base period of the RoPE embeddings.
        attention_bias (`bool`, defaults to `False`, *optional*, defaults to `False`):
            Whether to use a bias in the query, key, value and output projection layers during self-attention.  
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        num_experts_per_tok (`int`, *optional*, defaults to 2):
            The number of experts used in the sparse mixture of experts layer.
        num_local_experts (`int`, *optional*, defaults to 4):
            The number of local experts used in the sparse mixture of experts layer.
        router_aux_loss_coef (`float`, *optional*, defaults to 0.001):
            The coefficient for the auxiliary loss of the router.
        output_router_logits (`bool`, *optional*, defaults to `False`):
            Whether or not to output the logits of the routers.

    ```python
    >>> from transformers import YixtralModel, YixtralConfig

    >>> # Initializing a Yixtral Yixtral-Test style configuration
    >>> configuration = YixtralConfig() 

    >>> # Initializing a model from the Yixtral-Test style configuration
    >>> model = YixtralModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = "Yixtral"
    keys_to_ignore_at_inference = ["past_key_values"]

    def __init__(
        self,
        vocab_size=64000,
        hidden_size=4096,
        intermediate_size=11008,
        num_hidden_layers=48,
        num_attention_heads=32,  
        num_key_value_heads=4,
        hidden_act="silu",
        max_position_embeddings=262144,
        initializer_range=0.02,
        rms_norm_eps=1e-6,
        use_cache=True,
        pad_token_id=0,
        eos_token_id=2,
        bos_token_id=1,
        tie_word_embeddings=False,
        rope_theta=10000000.0,
        attention_bias=False,
        attention_dropout=0.0,
        num_experts_per_tok=2,
        num_local_experts=4, 
        router_aux_loss_coef=0.001,
        output_router_logits=False,
        **kwargs,
    ):
        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.hidden_size = hidden_size  
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.num_key_value_heads = num_key_value_heads
        self.hidden_act = hidden_act
        self.initializer_range = initializer_range
        self.rms_norm_eps = rms_norm_eps
        self.use_cache = use_cache
        self.rope_theta = rope_theta
        self.attention_bias = attention_bias
        self.attention_dropout = attention_dropout
        self.num_experts_per_tok = num_experts_per_tok  
        self.num_local_experts = num_local_experts
        self.router_aux_loss_coef = router_aux_loss_coef
        self.output_router_logits = output_router_logits

        super().__init__(
            pad_token_id=pad_token_id,
            bos_token_id=bos_token_id, 
            eos_token_id=eos_token_id,
            tie_word_embeddings=tie_word_embeddings,
            **kwargs,
        )