# ---------------------------------------------------------------------
# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

import torchvision.models as tv_models

from qai_hub_models.models._shared.deeplab.model import DeepLabV3Model
from qai_hub_models.utils.base_model import TargetRuntime

MODEL_ID = __name__.split(".")[-2]
MODEL_ASSET_VERSION = 2
DEFAULT_WEIGHTS = "COCO_WITH_VOC_LABELS_V1"


class DeepLabV3_ResNet50(DeepLabV3Model):
    """Exportable DeepLabV3_ResNet50 image segmentation applications, end-to-end."""

    @classmethod
    def from_pretrained(cls, weights: str = DEFAULT_WEIGHTS) -> DeepLabV3_ResNet50:
        model = tv_models.segmentation.deeplabv3_resnet50(weights=weights).eval()
        return cls(model)

    def get_hub_compile_options(
        self, target_runtime: TargetRuntime, other_compile_options: str = ""
    ) -> str:
        compile_options = super().get_hub_compile_options(
            target_runtime, other_compile_options
        )
        return compile_options + " --compute_unit gpu"

    def get_hub_profile_options(
        self, target_runtime: TargetRuntime, other_profile_options: str = ""
    ) -> str:
        profile_options = super().get_hub_profile_options(
            target_runtime, other_profile_options
        )
        return profile_options + " --compute_unit gpu"

    def forward(self, image):
        return super().forward(image)["out"]
