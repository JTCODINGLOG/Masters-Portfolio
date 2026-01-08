# The idea of the application comes from a friend's project with a cellar.
# In this project it is necessary to configure the cooling system that...
# ...acts on the different barrels of the cellar.
# I understood that the concept of client and server can be applied to the IoT...
# ...and that could be applied to the task3 of the Assessment 1 TECH6200

# Understanding the system:
# 1 server. This server would be connected to the switchboard.
# 1st client type: The temperature sensors of the barrel.
# 2nd client type: The solenoids that open and close the cooling system.
# Sensor regularly sends information to the server.
# Server interprets that information applying the following logic:
# If temperature of barrel is 1.5 degrees above set temperature (ideal temp):
#   Open solenoid and let chill water enter the circuit to cool barrel.
# When temperature of barrel comes back to the set temperature (ideal temp):
#   Close solenoid which stops cooling circuit from acting.
# Solenoid statis information is sent to the sensor too for temperature simulation purposes.

# 'socketserver' will help specially with the multithreading activity
import socketserver
# The transmitted data will be decoded into Json format
import json
# Importing datetime to add additional information to the history
from datetime import datetime

# Container dictionary to track every barrel
barrel_reg = {}
# File where we will load the information
LOG_FILE = "cellar_cooling_system.txt"


