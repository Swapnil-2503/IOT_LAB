import Adafruit_DHT
import requests
import time

# Set the sensor type, GPIO pin, and ThingSpeak channel details
sensor = Adafruit_DHT.DHT11
pin = 4
channel_id = 123456  # Replace with your channel ID
write_key = 'YOUR_WRITE_API_KEY'  # Replace with your write API key

# Continuously read data from the sensor and send it to ThingSpeak
while True:
  humidity, temperature = Adafruit_DHT.read(sensor, pin)
  if humidity is not None and temperature is not None:
    print(f'Temperature: {temperature:0.1f}C, Humidity: {humidity:0.1f}%')
    payload = {'api_key': write_key, 'field1': temperature, 'field2': humidity}
    r = requests.post('https://api.thingspeak.com/update', params=payload)
  else:
    print('Failed to get reading. Try again!')
  time.sleep(60)