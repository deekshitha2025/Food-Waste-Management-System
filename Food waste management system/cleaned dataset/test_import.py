import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:Deekshu%4013@localhost/food_waste"
)

food = pd.read_csv(
    r"C:\Users\User\My Drive\Food waste management system\dataset\food_listings_data.csv"
)

food["Expiry_Date"] = pd.to_datetime(
    food["Expiry_Date"],
    format="%m/%d/%Y"
)

print(food.head())
print(food.shape)

food.to_sql(
    "food_listings",
    engine,
    if_exists="append",
    index=False
)

print("Food data imported successfully!")