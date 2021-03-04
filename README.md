### Anger Alarm

The project is a script that is primarily built for Gamers who are prone to rage. The projects analyses live camera feed to detect you facial expression and then predicts the emotion.

If the emotion is detected to be a negetive emotion the script plays an audio that might soothe the user.

## Getting Started

### Prerequisites

-   python >= 3.7.9
-   keras >= 2.4.3
-   tensorflow >= 2.3.1
-   opencv >= 4.4
-   numpy >= 1.18.5

### Installation:

1. Clone the repo

```sh
git clone https://github.com/naman-gupta99/Anger-alarm.git
```

2. Install required packages

-   Use [anaconda](https://www.anaconda.com/) to easily install keras and tensorflow in addition to necessary cuda drivers to run the model on GPU.

```sh
conda install tensorflow
conda install keras
```

-   Other packages can be easily installed using either pip or conda.

```sh
pip install numpy
pip install opencv
```

### Usage

-   Run the following command to run the program

```sh
python main.py
```

### Customization

-   To change the sound of the alert just add the .wav file of the audio to this folder

## Credits

-   https://github.com/onnx/models/tree/master/vision/body_analysis/emotion_ferplus
-   https://github.com/microsoft/onnxjs-demo
-   https://github.com/MahmoudSabra1/Facial-emotion-recognition
