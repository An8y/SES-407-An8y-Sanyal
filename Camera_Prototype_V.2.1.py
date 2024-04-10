import serial
import os
import numpy as np
import matplotlib.pyplot as plt

# Serial port configuration
#ser = serial.Serial('COM15', 9600)

# Function to clear the output screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to capture and display images
def capture_images():

    line = '28.0, 28.5, 28.6, 28.8, 28.4, 28.2, 28.3, 28.0, 28.4, 28.4, 28.2, 28.0, 28.3, 28.3, 27.9, 28.1, 27.6, 28.1, 28.1, 28.2, 27.7, 28.0, 28.9, 28.2, 28.1, 28.4, 28.4, 28.0, 29.2, 28.9, 28.5, 29.4, 28.5, 27.7, 28.6, 28.1, 28.1, 27.9, 28.3, 28.5, 27.7, 28.0, 28.6, 28.2, 28.0, 28.2, 28.1, 28.6, 28.0, 28.1, 28.4, 28.0, 28.3, 28.0, 28.3, 28.8, 28.0, 28.5, 28.5, 28.6, 28.4, 28.6, 28.9, 28.9, 28.9, 28.4, 28.3, 28.3, 28.4, 27.8, 28.3, 28.6, 28.1, 28.2, 27.7, 28.3, 27.8, 28.4, 28.6, 28.5, 28.1, 28.1, 28.1, 28.3, 27.9, 28.4, 27.7, 28.4, 28.1, 28.4, 28.1, 28.9, 29.4, 28.4, 28.3, 28.4, 28.1, 28.0, 28.2, 28.3, 28.1, 27.8, 28.5, 28.2, 28.1, 27.8, 28.1, 28.3, 27.7, 27.9, 28.5, 28.5, 28.0, 28.2, 28.5, 28.5, 28.0, 28.0, 28.3, 28.4, 28.4, 28.1, 28.3, 28.5, 28.1, 28.1, 29.6, 29.0, 28.3, 28.3, 28.5, 28.6, 28.0, 28.1, 27.5, 28.1, 28.3, 27.8, 28.1, 28.3, 28.0, 28.5, 27.9, 28.5, 28.2, 28.1, 28.1, 28.3, 28.0, 28.3, 28.7, 28.5, 28.2, 28.4, 28.0, 28.5, 28.2, 28.6, 28.5, 29.1, 28.5, 28.4, 28.3, 28.6, 27.8, 28.2, 28.4, 28.4, 28.5, 27.9, 28.5, 28.6, 28.2, 28.2, 28.2, 28.4, 27.9, 28.0, 28.2, 28.2, 28.1, 28.0, 28.0, 28.1, 28.0, 28.0, 28.4, 28.4, 28.6, 28.1, 29.0, 29.1, 28.6, 28.8, 28.3, 28.6, 28.0, 27.8, 28.0, 28.5, 28.2, 28.2, 28.1, 28.3, 28.0, 28.2, 28.1, 28.4, 28.2, 28.3, 27.9, 28.5, 28.0, 28.4, 28.3, 28.7, 28.7, 28.0, 28.2, 28.3, 28.6, 28.8, 29.0, 28.7, 27.6, 28.9, 28.2, 28.2, 28.0, 27.9, 28.4, 28.8, 28.1, 28.0, 27.9, 28.3, 28.3, 28.0, 27.8, 28.2, 28.2, 28.1, 28.6, 28.4, 28.2, 27.8, 28.5, 28.3, 28.6, 28.3, 28.7, 28.5, 29.1, 28.1, 29.0, 28.0, 28.4, 28.8, 28.0, 28.3, 28.7, 28.4, 28.1, 28.3, 28.4, 28.0, 28.2, 28.2, 28.2, 28.5, 28.1, 28.0, 28.3, 28.5, 28.2, 28.4, 28.3, 28.2, 28.3, 28.8, 28.4, 28.7, 28.4, 28.5, 28.7, 28.6, 28.7, 29.2, 28.6, 28.5, 28.6, 28.3, 28.2, 28.4, 28.2, 28.2, 28.1, 28.3, 28.3, 28.2, 28.2, 28.0, 28.3, 28.7, 27.9, 28.1, 28.2, 28.4, 27.8, 27.9, 28.4, 28.5, 28.1, 28.4, 28.8, 28.3, 28.7, 28.3, 28.7, 29.2, 29.0, 28.2, 28.6, 28.6, 28.4, 28.0, 28.1, 28.1, 28.4, 28.2, 28.4, 28.6, 28.2, 28.1, 28.0, 28.3, 28.3, 27.9, 28.0, 28.4, 28.1, 28.3, 28.5, 28.3, 28.2, 28.6, 28.4, 28.4, 28.9, 28.5, 28.5, 29.2, 28.7, 28.0, 28.2, 28.7, 28.3, 28.2, 28.3, 28.4, 28.3, 28.2, 28.2, 28.1, 28.1, 27.9, 28.5, 28.1, 27.9, 28.0, 28.6, 28.6, 28.0, 28.0, 28.0, 28.8, 28.1, 28.3, 28.6, 28.7, 28.6, 28.6, 28.7, 29.2, 28.5, 28.6, 28.4, 28.6, 27.9, 28.1, 28.2, 28.6, 27.9, 28.1, 28.3, 28.3, 28.0, 28.3, 27.9, 28.5, 28.4, 28.2, 28.6, 28.1, 28.6, 28.4, 28.3, 28.5, 28.5, 28.4, 28.5, 29.0, 28.7, 28.4, 28.2, 29.2, 28.5, 28.4, 28.8, 28.7, 28.5, 28.4, 28.4, 27.9, 28.5, 28.0, 28.7, 28.6, 28.4, 28.0, 28.5, 28.4, 28.3, 28.1, 28.1, 28.5, 28.3, 28.5, 28.9, 28.4, 28.2, 28.3, 28.8, 28.6, 28.3, 28.7, 29.3, 29.4, 28.6, 28.4, 28.2, 28.9, 28.7, 28.0, 28.1, 29.0, 28.6, 28.0, 28.2, 28.9, 28.0, 28.2, 28.2, 28.4, 28.5, 28.3, 28.9, 28.3, 28.6, 28.6, 28.8, 28.8, 28.3, 28.7, 28.8, 28.9, 28.7, 28.6, 29.3, 29.0, 28.6, 28.3, 28.6, 28.7, 28.1, 28.3, 28.7, 28.4, 27.8, 28.1, 28.4, 28.5, 28.4, 28.3, 28.7, 28.5, 28.4, 28.1, 28.5, 28.5, 28.1, 28.3, 28.5, 28.6, 28.6, 28.8, 29.2, 29.2, 28.7, 28.8, 29.0, 29.1, 29.6, 28.5, 28.7, 28.4, 28.5, 28.5, 28.8, 28.5, 28.4, 28.5, 28.2, 28.7, 28.5, 28.4, 28.3, 28.6, 28.1, 28.3, 28.2, 28.9, 28.6, 28.4, 28.4, 29.1, 28.7, 28.7, 28.5, 29.1, 29.0, 29.3, 29.6, 29.6, 29.0, 28.8, 29.1, 28.8, 28.4, 28.8, 28.8, 28.8, 28.3, 28.1, 28.8, 29.0, 28.4, 28.1, 28.3, 28.4, 28.5, 28.1, 28.7, 28.5, 28.3, 28.5, 28.8, 29.2, 28.4, 28.9, 28.8, 29.2, 28.6, 28.8, 29.6, 29.3, 28.7, 29.3, 29.4, 29.2, 29.0, 28.9, 28.9, 29.0, 28.9, 28.6, 29.0, 28.5, 28.4, 28.4, 28.7, 28.7, 28.3, 28.4, 28.5, 28.4, 28.7, 28.8, 28.3, 29.2, 28.8, 28.8, 28.8, 29.2, 29.4, 29.3, 29.4, 29.8, 28.7, 28.6, 29.0, 28.7, 28.8, 29.3, 29.1, 28.8, 28.6, 28.4, 29.2, 28.8, 28.0, 28.7, 28.7, 28.8, 28.6, 28.3, 28.5, 28.7, 28.5, 28.5, 28.9, 28.8, 28.7, 29.2, 28.6, 29.3, 29.1, 29.6, 29.3, 29.8, 29.5, 29.4, 28.8, 29.9, 28.9, 28.9, 29.0, 28.8, 28.7, 28.7, 28.6, 29.1, 28.9, 28.8, 28.8, 29.1, 28.5, 28.6, 28.8, 29.1, 28.9, 28.5, 29.1, 29.1, 28.7, 28.8, 29.5, 29.7, 29.7, 28.9, 29.8, 29.7, 29.5, 29.8, 29.4, 28.6, 28.5, 29.0, 28.6, 29.1, 29.1, 28.5, 29.1, 29.4, 29.1, 28.8, 28.8, 28.9, 28.7, 28.5, 28.8, 29.0, 28.6, 28.6, 29.0, 29.0, 28.7, 29.0, 28.9, 29.7, 28.8, 29.1, 30.0, 30.4, 29.4, 29.8, 29.5, 30.1, 29.0, 29.1, 29.1, 29.0, 28.6, 28.7, 29.2, 29.3, 28.5, 29.2, 28.7, 29.4, 29.0, 29.2, 29.4, 29.1, 28.7, 28.7, 29.2, 28.8, 29.2, 29.3, 29.9, 29.8, 30.1, 29.8, 29.7, 30.4, 29.0, 28.8, 29.8, 29.9, 29.3, 28.7, 29.3, 29.4, 28.8, 28.7, 29.3, 29.3, 29.1, 28.6, 28.7, 29.2, 28.6, 29.2, 29.1, 29.0, 28.8, 28.9, 29.8, 29.4, 29.3, 29.3, 30.3, 30.3, 29.2, 29.5, 30.6, 31.0,'

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
    plt.show()

