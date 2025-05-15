import whisper

model = whisper.load_model("base")

tasks = [
    "lave a louça",
    "arrume minha cama",
    "varra a casa",
    "limpe a escada"
]

for task in tasks:
    audio_file = f"{task.replace(' ', '_')}.mp3"
    result = model.transcribe(audio_file, fp16=False)
    texto = result["text"].strip().lower()

    # decide
    if texto == "limpe a escada":
        print(f"Tarefa: «{texto}» → não faço")
    else:
        print(f"Tarefa: «{texto}» → faço")
