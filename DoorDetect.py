import  time
from wia import Wia
from sense_hat import SenseHat

sense = SenseHat()

wia = Wia()
wia.access_token = "d_sk_yxhosMPKxwC9HIg2pZLxi4w3"

motion = sense.get_accelerometer_raw()


while True:
  #if accel data passes threshold
    #publish event to wia
  #motion=sense.get_accelerometer_raw()
  #print(motion)
  	x = motion['x']
	y = motion['y']
	z = motion['z']

	x = round(x, 2)
	y = round(y, 2)
	z = round(z, 2)

	print("x={0}, y={1}, z={2}".format(x, y, z))

        wia.Event.publish(name="door open test", data = motion)


	time.sleep(5)
