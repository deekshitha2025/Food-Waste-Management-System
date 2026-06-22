import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:Deekshu%4013@localhost/food_waste"
)

claims = pd.read_csv(
    r"C:\Users\User\My Drive\Food waste management system\dataset\claims_data.csv"
)

claims["Claim_Timestamp"] = pd.to_datetime(
    claims["Timestamp"]
)

claims = claims.drop(columns=["Timestamp"])

print(claims.head())
print(claims.shape)

claims.to_sql(
    "claims",
    engine,
    if_exists="append",
    index=False
)

print("Claims imported successfully!")