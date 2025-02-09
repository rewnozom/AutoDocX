# src/model/__init__.py
"""
Model package - Innehåller moduler för hantering av LLM-modeller och deras konfigurationer.
Här ingår:
  - llm_models: Definierar interface och implementationer för olika LLM providers.
"""

from .llm_models import llm_manager, ModelProvider

__all__ = ['llm_manager', 'ModelProvider']