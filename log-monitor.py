import logging 
import time 
import random

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR,)
logging.basicConfig(level=logging.DEBUG,)


 # Create a logger 
logger = logging.getLogger("error-msg")
# Define log message formats 
formats = { logging.INFO: "HTTP 404 Not Found", 
           logging.DEBUG: "dependecies missing..", 
           logging.ERROR: "error messages",
          }

# Define log levels to cycle through 
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR,]

# Main loop to log messages 
while True:
    try: 
          #  Randomly select a log level 
         log_level = random.choice(log_levels)
          # Get the log message format for the selected log level
         log_message = formats[log_level]
          # Log the message 
         logger.log(log_level, log_message)

          # Sleep for a short interval 
         time.sleep(0.2)
    except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C)
             print("\nLogging interrupted. Exiting. DUE TO KEYBOARD INTERRUPTION") 
             break
