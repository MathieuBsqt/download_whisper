import sys

# Check if at least one command-line argument is provided
if len(sys.argv) !=2:
    print("Usage: python main.py <whisper_model_output_path>")
    print("Example: /workspace/whisper-model/")
    sys.exit(1)

# Check if the model path ends with '/'
model_path = sys.argv[1]
if not model_path.endswith('/'):
    model_path += '/'
  
### Download the model in a local directory - Specify the version you want to use in the first parameter
import whisper
model_id = 'large-v3'
model_path = f'{model_path}{model_id}'
# Available models = ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large']

# The whisper module’s load_model() method loads a whisper model in your Python application. You must pass the model name as a parameter to the load_model() method.
model = whisper.load_model(model_id, download_root=model_id)
