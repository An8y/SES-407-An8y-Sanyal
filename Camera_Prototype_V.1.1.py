import serial
import os
import numpy as np
import matplotlib.pyplot as plt

# Serial port configuration
ser = serial.Serial('COM15', 9600)

# Function to clear the output screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the menu options
def display_menu():
    clear_screen()
    print("\nMenu:\n\n")
    print("1. Check Shutter Status\n")
    print("2. Open Shutter\n")
    print("3. Close Shutter\n")
    print("4. Adjust shutter by 30 degrees\n")
    print("5. Take images\n")
    print("6. Exit program\n")

# Function to check the shutter status
def check_shutter_status():
    clear_screen()
    print("1. Check Shutter Status\n\n")
    ser.write(b'1')  # Send command to 
    # Read a line from the serial port
    line = ser.readline().decode().strip()
    # Process the received line
    print(line)
# Function to open the shutter
def open_shutter():
    clear_screen()
    print("2. Open Shutter\n\n")
    ser.write(b'2')  # Send command to Arduino
    # Read a line from the serial port
    line = ser.readline().decode().strip()
# Function to close the shutter
def close_shutter():
    clear_screen()
    print("3. Close Shutter\n\n")
    ser.write(b'3')  # Send command to 
    # Read a line from the serial port
    line = ser.readline().decode().strip()

# Function to capture images
def capture_images():
    clear_screen()
    print("5. Take images\n\n")
    ser.write(b'5')  # Send command to Arduino

    try:
        while ser.in_waiting > 0:
            # Read a line from the serial port
            line = ser.readline().decode().strip()
            
            # Split the line into individual temperature values
            temperature_values = line.split(',')
            
            # Convert the temperature values to a 2D NumPy array
            temperature_array = np.array(temperature_values, dtype=float)
            temperature_matrix = temperature_array.reshape(24, 32)
            
            # Display the thermal image
            plt.imshow(temperature_matrix, cmap='hot', interpolation='bicubic')
            plt.colorbar(label='Temperature (°C)')
            plt.title('Thermal Image')
            plt.xlabel('Column')
            plt.ylabel('Row')
            plt.show()
    finally:
        # Close the serial port
        ser.close()

# Function for manual shutter adjustment
def manual_shutter_adjustment():
    clear_screen()
    while True:
        direction = input("4. Adjust shutter by 30 degrees\n\na. Counter-clockwise\nb. Clockwise: \n\n")
        if direction == 'a':
            ser.write(b'a')  # Send command to Arduino for anticlockwise adjustment
        elif direction == 'b':
            ser.write(b'b')  # Send command to Arduino for clockwise adjustment
        else:
            print("Invalid input. Please enter 'a' or 'b'.")
            
            # Read a line from the serial port
        line = ser.readline().decode().strip()

        # Condition to check whether to continue the loop
        user_input = input("\n\nDo you want to continue? (yes/no): ")
        clear_screen()
        if user_input.lower() != 'yes':
            break

# Function to exit
def exit_program():
    clear_screen()
    ser.write(b'6')  # Send command to Arduino

# Main loop
while True:

    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        exit_program()
        break
    elif choice == '1':
        check_shutter_status()
        continue
    elif choice == '2':
        open_shutter()
        continue
    elif choice == '3':
        close_shutter()
        continue
    elif choice == '4':
        manual_shutter_adjustment()
        continue
    elif choice == '5':
        capture_images()
        continue
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        continue

# Close serial port
ser.close()
