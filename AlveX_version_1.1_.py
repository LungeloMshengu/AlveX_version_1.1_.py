import random
import csv
import time
import os
from datetime import datetime

# ==========================================
# ALVEX TECHNOLOGIES
# MACHINE INTELLIGENCE V1.1
# ==========================================

MAX_TEMPERATURE = 80
MAX_VIBRATION = 8.0

TOTAL_CYCLES = 5

# Ten independent factory motors
machines = [
    {"id": "MOTOR-001", "warnings": 0},
    {"id": "MOTOR-002", "warnings": 0},
    {"id": "MOTOR-003", "warnings": 0},
    {"id": "MOTOR-004", "warnings": 0},
    {"id": "MOTOR-005", "warnings": 0},
    {"id": "MOTOR-006", "warnings": 0},
    {"id": "MOTOR-007", "warnings": 0},
    {"id": "MOTOR-008", "warnings": 0},
    {"id": "MOTOR-009", "warnings": 0},
    {"id": "MOTOR-010", "warnings": 0}
]

# Statistics
total_readings = 0
total_alerts = 0
normal_readings = 0

# 1. Read machine temperature
def read_machine_temperature():
    return random.randint(35, 100)


# 2. Read machine vibration
def vibration_level():
    return round(random.uniform(1, 12), 2)


# 3. Detect abnormalities
def abnormal_readings(temperature, vibration):

    problems = []

    if temperature > MAX_TEMPERATURE:
        problems.append("HIGH TEMPERATURE")

    if vibration > MAX_VIBRATION:
        problems.append("EXCESSIVE VIBRATION")

    return problems


# 4. Generate individual warnings
def generate_warnings(machine_id, problems):

    if problems:
        print("WARNING:", machine_id)

        for problem in problems:
            print("  ALERT:", problem)

        return 1

    print("STATUS:", machine_id, "NORMAL")
    return 0


# 5. Save machine readings
def save_readings(machine_id, temperature,
                  vibration, problems):

    filename = "alvex_factory_data.csv"

    file_exists = os.path.exists(filename)
    needs_header = (
        not file_exists or os.path.getsize(filename) == 0
    )

    with open(filename, "a", newline="") as file:

        writer = csv.writer(file)

        if needs_header:
            writer.writerow([
                "Timestamp",
                "Machine ID",
                "Temperature",
                "Vibration",
                "Status",
                "Problems"
            ])

        status = "ABNORMAL" if problems else "NORMAL"

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            machine_id,
            temperature,
            vibration,
            status,
            "; ".join(problems)
        ])


# 6. Main monitoring system
def start_machine_monitor():

    global total_readings
    global total_alerts
    global normal_readings

    print("\n================================")
    print(" ALVEX MACHINE INTELLIGENCE")
    print(" VERSION 1.1")
    print("================================")

    for cycle in range(1, TOTAL_CYCLES + 1):

        print("\nFACTORY MONITORING CYCLE:", cycle)
        print("--------------------------------")

        for machine in machines:

            machine_id = machine["id"]

            temperature = read_machine_temperature()
            vibration = vibration_level()

            print("\nMachine:", machine_id)
            print("Temperature:", temperature, "C")
            print("Vibration:", vibration, "mm/s")

            problems = abnormal_readings(
                temperature, vibration
            )

            alert = generate_warnings(
                machine_id, problems
            )

            machine["warnings"] += alert

            total_readings += 1
            total_alerts += alert

            if not problems:
                normal_readings += 1

            save_readings(
                machine_id,
                temperature,
                vibration,
                problems
            )

        print("\nCycle", cycle, "completed.")
        print("--------------------------------")

        time.sleep(1)


# 7. Factory performance report
def factory_report():

    print("\n================================")
    print(" ALVEX FACTORY PERFORMANCE REPORT")
    print("================================")

    print("Machines monitored:", len(machines))
    print("Total readings:", total_readings)
    print("Normal readings:", normal_readings)
    print("Abnormal readings:", total_alerts)

    print("\nINDIVIDUAL MACHINE REPORT")

    for machine in machines:

        print(
            machine["id"],
            "| Warnings:",
            machine["warnings"]
        )

    print("\nMonitoring session completed.")
    print("Data saved to alvex_factory_data.csv")


# 8. Start the system
start_machine_monitor()
factory_report()