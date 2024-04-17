import serial
import os
import numpy as np
import matplotlib.pyplot as plt
import time


# Serial port configuration
arduino = serial.Serial(port='COM15', baudrate=9600, timeout=.1)

# Function to clear the output screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def capture_images():
    try:
        # Create a new folder to save the images
        if not os.path.exists('thermal_images'):
            os.makedirs('thermal_images')

        for i in range(1, 5):
            line = getValue()
            line = line.replace(" ", "")
            
            print("Line before splitting:", line)

            # Split the line into individual temperature values
            temperature_values = line.split(',')
            temperature_values = [value for value in line.split(',') if value]

            print(temperature_values)
            
            # Convert the temperature values to a 2D NumPy array
            temperature_array = np.array(temperature_values, dtype=float)
            print(temperature_array)
            temperature_matrix = temperature_array.reshape(24, 32)
            print(temperature_matrix)

            # Display the thermal image
            plt.imshow(temperature_matrix, cmap='hot', interpolation='bicubic')
            plt.colorbar(label='Temperature (°C)')
            plt.title('Thermal Image')
            plt.xlabel('Column')
            plt.ylabel('Row')

            # Save the thermal image to the 'thermal_images' folder
            image_path = os.path.join('thermal_images', f'thermal_image_{i}.png')
            plt.savefig(image_path)
            plt.clf()
            #plt.show()
            
            # Save the temperature values to a text file
            with open("temperature_data.txt", "a") as file:
                file.write(line + "\n\n\n")

    except Exception as e:
        print(e)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').strip()
    return data

def convert(value):
    try:
        cleaned_string = value.strip("b'").rstrip(',')
        float_list = [float(x) for x in cleaned_string.split(',')]
        return True, cleaned_string + ','
    except ValueError:
        return False, None

def validate_input(input_str):
    # Check if the input string contains only digits, dots, and commas
    if all(c.isdigit() or c == '.' or c == ',' for c in input_str):
        return True
    return False

# Main function to get the value from Arduino
def getValue():
    value = write_read("6")
    while convert(value)[0] is False:
        value = write_read("")
    return convert(value)[1]

# Main function
def main():
    while True:
        command = input("Welcome to SpaceWorks Team #1 IR Camera! What would you like to do?\n\n1. Check Shutter status\n2. Open shutter\n3. Close shutter\n4. Rotate shutter by 30 deg CCW\n5. Rotate shutter by 30 deg CW\n6. Capture 45 images\n")
        
        if command == '1':
            print("Checking status...")
            time.sleep(1)
            write_read("1")
            
        elif command == '2':
            print("Opening shutter...")
            write_read("2")
            time.sleep(0.5)
            
        elif command == '3':
            print("Closing shutter...")
            write_read("3")
            time.sleep(0.5)
            
        elif command == '4':
            print("Adjusting Camera by 30 deg CCW...")
            write_read("4")
            time.sleep(0.5)
            
        elif command == '5':
            print("Adjusting Camera by 30 deg CW...")
            write_read("5")
            time.sleep(0.5)
            
        elif command == '6':
            print("Capturing images...")
            capture_images()
            
        else:
            print("Invalid command!")

        time.sleep(3)

# Add the rest of your functions and imports here


if __name__ == "__main__":
    main()

