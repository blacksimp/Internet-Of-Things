import RPi.GPIO as GPIO
import time
from Adafruit_IO import Client, Feed, RequestError

# GPIO Pins for Ultrasonic Sensor
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# GPIO Pin for LED
GPIO_US_LED = 27  # LED pin for ultrasonic sensor

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_US_LED, GPIO.OUT)

# Ensure LED is off by default
GPIO.output(GPIO_US_LED, GPIO.LOW)

# Adafruit IO setup
ADAFRUIT_IO_USERNAME = 'blacksimp'
ADAFRUIT_IO_KEY = 'aio_yORR29ifXc58LZAvskRSqHoTZIqI'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Create feeds if they don't exist
try:
    ultrasonic_feed = aio.feeds('ultrasonic-sensor')
except RequestError:
    feed = Feed(name='ultrasonic-sensor')
    ultrasonic_feed = aio.create_feed(feed)

# Print startup message
print("Smart car park system started")

def distance():
    # Ensure trigger is low
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.2)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Measure the response time of ECHO
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
        if start_time - stop_time > 0.1:  # Timeout for no response
            return -1

    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
        if stop_time - start_time > 0.1:  # Timeout for no response
            return -1

    # Calculate distance (in cm)
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound is 343m/s
    return round(distance, 2)

try:
    while True:
        dist = distance()
        if dist > 0 and dist < 400:  # Valid range for HC-SR04 is 2cm to 400cm
            print(f"Distance: {dist} cm")
            if dist < 50:  # Assuming a car is detected if distance is less than 50 cm
                print("Car detected")
            aio.send_data(ultrasonic_feed.key, dist)
            GPIO.output(GPIO_US_LED, GPIO.LOW)  # Turn off ultrasonic sensor LED
        else:
            print("Out of range")
            aio.send_data(ultrasonic_feed.key, 0)  # Send 0 to indicate out of range
            GPIO.output(GPIO_US_LED, GPIO.HIGH)  # Turn on ultrasonic sensor LED
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
