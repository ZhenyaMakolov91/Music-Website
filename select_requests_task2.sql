SELECT name, year FROM albums -- 1
WHERE year = 2018;

SELECT name, duration FROM tracks -- 2
ORDER BY duration DESC
LIMIT 1;

SELECT name FROM tracks
WHERE duration >= 210; -- 3

SELECT name FROM collections -- 4
WHERE year between 2018 AND 2020;

SELECT name FROM perfomers -- 5
WHERE name NOT LIKE '% %';

SELECT name FROM tracks -- 6
WHERE name LIKE '%my%' OR name LIKE '%My%';