# Main function
def main():
    clear_screen()
    #ser.write()
    capture_images()

if __name__ == "__main__":
    main()

# # Function to capture and display images
# def capture_images():
#     #try:
#         #while True:
#             # Read a line from the serial port
#             #line = ser.readline().decode().strip()
#             line = 25.7, 26.2, 25.6, 25.8, 25.5, 25.5, 25.6, 26.6, 25.9, 26.1, 26.2, 26.7, 26.4, 26.8, 26.8, 26.6, 26.9, 26.9, 26.4, 26.8, 26.5, 26.2, 26.6, 27.0, 26.8, 26.8, 27.0, 27.2, 26.8, 26.6, 27.2, 27.4, 
# 26.2, 25.9, 25.5, 26.9, 26.0, 26.0, 25.7, 26.1, 26.5, 26.0, 26.5, 26.8, 26.8, 26.6, 26.3, 26.9, 26.3, 26.6, 26.6, 26.9, 26.8, 26.4, 27.1, 27.2, 27.4, 27.4, 26.7, 27.1, 27.1, 27.1, 27.0, 27.3, 
# 25.7, 25.9, 25.8, 26.1, 26.1, 25.3, 25.5, 25.6, 26.1, 26.6, 26.6, 26.6, 26.6, 26.3, 26.5, 26.6, 26.8, 26.6, 26.6, 27.0, 26.8, 26.9, 27.2, 26.7, 27.0, 27.1, 26.5, 27.4, 27.3, 27.2, 27.3, 27.0, 
# 25.8, 25.8, 25.9, 26.2, 25.6, 25.3, 25.3, 25.5, 25.7, 26.1, 26.2, 26.6, 26.2, 26.4, 27.1, 27.2, 26.5, 26.2, 26.6, 27.2, 26.9, 26.7, 27.1, 26.8, 27.0, 26.8, 26.8, 27.5, 26.8, 27.1, 27.6, 27.5, 
# 25.2, 25.9, 25.5, 25.6, 25.5, 26.0, 25.7, 25.6, 26.0, 26.0, 25.8, 25.9, 26.2, 26.4, 26.0, 26.1, 26.8, 26.7, 26.4, 26.9, 26.9, 26.8, 26.9, 27.1, 27.4, 27.0, 27.1, 27.2, 27.0, 26.9, 27.2, 28.1, 
# 26.1, 25.6, 25.4, 25.5, 24.9, 25.1, 24.9, 25.1, 25.6, 25.4, 25.6, 26.6, 26.0, 26.3, 26.5, 26.5, 26.6, 26.4, 26.4, 27.0, 26.6, 26.6, 26.3, 26.7, 26.8, 26.9, 26.8, 26.9, 27.3, 27.2, 27.2, 28.0, 
# 26.0, 25.9, 25.7, 26.2, 25.6, 25.9, 24.8, 24.9, 25.0, 25.4, 25.4, 26.0, 25.5, 25.8, 25.6, 26.1, 26.0, 26.0, 26.3, 26.3, 26.5, 26.2, 26.8, 27.0, 26.8, 26.9, 26.6, 27.1, 27.3, 27.0, 27.3, 27.6, 
# 26.3, 26.0, 25.8, 26.3, 25.9, 25.5, 24.7, 25.7, 25.7, 24.8, 25.1, 25.2, 24.8, 25.3, 25.2, 25.6, 25.5, 25.5, 26.4, 25.8, 26.1, 25.8, 26.4, 26.5, 26.2, 25.9, 26.6, 27.6, 27.2, 27.2, 27.6, 28.2, 
# 26.1, 26.6, 26.3, 26.1, 26.0, 25.6, 25.4, 25.8, 25.3, 25.7, 25.4, 25.5, 25.6, 25.2, 24.9, 25.2, 24.9, 24.7, 25.4, 25.5, 26.1, 25.8, 25.9, 26.3, 26.3, 26.1, 26.3, 27.4, 26.4, 26.8, 27.0, 27.8, 
# 26.0, 26.1, 25.9, 26.6, 25.4, 25.5, 25.4, 26.0, 25.7, 25.5, 25.5, 25.9, 25.4, 25.8, 25.3, 25.8, 25.0, 25.4, 25.2, 25.9, 25.0, 25.3, 25.6, 26.2, 25.7, 26.0, 26.4, 26.7, 27.1, 26.7, 27.5, 27.6, 
# 26.3, 26.3, 26.0, 26.1, 25.5, 25.8, 25.5, 25.9, 25.7, 25.7, 25.7, 26.3, 25.5, 25.4, 25.5, 25.9, 25.6, 25.7, 26.0, 25.7, 25.6, 25.0, 25.2, 25.9, 25.7, 25.7, 25.4, 25.5, 25.8, 26.6, 26.3, 27.0, 
# 25.9, 26.0, 26.3, 26.4, 26.2, 25.3, 25.9, 26.0, 25.8, 25.8, 25.8, 25.9, 25.8, 26.0, 25.7, 25.8, 25.4, 25.8, 25.7, 26.1, 25.1, 24.9, 25.8, 26.0, 26.1, 25.6, 25.9, 25.7, 26.3, 26.0, 25.7, 26.3, 
# 26.6, 26.0, 26.1, 25.7, 26.1, 25.8, 25.9, 26.1, 25.9, 25.7, 25.7, 26.3, 25.6, 26.0, 26.0, 26.2, 25.4, 26.1, 25.8, 26.2, 25.2, 25.5, 25.7, 26.3, 26.3, 26.1, 26.5, 26.5, 26.0, 26.2, 26.8, 27.0, 
# 26.5, 26.3, 26.3, 27.0, 26.3, 25.4, 26.5, 26.1, 25.6, 26.3, 26.5, 26.3, 25.8, 26.0, 26.1, 26.1, 26.1, 25.8, 25.6, 26.0, 25.1, 25.7, 25.7, 26.3, 25.8, 26.5, 26.0, 26.7, 26.7, 26.4, 27.6, 27.4, 
# 27.2, 26.6, 26.5, 27.0, 26.3, 25.5, 26.2, 26.9, 26.0, 26.2, 26.2, 26.4, 25.9, 26.1, 26.2, 26.5, 26.2, 25.8, 26.4, 26.2, 26.0, 25.7, 26.2, 26.7, 26.3, 26.4, 26.2, 26.7, 26.4, 26.6, 26.9, 26.8, 
# 26.9, 26.7, 26.6, 26.8, 26.3, 26.2, 26.1, 26.1, 26.5, 25.7, 26.6, 26.3, 26.2, 26.1, 26.2, 26.4, 25.9, 26.1, 25.7, 26.2, 26.1, 25.7, 26.5, 26.8, 26.5, 26.1, 26.7, 27.2, 27.2, 27.1, 27.4, 27.6, 
# 26.8, 27.0, 26.7, 27.1, 26.3, 26.6, 26.5, 26.7, 26.4, 26.8, 26.7, 26.5, 25.9, 26.1, 25.8, 26.8, 26.4, 26.1, 26.1, 26.1, 26.5, 26.0, 26.3, 26.7, 27.0, 26.1, 27.3, 26.8, 26.5, 27.2, 27.6, 27.8, 
# 26.9, 26.5, 26.6, 27.0, 26.9, 25.8, 26.6, 26.6, 26.3, 26.1, 26.4, 26.8, 26.2, 26.0, 25.9, 26.7, 26.3, 26.0, 26.0, 26.2, 26.3, 25.9, 27.1, 26.8, 26.5, 26.2, 26.8, 27.4, 27.2, 27.1, 28.3, 28.3, 

            
#             # Split the line into individual temperature values
#             temperature_values = line.split(',')
            
