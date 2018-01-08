-- This file contains the definitions of the tables used in the application.
--
-- Users table
create table users(uID serial primary key, uFirstName varchar(20), uLastName varchar(20), uGender char(1), uBirthDate date);

-- Addresses table
create table addresses(addID serial primary key, uID integer references users(uID), city varchar(20), street varchar(30), country varchar(20), zipCode integer);

-- Credentials table
create table credentials(cid serial primary key, uID integer references users(uID), username varchar(20), password varchar(20), email varchar(20));

-- Credit Card table
create table creditCards(ccID serial primary key, uID integer references users(uID), ccNumber integer, ccExpDate date, ccSecurityCode integer);

-- Telephone Numbers table
create table telephoneNumbers(tID serial primary key, uID integer references users(uID), homeNumber varchar(20), mobileNumber varchar(20), workNumber varchar(20), otherNumber varchar(20));

-- Admins table
create table admins(adminID serial primary key, uID integer references users(uID));

-- Suppliers table
create table suppliers(suppID serial primary key, uID integer references users(uID));

-- Requesters table
create table requesters(reqID serial primary key, uID integer references users(uID));

-- Inventory table
create table inventory(invID serial primary key, suppID integer references suppliers(suppID), invDate date, invQty integer, invReserved integer, invAvaiable integer, invPrice float);

-- Price History table
create table priceHistory(phID serial primary key, invID integer references inventory(invID), startDate date, thruDate date, priceAtMoment float);

-- Purchases table
create table purchases(reqID integer references requesters(reqID), invID integer references inventory(invID), purchaseDate date, purchaseAmount float, primary key (reqID, invID));

-- Reserves table
create table reserves(reqID integer references requesters(reqID), invID integer references inventory(invID), resQty integer, resDate date, resExpDate date, primary key (reqID, invID));

--Category table
create table Category(catID serial primary key, catName varchar(20));

-- Resources table
create table resources(resID serial primary key, resName varchar(20), catID integer references category(catID));

-- Requests table
create table requests(reqID integer references requesters(reqID), resID integer references resources(resID), requestQty integer, requestDate date, primary key(reqID, resID));

-- Sells table
create table sells(invID integer references inventory(invID), resID integer references resources(resID), primary key (invID, resID));

--FoodSubCategory
create table foodSubCategory(fscID serial primary key, fscName varchar(20));

-- Food table
create table foods(fID serial primary key, catID integer references category(catID), fsc integer references foodSubCategory(fscID), resID integer references resources(resID), fBrand varchar(20), fOz float, fExpDate date);

-- Medications table
create table medications(medID serial primary key, catID integer references category(catID), resID integer references resources(resID), medBrand varchar(20), medType varchar(20), medQty float, medExpDate date);

-- Ice table
create table ice(iceID serial primary key, resID integer references resources(resID), catID integer references category(catID), iceWeight float, iceContainer varchar(20));

-- Tools table
create table tools(tID serial primary key, resID integer references resources(resID), catID integer references category(catID), tType varchar(20), tWeight float, tSize float, tFuel varchar(20));

-- Clothing table
create table clothings(clothID serial primary key, resID integer references resources(resID), catID integer references category(catID), clothGender char(1), clothBrand varchar(20), clothSize varchar(10), clothColor varchar(20), clothDesignPatterns varchar(20));

--waterSubCategory
create table waterSubCategory(wscID serial primary key, wscName varchar(20));

-- Water table
create table water(wID serial primary key, resID integer references resources(resID), catID integer references category(catID), wscID integer references waterSubCategory(wscID), wBrand varchar(20), wExpDate date);

-- Power Generators table
create table powerGenerators(pgID serial primary key, resID integer references resources(resID), catID integer references category(catID), pgBrand varchar(20), pgType varchar(20), pgPower integer, pgFuelType varchar(10));

-- Batteries table
create table batteries(bID serial primary key, resID integer references resources(resID), catID integer references category(catID), bType varchar(20), bBrand varchar(20));

-- Medical Devices table
create table medicalDevices(mdID serial primary key, resID integer references resources(resID), catID integer references category(catID), mdName varchar(20), mdType varchar(20), mdWeight float, mdSize float);

-- Heavy Equipment table
create table heavyEquipments(heID serial primary key, resID integer references resources(resID), catID integer references category(catID), heType varchar(20), heWeight float, heSize float);

--fuelSubCategory
create table fuelSubCategory(fuscID serial primary key, fuscName varchar(20));

-- Fuel table
create table fuel(fuelID serial primary key, resID integer references resources(resID), catID integer references category(catID), fuscID integer references fuelSubCategory(fuscID));