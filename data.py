# import pandas as pd

# climate_watch_GCP = pd.read_csv("CW_HistoricalEmissions_GCP.csv")
# climate_watch_GCP.head() 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("All libraries imported successfully!")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")

# Quick test
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("\nTest DataFrame:")
print(df)