#             # Convert the temperature values to a 2D NumPy array
#             temperature_array = np.array(temperature_values, dtype=float)
#             temperature_matrix = temperature_array.reshape(24, 32)
            
#             # Display the thermal image
#             plt.imshow(temperature_matrix, cmap='hot', interpolation='bicubic')
#             plt.colorbar(label='Temperature (°C)')
#             plt.title('Thermal Image')
#             plt.xlabel('Column')
#             plt.ylabel('Row')
#             plt.show()
#     #finally:
#         # Close the serial port
#         #ser.close()














# import serial
# import os
# import numpy as np
# import matplotlib.pyplot as plt

# # Serial port configuration
# ser = serial.Serial('COM15', 9600)

# # Function to clear the output screen
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # # Function to display the menu options
# # def display_menu():
# #     clear_screen()
# #     print("\nMenu:\n\n")
# #     print("1. Check Shutter Status\n")
# #     print("2. Open Shutter\n")
# #     print("3. Close Shutter\n")
# #     print("4. Adjust shutter by 30 degrees\n")
# #     print("5. Take images\n")
# #     print("6. Exit program\n")

# # # Function to check the shutter status
# # def check_shutter_status():
# #     clear_screen()
# #     print("1. Check Shutter Status\n\n")
# #     ser.write(b'1')  # Send command to 
# #     # Read a line from the serial port
# #     line = ser.readline().decode().strip()
# #     # Process the received line
# #     print(line)
# # # Function to open the shutter
# # def open_shutter():
# #     clear_screen()
# #     print("2. Open Shutter\n\n")
# #     ser.write(b'2')  # Send command to Arduino
# #     # Read a line from the serial port
# #     line = ser.readline().decode().strip()
# # # Function to close the shutter
# # def close_shutter():
# #     clear_screen()
# #     print("3. Close Shutter\n\n")
# #     ser.write(b'3')  # Send command to 
# #     # Read a line from the serial port
# #     line = ser.readline().decode().strip()

