import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Generate synthetic energy consumption data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'meter_id': fake.uuid4(),
            'timestamp': fake.date_time_this_year(),
            'energy_consumption': round(np.random.uniform(0.5, 5.0), 2)
        }
        data.append(record)
    return pd.DataFrame(data)

# Generate 10,000 records of synthetic data
df = generate_data(5)
print(df.head())
