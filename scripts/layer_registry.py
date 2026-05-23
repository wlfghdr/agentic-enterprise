#!/usr/bin/env python3
"""Helpers for reading the configurable layer registry."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).parent.parent.resolve()
LAYER_REGISTRY_PATH = REPO / "org" / "layers.yaml"


def load_layer_registry(path: Path | None = None) -> list[dict[str, Any]]:
    registry_path = path or LAYER_REGISTRY_PATH
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
    layers = data.get("layers")
    if not isinstance(layers, list) or not layers:
        raise ValueError(f"{registry_path.relative_to(REPO)}: missing non-empty 'layers' list")
    return sorted(layers, key=lambda layer: layer["order"])


def layer_ids(path: Path | None = None) -> list[str]:
    return [layer["id"] for layer in load_layer_registry(path)]


def layer_directories(path: Path | None = None) -> list[str]:
    return [layer["directory"] for layer in load_layer_registry(path)]


def layer_org_size_keys(path: Path | None = None) -> dict[str, str]:
    return {layer["id"]: f"{layer['id']}_layer" for layer in load_layer_registry(path)}
