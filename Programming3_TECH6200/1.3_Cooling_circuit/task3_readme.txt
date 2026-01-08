Hello, 

To understand better this program please keep reading.

The best order to understand the code is: 
task3_sensor_client.py --> task3_server.py --> task3_solenoid_client.py

To test the code, first run the server and then run both clients.


Here there is a quick and raw schema of what you can find in each file.
It might help to understand what happens in every Loop Cycle (tick):


task3_sensor_client.py

	-Connects to server
	-Sends identity json message to server.
	-While loop:
		.Temperature simulation
			..cooling_on
			..cooling_off
		.Send temperature message.
		.Receives command message from server (for next temp. simulation)
		.Sleep Interval to slow down the loop repetition


task3_server.py

	-Creates server, threading possibility
	-Receives identity json message from sensor/solenoid
	-If sensor identity:
		.Save sensor socket and information
		.While loop:
			..if received data(not received data, break:
			....update data of barrel_Registry
			..calls process_temp method
	-elif solenoid identity:
		.Save solenoid socket and information
		.Send initial state to solenoid
		.Keeps connection with solenoid on

	-process_temp method:
		.Conditional to determine solenoid_state and command
		.log_event, write the solenoid activity in .txt file
		.Send command to sollenoid
		.Send command to sensor(change in temp.simulation)


task3_solenoid_client.py

	-Connects to server
	-Sends identityjson message to server
	-While loop:
		.Receives message
		.Prints State
		


