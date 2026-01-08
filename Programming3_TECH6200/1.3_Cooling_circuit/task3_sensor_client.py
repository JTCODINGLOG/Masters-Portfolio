import socket
import json
# to send the data to the server in intervals of time
import time
# to simulate random temperatures
import random

# We create a BarrelSensorClient with the attributes needed to...
# ...create an object with methods that can simulate barrel temperatures,...
# ...connecting to the server, and send data according to the written logic.
# A unique characteristic of the sensor client: it only sends data to the server.
# Update: now it also receives data although, in real life it is as mentioned above.
# This change is due to, in this program, the temperature simulation is a...
# ...BarrelSensorClient method and, it needs updates about the solenoid status...
# ...to simulate the temperature in a better way
class BarrelSensorClient:
    def __init__(self, barrel_id, set_point, interval=2, cooling_on=False, host='localhost', port=9999):
        self.barrel_id = barrel_id
        self.set_point = set_point
        # The program starts with the set_point temperature
        self.current_temp = set_point
        # The interval between temperature messages sent
        self.interval = interval
        # The only purpose of this attribute is to help in temperature simulation.
        # When the solenoid opens, it will change to True and change the simulation to 'cooling mode'
        self.cooling_on = cooling_on
        # These attributes are needed to connect to the server
        # They can be modified but the default values will connect to our server.
        self.host = host
        self.port = port

    # Because we do not have real data provided by the sensor...
    # ...a recreation of a scenario is needed.
    # This function updates the current sensor temperature with...
    # ...a new random number that simulates a controlled variation...
    # ...of the current temperature.
    def simulate_temperature(self):
        # We want to see a random temp change that happens gradually
        # self.cooling_on will be set to True the moment the solenoid acts
        # When the cooling system is acting, the temperature tends to drop
        # The temperature needs to drop as result of the cooling circuit working
        # Returns a random number between -0.5 and 0
        # The -0.2 makes it drop in overall
        if self.cooling_on:
            change = random.uniform(-0.5, 0.0) -0.2
        # If the cooling is not acting, self.cooling_on is False:
        # The temperature needs to rise progressively in order to test our system
        # Returns a random number between -0.5 and 0.5
        # The 0.2 makes it rise in overall
        else:
            change = random.uniform(-0.4,0.5) + 0.3
        # Updating current temperature adding 'change' value
        # It is also rounded up to 2 decimals
        # The idea is that temperature does not go down in this case and...
        # ...self.set_point -1.5 applies that principle
        self.current_temp = round(max(self.set_point - 1.5, self.current_temp + change), 2)

    def run(self):
        # Creating a socket instance with the below parameters:
        # AF_INET is the internet address family for IPv4
        # SOCK_STREAM is implemented on the TCP protocol
        sensor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establishing connection with the server
        # 'host' and 'post' are the default values set in the attribute definitions
        # The parameters are 'localhost' and '9999', respectively for host and port.
        # These parameters are the host and port of our server.
        sensor_socket.connect((self.host, self.port))
        # In order to keep the sensor sending temperature data per interval we keep a...
        # ...small time out. Without this the sensor might stop sending temperature information...
        # ...until some information comes.
        # At the beginning the idea was that sensor client only sends information, but, to simulate...
        # ...temperature correctly, the sensor clients now receives information to see...
        # ...if solenoid status has changed, to update temperature simulation accordingly
        sensor_socket.settimeout(0.1)

        # Creating the variable data that will be sent to the server
        identity = {
            "type": "sensor",
            "barrel_id": self.barrel_id
        }
        # Sending the variable identity over the network to the server
        # '.sendall' guarantees that the entire byte message is sent...
        # ...but currently we have a dictionary that needs to be transformed into bytes:
        # 'json.dumps' converts the dictionary into a json string
        # This is just the standard format we are using for data transmission
        # 'encode('utf-8') converts the json string into bytes
        # Default value of '.encode()' is utf-8.
        sensor_socket.sendall(json.dumps(identity).encode('utf-8'))
        # This line was a quick fix. It looks like is a classic TCP thing.
        # The sensor sends the  temperature and the temperature very fast and the server...
        # ...receives them together, in one glued recv(). The server crashes when it receives...
        # ...extra data and then does not reply to the sensor with the 'command' message, then sensor...
        # ...effectuates a normal exit with code 0.
        # To fix it, this line of code will slowdown the code.
        #  This functionality was already used at the end of this file because I did not want the sensor...
        # ...to send data very often, but in this case it is a quick fix.
        time.sleep(0.1)

        # printing connection confirmation message
        print(f"-The sensor of the barrel #{self.barrel_id} is connected")

        # Now we execute the logic
        while True:
            self.simulate_temperature()
            # Creating the second block of data that will be sent to the server
            # Similar than it is previously done with the variable Identity
            # In this case we are sending to the server the information needed...
            # ...to execute the cooling logic and send an order to the solenoid
            message = {
                "barrel_id": self.barrel_id,
                "current_temp": self.current_temp,
                "set_point": self.set_point
            }
            sensor_socket.sendall(json.dumps(message).encode('utf-8'))
            print(f"Sent: Temperature = {self.current_temp}°C | Set point = {self.set_point}")

            # This step would not happen in the real project, it is just for temperature simulation matters
            # Here we check if the solenoid has been opened and update our attribute...
            # ...self.cooling_on to True or False
            # We use try because recv() within 0.1 second timeout might fail
            try:
                # Let's try to receive the message
                data = sensor_socket.recv(1024)
                if not data:
                    # Server is closed
                    return
                # Formatting the data to compare later with 'OPEN' or 'CLOSE'
                command = data.decode("utf-8").strip().upper()
                # Validating that we have received the correct data
                if command in ("OPEN", "CLOSE"):
                    # If the received command message is OPEN, it adds True to the attribute cooling.on
                    self.cooling_on = (command == "OPEN")
            # if no data arrives within the 0.1 timeout then we keep going
            except socket.timeout:
                pass

            # Slowing down the repetition of the loop thanks to this function
            # Later on, we can set the 'interval' to see how often the sensor...
            # ...runs the while loop again and provides temperature information...
            # ...to the server.
            # The bigger is the barrel, the longer can be the interval because...
            # ...a big volume of water will take more time in changing the temperature
            time.sleep(self.interval)

if __name__ == "__main__":
    # Here we create a 'BarrelSensor' object with the following parameters:
    # -Barrel_id
    # -Set_point for the brew
    # -Interval of temperature check (seconds)
    # -Host: default server host (localhost)
    # -Port: default server port (9999)
    # It can be changed with the purpose of testing the program
    sensor = BarrelSensorClient(barrel_id=1, set_point=13.0, interval=10)
    # We call the 'run' method which is the one implementing the logic of the sensor
    sensor.run()


