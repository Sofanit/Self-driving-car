# Self-driving-car
Raspberry pi 4
## The aim of this project is to develop self-driving car that can travel through the following lane based on deep learning approaches.

<img src="https://github.com/Sofanit/Self-driving-car/blob/buzzer/lane_map.jpg" width="440"> </img>

## Data Collection 
➢ The first step of our project is to collect data. Therefore, we drove the car through the lane and saved the collected images based on three steering angles (45,90,135).
## Data Processing
- After the data is collected, in order to make sure that the model learns to follow the line in the lane, we preprocessed the data to have a high contrast between the lane and the rest of the image.

## Model Architecture
➢ The preprocessed data is then fed into the model.

<img src="https://github.com/Sofanit/Self-driving-car/blob/buzzer/Model_arch.png" width="440"> </img>


- The TensorFlow Lite converter takes a TensorFlow model and generates a TensorFlow Lite model (an optimized FlatBuffer format identified by the .tflite
file extension)
## Training result
<img src="https://github.com/Sofanit/Self-driving-car/blob/buzzer/Training_res.png" width="440"> </img>
<img src="https://github.com/Sofanit/Self-driving-car/blob/buzzer/Car_inlane.png" width="440"> </img>