FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    libvlc-dev \
    libvlccore-dev \
    vlc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    git+https://github.com/openai/whisper.git \
    torch \
    torchvision \
    torchaudio \
    gTTS \
    python-vlc

WORKDIR /app

COPY verbal.py .

CMD ["python", "verbal.py"]
