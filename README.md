# AI talks Neural Network Visualizer

<img src="AI talks screenshot.jpg" alt="AI talks screenshot" height="400">

The demo code in the recent "AI talks" video where we explained neural networks and their parameters. This code is built on top of `keras-visualizer` to allow you to easily create and visualize neural network architectures using Keras.

## Installation Instructions

### Step 1: Install Python 3.12.4
Download and install Python 3.12 from the [official Python website](https://www.python.org/downloads/release/python-3124/).

### Step 2: Install Graphviz
Download and install Graphviz from the [official Graphviz website](https://graphviz.org/download/). Make sure to add Graphviz to your system PATH during installation.

### Step 3: Add Python and Graphviz to PATH
Ensure that both Python and Graphviz are added to your system [PATH](https://www.itprotoday.com/windows-server/how-can-i-add-a-new-folder-to-my-system-path-).

### Step 4: Install Other Requirements
Open a terminal and run the following commands to install the necessary Python packages:
```sh
pip install keras tensorflow pandas keras-visualizer
```

### Step 5: Open the Jupyter Notebook
Navigate to the project directory and open the Jupyter Notebook `AI talks neural networks visualizer.ipynb`


### Step 6: Using the Neural Network Visualizer
Feel free to experiment with different layer types and configurations to suit your needs then run the cells

```python
from tensorflow.keras import models, layers
model = models.Sequential([
    layers.Input((3,)),
    layers.Dense(6, activation='softmax'),
    layers.Dense(8, activation='softmax'),
    layers.Dense(8, activation='softmax'),
    layers.Dense(6, activation='softmax'),
    layers.Dense(5, activation='softmax'),
    layers.Dense(1)
])
```

To learn more about the syntax and functionalities of Keras, refer to the [Keras documentation](https://keras.io/api/layers/)

### Happy learning! Click here to watch the [AI talks demo video](https://linktr.ee/omaralsharif)

<img src="AI talks screenshot.jpg" alt="AI talks screenshot" height="400">