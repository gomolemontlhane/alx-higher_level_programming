-- List all cities with their corresponding states using a JOIN operation
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;

