import pandas as pd
from datetime import datetime

def save_data(
    voltage,
    current,
    power,
    energy,
    cost,
    status
):

    data = {
        "Timestamp":[datetime.now()],
        "Voltage":[voltage],
        "Current":[current],
        "Power":[power],
        "Energy":[energy],
        "Cost":[cost],
        "Status":[status]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        "data/energy_data.csv",
        mode="a",
        index=False,
        header=False
    )