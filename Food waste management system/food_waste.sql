USE food_waste;
SELECT City, COUNT(*) AS Total_Providers
FROM providers
GROUP BY City
ORDER BY Total_Providers DESC;
SELECT City, COUNT(*) AS Total_Receivers
FROM receivers
GROUP BY City
ORDER BY Total_Receivers DESC;
SELECT
Provider_Type,
SUM(Quantity) AS Total_Quantity
FROM food_listings
GROUP BY Provider_Type
ORDER BY Total_Quantity DESC;
SELECT Name, Contact
FROM providers
WHERE City = 'New Jessica';
SELECT
Receiver_ID,
COUNT(*) AS Total_Claims
FROM claims
GROUP BY Receiver_ID
ORDER BY Total_Claims DESC
LIMIT 10;
SELECT SUM(Quantity) AS Total_Food_Available
FROM food_listings;
SELECT
Location,
COUNT(*) AS Total_Listings
FROM food_listings
GROUP BY Location
ORDER BY Total_Listings DESC;
SELECT
Food_Type,
COUNT(*) AS Count
FROM food_listings
GROUP BY Food_Type
ORDER BY Count DESC;
SELECT
Food_ID,
COUNT(*) AS Total_Claims
FROM claims
GROUP BY Food_ID
ORDER BY Total_Claims DESC;
SELECT
f.Provider_ID,
COUNT(*) AS Successful_Claims
FROM claims c
JOIN food_listings f
ON c.Food_ID = f.Food_ID
WHERE c.Status = 'Completed'
GROUP BY f.Provider_ID
ORDER BY Successful_Claims DESC;
SELECT
Status,
COUNT(*) * 100.0 /
(SELECT COUNT(*) FROM claims) AS Percentage
FROM claims
GROUP BY Status;
SELECT
c.Receiver_ID,
AVG(f.Quantity) AS Avg_Quantity
FROM claims c
JOIN food_listings f
ON c.Food_ID = f.Food_ID
GROUP BY c.Receiver_ID
ORDER BY Avg_Quantity DESC;
SELECT
f.Meal_Type,
COUNT(*) AS Total_Claims
FROM claims c
JOIN food_listings f
ON c.Food_ID = f.Food_ID
GROUP BY f.Meal_Type
ORDER BY Total_Claims DESC;
SELECT
Provider_ID,
SUM(Quantity) AS Total_Donated
FROM food_listings
GROUP BY Provider_ID
ORDER BY Total_Donated DESC;
SELECT
Provider_ID,
SUM(Quantity) AS Total_Donated
FROM food_listings
GROUP BY Provider_ID
ORDER BY Total_Donated DESC
LIMIT 10;