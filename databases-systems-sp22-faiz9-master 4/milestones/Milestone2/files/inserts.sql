-- Script name: inserts.sql
-- Author: Syed Faiz
-- Purpose: insert sample data to test the integrity of this database

-- the database used to insert the data into. 
USE heathcareDB;

-- 1 Healthcare Organization Table Inserts
INSERT INTO HealthcareOrganization (idHealthcenter, Name) VALUES (631152000, OaklandCenter), (694742400, SFCenter), (958089600, BerkeleyCenter);

-- 2 Location Table Inserts
INSERT INTO Location (idLocation, Name, Address) VALUES (631152000, OaklandCenter, 1450Street), (694742400, SFCenter, 1850Street),(958089600, BerkeleyCenter, 1250Street);

-- 3 Employee Table Inserts
INSERT INTO Employee (idEmployees, name, social, role, salary, hireDate, Address) VALUES (225, Bob, 878-09-4592, labtech, 8000, 11-09-2005, 17thst), (299, John, 334-07-4452, manager, 12000, 12-04-2009, 49thst), (388, Syed, 661-04-9982, HR, 13000, 11-11-2011, 09thst);

-- 4 Customer Table Inserts
INSERT INTO Customer (idCustomer, name, social, dateofbirth, address, phone, email) VALUES (123, Helen, 884-43-9991, 12-03-1996, 45thst, 650-888-4590, noemail), (120, Syed, 994-93-8881, 11-03-1996, 35thst, 650-899-2290, noemail), (441, Jose, 114-40-8721, 04-01-1997, 12thst, 925-231-8590, noemail);

-- 5 Payment Table Inserts
INSERT INTO Payment (idPayment, Type, installment, amount) VALUES (1235, Debit, no, 123), (1288, Debit, no, 100), (1800, Credit, no, 400);

-- 6 Supplies Table Inserts
INSERT INTO Supplies (idSupplies, Gloves, Masks, Syringes) VALUES (55667, 200, 200, 300), (55448, 200, 200, 300), (55867, 200, 200, 300);

-- 7 Supplies Order Table Inserts
INSERT INTO SuppliesOrder () VALUES ();

-- 8 Maintenance Table Inserts
INSERT INTO Maintenance () VALUES ();

-- 9 Owner Table Inserts
INSERT INTO Owner (idOwner, name) VALUES (3345, Henry), (3321, Eric), (2292, Brian);

-- 10 Revenue Table Inserts
INSERT INTO Revenue (date, netprofit, loss) VALUES (04-19-2022, 189900, 11000), (04-18-2022, 179900, 10000), (04-17-2022, 169900, 9000);

-- 11 Marketing Campaign Table Inserts
INSERT INTO MarketingCampaign (campaignid, campaignname) VALUES (1122, Welcome), (1102, Discounts), (1002, Welcome2);

-- 12 Account Table inserts
INSERT INTO Account (idAccount, type, password) VALUES (123, user, hellouser), (120, user, syed123), (441, user, hellojose );

-- 13 Med Order Table inserts
INSERT INTO MedOrder (Prescription, Order_num, order_date) VALUES (Drugone, 22333, 04-19-2022), (Drugtwo, 3344, 04-19-2022), (Drugthree, 4499, 04-19-2022);

-- 14 Medical Records Table inserts
INSERT INTO MedicalRecords (idMedicalRecords, Screeningresults, Visithistory, Receipts) VALUES (12345, available, available, available), (12999, available, available, available), (12885, available, available, available);

-- 15 Appointment Table inserts 
INSERT INTO Appointment (idAppointment, Appointmentdate) VALUES (2284, 12-04-2022), (3349, 11-06-2022), (4568, 09-07-2022);

-- 16 Services Table inserts
INSERT INTO Service (idService, Drugscreening, expredite, servicedate) VALUES (11223, yes, yes, 04-12-2022), (11299, yes, yes, 04-14-2022), (11883, yes, yes, 05-12-2022) ;
