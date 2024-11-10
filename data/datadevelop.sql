BEGIN;

-- Clear the entire database
DELETE FROM auth_user;
DELETE FROM user_profile;
DELETE FROM document_titles;
DELETE FROM document_clients;
DELETE FROM staff;
DELETE FROM role_names;
DELETE FROM qualification;
DELETE FROM staff_role;
DELETE FROM staff_qualification;
DELETE FROM equipment;
DELETE FROM equipment_group;
DELETE FROM equipment_user;
DELETE FROM equipment_test;

-- Insert test data
INSERT INTO auth_user (id, username, first_name, last_name, email, password, is_superuser, is_staff, is_active, date_joined) VALUES 
    (1, 'admin', 'Admin', '', 'admin@example.com', 'pbkdf2_sha256$870000$ljSoPNg47pfEPaqMM68nTQ$9dsw6LFNeXiaDu+uUNGZwxdWUE+wuiT5XxTXEUHDf5A=', 1, 1, 1, CURRENT_TIMESTAMP);

COMMIT