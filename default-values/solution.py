-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO videos (id, name, is_published) INSERT INTO videos (id, name, is_published) 
VALUES (1, 'My Video', true),VALUES (1, 'My Video', true),
       (2, 'Another Video', false);       (2, 'Another Video', false);

INSERT INTO videos (id)INSERT INTO videos (id)
VALUES (3),VALUES (3),
       (4);       (4);




INSERT INTO videos (name)INSERT INTO videos (name)
VALUES ('Video with no ID');VALUES ('Video with no ID');

SELECT * FROM videos;SELECT * FROM videos;
