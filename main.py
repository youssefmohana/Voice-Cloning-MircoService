# main api endpoints
from fastapi import FastAPI, BackgroundTasks, Request, UploadFile, File,Response, APIRouter
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from schemas.response_schemas import MainVoiceClone, AudioInput
from typing import IO, Any, List
import base64
import io
from pydub import AudioSegment
import wave
from config import settings
import io
import soundfile as sf
import numpy as np
from core.runner import synthesize_speech
router = APIRouter(
    prefix=f"{settings.BASE_URL}",
    tags=["Train Embedding on Custom Voice"],
)
app = FastAPI()





@app.post("/encode_audio")
async def encode_audio(audio_file: UploadFile = File(...)):
    print(audio_file.file.read)
    encoded_audio =  base64.b64encode(bytes(audio_file.file.read()))
    return {"encoded_audio": encoded_audio, "headers": {"Content-Disposition": "attachment;filename=audio.wav"} ,"media_type": "audio/WAV"}

@app.post("/decode_audio")
async def decode_audio(encoded_audio: dict):
    # Decode the base64 data
    decoded_data =base64.b64decode(encoded_audio["encoded_audio"])
    wav_file = open("temp.wav", "wb")
    wav_file.write(decoded_data)
    return StreamingResponse(io.BytesIO(decoded_data), media_type="audio/WAV")



@app.post("/VoiceCloning")
async def decode_audio(txt : str  , encoded_audio: dict):
    # Decode the base64 data
    decoded_data =base64.b64decode(encoded_audio["encoded_audio"])
    sound, sample_rate = sf.read(io.BytesIO(decoded_data))
    generated_wav, tsample_rate = synthesize_speech(sound,txt)
    # Output as memory file
    file_format = "WAV"
    memory_file = io.BytesIO()
    memory_file.name = "generated_audio.wav"
    sf.write(memory_file, generated_wav.astype(np.float32), tsample_rate, format=file_format)
    encoded_audio = base64.b64encode(bytes(memory_file.getvalue()))
    wav_file = open("temp1.wav", "wb")
    wav_file.write(memory_file.getvalue())
    return {"encoded_audio": encoded_audio, "headers": {"Content-Disposition": "attachment;filename=audio.wav"},
            "media_type": "audio/WAV"}


@app.post("/train-embedding-on-custom-voice")
async def train_embedding_on_custom_voice(txt : str ,audio: bytes = File(...)):
    """Trains TTS Embedding on custom voice input.

    Args:
        Input: Audio File.

    Returns:
        Output: Bytes.
    """

    audio_file, sample_rate = sf.read(io.BytesIO(audio))

    generated_wav, tsample_rate = synthesize_speech(audio_file,txt)

    # Output as memory file
    file_format = "WAV"
    memory_file = io.BytesIO()
    memory_file.name = "generated_audio.wav"
    sf.write(memory_file, generated_wav.astype(np.float32), tsample_rate, format=file_format)
    encoded_audio = base64.b64encode(bytes(memory_file.getvalue()))
    wav_file = open("temp2.wav", "wb")
    wav_file.write(memory_file.getvalue())
    return {"encoded_audio": encoded_audio, "headers": {"Content-Disposition": "attachment;filename=audio.wav"},
            "media_type": "audio/WAV"}

