## Setup instructions for doing screen capture facial expression recognition via OBS virtual camera from desktop video grid

This is a modified version of the Facial-Expression-Recognition demo, with the following added features:

- detect multiple faces and run the same emotional predictions each face
- emit the probabilities as OSC message to an endpoint

NOTE: in Windows the built in OBS virtual camera doesn't work, and [this plugin](https://github.com/CatxFish/obs-virtual-cam) is needed

#### Setup:

- Install Python 3.7 environment (ideally venv, but could be site wide install)
- update pip `python -m pip install –upgrade pip`
- run `python setup.py install` to install dependencies
- run `pip install opencv-python` to install opencv separately (doesn't install properly with setup.py above)
- run `python main.py`

#### Configuration:

- `demo.py` has configuration settings OSC IP address and port, and video device index (set to OBS virtual cam)
```
OSC_IP = "127.0.0.1"
OSC_PORT = 7000
VID_DEVICE_IDX = 1
```
original documentation follows

---

![amazing](./amazingkelly.jpeg)

Opensource deep learning framework [TensorFlow](https://www.tensorflow.org) is used in **Facial Expression Recognition(FER)**. 
The trained models achieved 65% accuracy in fer2013. If you like this, please give me a star.

#### Dependencies

FER requires:
- Python (>= 3.3)
- TensorFlow (>= 1.1.0) [Installation](https://www.tensorflow.org/install/)
- OpenCV (python3-version) [Installation](http://docs.opencv.org/master/da/df6/tutorial_py_table_of_contents_setup.html)

Only tested in Ubuntu and macOS Sierra. Other platforms are not sure work well. When problems meet, open an issue, I'll do my best to solve that.

#### Usage
###### demo
To run the demo, just type:
```shell
python3 main.py
```
Then the program will creat a window to display the scene capture by webcamera. You need press <kbd>SPACE</kbd> key to capture face in current frame and recognize the facial expression.

If you just want to run this demo instead of training the model from scaratch, the following content can be skipped.

###### train models
If you want to train a model from scaratch by yourself, download the fer2013 datasets in [kaggle(91.97MB)](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data). Then extract the data to `data/fer2013` folder.

It's is import that modifying the `MODE`(in `main.py`) from `demo` to `train`  before you start training.
Then type:
```shell
python3 main.py
```

#### Issues & Suggestions
If any issues and suggestions to me, you can create an [issue](https://github.com/xionghc/Facial-Expression-Recognition/issues/).
