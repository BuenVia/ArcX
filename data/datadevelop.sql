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
    (1, 1, '2025-01-15'), -- VDA Qual
    (1, 5, '2025-03-10'), -- Audatex

    -- Qualifications for a MET and PNL staff member (dual-role)
    (2, 2, '2024-11-20'), -- MET Qual
    (2, 7, '2024-08-25'), -- ADAS AOM230

    -- More qualifications for another staff member with MET and PNL roles
    (3, 2, '2025-05-22'), -- MET Qual
    (3, 6, '2025-07-05'), -- GEOM AOM220
    (3, 8, '2023-08-30'), -- Glazing

    -- Qualifications for a PNT staff member
    (4, 4, '2024-11-12'), -- PNT Qual

    -- Qualifications for a PNL-only staff member
    (5, 11, '2025-10-01'), -- HEV Aware
    (5, 12, '2024-12-14')  -- 1140 Spot
    ;

-- Repeat and vary the assignments above to suit the number of staff and qualifications.

-- Insert data into equipment_group table with predefined IDs
INSERT INTO equipment_group (id, name) VALUES
    (1, 'Pulling and Body Alignment'),
    (2, 'Welding Equipment'),
    (3, 'Ramps and Lifting Equipment'),
    (4, 'Paint Booth and Mixing Room'),
    (5, 'Painting & Paintshop Equipment'),
    (6, 'Compressors & Dryers'),
    (7, 'Alignment & Geometry'),
    (8, 'Specialist Measuring'),
    (9, 'General Workshop Equipment'),
    (10, 'Site Information & Certificates');


-- Insert data into equipment table with reference to equipment_group table

-- Pulling and Body Alignment (equipment_group_id = 1)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (1, '001', 'Pulling and Alignment Jig', 'Blackhawk', 'Koreck', 'N/A', 1),
    (2, '002', 'Measuring System', 'Blackhawk', 'Shark', 'B02C5460', 1);

-- Welding Equipment (equipment_group_id = 2)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (3, '009', 'Inverter Spot Weld+F1+C15:W17', 'GYS', 'PTI Gebius', '22.05.024700.00033', 2),
    (4, '010', 'MIG Welder', 'Telwin', 'Treo 243', 'NK - First new', 2),
    (5, '011', 'Oxy-Accetyline', 'N/K', 'BOC', 'N/K', 2),
    (6, '012', 'Self Peircing Riviter', 'W&S', 'Xpress 800', '201401296', 2),
    (7, '013', 'Dent Puller', 'Telwin', 'Duo', '28708417 + 32196417', 2);

-- Ramps and Lifting Equipment (equipment_group_id = 3)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (8, '017', 'Vehicle Lift 2 Post', 'Bend Pax', 'XPR9', '50000006109-016', 3),
    (9, '018', 'Vehicle Lift 2 Post', 'Automotech', 'AS6140A', '6610740703831', 3),
    (10, '019', 'Vehicle Lift 4 Post', 'Ravaglioli', '4400.3', '10559556', 3),
    (11, '020', 'Vehicle Lift AirBag', 'Guiliano', '', '42L1700268', 3),
    (12, '021', 'Vehicle Lift AirBag', 'Guiliano', '', '42L1700264', 3),
    (13, '022', 'Vehicle Lift AirBag', 'Guiliano', '', '42L1700262', 3);

-- Paint Booth and Mixing Room (equipment_group_id = 4)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (14, '025', 'Paint Booth', 'Dalby', 'X Booth', 'LHS', 4),
    (15, '026', 'Paint Booth', 'Dalby', 'X Booth', 'RHS', 4);

-- Painting & Paintshop Equipment (equipment_group_id = 5)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (16, '033', 'Paint Scales', 'Metler Toledo', 'RPA', 'C246250329', 5),
    (17, '034', 'Paint Scales', 'Milsteda', 'PMA7501', '33006680', 5);

-- Compressors & Dryers (equipment_group_id = 6)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (18, '041', 'Blackhawk Korek', 'MARK', 'MSA15-8', '1TJ487981', 6);

-- Alignment & Geometry (equipment_group_id = 7)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (19, '045', 'Wheel Aligner', 'Hofmann', 'Logik 6', '10444722', 7),
    (20, '046', 'Headlamp Beam Setter', 'Tecnolux', 'Polar', '3346', 7);

-- Specialist Measuring (equipment_group_id = 8)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (21, '049', 'Torque Wrench TW1 00-20 Nm - Company Owned', 'Sealey', 'STS104', 'NA', 8),
    (22, '050', 'Torque Wrench TW2 20-200 Nm - Company Owned', 'Sealey', 'STW309', 'NA', 8),
    (23, '051', 'Torque Wrench TW3 15-300 Nm - Company Owned', 'Snap-On', 'ATeCH3F', '917104682', 8),
    (24, '052', 'Torque Wrench TW4 19-110Nm', 'TengTools', '', 'WTW1', 8),
    (25, '053', 'Torque Wrench TW5 30-210 Nm', 'TengTools', '', '338996', 8),
    (26, '054', 'Torque Wrench TW6 30-210 Nm', 'Draper', '', '2012010708', 8),
    (27, '055', 'Torque Wrench TW7 60-300 Nm', 'Norbar', '', '2010/269241', 8),
    (28, '056', 'Torque Wrench TW8 70-350 Nm', 'Snap-On', '', '0113505208', 8),
    (29, '057', 'Tyre Inflator 0-9 bar TF1', 'NK', '', '4045121', 8),
    (30, '058', 'Tyre Inflator 0-9 bar TF2', 'NK', '', '5223055', 8),
    (31, '059', 'Tyre Inflator 0-9 bar TF3', 'NK', '', '1473618', 8),
    (32, '060', 'Tyre Inflator 0-9 bar TF4 - PCL Digital', 'NK', '', '240409189', 8);

-- General Workshop Equipment (equipment_group_id = 9)
INSERT INTO equipment (id, item_number, name, make, model, serial_number, equipment_group_id) VALUES
    (33, '063', 'Air Con Machine', 'Ecotechnics', 'Twin Pro', 'EC1704663/2017', 9),
    (34, '064', 'Tyre Machine', 'Bradbury', 'WC5201', 'NK', 9),
    (35, '065', 'ADAS Tablet', 'Hella Gutmann', 'MEGA Max', 'K2210N0098338', 9),
    (36, '066', 'Dust Extraction', 'Festool', '', '', 9);


COMMIT;