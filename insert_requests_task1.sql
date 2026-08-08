INSERT INTO genres(name)
VALUES('Rock'), ('Rap'), ('Pop'), ('Chanson'), ('Rock and roll');

INSERT INTO perfomers(name, genre)
VALUES('Rammstein', 'Rock'), ('Madonna', 'Pop'), ('Eminem', 'Rap'),
('AC/DC', 'Rock'), ('50 Cent', 'Rap'), ('Mikhail Krug', 'Chanson'),
('Metallica', 'Rock'), ('Elvis Presley', 'Rock and Roll');

INSERT INTO albums(name, year, perfomer)
VALUES('Live aus Berlin', 1999, 'Rammstein'), ('Encore', 2004, 'Eminen'),
('American Life', 2003, 'Madonna'), ('T.N.T', 1975, 'AC/DC'),
('Curtis', 2007, '50 Cent'), ('Zhigan-lemon', 1994, 'Michael Krug'),
('Loving You', 1957, 'Elvis Presley'), ('Black Album', 1991, 'Metallica');

INSERT INTO tracks(name, duration, album_id)
VALUES('Weisses Fleisch', 275, 1), ('Never Enough', 159, 2),
('Love Profusion', 216, 3), ('The Jack', 352, 4), ('Come & Go', 208, 5),
('Электричка', 186, 6), ('Loving You', 135, 7), ('Nothing Else Matters', 388, 8),
('Du hast', 267, 1), ('Big Weenie', 267, 2), ('Intervention', 294, 3),
('Rocker', 175, 4), ('Man Down', 169, 5), ('Осенний дождь', 341, 6),
('Weisses Fleisch', 106, 7);

INSERT INTO collections(name, year)
VALUES('Summer 2016', 2016), ('Tracks for Dance', 2017),
('Rock Legends', 2016), ('The King''s Music', 2021),
('Alternative Rock', 2019), ('Russina Music', 2020),
('American Rap', 2025), ('Romantic tracks', 2023);

INSERT INTO collection_track(track_id, collection_id)
VALUES (11, 1), (2, 1), (4, 2), (5, 2), (8, 3), (4, 3),
(7, 4), (15, 4), (1, 5), (9, 5), (6, 6), (14, 6),
(2, 7), (5, 7), (10, 7), (13, 7), (3, 8), (12, 3);

INSERT INTO genre_perfomer(genre_id, perfomer_id)
VALUES(1, 1), (3, 2), (2, 3), (1, 4), (2, 5),
(4, 6), (1, 7), (5, 8);

INSERT INTO perfomer_album(perfomer_id, album_id)
VALUES (1, 1), (2, 3), (3, 2), (4, 4),
(5, 5), (6, 6), (7, 8), (8, 7);