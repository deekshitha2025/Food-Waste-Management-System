import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:Deekshu%4013@localhost/food_waste"
)

providers = pd.read_csv(r"C:\Users\User\My Drive\Food waste management system\dataset\providers_data.csv")
receivers = pd.read_csv(r"C:\Users\User\My Drive\Food waste management system\dataset\receivers_data.csv")
food = pd.read_csv(r"C:\Users\User\My Drive\Food waste management system\dataset\food_listings_data.csv")
claims = pd.read_csv(r"C:\Users\User\My Drive\Food waste management system\dataset\claims_data.csv") 
food["Expiry_Date"] = pd.to_datetime(
    food["Expiry_Date"],
    format="%m/%d/%Y"
)

claims["Timestamp"] = pd.to_datetime(
    claims["Timestamp"]
)

providers.to_sql("providers", engine, if_exists="append", index=False)
receivers.to_sql("receivers", engine, if_exists="append", index=False)
# providers.to_sql("providers", engine, if_exists="append", index=False)
# receivers.to_sql("receivers", engine, if_exists="append", index=False)

food.to_sql("food_listings", engine, if_exists="append", index=False)
claims.to_sql("claims", engine, if_exists="append", index=False)

print("Data imported successfully!")