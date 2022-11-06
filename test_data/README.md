# Running inference

Using this directory, you can use the coqui stt to run inference and recognize English speech.

## Installation

Clone this git to your personal device.
[Download](https://coqui.ai/english/coqui/v1.0.0-huge-vocab) the vocabulary (the .scorer file) for the model and save it in the directory test_data.

## Usage

Run test.py in the test_data directory. A .wav file is provided. If you want to use your own audio, make sure to upload a 16000 Hz file, or install [SoX](https://sox.sourceforge.net/).