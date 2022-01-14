# Self-driving-car
## Raspberry pi 4 ~ Control Buzzer and Led

### GPIO Mappings
- **LED**
  - LED1 = GPIO26
  - LED2 = GPIO16
  - LED3 = GPIO20
  - LED4 = GPIO21
- **Buzzer**
  - Buzzer = GPIO12
- **Motor**
  - PWMA = GPIO18
  - PWMB = GPIO25
  - AIN2 = GPIO27
  - AIN1 = GPIO22
  - BIN2 = GPIO24
  - BIN1 = GPIO23
 ### AI car ~ Buzzer

<img align="center" src="https://github.com/Sofanit/Self-driving-car/blob/buzzer/BUZZ.png" width="440"> </img>
### The mini-project consists of two parts
1. Playing the famous Korean song ARIRANG with the piezo buzzer
- Change musical notes to their corresponding frequencies 

~~~ 
D4","E4","D4","E4","G4","A4","G4","A4","B4","A4","B4","G4","E4","D4"," 
E4","D4","E4","G4","A4","G4","A4","B4","A4","G4","E4","D4","E4","G4","
A4","G4","D5","D5","D5","B4","A4","B4","A4","B4","G4","E4","D4","E4","
D4","E4","G4","A4","G4","A4","B4","A4","G4","E4","D4","E4","G4","A4","
G4","G4"
~~~
<h3 align="center" style="color:blue;">⬇</h3>

~~~
294, 330, 294, 330, 392, 440, 392, 440, 440, 494, 392, 330, 294, ... 
~~~
- Rewrite the musical note in such a way that it represents the melody.
~~~
"D4","P","P","E4","D4","E4","G4","P","P","A4","G4","A4","B4","P","P","A4","B4" 
~~~
   - "P" represents a break. At this point the buzzer will not make any sound and the LED will be off.
   - The rest of the musical notes represent different sounds. At these points,the buzzer will make a sound  
      corresponding to specific frequencies and the LED will be ON. Checkout the details in buzz.py and playsong.py
      
  <img src="https://github.com/Sofanit/Self-driving-car/blob/buzzer/led.png" width="440"> </img>

2. Create a simple keyboard and compose our own melody with the buzzer.
- We used a simple interface built using tkinter. Checkout the details in Piano.py.


## References

1. https://roboindia.com/tutorials/raspberry-buzzer/
2. http://www.sengpielaudio.com/calculator-notenames.htm
3. https://en.wikipedia.org/wiki/Arirang






