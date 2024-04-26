from typing import List, Optional, Type

from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, ConfigDict, SecretStr
from datetime import datetime, date
from cat.factory.llm import LLMSettings
from langchain_anthropic import OpenAI

class OpenRouterConfig(LLMSettings):
    openrouter_api_key: Optional[SecretStr]
    openrouter_base_url: Optional[str]
    modelName: Optional[str]
    max_tokens: Optional[int] = 300
    temperature: Optional[float] = 0.7
    streaming: Optional[bool] = True

    _pyclass: Type = OpenAI

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "OpenRouter.ai",
            "description": "Setup for OpenRouter.ai",
            "link": "https://openrouter.ai/",
        }
    )

@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(OpenRouterConfig)
    return allowed