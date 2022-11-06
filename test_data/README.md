# Running inference

Using this directory, you can use the coqui stt to run inference and recognize English speech.

## Installation

Clone this git to your personal device.
[Download](https://coqui.ai/english/coqui/v1.0.0-huge-vocab) the vocabulary (the .scorer file) for the model and save it in the directory test_data.

## Usage

Run test.py in the test_data directory. A .wav file is provided. If you want to use your own audio, make sure to upload a 16000 Hz file, or install [SoX](https://sox.sourceforge.net/).

When succesful, the output should look like this:

```bash
Loading model from file model.tflite
TensorFlow: v2.9.1-11-gf8242ebc005
 Coqui STT: v1.4.0-0-gfcec06bd
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Loaded model in 0.0236s.
Loading scorer from files huge-vocabulary.scorer
Loaded scorer in 0.15s.
Running inference.
no i do this is a test
Inference took 4.796s for 5.759s audio file.
```