import os
# run the English language model using the test.wav file
os.system('stt --model test_data/model.tflite --scorer test_data/huge-vocabulary.scorer --audio test_data/test.wav')