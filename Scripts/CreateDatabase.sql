CREATE TABLE "Menu" (
MenuID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
ItemName text NOT NULL);

CREATE TABLE "Event" (
EventID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
EventName text NOT NULL,
NumberOfPeople text NOT NULL,
"Date" date NOT NULL CHECK(LENGTH(TheColumn) == 10),
"Time" time NOT NULL CHECK(LENGTH(TheColumn) == 5));

CREATE TABLE "CardDetails" (
CardID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
CardName text NOT NULL,
CardNumber integer NOT NULL CHECK(LENGTH(TheColumn) == 16),
ExpiryDate integer NOT NULL CHECK(LENGTH(TheColumn) == 4),
CVV integer NOT NULL CHECK(LENGTH(TheColumn) == 3));

CREATE TABLE "TypesOfCatering" (
TypesOfCateringID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
TypesOfCateringName text NOT NULL);

CREATE TABLE "AccountType" (
AccountTypeID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
AccountTypeName text NOT NULL);

CREATE TABLE "User" (
UserID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
AccountTypeID integer NOT NULL,
FirstName text NOT NULL,
LastName text NOT NULL,
PhoneNumber integer NOT NULL CHECK(LENGTH(TheColumn) == 10),
Email text NOT NULL,
Username text NOT NULL,
Password text NOT NULL);

CREATE TABLE "Meals" (
MealID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
MealName text NOT NULL,
MealPrice text NOT NULL);

CREATE TABLE "CardDetails" (
CardID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
CardName text NOT NULL,
CardNumber integer NOT NULL CHECK(LENGTH(TheColumn) == 16),
ExpiryDate integer NOT NULL CHECK(LENGTH(TheColumn) == 4),
CVV integer NOT NULL CHECK(LENGTH(TheColumn) == 3));