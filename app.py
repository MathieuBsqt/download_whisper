import numpy as np
import streamlit as st
import torch 
import whisper


# Define Device (CPU/GPU)
device = "cuda" if torch.cuda.is_available() else "cpu"

### get saved model.pt file path
model_path = f'{download_root}/{model_id}.pt'

# Load model on available device
model = whisper.load_model(model_path, device=device)

# Display parameters in the app's logs
print(
    f"Model will be run on {device}\n"
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)

def main():
    st.title("Whisper Large-v3 Speech-to-Text Transcription")

    # Upload audio file
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if audio_file:
        st.audio(audio_file, format='audio/wav')

        # Transcribe audio on button click
        if st.button("Transcribe"):
            transcription = transcribe_audio(audio_file)
            st.subheader("Transcription:")
            st.write(transcription)

if __name__ == "__main__":
    main()
