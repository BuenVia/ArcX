BEGIN;

-- Clear the entire database
DELETE FROM auth_user;
DELETE FROM document_titles;
DELETE FROM document_clients;
-- DROP TABLE client_app_clientuserpdf;

-- DROP TABLE IF EXISTS document_titles;
-- DROP TABLE IF EXISTS document_clients;

INSERT INTO auth_user (id, username, first_name, last_name, email, password, is_superuser, is_staff, is_active, date_joined)
VALUES 
    (1, 'admin', 'Admin', '', 'admin@example.com', 'pbkdf2_sha256$870000$ljSoPNg47pfEPaqMM68nTQ$9dsw6LFNeXiaDu+uUNGZwxdWUE+wuiT5XxTXEUHDf5A=', 1, 1, 1, CURRENT_TIMESTAMP),
    (2, 'test1', 'Test', 'Client 1', 'testclient1@example.com', 'pbkdf2_sha256$870000$ljSoPNg47pfEPaqMM68nTQ$9dsw6LFNeXiaDu+uUNGZwxdWUE+wuiT5XxTXEUHDf5A=', 0, 0, 1, CURRENT_TIMESTAMP),
    (3, 'test2', 'Test', 'Client 2', 'testclient2@example.com', 'pbkdf2_sha256$870000$ljSoPNg47pfEPaqMM68nTQ$9dsw6LFNeXiaDu+uUNGZwxdWUE+wuiT5XxTXEUHDf5A=', 0, 0, 1, CURRENT_TIMESTAMP),
    (4, 'test3', 'Test', 'Client 3', 'testclient3@example.com', 'pbkdf2_sha256$870000$ljSoPNg47pfEPaqMM68nTQ$9dsw6LFNeXiaDu+uUNGZwxdWUE+wuiT5XxTXEUHDf5A=', 0, 0, 1, CURRENT_TIMESTAMP);

-- CREATE TABLE IF NOT EXISTS document_titles (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     title varchar(255) NOT NULL
-- );
INSERT INTO document_titles (id, title) VALUES
    (1, '4.0 Repair Process'),
    (2, '4.4 People Processes'),
    (3, '4.5 Relevant Repair Methods'),
    (4, '4.6 Equipment and Tools'),
    (5, '4.7 Parts & Controlled Consumables'),
    (6, '4.8 Repair Task Control'),
    (7, '4.9 Use of Subcontractors'),
    (8, '5.0 Repair Process Management'),
    (9, '6.0 Claims of Conformity'),
    (10, '7.0 Customer Complaints'),
    (11, 'Internal Audits and Reports');


-- Step 1: Create the document_clients table if it does not exist
-- CREATE TABLE IF NOT EXISTS document_clients (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     document INTEGER REFERENCES document_titles(id) ON DELETE CASCADE,
--     user INTEGER REFERENCES auth_user(id) ON DELETE CASCADE,
--     uploaded BOOLEAN NOT NULL DEFAULT FALSE,
--     upload_date TIMESTAMP,
--     file TEXT
-- );

-- Step 2: Insert records into document_clients for each user and document
-- Assuming the documents are already inserted in the document_titles table
-- and have IDs from 1 to 11 in the correct order.

INSERT INTO document_clients (document_id, user_id, uploaded, upload_date, file)
VALUES
    (1, 2, FALSE, NULL, NULL), (2, 2, FALSE, NULL, NULL), (3, 2, FALSE, NULL, NULL), (4, 2, FALSE, NULL, NULL), (5, 2, FALSE, NULL, NULL),
    (6, 2, FALSE, NULL, NULL), (7, 2, FALSE, NULL, NULL), (8, 2, FALSE, NULL, NULL), (9, 2, FALSE, NULL, NULL), (10, 2, FALSE, NULL, NULL), (11, 2, FALSE, NULL, NULL),

    (1, 3, FALSE, NULL, NULL), (2, 3, FALSE, NULL, NULL), (3, 3, FALSE, NULL, NULL), (4, 3, FALSE, NULL, NULL), (5, 3, FALSE, NULL, NULL),
    (6, 3, FALSE, NULL, NULL), (7, 3, FALSE, NULL, NULL), (8, 3, FALSE, NULL, NULL), (9, 3, FALSE, NULL, NULL), (10, 3, FALSE, NULL, NULL), (11, 3, FALSE, NULL, NULL),

    (1, 4, FALSE, NULL, NULL), (2, 4, FALSE, NULL, NULL), (3, 4, FALSE, NULL, NULL), (4, 4, FALSE, NULL, NULL), (5, 4, FALSE, NULL, NULL),
    (6, 4, FALSE, NULL, NULL), (7, 4, FALSE, NULL, NULL), (8, 4, FALSE, NULL, NULL), (9, 4, FALSE, NULL, NULL), (10, 4, FALSE, NULL, NULL), (11, 4, FALSE, NULL, NULL);


COMMIT;