BELLO RILWAN OLUWAKAYODE


Smart Car Park Surveillance System
The goal of this project is to develop a smart system for monitoring parking lots. The system displays the availability and occupancy of parking spaces on a central hub after using sensors to identify which spaces are free. Ultrasonic sensors for detecting the presence of cars and a PIR sensor for motion detection are important parts. Visual indicators of available space are provided by LEDs.
Overview of the System
This IOT system will provide real-time updates on available spaces in an effort to increase parking efficiency. Using ultrasonic sensors to detect the presence of cars, a PIR sensor to monitor motion, and LEDs to indicate open spots are some of the key capabilities. Updates such as "Car detected" and "Out of range" are printed by the system to a console. Users are guaranteed to receive a clear and immediate understanding of parking space status, enhancing the overall parking experience. I have used the PIR and ultrasonic sensors because they work together to provide accurate and dependable monitoring.
![2024-07-18-234604_1920x1080_scrot](https://github.com/user-attachments/assets/b89f4413-b31a-48a0-83a4-e690c8e8a101)
![2024-07-18-234717_1920x1080_scrot](https://github.com/user-attachments/assets/c349087d-c79f-4fab-abe9-f5844b1fc03d)
![2024-07-18-220731_1920x1080_scrot](https://github.com/user-attachments/assets/1a5f561e-d56e-4863-963d-51a6f30d6661)
![2024-07-18-220643_1920x1080_scrot](https://github.com/user-attachments/assets/b68ded95-92ed-4fb3-af37-f244b6967cc7)
Overall System Design
The smart car park monitoring system is devised to efficiently manage parking spaces by providing real-time updates on space availability. The system comprises various IoT nodes, each serving a specific purpose in the overall functionality.

Types of IoT Nodes and Their Roles:

Sensor Nodes: These include ultrasonic sensors and PIR (Passive Infrared) sensors. The ultrasonic sensors detect the presence of vehicles in parking spaces, while the PIR sensors detect motion in the vicinity of the parking spaces.
Hub/Gateway Node: This node serves as the central communication point for the sensor nodes, collecting data and transmitting it to the cloud or a local server for processing. The hub also controls the LED indicators, which display the availability of parking spaces.
Network Topology and Computing Paradigm:

The network topology follows a star configuration, where each sensor node communicates directly with the hub. This topology is selected for its simplicity and effectiveness in small to medium-sized networks, typical of parking lots. The computing paradigm employed is edge computing, where initial data processing occurs at the sensor nodes, reducing the data transmitted to the cloud and improving response times.

Messaging Protocols and Technologies:

The system uses MQTT (Message Queuing Telemetry Transport) as the primary messaging protocol. MQTT is lightweight and designed for efficient communication in low-bandwidth environments, making it ideal for IoT applications. Communication between nodes and the hub is facilitated by Wi-Fi, ensuring reliable and fast data transmission.

User Control and System Operation:

Users control the system setup and operation through a web interface or mobile application. This interface allows users to view real-time updates on parking space availability, configure sensor settings, and receive notifications. Administrators can also manage and monitor the system remotely, ensuring optimal performance and addressing issues promptly.

Additional Information:

The system is designed with scalability in mind, allowing for easy addition of more sensor nodes as the parking lot expands. Security measures, including encryption and authentication, protect data integrity and prevent unauthorized access. Power management strategies ensure the system remains energy-efficient, with sensor nodes utilizing low-power modes when not actively transmitting data.

Detailed Node Descriptions
1. Hub/Gateway Node

Role and Functionalities:
The hub/gateway node acts as the central communication point for the sensor nodes. It collects data from the ultrasonic and PIR sensors, processes this data, and determines the availability of parking spaces. The hub then controls the LED indicators, providing visual cues for available and occupied spaces. Additionally, the hub transmits data to the cloud for storage and further analysis, and it serves as the interface for user interaction through the web or mobile application.

Suitable Single Board Computers:

Raspberry Pi 3B+: The Raspberry Pi 3B+ is a popular choice due to its affordability, ease of use, and extensive community support. It has sufficient processing power and connectivity options (Wi-Fi, Ethernet) to serve as an effective hub.
Sensor Nodes (Ultrasonic and PIR Sensors)
Role and Functionalities:
The sensor nodes are responsible for detecting the presence of vehicles and motion within the parking spaces. The ultrasonic sensors measure the distance to the nearest object, determining if a vehicle is present in the space. The PIR sensors detect motion around the parking space, which can be used for security purposes or to detect if a vehicle is maneuvering into the space. These sensors transmit data to the hub for processing.

Suitable Single Board Computers:

Raspberry Pi Zero W: Due to its small size, low power consumption, and built-in Wi-Fi, the Raspberry Pi Zero W is a cost-effective option for sensor nodes. It can handle the data from ultrasonic and PIR sensors and transmit it to the hub.
ESP32: This microcontroller offers Wi-Fi and Bluetooth connectivity, making it suitable for wireless sensor nodes. Its low power consumption and adequate processing power make it a good choice for edge computing tasks.
Arduino Uno with Wi-Fi Shield: For simpler, cost-sensitive applications, the Arduino Uno with a Wi-Fi shield can be used. It provides sufficient processing power for basic sensor data collection and transmission.
 
The smart car park monitoring system effectively combines various IoT technologies to provide a robust solution for managing parking spaces. By utilizing ultrasonic and PIR sensors, a central hub, and modern communication protocols, the system ensures real-time monitoring and efficient utilization of parking resources. The use of single board computers like the Raspberry Pi and ESP32 allows for flexibility and scalability, accommodating future expansion and additional features. With a user-friendly interface and a strong emphasis on security, the system meets the needs of both end-users and administrators, enhancing the overall parking experience

Integration of Adafruit for System Management

In the smart car park monitoring system, instead of developing a custom website or mobile application for user interface and management, we opted to use Adafruit's platform for several key reasons:

Adafruit Platform Integration

Ease of Use and Rapid Deployment,
Built-in Dashboard and Data Visualization,
Data Integration and Management,
Remote Access and Control,
Security Features, and
Scalability and Flexibility
Setup Guide for Ultrasonic and PIR Sensors in the Smart Car Park Monitoring System
This guide provides a step-by-step process for setting up ultrasonic and PIR sensors with the smart car park monitoring system. The instructions are tailored for use with a Raspberry Pi (either Raspberry Pi Zero W or Raspberry Pi 3B+) and ESP32, as applicable.

Setup Guide for Ultrasonic and PIR Sensors
This guide provides the steps to set up ultrasonic and PIR sensors for the smart car park monitoring system. It includes hardware connections and basic configuration instructions.

1. Ultrasonic Sensor Setup
Components Needed:

HC-SR04 Ultrasonic Sensor
Raspberry Pi or ESP32
Jumper wires
Breadboard (optional)
Connections:

HC-SR04 Pinout:

VCC: Connect to 5V
Trig: Connect to a GPIO pin
Echo: Connect to a GPIO pin through a voltage divider
GND: Connect to Ground
Raspberry Pi:

Connect VCC to 5V (Pin 2).
Connect GND to Ground (Pin 6).
Connect Trig and Echo to GPIO pins (e.g., GPIO 23 and GPIO 24), using a voltage divider for Echo.
ESP32:

Connect VCC to 3.3V or 5V.
Connect GND to Ground.
Connect Trig and Echo to GPIO pins (e.g., GPIO 5 and GPIO 18), using a voltage divider for Echo.
2. PIR Sensor Setup
Components Needed:

PIR Sensor Module
Raspberry Pi or ESP32
Jumper wires
Connections:

PIR Sensor Pinout:

VCC: Connect to 5V or 3.3V
OUT: Connect to a GPIO pin
GND: Connect to Ground
Raspberry Pi:

Connect VCC to 5V (Pin 2) or 3.3V (Pin 1).
Connect GND to Ground (Pin 6).
Connect OUT to a GPIO pin (e.g., GPIO 17).
ESP32:

Connect VCC to 3.3V or 5V.
Connect GND to Ground.
Connect OUT to a GPIO pin (e.g., GPIO 15).
Conclusion
This guide covers the essential steps for connecting and configuring ultrasonic and PIR sensors with either a Raspberry Pi or ESP32. Ensure all connections are secure and verify sensor functionality as per your project's requirements.
![WhatsApp Image 2024-07-19 at 00 49 19_514ba76d](https://github.com/user-attachments/assets/ec5600a6-0c1a-4c63-aa64-26b5e1ea6da7)
![WhatsApp Image 2024-07-19 at 00 49 19_f32a4d79](https://github.com/user-attachments/assets/f71ae3c2-a26f-4504-8bd5-ff60c0dd708b)


