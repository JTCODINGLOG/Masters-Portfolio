"""
APPLICATION THAT HELPS STUDENTS TO PERFORM 3D VECTOR OPERATIONS
I chose a program for vectors because of 2 main reasons:
-Allowed to implement a program that uses different complex classes
-To utilise the widely used numpy library
-To remember some concepts regarding vectors that I learned in the past
Data types used are: tensors (1D arrays, tank1 tensors), custom classes, dictionaries, lists.
"""

# To work with tensors we import NumPy library
# It is required to install the package 'numpy'
import numpy as np
import math


# Definition of a custom class to generate 3D-vector objects
class Vector3d:
    # The idea is that to create the object, 'values' parameter has to be passed as a '3d-vector-list', [x,y,z]
    def __init__(self, name, values):
        self.name = name
        self.values = np.array(values, dtype=float)

    # Now vector math is added.
    # Library NumPy will provide efficient functions that will simplify these methods
    # Library math is added to calculate angles

    # Method to calculate dot product (or scalar product). Returns a number (scalar).
    # Expected output: dot product between 'self_object.values' (first vector) and 'vector2.values' (second vector).
    def dot(self, vector2):
        return np.dot(self.values, vector2.values)

    # Method to calculate cross product. Returns an array (vector).
    # Expected output: cross product between 'self_object.values' (first vector) and 'vector2.values' (second vector).
    def cross(self, vector2):
        return np.cross(self.values, vector2.values)

    # Method to calculate the magnitude (size/length) of a 3d vector
    # It uses linalg.norm from numpy.
    # This function is used to measure vectors and matrix
    # The parameter ord = None (default) sets L2 norm (Euclidean distance), to calculate distance between vectors
    # Expected output is the length of 'self_object.values' vector
    def magnitude(self):
        return np.linalg.norm(self.values)

    # Method to calculate the angle between vectors
    def angle(self, vector2):
        # We calculate the cosine of the angle(theta) using other Vectors3's methods:
        # Cosine = dot product of both vectors/product of the magnitudes of both vectors
        dot_vector2 = self.dot(vector2)
        mag_self = self.magnitude()
        mag_vector2 = vector2.magnitude()
        # Magnitude cannot be negative but a 'zero vector' is a possibility...
        # ...therefore division by zero is avoided because in that case there would not exist an angle.
        # A vector without length, is a vector without direction, a point.
        # It is impossible to calculate the angle between a point and a vector.
        if mag_self == 0 or mag_vector2 == 0:
            return None
        # We proceed to calculate the cosine as explained above.
        # 1 and -1 are the maximum are minimum numbers. Mathematically, cosine must be inbetween them.
        cos_theta = np.clip(dot_vector2 / (mag_self * mag_vector2), -1.0, 1.0)
        # To get the angle, we need to calculate the inverse of the cosine, the arccosine
        # The 'acos' function (arccosine), included in 'math' library, returns the angle measured in radians
        angle_rad = math.acos(cos_theta)
        # The 'degrees' function included in math returns the angle measured in degrees
        angle_deg = math.degrees(angle_rad)
        return angle_deg

    # Method that provides an informal string representation of the object
    # The idea is to provide understandable information about the object to the user
    def __str__(self):
        return f"{self.name}: ({self.values[0]}, {self.values[1]}, {self.values[2]})"


