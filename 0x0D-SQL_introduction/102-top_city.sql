-- top 3 cities
SELECT city , AVG(value) as avg_temp 
FROM temperatures 
GROUP BY city 
WHERE MONTH = 7 OR MONTH = 8
ORDER BY avg_temp DESC
LIMIT 3;
