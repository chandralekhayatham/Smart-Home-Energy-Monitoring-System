from src.sensor import get_voltage
from src.sensor import get_current

from src.calculator import calculate_power
from src.calculator import calculate_energy
from src.calculator import calculate_cost

from src.alert import get_status
from src.dashboard import save_data

print("=" * 55)
print(" SMART HOME ENERGY MONITORING SYSTEM ")
print("=" * 55)

voltage = get_voltage()

current = get_current()

power = calculate_power(
    voltage,
    current
)

energy = calculate_energy(
    power
)

cost = calculate_cost(
    energy
)

status = get_status(
    power
)

save_data(
    voltage,
    current,
    power,
    energy,
    cost,
    status
)

print("\nVoltage :", voltage, "V")
print("Current :", current, "A")
print("Power   :", power, "W")
print("Energy  :", energy, "kWh")
print("Cost    : ₹", cost)
print("Status  :", status)

if status == "HIGH":
    print("\n🚨 ALERT : High Energy Consumption!")

elif status == "NORMAL":
    print("\n🟡 Energy Usage Normal")

else:
    print("\n🟢 Low Energy Consumption")

print("\nThank You for Using Smart Home Energy Monitoring System")