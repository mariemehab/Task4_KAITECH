sensor_data = [
("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
]
#    Organize readings per sensor.
organized_data = {}
for record in sensor_data:
    sensor_id = record[0]
    reading = record[1:]  # Exclude sensor_id
    if sensor_id not in organized_data:
        organized_data[sensor_id] = []
    organized_data[sensor_id].append(reading)

# Displaying the organized data
for sensor_id in organized_data:
    print(sensor_id + ":")
    for reading in organized_data[sensor_id]:
        print(" ", reading)
###############################################3
#    Identify unique sensors with extreme values.
# إextreme values
max_temp = max([row[2] for row in sensor_data])
max_stress = max([row[3] for row in sensor_data])
max_disp = max([row[4] for row in sensor_data])

extreme_sensors = set()

for row in sensor_data:
    sensor_id, _, temp, stress, disp = row
    if temp == max_temp or stress == max_stress or disp == max_disp:
        extreme_sensors.add(sensor_id)

print("Sensors with extreme values:", extreme_sensors)
    ####################################################
#    Compare readings from different time intervals.
sensor_dict = {}

for sensor_id, timestamp, temp, stress, disp in sensor_data:
    if sensor_id not in sensor_dict:
        sensor_dict[sensor_id] = []
    sensor_dict[sensor_id].append((timestamp, temp, stress, disp))
for sensor_id, readings in sensor_dict.items():
    readings.sort(key=lambda x: x[0])  # ترتيب حسب الوقت
    first = readings[0]
    last = readings[-1]
    print(f"\nSensor {sensor_id}:")
    print(f"  First Reading : Temp={first[1]}, Stress={first[2]}, Disp={first[3]}")
    print(f"  Last Reading  : Temp={last[1]}, Stress={last[2]}, Disp={last[3]}")
    print("  Changes:")
    print(f"    ΔTemp   = {last[1] - first[1]:.2f}")
    print(f"    ΔStress = {last[2] - first[2]:.2f}")
    print(f"    ΔDisp   = {last[3] - first[3]:.5f}")
######################################################################
#    Summarize the data by calculating max, min, and average readings per sensor.
# Group data by sensor
grouped_by_sensor = {}
for record in sensor_data:
    sensor_id = record[0]

    if sensor_id not in grouped_by_sensor:
        grouped_by_sensor[sensor_id] = {"temps": [], "stresses": [], "displacements": []}

    # Collect the readings for each sensor
    grouped_by_sensor[sensor_id]["temps"].append(record[2])
    grouped_by_sensor[sensor_id]["stresses"].append(record[3])
    grouped_by_sensor[sensor_id]["displacements"].append(record[4])

# Calculate max, min, and average for each sensor
for sensor_id, values in grouped_by_sensor.items():
    temps = values["temps"]
    stresses = values["stresses"]
    displacements = values["displacements"]

    # Calculate max, min, and average for temperature
    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = sum(temps) / len(temps)

    # Calculate max, min, and average for stress
    max_stress = max(stresses)
    min_stress = min(stresses)
    avg_stress = sum(stresses) / len(stresses)

    # Calculate max, min, and average for displacement
    max_disp = max(displacements)
    min_disp = min(displacements)
    avg_disp = sum(displacements) / len(displacements)

    # Print the summary for each sensor
    print(f"Sensor {sensor_id}:")
    print(f"  Max Temp: {max_temp}, Min Temp: {min_temp}, Avg Temp: {avg_temp}")
    print(f"  Max Stress: {max_stress}, Min Stress: {min_stress}, Avg Stress: {avg_stress}")
    print(f"  Max Displacement: {max_disp}, Min Displacement: {min_disp}, Avg Displacement: {avg_disp}")
    print()
####################################################################3
# Group data by sensor_id using a dictionary
grouped_by_sensor = {}

for record in sensor_data:
    sensor_id = record[0]

    # If the sensor is not already in the dictionary, initialize the key with an empty list
    if sensor_id not in grouped_by_sensor:
        grouped_by_sensor[sensor_id] = []

    # Append the current reading (tuple) to the list corresponding to the sensor_id
    grouped_by_sensor[sensor_id].append(record)

# Display the grouped data
for sensor_id, readings in grouped_by_sensor.items():
    print(f"Sensor {sensor_id}:")
    for reading in readings:
        print(f"  {reading}")
    print()
###################################################
# Create a set to store unique sensor IDs that recorded stress > 13.0
sensors_above_13_stress = set()

for record in sensor_data:
    stress = record[3]
    sensor_id = record[0]

    # Check if stress is greater than 13.0 and add the sensor_id to the set
    if stress > 13.0:
        sensors_above_13_stress.add(sensor_id)

# Display the unique sensor IDs
print("Sensors with stress > 13.0:", sensors_above_13_stress)
####################################################################

# Group data by sensor
grouped_by_sensor = {}

for record in sensor_data:
    sensor_id = record[0]

    if sensor_id not in grouped_by_sensor:
        grouped_by_sensor[sensor_id] = {"temps": [], "stresses": [], "displacements": []}

    # Collect the readings for each sensor
    grouped_by_sensor[sensor_id]["temps"].append(record[2])
    grouped_by_sensor[sensor_id]["stresses"].append(record[3])
    grouped_by_sensor[sensor_id]["displacements"].append(record[4])

# Calculate statistics for each sensor
for sensor_id, values in grouped_by_sensor.items():
    temps = values["temps"]
    stresses = values["stresses"]
    displacements = values["displacements"]

    # Calculate max, min, and average for temperature
    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = sum(temps) / len(temps)

    # Calculate max, min, and average for stress
    max_stress = max(stresses)
    min_stress = min(stresses)
    avg_stress = sum(stresses) / len(stresses)

    # Calculate max, min, and average for displacement
    max_disp = max(displacements)
    min_disp = min(displacements)
    avg_disp = sum(displacements) / len(displacements)

    # Print the summary for each sensor
    print(f"Sensor {sensor_id}:")
    print(f"  Max Temp: {max_temp}, Min Temp: {min_temp}, Avg Temp: {avg_temp}")
    print(f"  Max Stress: {max_stress}, Min Stress: {min_stress}, Avg Stress: {avg_stress}")
    print(f"  Max Displacement: {max_disp}, Min Displacement: {min_disp}, Avg Displacement: {avg_disp}")
    print()

################################################333
# Group data by sensor
grouped_by_sensor = {}

for record in sensor_data:
    sensor_id = record[0]

    if sensor_id not in grouped_by_sensor:
        grouped_by_sensor[sensor_id] = {"temps": []}

    # Collect the temperature readings for each sensor
    grouped_by_sensor[sensor_id]["temps"].append(record[2])

# Calculate max, min, and average temperature for each sensor
for sensor_id, values in grouped_by_sensor.items():
    temps = values["temps"]

    # Calculate max, min, and average for temperature
    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = sum(temps) / len(temps)

    # Print the summary for temperature
    print(f"Sensor {sensor_id}:")
    print(f"  Max Temp: {max_temp}")
    print(f"  Min Temp: {min_temp}")
    print(f"  Avg Temp: {avg_temp}")
    print()
############################################
# Find max displacement
max_displacement = 0
for record in sensor_data:
    if record[4] > max_displacement:
        max_displacement = record[4]

print("Max Displacement:", max_displacement)
###################################################33
# Extract all timestamps
timestamps = []
for record in sensor_data:
    timestamps.append(record[1])

# Sort the timestamps (format allows string sorting)
for i in range(len(timestamps)):
    for j in range(i + 1, len(timestamps)):
        if timestamps[j] < timestamps[i]:
            timestamps[i], timestamps[j] = timestamps[j], timestamps[i]

print("Sorted Timestamps:")
for t in timestamps:
    print(t)
###################################################
# Store most recent reading per sensor
latest_readings = {}

for record in sensor_data:
    sensor_id = record[0]
    timestamp = record[1]

    # If sensor is new or current record is more recent, update
    if sensor_id not in latest_readings or timestamp > latest_readings[sensor_id][1]:
        latest_readings[sensor_id] = record

# Convert to list of tuples
most_recent_readings = []
for sensor_id in latest_readings:
    most_recent_readings.append(latest_readings[sensor_id])

print("Most Recent Readings per Sensor:")
for r in most_recent_readings:
    print(r)
