//-----------------------------------------------Header files-------------------------------------------

// <header files for limit switch><nothing specific>
//—-------------------------------------------------------------------------------------------------------
#include <Stepper.h>
//—-------------------------------------------------------------------------------------------------------
#include <Adafruit_MLX90640.h>
//—-------------------------------------------------------------------------------------------------------
// <header files for itsybitsy><nothing specific>
//—-------------------------------------------------------------------------------------------------------
// <header files for miscellaneous><TBD>

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//------------------------------------------Variable initializations-----------------------------------

// Define the pin connected to the SPDT switch
const int switchPin1 = 7; 
const int switchPin2 = 4;
//—-------------------------------------------------------------------------------------------------------
#define STEPS 200
// create an instance of the stepper class, specifying
// the number of steps of the motor and the pins it's
// attached to
Stepper stepper(STEPS, 9, 10, 12, 13);
//—-------------------------------------------------------------------------------------------------------
Adafruit_MLX90640 mlx;
float frame[24*32]; // buffer for full frame of temperatures

// uncomment *one* of the below
#define PRINT_TEMPERATURES
//#define PRINT_ASCIIART
//—-------------------------------------------------------------------------------------------------------
// <variables for itsybitsy><TBD>
//—-------------------------------------------------------------------------------------------------------
// <variables for miscellaneous><TBD>

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//-------------------------------------------------Setup-------------------------------------------------

void setup() {// Setup pins 

  // Initialize serial communication
  Serial.begin(9600);

// Set the switch pin as input
  pinMode(switchPin1, INPUT_PULLUP); // Use INPUT_PULLUP if the switch is connected to ground when press
  pinMode(switchPin2, INPUT_PULLUP); // Use INPUT_PULLUP if the switch is connected to ground when press
//—-------------------------------------------------------------------------------------------------------
  // set the speed of the motor to 60 RPMs
  stepper.setSpeed(60);
//—-------------------------------------------------------------------------------------------------------
  while (!Serial) delay(10);
  Serial.begin(115200);
  delay(100);

  // Initialize IR camera
  mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire);

  Serial.print("Serial number: ");
  Serial.print(mlx.serialNumber[0], HEX);
  Serial.print(mlx.serialNumber[1], HEX);
  Serial.println(mlx.serialNumber[2], HEX);


  //mlx.setMode(MLX90640_INTERLEAVED);
  mlx.setMode(MLX90640_CHESS);
  Serial.print("Current mode: ");
  if (mlx.getMode() == MLX90640_CHESS) {
    Serial.println("Chess");
  } else {
    Serial.println("Interleave");
  }


  mlx.setResolution(MLX90640_ADC_18BIT);
  Serial.print("Current resolution: ");
  mlx90640_resolution_t res = mlx.getResolution();
  switch (res) {
    case MLX90640_ADC_16BIT: Serial.println("16 bit"); break;
    case MLX90640_ADC_17BIT: Serial.println("17 bit"); break;
    case MLX90640_ADC_18BIT: Serial.println("18 bit"); break;
    case MLX90640_ADC_19BIT: Serial.println("19 bit"); break;
  }


  mlx.setRefreshRate(MLX90640_16_HZ);
  Serial.print("Current frame rate: ");
  mlx90640_refreshrate_t rate = mlx.getRefreshRate();
  switch (rate) {
    case MLX90640_0_5_HZ: Serial.println("0.5 Hz"); break;
    case MLX90640_1_HZ: Serial.println("1 Hz"); break;
    case MLX90640_2_HZ: Serial.println("2 Hz"); break;
    case MLX90640_4_HZ: Serial.println("4 Hz"); break;
    case MLX90640_8_HZ: Serial.println("8 Hz"); break;
    case MLX90640_16_HZ: Serial.println("16 Hz"); break;
    case MLX90640_32_HZ: Serial.println("32 Hz"); break;
    case MLX90640_64_HZ: Serial.println("64 Hz"); break;
  }
//—-------------------------------------------------------------------------------------------------------
// <setup for itsybitsy>
//—-------------------------------------------------------------------------------------------------------
// <setup for miscellaneous>

}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//----------------------------------------------Main loop-----------------------------------------------

void loop() {//main loop

// Read the incoming byte
  char command = Serial.read();

  // Execute corresponding function based on command
  switch (command) {
    case '1':
      Serial.println("Checking status...\n");
      delay(1000);
      ShutterStatus();
      break;
    case '2':
      Serial.println("Deploying Camera...\n");
      stepper.step(-STEPS/6);
      delay(500);
      break;
    case '3':
      Serial.println("Closing Camera...\n");
      stepper.step(STEPS/6);
      delay(500);
      break;
    case 'a':
      Serial.println("Adjusting Camera by 30 deg CCW...\n");
      stepper.step(-STEPS/12);
      delay(500);
      break;
    case 'b':
      Serial.println("Adjusting Camera by 30 deg CW...\n");
      stepper.step(STEPS/12);
      delay(500);
      break;
    case '5':
      Serial.println("Capturing images...\n");
      delay(500);
      GetImages();
      break;
    case '6':
      Serial.println("Closing...\n");
      break;
    default:
      Serial.println("Invalid command!\n");
      break;
  }
}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//---------------------------------------Function definitions-----------------------------------------

void ShutterStatus() {
  // Read the state of the switch
  int switch1State = digitalRead(switchPin1);
  int switch2State = digitalRead(switchPin2);
  
  // Check the state of the switch
  if ((switch1State == LOW)&&(switch2State == HIGH)) { 
    Serial.println("Shutter is open");
    
  } else if ((switch1State == HIGH)&&(switch2State == LOW)) {
    Serial.println("Shutter is closed");
    
  }
  
  // Add a small delay to debounce the switch
  delay(100);
}

//—-------------------------------------------------------------------------------------------------------
// <function definition for stepper motor driver><nothing specific>
//—-------------------------------------------------------------------------------------------------------
void GetImages()  {  
delay(500);
  if (mlx.getFrame(frame) != 0) {
    Serial.println("Failed");
    return;
  }

//  Serial.println("===================================");
//  Serial.print("Ambient temperature = ");
//  Serial.print(mlx.getTa(false)); // false = no new frame capture
//  Serial.println(" degC");
//  Serial.println();
//  Serial.println();

  for (uint8_t h=0; h<24; h++) {
    for (uint8_t w=0; w<32; w++) {
      float t = frame[h*32 + w];
#ifdef PRINT_TEMPERATURES
      Serial.print(t, 1);
      Serial.print(", ");
#endif
#ifdef PRINT_ASCIIART
      char c = '&';
      if (t < 20) c = ' ';
      else if (t < 23) c = '.';
      else if (t < 25) c = '-';
      else if (t < 27) c = '*';
      else if (t < 29) c = '+';
      else if (t < 31) c = 'x';
      else if (t < 33) c = '%';
      else if (t < 35) c = '#';
      else if (t < 37) c = 'X';
      Serial.print(c);
#endif
    }
    Serial.println();
  }
}
//—-------------------------------------------------------------------------------------------------------
// <function definition for itsybitsy>
//—-------------------------------------------------------------------------------------------------------
// <function definition for miscellaneous>
