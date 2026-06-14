# Smart-Home-Energy-Monitoring-System
IoT-based Smart Home Energy Monitoring System using Python Simulation for real-time energy usage tracking, electricity cost estimation, alert generation, and CSV data logging.
# Smart Home Energy Monitoring System

## Overview

The Smart Home Energy Monitoring System is an IoT-inspired project that monitors electrical parameters such as voltage, current, power consumption, and energy usage. It estimates electricity costs and generates alerts when energy consumption exceeds predefined limits.

---

## Features

- Real-Time Voltage Monitoring
- Current Monitoring
- Power Calculation
- Energy Consumption Tracking
- Electricity Cost Estimation
- High Energy Usage Alert
- CSV Data Logging
- Python-Based IoT Simulation

---

## Technologies Used

- Python
- IoT Concepts
- Sensor Simulation
- CSV File Handling

---

## Project Structure

Smart-Home-Energy-Monitoring-System

│

├── data

│ └── energy_data.csv

│

├── src

│ ├── __init__.py

│ ├── sensor.py

│ ├── calculator.py

│ ├── alert.py

│ └── dashboard.py

│

├── main.py

├── requirements.txt

└── README.md

---

## How to Run

```bash
pip install pandas matplotlib
python main.py
```

## Sample Output

```text
=======================================================
 SMART HOME ENERGY MONITORING SYSTEM
=======================================================

Voltage : 226 V
Current : 3.04 A
Power   : 687.04 W
Energy  : 0.69 kWh
Cost    : ₹ 5.52
Status  : NORMAL

🟡 Energy Usage Normal

Thank You for Using Smart Home Energy Monitoring System
```

## Applications

- Smart Homes
- Smart Buildings
- Hostels
- Energy Management
- Smart Cities

## Future Enhancements

- ESP32 Integration
- ACS712 Current Sensor
- ThingSpeak Dashboard
- Blynk Dashboard
- Mobile Notifications
- AI-Based Energy Prediction
