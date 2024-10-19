#basic logging
import logging

# Setting up the basic configuration for logging
logging.basicConfig(level=logging.INFO)

def process_data(data):
    if data:
        logging.info(f"Processing data: {data}")
    else:
        logging.warning("No data provided!")

# Test cases
process_data("Sample data")
process_data(None)

#using different log levels
logging.basicConfig(level=logging.DEBUG)

def divide_numbers(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        return None

# Test cases
divide_numbers(10, 2)
divide_numbers(10, 0)
