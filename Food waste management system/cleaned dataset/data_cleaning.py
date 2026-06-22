import pandas as pd

providers = pd.read_csv("dataset/providers_data.csv")
receivers = pd.read_csv("dataset/receivers_data.csv")
food = pd.read_csv("dataset/food_listings_data.csv")
claims = pd.read_csv("dataset/claims_data.csv")
print(providers.head())
print(receivers.head())
print(food.head())
print(claims.head())
print(providers.info())
print(receivers.info())
print(food.info())
print(claims.info())
print(providers.isnull().sum())
print(receivers.isnull().sum())
print(food.isnull().sum())
print(claims.isnull().sum())
print(providers.duplicated().sum())
print(receivers.duplicated().sum())
print(food.duplicated().sum())
print(claims.duplicated().sum())
providers.drop_duplicates(inplace=True)
receivers.drop_duplicates(inplace=True)
food.drop_duplicates(inplace=True)
claims.drop_duplicates(inplace=True)
print(food.dtypes)
print(claims.dtypes)
food["Expiry_Date"] = pd.to_datetime(food["Expiry_Date"])

claims["Timestamp"] = pd.to_datetime(
    claims["Timestamp"]
)
providers["City"] = providers["City"].str.title()
receivers["City"] = receivers["City"].str.title()
food["Location"] = food["Location"].str.title()
providers.to_csv(
    "dataset/providers_clean.csv",
    index=False
)

receivers.to_csv(
    "dataset/receivers_clean.csv",
    index=False
)

food.to_csv(
    "dataset/food_clean.csv",
    index=False
)

claims.to_csv(
    "dataset/claims_clean.csv",
    index=False
)
print(providers.info())
print(receivers.info())
print(food.info())
print(claims.info())

providers.to_csv("dataset/providers_clean.csv", index=False)

receivers.to_csv("dataset/receivers_clean.csv", index=False)

food.to_csv("dataset/food_clean.csv", index=False)

claims.to_csv("dataset/claims_clean.csv", index=False)

print("Cleaned files saved successfully")