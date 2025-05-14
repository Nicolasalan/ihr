from gtts import gTTS
import whisper

tts = gTTS('Olá, como posso te ajudar?', lang ="pt",)
tts.save('hello.mp3')
model = whisper.load_model("base")
result = model.transcribe("hello.mp3", fp16=False)
print(result["text"])
