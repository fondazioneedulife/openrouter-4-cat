from typing import List, Optional, Type
from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, ConfigDict, SecretStr
from datetime import datetime, date
from cat.factory.llm import LLMSettings
from langchain.chat_models import ChatOpenAI as OpenRouter

class OpenRouterConfig(LLMSettings):

    openai_api_key: Optional[SecretStr]
    openai_api_base: Optional[str]
    model: Optional[str]
    max_tokens: Optional[int] = 300
    temperature: Optional[float] = 0.1
    streaming: bool = True

    _pyclass: Type = OpenRouter

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