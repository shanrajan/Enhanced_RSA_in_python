import datetime

# Get the current system time with microseconds
system_time = datetime.datetime.now()

# Print the microseconds part
microseconds_part = system_time.microsecond
print(f"Microseconds: {microseconds_part}")

