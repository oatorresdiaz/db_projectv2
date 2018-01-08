-- This file contains the definitions of the tables used in the application.
--
-- Users table
create table users(uID serial primary key, uFirstName varchar(20), uLastName varchar(20), uGender char(1), uBirthDate date);

-- Addresses table
create table addresses(addID serial primary key, uID integer references users(uID), city varchar(20), street varchar(30), country varchar(20), zipCode integer);

-- Credentials table
create table credentials(cid serial primary key, uID integer references users(uID), username varchar(20), password varchar(20), email varchar(20));

-- Credit Card table
create table creditCards(ccID serial primary key, uID integer references users(uID), ccNumber varchar(20), ccExpDate date, ccSecurityCode integer);

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

-- Resources table
create table resources(resID serial primary key, resCategory varchar(20));

-- Requests table
create table requests(reqID integer references requesters(reqID), resID integer references resources(resID), requestQty integer, requestDate date, primary key(reqID, resID));

-- Sells table
create table sells(invID integer references inventory(invID), resID integer references resources(resID), primary key (invID, resID));

-- Food table
create table foods(fID serial primary key, resID integer references resources(resID), fCategory varchar(20), fExpDate date);

-- Baby Food table
create table babyFoods(bfID serial primary key, fID integer references food(fID), bfName varchar(20), bfBrand varchar(20), bfOz float);

-- Canned Food table
create table cannedFoods(cfID serial primary key, fID integer references food(fID), cfName varchar(20), cfBrand varchar(20), cfOz float);

-- Dry Food table
create table dryFoods(dfID serial primary key, fID integer references food(fID), dfName varchar(20), dfBrand varchar(20), dfOz float);

-- Medications table
create table medications(medID serial primary key, resID integer references resources(resID), medName varchar(20), medBrand varchar(20), medType varchar(20), medOz float, medExpDate date);

-- Ice table
create table ice(iceID serial primary key, resID integer references resources(resID), iceWeight float, iceContainer varchar(20));

-- Tools table
create table tools(tID serial primary key, resID integer references resources(resID), tName varchar(20), tType varchar(20), tWeight float, tSize float);

-- Clothing table
create table clothings(clothID serial primary key, resID integer references resources(resID), clothGenger char(1), tType varchar(20), clothBrand varchar(20), clothSize varchar(10), clothColor varchar(20), clothDesignPatterns varchar(20));

-- Water table
create table water(wID serial primary key, resID integer references resources(resID), wCategory varchar(20), wExpDate date);

-- Water Bottles table
create table waterBottles(wbID serial primary key, wID integer references water(wID), wbBrand varchar(20), wbOz float, wbMaterial varchar(20));

-- Water Gallons table
create table waterGallons(wgID serial primary key, wID integer references water(wID), wgBrand varchar(20), wgMaterial varchar(20));

-- Power Generators table
create table powerGenerators(pgID serial primary key, resID integer references resources(resID), pgBrand varchar(20), pgType varchar(20), pgPower integer, pgFuelType varchar(10));

-- Batteries table
create table batteries(bID serial primary key, resID integer references resources(resID), bType varchar(20), bBrand varchar(20));

-- Medical Devices table
create table medicalDevices(mdID serial primary key, resID integer references resources(resID), mdName varchar(20), mdType varchar(20), mdWeight float, mdSize float);

-- Heavy Equipment table
create table heavyEquipments(heID serial primary key, resID integer references resources(resID), heName varchar(20), heType varchar(20), heWeight float, heSize float);

-- Fuel table
create table fuel(fuelID serial primary key, resID integer references resources(resID), fuelCategory varchar(10));

-- Diesel table
create table diesel(dID serial primary key, fuelID integer references fuel(fuelID), dLiters float, dContainer varchar(20));

-- Propane table
create table propane(pID serial primary key, fuelID integer references fuel(fuelID), pLiters float, pContainer varchar(20));

-- Gasoline Food table
create table gasoline(dID serial primary key, fuelID integer references fuel(fuelID), gLiters float, gContainer varchar(20));