# # Function to capture images
# def capture_images():
#     clear_screen()
#     # print("5. Take images\n\n")
#     # ser.write(b'5')  # Send command to Arduino

#     try:
#         while ser.in_waiting > 0:
#             # Read a line from the serial port
#             line = ser.readline().decode().strip()
            
#             # Split the line into individual temperature values
#             temperature_values = line.split(',')
            
#             # Convert the temperature values to a 2D NumPy array
#             temperature_array = np.array(temperature_values, dtype=float)
#             temperature_matrix = temperature_array.reshape(24, 32)
            
#             # Display the thermal image
#             plt.imshow(temperature_matrix, cmap='hot', interpolation='bicubic')
#             plt.colorbar(label='Temperature (°C)')
#             plt.title('Thermal Image')
#             plt.xlabel('Column')
#             plt.ylabel('Row')
#             plt.show()
#     finally:
#         # Close the serial port
#         ser.close()

# # # Function for manual shutter adjustment
# # def manual_shutter_adjustment():
# #     clear_screen()
# #     while True:
# #         direction = input("4. Adjust shutter by 30 degrees\n\na. Counter-clockwise\nb. Clockwise: \n\n")
# #         if direction == 'a':
# #             ser.write(b'a')  # Send command to Arduino for anticlockwise adjustment
# #         elif direction == 'b':
# #             ser.write(b'b')  # Send command to Arduino for clockwise adjustment
# #         else:
# #             print("Invalid input. Please enter 'a' or 'b'.")
            
# #             # Read a line from the serial port
# #         line = ser.readline().decode().strip()

# #         # Condition to check whether to continue the loop
# #         user_input = input("\n\nDo you want to continue? (yes/no): ")
# #         clear_screen()
# #         if user_input.lower() != 'yes':
# #             break

# # # Function to exit
# # def exit_program():
# #     clear_screen()
# #     ser.write(b'6')  # Send command to Arduino

# # Main loop
# while True:
#  capture_images()
#     # display_menu()
#     # choice = input("Enter your choice (1-6): ")

#     # if choice == '6':
#     #     exit_program()
#     #     break
#     # elif choice == '1':
#     #     check_shutter_status()
#     #     continue
#     # elif choice == '2':
#     #     open_shutter()
#     #     continue
#     # elif choice == '3':
#     #     close_shutter()
#     #     continue
#     # elif choice == '4':
#     #     manual_shutter_adjustment()
#     #     continue
#     # elif choice == '5':
#     #     capture_images()
#     #     continue
#     # else:
#     #     print("Invalid choice. Please enter a number between 1 and 6.")
#     #     continue

# # Close serial port
# ser.close()

