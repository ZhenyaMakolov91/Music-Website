SELECT COUNT(name), genre FROM perfomers -- 1
GROUP BY genre;

SELECT a.name, a.year, COUNT(t.name) count_tracks FROM tracks t -- 2
JOIN albums a ON a.id = t.album_id
WHERE year IN (2019, 2020)
GROUP BY t.album_id, a.year, a.name;


SELECT a.name, AVG(t.duration) FROM tracks t -- 3
JOIN albums a ON a.id = t.album_id
GROUP BY a.name, a.id;

SELECT p.name FROM perfomers p -- 4
JOIN albums a ON p.name = a.perfomer
WHERE a.year != 2020;

SELECT DISTINCT c.name FROM collections c -- 5
JOIN collection_track ct ON c.id = ct.collection_id
JOIN tracks t ON ct.track_id = t.id
JOIN albums a ON t.album_id = a.id
WHERE a.perfomer = 'AC/DC';

SELECT a.name FROM albums a -- 6
JOIN perfomer_album pa ON pa.album_id = a.id
JOIN genre_perfomer gp ON gp.perfomer_id = pa.perfomer_id
GROUP BY a.name
HAVING COUNT(pa.perfomer_id) > 1;

SELECT t.name FROM tracks t -- 7
LEFT JOIN collection_track ct ON t.id = ct.track_id
WHERE ct.collection_id IS NULL;

SELECT p.name FROM perfomers p -- 8
JOIN perfomer_album pa ON p.id = pa.perfomer_id
JOIN tracks t ON pa.album_id = t.album_id
WHERE t.duration = (SELECT MIN(duration) FROM tracks);

SELECT a.name FROM tracks t -- 9
JOIN albums a ON t.album_id = a.id
GROUP BY a.name
HAVING COUNT(t.name)= (SELECT MIN(count) FROM (
					   SELECT COUNT(t.name) FROM tracks t
					   JOIN albums a ON t.album_id = a.id
					   GROUP BY a.name));