# Defining the main function
def main():
    # The container that will store the vectors object is a dictionary.
    vector_container = {}

    # Generating the menu for the user
    while True:
        print("\n Welcome to your favourite 3D Vector Calculator!\n")
        print("1. Add a vector")
        print("2. Display vectors (x,y,z)")
        print("3. Calculate Dot product")
        print("4. Calculate Cross product")
        print("5. Calculate Vector Magnitude")
        print("6. Compute angle between vectors")
        print("7. Exit the program")
        choice = input("\nPlease, enter one of the above option numbers(1-7): ").strip()

        if choice == "1":
            while True:
                v_name = input("Please, enter the name of the vector: ").strip()
                # Vector name validation
                if not v_name:
                    print("The input is empty, please enter a valid input")
                elif v_name in vector_container:
                    print("This vector name is already in the program")
                else:
                    break

            while True:
                v_values_raw = input("Please, enter values of the vector in this format 'x,y,z': ")
                # Formating. Creating a list with 3 values: x, y, z
                # That is the format we need when adding values as parameter for the vector object.
                try:
                    # Let's use list comprehension
                    # v_values string is stripped and then split by the commas.
                    # Then, the 'preformatted' v_values can be iterated over.
                    # In every iteration the element is transformed into float type
                    # The expected outcome is a list with float elements, that
                    v_values = [float(x) for x in v_values_raw.strip().split(",")]
                    # Validating input
                    # We do not need to check if there is a similar vector as that is a possibility
                    # We want to check if it is a 3D vector as expected
                    if len(v_values) != 3:
                        print("You must enter 3 numbers in this format 'x, y, z'")
                        # Prompt again for the values
                        continue
                    # Creating an object with class 'Vector3d'
                    # 'v_name' parameter is just a string
                    # 'v_values' is a 3-elements-list with this format [x,y,z]
                    vector = Vector3d(v_name, v_values)
                    # Storing the vector name and object in the dictionary
                    # The key is the name of the vector, that way we can easily access any vector in the dict
                    # The value is the 'Vector3d' object
                    vector_container[v_name] = vector
                    # Confirm the user that the vector has been added
                    print(f"New vector {v_name} has been added")
                    break
                except ValueError:
                    print("The input is invalid")

        elif choice == "2":
            # If dictionary is empty, then vectors cannot be printed
            if not vector_container:
                print("No vectors stored.")
            else:
                # Iterating over the vector values, the vector objects
                for vector in vector_container.values():
                    # Printing the result of each iteration
                    # __str__ method was redefined in the Vector3d class to get a cleaner print
                    print(vector)

        elif choice == "3":
            # If dictionary has less than 2 vectors, then calculations cannot be done.
            if len(vector_container) < 2 :
                print("Not enough stored vectors to calculate dot product.")
                # Back to the main menu
                continue
            while True:
                v1_name = input("Enter first vector name: ")
                v2_name = input("Enter second vector name: ")
                # Searching for elements in 'vector_container' dictionary.
                # Remember that keys are the vector names
                if v1_name in vector_container and v2_name in vector_container:
                    # Calling dot method from the corresponding vector object
                    # Adding second vector object as a parameter for dot method
                    # This method already calls for the attribute ".values" of the object
                    result = vector_container[v1_name].dot(vector_container[v2_name])
                    # For printing purposes: accessing vector object in the dictionary, then calling attribute '.values'
                    print(f"Dot product -> {vector_container[v1_name].values}·{vector_container[v2_name].values}: {result}")
                    break
                else:
                    print("One or both vector names have not been found.")

        elif choice == "4":
            # If dictionary has less than 2 vectors, then calculations cannot be done.
            if len(vector_container) < 2 :
                print("Not enough stored vectors to calculate cross product.")
                # Back to the main menu
                continue
            while True:
                v1_name = input("Enter first vector name: ")
                v2_name = input("Enter second vector name: ")
                # Searching for elements in 'vector_container' dictionary.
                # Remember that keys are the vector names
                if v1_name in vector_container and v2_name in vector_container:
                    # Calling cross method from the corresponding vector object
                    # Adding second vector object as a parameter for cross method
                    # This method already calls for the attribute ".values" of the object
                    result = vector_container[v1_name].cross(vector_container[v2_name])
                    # For printing purposes: accessing vector object in the dictionary and calling attribute '.values'
                    print(f"Cross product -> {vector_container[v1_name].values}x{vector_container[v2_name].values}: {result}")
                    break
                else:
                    print("One or both vector names have not been found.")

        elif choice == "5":
            # If dictionary is empty, then calculations cannot be performed
            if not vector_container:
                print("No vectors stored.")
                # Back to the main menu
                continue
            while True:
                v_name = input("Enter vector name: ")
                # Searching for elements in 'vector_container' dictionary.
                # Remember that keys are the vector names
                if v_name in vector_container:
                    # Calling magnitude method from the corresponding vector object
                    mag = vector_container[v_name].magnitude()
                    # For printing purposes: accessing vector object in the dictionary, then calling attribute '.values'
                    print(f"Magnitude of {v_name}{vector_container[v_name].values}: {mag}")
                    break
                else:
                    print("Vector name not found.")

        elif choice == "6":
            # If dictionary has less than 2 vectors, then calculations cannot be done.
            if len(vector_container) < 2 :
                print("Not enough stored vectors to calculate an angle.")
                # Back to the main menu
                continue
            while True:
                v1_name = input("Enter first vector name: ")
                v2_name = input("Enter second vector name: ")
                # Searching for elements in 'vector_container' dictionary.
                # Remember that keys are the vector names
                if v1_name in vector_container and v2_name in vector_container:
                    # Calling angle method from the corresponding vector object
                    # Adding second vector object as a parameter for angle method
                    # This method already calls for the attribute ".values" of the object
                    angle = vector_container[v1_name].angle(vector_container[v2_name])
                    # When calculating the angle between similar vectors, the result is numerical noise
                    # That numerical noise is considered 0 in this program
                    if abs(angle) < 1e-8:
                        print(f"Angle between {vector_container[v1_name].values} and {vector_container[v2_name].values}: 0 degrees")
                        break
                    elif angle is not None:
                        # For printing: accessing vector object in the dictionary and calling attribute '.values'
                        print(f"Angle between {vector_container[v1_name].values} and {vector_container[v2_name].values}: {angle} degrees")
                        break
                    else:
                        print("Zero magnitude vectors do not have direction. It is not possible to calculate an angle")
                else:
                    print("One or both vector names have not been found.")

        elif choice == "7":
            print("Thank you for using 3D Vector Calculator. See you soon!")
            # Exiting the program
            break

        else:
            print("The input is invalid. Please enter a number between 1 and 7")


# Calling main function
if __name__ == "__main__":
    main()
