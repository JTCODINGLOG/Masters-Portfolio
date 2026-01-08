import socket
import json
from datetime import datetime

# We create a SolenoidClient with the attributes needed to...
# ...create an object with methods that allows the solenoid to connect...
# ...to the server, and receive data according to the server written logic.
# A singular characteristic of the solenoid client: it sends data to the...
# ...server just to identify itself, but then it enters inside a while-loop where...
# ...the solenoid just receives command messages from the server
class SolenoidClient:
    # Solenoid attributes are a bit simpler than sensor attributes:
    # 'barrel_id' to identify to which barrel is associated to
    # 'host' and 'port' attributes that have default values...
    # ...to easily connect to the server
    def __init__(self, barrel_id, host='localhost', port=9999):
        self.barrel_id = barrel_id
        self.host = host
        self.port = port

    # Methods are also simpler than in the other task3 classes
    # 'log_Action' just generates a statement to communicate changes...
    # ...in the solenoid and when these changes happen (date and time)
    def log_action(self, action):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] - Solenoid {action}  barrel #{self.barrel_id}")

    # In the run method we implement the logic of how the solenoid program works
    # The logic regarding socket connection and first message('type' and 'barrel_id' info)...
    # ...sent it is nearly identical. This is because the server implements similar...
    # ...logic for both clients until it recognises from which client type the data is...
    # ...Then, the code will diverge for both of them and in the server, although these 'actors'...
    # ... are still involved in the same general logic that helps keeping the barrels...
    # ...at the right temperature.
    def run(self):
        # Creating a socket instance with the below parameters:
        # Similar socket programming as the other client(sensor):
        # AF_INET is the internet address family for IPv4
        # SOCK_STREAM is implemented on the TCP protocol
        solenoid_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establishing connection with the server
        # 'host' and 'post' are the default values set in the attribute definitions
        # The parameters are 'localhost' and '9999', respectively for host and port.
        # These parameters are the host and port of our server.
        solenoid_socket.connect((self.host, self.port))

        # Creating the variable data that will be sent to the server
        identity = {
            "type": "solenoid",
            "barrel_id": self.barrel_id
        }
        # Sending the variable identity over the network to the server
        # '.sendall' guarantees that the entire byte message is sent...
        # ...but currently we have a dictionary that needs to be transformed into bytes:
        # 'json.dumps' converts the dictionary into a json string
        # This is just the standard format we are using for data transmission
        # 'encode('utf-8') converts the json string into bytes
        # Default value of '.encode()' is utf-8. It is written for visualisation purposes.
        solenoid_socket.sendall(json.dumps(identity).encode('utf-8'))

        # Printing connection 'confirmation and waiting for commands' message
        print(f"-The solenoid for the barrel #{self.barrel_id} is connected and waiting for commands")

        # Here is where the logic between clients diverge
        # The solenoid program enters in a loop where a command from the server...
        # ...is expected. If there is no command loop is broken.
        while True:
            # Receiving 1024 bytes of data from the server
            # The expected data is a command to open or close the solenoid...
            # ...based on the server logic
            command = solenoid_socket.recv(1024).decode('utf-8')
            # If there is not an answer from the server we stop solenoid program,...
            # therefore the solenoid is no longer connected to the server
            if not command:
                print("No command received from the server")
                break
            # If there is a command, we just print the confirmation message
            # In real life, the solenoid would need to execute the action of opening himself...
            # ...which would probably be another method but here we just log the solenoid state
            # Meanwhile the server will register the solenoid action if there is a change.
            self.log_action(command.strip())

if __name__ == "__main__":
    # A solenoid object is created with the following parameters:
    # barrel_id
    # host
    # portif
    # Parameters can be changed with the purpose of testing the program
    solenoid = SolenoidClient(barrel_id = 1)
    # We call the 'run' method which is the one implementing the logic of the solenoid
    solenoid.run()