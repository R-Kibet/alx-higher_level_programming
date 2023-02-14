-- showing max value of temp
SELECT state , MAX(value) as max_temp FROM temperatures
ORDER BY state 
LIMIT 3;
