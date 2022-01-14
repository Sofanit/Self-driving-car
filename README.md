# Self-driving-car
## Project Description
- The aim of this project is to develop a self-driving car that can travel through a lane based on Deep learning approaches.
1. Introduction to Raspberry Pi-4 (Master branch)
    - Buzzer and Led
3. Lane keeping of autonomous car using Deep Learning
    - Data Collection
    - Training
    - Testing



## Data Collection 
- The first step of our project is to collect data. Therefore, we drove the car through the lane and saved the collected images based on three steering angles (45,90,135).


<img src="https://github.com/Sofanit/Self-driving-car/blob/main/lane_map.jpg" width="440"> </img>
## Data Processing
- After the data is collected, in order to make sure that the model learns to follow the line in the lane, we preprocessed the data to have a high contrast between the lane and the rest of the image.

<img src="https://github.com/Sofanit/Self-driving-car/blob/main/lane_proc.png" width="440"> </img>
## Model Architecture
➢ The preprocessed data is then fed into the model.

<img src="https://github.com/Sofanit/Self-driving-car/blob/main/Model_arch.png" width="440"> </img>


- The TensorFlow Lite converter takes a TensorFlow model and generates a TensorFlow Lite model (an optimized FlatBuffer format identified by the .tflite
file extension)
## Training result
<img src="https://github.com/Sofanit/Self-driving-car/blob/main/Training_res.png" width="440"> </img>
<img src="https://github.com/Sofanit/Self-driving-car/blob/main/Car_inlane.png" width="440"> </img>

## References
1. https://github.com/murtazahassan/Neural-Networks-Self-Driving-Car-Raspberry-Pi/tree/main/Step1-Data-Collection
