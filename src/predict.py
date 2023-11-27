import datetime
from tqdm import tqdm
from faster_whisper import WhisperModel

MODEL_DIR = '/workspace/models/faster-whisper-large-v3'
DEVICE = 'gpu'
COMPUTE_TYPE = 'float16'

''' Initialise model '''
if DEVICE == 'cpu':
    model = WhisperModel(MODEL_DIR, device="cpu")
elif DEVICE == 'gpu' or DEVICE == 'cuda':
    # Run on GPU with FP16
    model = WhisperModel(MODEL_DIR, device="cuda", compute_type=COMPUTE_TYPE)
else:
    raise f'No device called {DEVICE}'

def convert_sec(seconds: int) -> str:
    return str(datetime.timedelta(seconds = seconds))

def transcribe(audio_path: str) -> str:

    transcript = ''

    segments, _ = model.transcribe(audio_path, language='en')
    for segment in tqdm(segments):
        start = convert_sec(int(segment.start))
        end = convert_sec(int(segment.end))
        transcript += f'[{start} -> {end}] {segment.text}\n'

    return transcript

if __name__ == '__main__':
    print(transcribe('test.wav'))
