import RPi.GPIO as GPIO
import vlc
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that the button is connected to
button_pin = 26

# Set up the button pin as an input with a pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define a callback function to run when the button is pressed
def button_callback(channel):
    print("GPIO 26 pressed")
    media_player = vlc.MediaPlayer()
    media = vlc.Media("Thayna_Test.avi")
    media_player.set_media(media)
    media_player.play()
    time.sleep(15)
    media_player.release()
    
# Add the button callback function to the button pin
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback)

# Keep the script running
while True:
    pass