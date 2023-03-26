"""response models for voice cloning api"""
from pydantic import BaseModel
from typing import Optional, IO


# response class for main voice cloning functionality
class MainVoiceClone(BaseModel):
    """main voice cloning class"""
    output_file: IO

    class Config:
        arbitrary_types_allowed = True


class AudioInput(BaseModel):
    audio_file: str
