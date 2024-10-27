BEGIN;

-- Clear the entire database
DELETE FROM auth_user;
DELETE FROM document_titles;
DELETE FROM document_clients;
DELETE FROM staff;
DELETE FROM role_names;
DELETE FROM qualification;
DELETE FROM staff_role;
DELETE FROM staff_qualification;


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


-- Populate Staff table with predefined IDs
INSERT INTO staff (id, first_name, last_name, staff_id, user_id) VALUES
    (1, 'John', 'Doe', 'JD001', 2),
    (2, 'Jane', 'Smith', 'JS002', 2),
    (3, 'Alice', 'Brown', 'AB003', 2),
    (4, 'Robert', 'Davis', 'RD004', 2),
    (5, 'Laura', 'Wilson', 'LW005', 2),
    
    (6, 'Tom', 'Taylor', 'TT006', 3),
    (7, 'Lucy', 'Adams', 'LA007', 3),
    (8, 'Ethan', 'Clark', 'EC008', 3),
    (9, 'Olivia', 'Johnson', 'OJ009', 3),
    (10, 'Daniel', 'Martinez', 'DM010', 3),
    
    (11, 'Emily', 'Lopez', 'EL011', 4),
    (12, 'Aaron', 'Hall', 'AH012', 4),
    (13, 'Sophia', 'Lee', 'SL013', 4),
    (14, 'Michael', 'Young', 'MY014', 4),
    (15, 'Grace', 'Harris', 'GH015', 4);

-- Populate Roles table with predefined IDs for consistency
INSERT INTO role_names (id, role_name) VALUES
    (1, 'VDA'),
    (2, 'MET'),
    (3, 'PNL'),
    (4, 'PNT');

-- Populating the Qualification table with qualification names, durations, and role IDs
INSERT INTO qualification (qualification_name, duration, role_id) VALUES
    ('VDA Qual', NULL, 1),
    ('MET Qual', NULL, 2),
    ('PNL Qual', NULL, 3),
    ('PNT Qual', NULL, 4),
    ('Audatex', 12, 1),
    ('GEOM AOM220', NULL, 2),
    ('ADAS AOM230', NULL, 2),
    ('Glazing', 36, 2),
    ('F Gas', NULL, 2),
    ('Hybrid', 36, 2),
    ('HEV Aware', NULL, 2),
    ('1140 Spot', 24, 3),
    ('4872 MIG', 24, 3),
    ('Braze', 24, 3),
    ('Boron', 24, 3),
    ('AOM009', 24, 3),
    ('St Bond', 36, 3),
    ('Rivet', 36, 3),
    ('AOM030', 36, 3),
    ('AOM028', 36, 3),
    ('AOM032', 36, 3);


-- Populate StaffRole table, adding MET and PNL roles for applicable staff
INSERT INTO staff_role (staff_id, role_id) VALUES
    (1, 1), -- VDA
    (2, 2), (2, 3), -- MET, PNL
    (3, 4), -- PNT
    (4, 2), (4, 3), -- MET, PNL
    (5, 1), -- VDA
    
    (6, 4), -- PNT
    (7, 2), (7, 3), -- MET, PNL
    (8, 1), -- VDA
    (9, 2), (9, 3), -- MET, PNL
    (10, 4), -- PNT
    
    (11, 1), -- VDA
    (12, 2), (12, 3), -- MET, PNL
    (13, 4), -- PNT
    (14, 2), (14, 3), -- MET, PNL
    (15, 1); -- VDA

-- Example insertion for the `StaffQualification` table
-- Ensure that dates are within a valid range and assigned to staff based on their roles.

-- Select a random subset of staff for qualification assignment.
-- Assign 1-3 qualifications per staff member.

INSERT INTO staff_qualification (staff_id, qualification_id, qualification_date)
VALUES 
    -- Qualifications for a VDA staff member
    (1, 1, '2022-01-15'), -- VDA Qual
    (1, 5, '2023-03-10'), -- Audatex

    -- Qualifications for a MET and PNL staff member (dual-role)
    (2, 2, '2022-02-20'), -- MET Qual
    (2, 7, '2023-04-25'), -- ADAS AOM230

    -- More qualifications for another staff member with MET and PNL roles
    (3, 2, '2022-05-22'), -- MET Qual
    (3, 6, '2023-07-05'), -- GEOM AOM220
    (3, 8, '2023-08-30'), -- Glazing

    -- Qualifications for a PNT staff member
    (4, 4, '2021-11-12'), -- PNT Qual

    -- Qualifications for a PNL-only staff member
    (5, 11, '2022-10-01'), -- HEV Aware
    (5, 12, '2022-12-14')  -- 1140 Spot
    ;

-- Repeat and vary the assignments above to suit the number of staff and qualifications.


COMMIT;