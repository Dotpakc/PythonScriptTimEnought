-- CREATE TABLE IF NOT EXISTS "user"(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     email VARCHAR(255) NOT NULL UNIQUE
-- );

-- INSERT INTO "user" (name, email) VALUES ('John Doe', '223@exam.ww');
-- INSERT INTO "user" (name, email) VALUES ('Mari DOe', 'Mdsfsdfari@exam.ww');
-- INSERT INTO "user" (name, email) VALUES ('John Doe', 'joundd@exam.ww');
-- INSERT INTO "user"(id,name, email) VALUES (10,'Вася', 'vasya@gmail.com');
-- INSERT INTO "user"(name, email) VALUES ('Оля', 'olya@gmail.com');
-- INSERT INTO "user"(name, email) VALUES ('Гаврила', 'gavrila@gmail.com');



-- SELECT * FROM "user" ;
-- SELECT email FROM "user" WHERE id = 11;
-- SELECT email FROM "user" WHERE id < 8;

-- SELECT email FROM "user" WHERE id < 8 OR id > 10;

-- DELETE FROM "user" WHERE name = 'John Doe';
-- DELETE FROM "user" WHERE id = 10;


-- DROP TABLE IF EXISTS "user";


-- CREATE TABLE IF NOT EXISTS "article"(
--     id SERIAL PRIMARY KEY,
--     title VARCHAR(255),
--     content TEXT,
--     user_id INTEGER CONSTRAINT fk_user_id REFERENCES "user"(id),
--     date DATE NOT NULL,
--     create_at TIMESTAMP,
--     update_at TIMESTAMP NOT NULL
-- );

-- INSERT INTO article (title, content, user_id, date, create_at, update_at) 
-- VALUES ('Интересная статья sdf', 'текст интересной статьи', 17, '2021-01-01', '2021-01-01', '2021-01-01');
-- INSERT INTO article (title, content, user_id, date, create_at, update_at) 
-- VALUES ('Интересная статья2312', 'текст интересной статьи', 19, NOW(), NOW(), NOW());

-- INSERT INTO article (title, content, user_id, date, create_at, update_at) 
-- VALUES ('Интересная dsfsdfстатья', 'текст интересной статьи', 20, '2021-01-01', '2021-01-01', '2021-01-01');
-- INSERT INTO article (title, content, user_id, date, create_at, update_at) 
-- VALUES ('Интересная статьяfsdfsdf', 'текст интересной статьи', 20, NOW(), NOW(), NOW());


-- UPDATE "user" SET name = 'Вася Пупкин' , email = 'jounbdd@exam.ww' WHERE id = 10;
-- UPDATE "user" SET name = 'JJ' WHERE id = 21;
-- UPDATE "user" SET name = 'sdgfsdg' WHERE id = 5;
-- UPDATE "user" SET name = 'sdgsdg' WHERE id = 24;


-- SELECT * FROM "user" ORDER BY id ASC;
-- SELECT * FROM "user" ORDER BY id DESC;

-- create table tag
-- (
--     id  serial primary key,
--     name varchar(255) not null UNIQUE
-- );

-- create table article_tag
-- (
--     article_id integer not null,
--     tag_id     integer not null,
--     constraint article_tag_article_id_fkey
--         foreign key (article_id) references article (id) on UPDATE CASCADE on DELETE CASCADE,
--     constraint article_tag_tag_id_fkey
--         foreign key (tag_id) references tag (id) ON UPDATE CASCADE on DELETE CASCADE
-- );

-- INSERT INTO tag (name) VALUES ('tag1');
-- INSERT INTO tag (name) VALUES ('tag2');
-- INSERT INTO tag (name) VALUES ('tag3');

-- INSERT INTO article_tag (article_id, tag_id) VALUES (2, 1);
-- INSERT INTO article_tag (article_id, tag_id) VALUES (2, 2);
-- INSERT INTO article_tag (article_id, tag_id) VALUES (3, 1);
-- INSERT INTO article_tag (article_id, tag_id) VALUES (4, 2);
-- INSERT INTO article_tag (article_id, tag_id) VALUES (5, 1);
-- INSERT INTO article_tag (article_id, tag_id) VALUES (5, 2);
-- INSERT INTO article_tag (article_id, tag_id) VALUES (6, 3);
-- INSERT INTO article_tag (article_id, tag_id) VALUES (2, 3);

-- SELECT a.title,a.content,a.date, u.name from article as a 
--     LEFT JOIN "user" u on u.id = a.user_id 
--     WHERE u.id = 10;

-- SELECT * FROM article_tag as at
--     LEFT JOIN article as a on a.id = at.article_id
--     LEFT JOIN tag as t on t.id = at.tag_id
--     WHERE t.id = 3;



SELECT * FROM article_tag as at
    LEFT JOIN article as a on a.id = at.article_id
    LEFT JOIN tag as t on t.id = at.tag_id
    WHERE t.id = 3;

ALTER USER користувач SET search_path = public, "$user", public ADDITIONAL_ROLES;