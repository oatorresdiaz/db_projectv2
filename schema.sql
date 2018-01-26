-- This file contains the definitions of the tables used in the application.
--
-- Users table
create table users(uID serial primary key, uFirstName varchar(20), uLastName varchar(20), uGender char(1), uBirthDate date);

-- Addresses table
create table addresses(addID serial primary key, uID integer references users(uID), city varchar(20), street varchar(30), country varchar(20), zipCode varchar(10));

-- Credentials table
create table credentials(cid serial primary key, uID integer references users(uID), username varchar(20), password varchar(20), email varchar(20));

-- Credit Card table
create table creditCards(ccID serial primary key, uID integer references users(uID), ccNumber bigint, ccExpDate date, ccSecurityCode integer);

-- Telephone Numbers table
create table telephoneNumbers(tID serial primary key, uID integer references users(uID), homeNumber varchar(20), mobileNumber varchar(20), workNumber varchar(20), otherNumber varchar(20));

-- Admins table
create table admins(adminID serial primary key, uID integer references users(uID));

-- Suppliers table
create table suppliers(suppID serial primary key, uID integer references users(uID));

-- Requesters table
create table requesters(reqID serial primary key, uID integer references users(uID));

-- Inventory table
create table inventory(invID serial primary key, suppID integer references suppliers(suppID), invDate date, invQty integer, invReserved integer, invAvailable integer, invPrice float);

-- Price History table
create table priceHistory(phID serial primary key, invID integer references inventory(invID), startDate date, thruDate date, priceAtMoment float);

-- Purchases table
create table purchases(reqID integer references requesters(reqID), invID integer references inventory(invID), purchaseDate date, purchaseAmount float, primary key (reqID, invID));

-- Reserves table
create table reserves(reqID integer references requesters(reqID), invID integer references inventory(invID), resQty integer, resDate date, resExpDate date, primary key (reqID, invID));

--Categories table
create table categories(catID serial primary key, catName varchar(20));

-- Resources table
create table resources(resID serial primary key, resName varchar(20), catID integer references categories(catID), resspecification varchar(100));

-- Requests table
create table requests(reqID integer references requesters(reqID), resID integer references resources(resID), requestQty integer, requestDate date, primary key(reqID, resID));

-- Sells table
create table sells(invID integer references inventory(invID), resID integer references resources(resID), primary key (invID, resID));
