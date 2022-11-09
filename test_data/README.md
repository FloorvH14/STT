# Running inference

Using this directory, you can use the coqui stt to run inference and recognize English speech.

## Installation

Clone this git to your personal device. Check [here](https://code.visualstudio.com/docs/sourcecontrol/github) how to clone using Visual Studio Code or [https://www.folkstalk.com/tech/how-to-run-a-code-in-github-with-code-examples/] for a more general explanation. Make sure stt is installed (Coqui STT  1.4.0). You can do this by using the following command in the command line/terminal:

```bash
pip install stt
```
[Download](https://coqui.ai/english/coqui/v1.0.0-huge-vocab) the vocabulary (the .scorer file) for the model and save it in the directory test_data. The file is on the bottom of the page and can be downloaded by clicking on the name of the file.

Then, run the test.py file, either by running 
```bash
python test_data\test.py
```
in the terminal, or going to the file and manually running it.

If instead of cloning the directory you want to download the files, [create a python virtual environment] (https://docs.python.org/3/library/venv.html) and run the following in the command line:

```bash
python stt --model test_data/model.tflite --scorer test_data/huge-vocabulary.scorer --audio test_data/test.wav
```

Make sure that the path to the files and filenames correspond to the files and filenames on your computer.

In case you run into any other issues, check [here](https://stt.readthedocs.io/en/latest/DEPLOYMENT.html#download-models) for more detailed instrucions and documentions of stt. 

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

## result evaluation

The orginal text in test.wav is "hello, hello, this is a test". Although the transcription "no i do this is a test" is not perfect, it should be noted the first part of the text ("hello, hello") is of low quality. Therefore I think this is a very decent result.