class BarrelRequestHandler(socketserver.BaseRequestHandler):
    # The 'handle' method focusses on requesting information from both...
    # ...clients, using it to populate the 'barrel_reg' dictionary container.
    # Then, it 'redirects' the code if the client type is sensor or...
    # ...keeps the connection open if it is a solenoid.
    def handle(self):
        try:
            # Receiving 1024 bytes of data from client
            # This is the first message sent in the client code...
            # ...that was originally a dictionary with 'type' and 'barrel_id' keys
            # It will help us to know which client is the sender(type)...
            # ...and what is the barrel of the client(barrel_id).
            c_data_utf = self.request.recv(1024).strip()
            # Changing data format: from utf-8 to .json
            c_data_json = json.loads(c_data_utf.decode('utf-8'))

            # As we have several clients, we need to determine the type
            c_type = c_data_json.get("type")
            # Getting 'barrel_id' to add later to execute below barrel...
            # ...registration logic
            barrel_id = c_data_json.get("barrel_id")

            # Creating a log for the barrel if it is not registered yet
            if barrel_id not in barrel_reg:
                barrel_reg[barrel_id] = {
                    # For this key, the value will be a socket server-sensor
                    "sensor": None,
                    "current_temp": None,
                    "set_point": None,
                    # For this key, the value will be a socket server-solenoid
                    "solenoid": None,
                    "solenoid_open": False
                }

            # Now we implement different logic based on the type of client
            # Solenoid usability depends on sensor data. When we run the code,...
            # ...first we should receive sensor client data, that is one of the reasons...
            # ...why we write logic for sensor client before logic for solenoid client
            # This is also more efficient because sensor sends data continuously...
            # ...but the solenoid is only called when there is a significant change...
            # ...in the temperature. This means, that the probability of sensor interaction...
            # ...is higher, constant, frequent, but the solenoid interaction does not have to be...
            # ...constant or frequent, but 'random' and lower than sensor interaction...
            # In this program temperature depends on a simple simulation, but...
            # ...in real life there are many factors that affect the barrel temperature,...
            # ...and solenoids are subject to these significant changes unlike sensors,
            # ...that always send temperature information even if it does not change.
            if c_type == "sensor":
                print(f"-Sensor connected for Barrel #{barrel_id}")
                # Storing 'self.request' which is the socket object assigned by socketserver...
                # ...for this connection inside "barrel_reg/barrel_id/sensor"
                barrel_reg[barrel_id]["sensor"] = self.request

                # The sensor temperature is monitored continuously.
                while True:
                    # Limiting the data received
                    s_data_utf = self.request.recv(1024).strip()
                    # Quick data validation
                    if not s_data_utf:
                        break

                    try:
                        # Handling received data
                        s_data_json = json.loads(s_data_utf.decode("utf-8"))
                        # Requesting specific data from the client
                        # The current temperature is generated and simulated...
                        # ...in the sensor client
                        current_temp = s_data_json.get("current_temp")
                        # The set point is also specified in the sensor client
                        # Each barrel might have a different set point depending on the brew
                        set_point = s_data_json.get("set_point")

                        # Updating barrel registry data
                        barrel_reg[barrel_id]["current_temp"] = current_temp
                        barrel_reg[barrel_id]["set_point"] = set_point

                        # 'process_temperature' is a method from the server main class...
                        # ... defined below, after the handle method.
                        # It is called when the temperature reading is received from a sensor
                        self.process_temp(barrel_id)

                    except json.JSONDecodeError:
                        print("Invalid JSON file from sensor.")

            elif c_type == "solenoid":
                print(f"-Solenoid connected for barrel #{barrel_id}")
                # Storing 'self.request' which is the socket object assigned by socketserver...
                # ...for this connection inside "barrel_reg/barrel_id/solenoid"
                barrel_reg[barrel_id]["solenoid"] = self.request

                # We send an initial state to the solenoid because the idea is that...
                # ...initially the solenoid is closed because we part from a barrel temperature...
                # ...equals to the barrel set temperature
                # Therefore, in fresh starts of the program, solenoid client receives 'CLOSE'...
                # ...but if solenoid is reconnecting while server is open, solenoid client receives 'OPEN'
                state = "OPEN" if barrel_reg[barrel_id]["solenoid_open"] else "CLOSE"
                # sending message to solenoid client
                self.request.sendall(state.encode('utf-8'))

                # Maintain the solenoid alive although the only data received from...
                # ...the solenoid is about 'barrel_id' and 'type'.
                # Without the loop the server would just accept one message in every connection...
                # ...and it would be necessary to reconnect for solenoid changes
                # The connection will be closed from the client side if...
                # ...the server does not respond to this received message.
                while True:
                    s_data_utf = self.request.recv(1024)
                    if not s_data_utf:
                        break

            else:
                print("Unknown client type")

        except Exception as issue:
            print(f"Error: {issue}")

        print(f"-Disconnected: {self.client_address}")

    # Method were the process regarding temperature is defined
    def process_temp(self, barrel_id):
        # It has been preferred to create variables with different names than outer scope...
        # ...to make it more understandable and simpler
        # This barrels are populated thanks to the dictionary 'barrel_reg'...
        # ...that has been previously populated in the method 'handle'
        barrel = barrel_reg[barrel_id]
        temp = barrel["current_temp"]
        setp = barrel["set_point"]
        solop = barrel["solenoid_open"]

        # If there is not temperature (it should be a temperature log) we end the program
        if temp is None or setp is None:
            return

        # This variable 'command' will be populated and send later to the solenoid client
        command = None

        # Applying some process logic
        # If temperature is higher than we declare with the set point temperature
        if temp > setp + 1.5:
            # If solenoid is closed
            if not solop:
                # Open solenoid and cool down the barrel
                barrel["solenoid_open"] = True
                # Populate the variable 'command' or change it based on solenoid action
                command = "OPEN"
                # We call the method 'log_event' with these attributes...
                # ...to register info about the cool circuit being opened by the solenoid
                self.log_event(barrel_id, command, temp, setp)
        # If temperature has reached or gone under set_point
        elif temp <= setp:
            # If solenoid is opened
            if solop:
                # Close solenoid and stop the cooling system for that barrel
                barrel["solenoid_open"] = False
                # Populate the variable 'command or change it based in solenoid action
                command = "CLOSE"
                # We call the method 'log_event' with these attributes
                # ...to register info about the cool circuit being closed by the solenoid
                self.log_event(barrel_id, command, temp, setp)

        # If there is an action taken by the solenoid the command is sent to the solenoid
        if command:
            solenoid_socket = barrel.get("solenoid")
            if solenoid_socket:
                try:
                    solenoid_socket.sendall(command.encode("utf-8"))
                except Exception as issue:
                    print(f"Command was not send to solenoid of barrel{barrel_id}: {issue}")
            # The command is also sent to the sensor just because the simulation of temperature happens there
            # This would not happen in real life
            sensor_socket = barrel.get("sensor")
            if sensor_socket:
                try:
                    sensor_socket.sendall(command.encode("utf-8"))
                except Exception as issue:
                    print(f"Command was not send to sensor of barrel{barrel_id}: {issue}")

    # This method will register a row in "cellar_cooling_system.txt"(LOG_FILE variable)...
    # ...for each change in the position of the solenoid.
    # It populates the row with:
    # -Date and time
    # -Barrel_id
    # -Solenoid position)
    # -Temperature of the barrel
    # -Set temperature of the barrel (ideal temp)
    # Creating a history of 'cooling system changes'
    def log_event(self, barrel_id, action, temp, setp):
        # Logging also the date and time the action happens
        # Format: year-month-date hour:minutes:seconds
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Defining how info will display in each row
        row = f"[{now}] Barrel #{barrel_id} | Solenoid {action} | Temp: {temp}°C | Set: {setp}°C "
        print(row)
        # 'a' is for append, so that we keep previous events of the history
        with open(LOG_FILE, "a") as log_file:
            log_file.write(row + "\n")


if __name__ == "__main__":
    # Setting server host and port
    HOST, PORT = "localhost", 9999
    # Creating a TCP thread for each barrel that establishes a connection
    server = socketserver.ThreadingTCPServer((HOST, PORT), BarrelRequestHandler)
    # Printing a confirmation message
    print(f"Server is running at {HOST}:{PORT}")
    # Server is indicated to keep running.
    server.serve_forever()



