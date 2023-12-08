### Download the model in a local directory - Specify the version you want to use in the first parameter
import whisper
model_id = 'large-v3'
# Available models = ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large']

# The whisper module’s load_model() method loads a whisper model in your Python application. You must pass the model name as a parameter to the load_model() method.
model = whisper.load_model(model_id, download_root=model_id)
