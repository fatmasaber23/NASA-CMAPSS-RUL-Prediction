import pandas as pd
from pathlib import Path


# Paths
raw_dir = Path("data/raw")
processed_dir = Path("data/processed")

# Create processed folder if it doesn't exist
processed_dir.mkdir(parents=True, exist_ok=True)


# Column names for C-MAPSS FD001
columns = [
    "engine_id",
    "cycle",
    "setting_1",
    "setting_2",
    "setting_3",
    "sensor_1",
    "sensor_2",
    "sensor_3",
    "sensor_4",
    "sensor_5",
    "sensor_6",
    "sensor_7",
    "sensor_8",
    "sensor_9",
    "sensor_10",
    "sensor_11",
    "sensor_12",
    "sensor_13",
    "sensor_14",
    "sensor_15",
    "sensor_16",
    "sensor_17",
    "sensor_18",
    "sensor_19",
    "sensor_20",
    "sensor_21"
]


# Train
train = pd.read_csv(
    raw_dir / "train_FD001.txt",
    sep=r"\s+",
    header=None,
    names=columns
)

train.to_csv(
    processed_dir / "train_FD001.csv",
    index=False
)


# Test
test = pd.read_csv(
    raw_dir / "test_FD001.txt",
    sep=r"\s+",
    header=None,
    names=columns
)

test.to_csv(
    processed_dir / "test_FD001.csv",
    index=False
)


# RUL
rul = pd.read_csv(
    raw_dir / "RUL_FD001.txt",
    header=None,
    names=["RUL"]
)

rul.to_csv(
    processed_dir / "RUL_FD001.csv",
    index=False
)


print("Conversion completed successfully!")
print(f"Train shape: {train.shape}")
print(f"Test shape:  {test.shape}")
print(f"RUL shape:   {rul.shape}")