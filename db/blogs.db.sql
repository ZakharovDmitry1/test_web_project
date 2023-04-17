--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.0 в Пн апр 17 07:58:47 2023
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: jobs
CREATE TABLE IF NOT EXISTS jobs (
	id INTEGER NOT NULL, 
	team_leader INTEGER, 
	job VARCHAR, 
	work_size INTEGER, 
	collaborators VARCHAR, 
	start_date DATE, 
	end_date DATE, 
	is_finished BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(team_leader) REFERENCES users (id)
);
INSERT INTO jobs (id, team_leader, job, work_size, collaborators, start_date, end_date, is_finished) VALUES (1, 1, 'deployment of residential modules 1 and 2', 15, '2, 3, 4', '2023-04-11', '2023-04-12 12:02:02', 0);
INSERT INTO jobs (id, team_leader, job, work_size, collaborators, start_date, end_date, is_finished) VALUES (2, 2, 'deployment of ewdcdcsdc modules 1 and 2', 23, '1, 2, 5, 7', '2023-04-11', '2023-04-12 12:02:02', 1);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
