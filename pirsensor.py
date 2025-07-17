import RPi.GPIO as GPIO
import time
from Adafruit_IO import Client, Feed, RequestError

# GPIO Pin for PIR Sensor
GPIO_PIR = 16
GPIO_LED = 17  # LED for PIR sensor

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIR, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT)

# Ensure LED is off by default
GPIO.output(GPIO_LED, GPIO.LOW)


# Adafruit IO setup
ADAFRUIT_IO_USERNAME = 'blacksimp'
ADAFRUIT_IO_KEY = 'aio_yORR29ifXc58LZAvskRSqHoTZIqI'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Create feeds if they don't exist
try:
    pir_feed = aio.feeds('pirsensor')
except RequestError:
    feed = Feed(name='pirsensor')
    pir_feed = aio.create_feed(feed)

# Print startup message
print("PIR sensor system started")

try:
    while True:
        if GPIO.input(GPIO_PIR):
            print("Motion detected!")
            aio.send_data(pir_feed.key, 1)  # Send 1 to indicate motion detected
            GPIO.output(GPIO_LED, GPIO.HIGH)  # Turn on PIR sensor LED
        else:
            aio.send_data(pir_feed.key, 0)  # Send 0 to indicate no motion
            GPIO.output(GPIO_LED, GPIO.LOW)  # Turn off PIR sensor LED
        time.sleep(1)

except KeyboardInterrupt:
    print("Motion detection stopped by User")
    GPIO.cleanup()
