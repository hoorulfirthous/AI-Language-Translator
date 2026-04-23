import whisper
import tempfile

def load_model():
    return whisper.load_model("base")


def speech_to_text(audio_bytes, model):
    try:
        # Save audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        # Transcribe using Whisper
        result = model.transcribe(temp_audio_path)
        return result["text"]

    except Exception:
        return None