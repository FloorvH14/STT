import os
os.system('stt --model test_data/model.tflite --scorer test_data/huge-vocabulary.scorer --audio test_data/test.wav')