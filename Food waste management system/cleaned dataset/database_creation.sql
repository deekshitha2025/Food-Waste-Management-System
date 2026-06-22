CREATE DATABASE food_waste;
USE food_waste;
CREATE TABLE providers(
Provider_ID INT PRIMARY KEY,
Name VARCHAR(255),
Type VARCHAR(100),
Address TEXT,
City VARCHAR(100),
Contact VARCHAR(100)
);
CREATE TABLE receivers(
Receiver_ID INT PRIMARY KEY,
Name VARCHAR(255),
Type VARCHAR(100),
City VARCHAR(100),
Contact VARCHAR(100)
);
CREATE TABLE food_listings(
Food_ID INT PRIMARY KEY,
Food_Name VARCHAR(100),
Quantity INT,
Expiry_Date DATE,
Provider_ID INT,
Provider_Type VARCHAR(100),
Location VARCHAR(100),
Food_Type VARCHAR(50),
Meal_Type VARCHAR(50)
);
CREATE TABLE claims(
Claim_ID INT PRIMARY KEY,
Food_ID INT,
Receiver_ID INT,
Status VARCHAR(50),
Timestamp DATETIME
);
ALTER TABLE food_listings
ADD FOREIGN KEY (Provider_ID)
REFERENCES providers(Provider_ID);
ALTER TABLE claims
ADD FOREIGN KEY (Food_ID)
REFERENCES food_listings(Food_ID);
ALTER TABLE claims
ADD FOREIGN KEY (Receiver_ID)
REFERENCES receivers(Receiver_ID);