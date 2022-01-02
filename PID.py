import matplotlib.pyplot as plt
import numpy as np
from simple_pid import PID

debug = True


pid = PID(Kp=0.1, Ki=55, Kd=0.00020, setpoint=0, sample_time=(1/10000))

rangeMax = 10000
current_value = 0
output = []
target = []

for i in range(0,rangeMax,1):
	output.append(pid(current_value))
	current_value = output[i]
	if i == 1000:
		pid.setpoint = 35
	elif i == 6000:
		pid.setpoint = 10
	target.append(pid.setpoint)
	if debug == True:
		print("set point: " + str(pid.setpoint))
		print("current value: " + str(current_value))
		print("output value: " + str(output[i]))

xpoints = range(0,rangeMax,1)

plt.plot(xpoints, output)
plt.plot(xpoints, target)
plt.show()

# for i in range(0, rangeMax - 1, 1):
# 	output[i] = PID(current_value[i])
# 	current_value[i] = output[i]
# 	if i == 150:
# 		pid.setpoint = 10

# xpoints = range(0 , rangeMax , 1)
# plt.plot(xpoints, output)
# plt.show()