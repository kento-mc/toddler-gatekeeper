import  time
from sense_hat import SenseHat

sense = SenseHat()

while True:
  motion=sense.get_accelerometer_raw()
  print(motion)
  time.sleep(1)
