CREATE TABLE "Menu" ( /* Creates a table with the name that is inside the "" */
MenuID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
ItemName text NOT NULL); /* Creates a row that is an integer and is not null */

CREATE TABLE "Event" ( /* Creates a table with the name that is inside the "" */
EventID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
EventName text NOT NULL, /* Creates a row that is a text and is not null */
NumberOfPeople text NOT NULL, /* Creates a row that is a text and is not null */
"Date" date(10) NOT NULL, /* Creates a row that is a date with max of 10 characters and is not null */
"Time" time(5) NOT NULL); /* Creates a row that is a time with max of 5 characters and is not null */

CREATE TABLE "TypesOfCatering" ( /* Creates a table with the name that is inside the "" */
TypesOfCateringID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
TypesOfCateringName text NOT NULL); /* Creates a row that is a text and is not null */

CREATE TABLE "AccountType" ( /* Creates a table with the name that is inside the "" */
AccountTypeID integer PRIMARY KEY AUTOINCREMENT NOT NULL,  /* Creates a primary key that is an integer, autoicrements and in not null */
AccountTypeName text NOT NULL); /* Creates a row that is a text and is not null */

CREATE TABLE "Meals" ( /* Creates a table with the name that is inside the "" */
MealID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
MealName text NOT NULL, /* Creates a row that is a text and is not null */
MealPrice float NOT NULL); /* Creates a row that is a float and is not null */

CREATE TABLE "DietaryTypes" ( /* Creates a table with the name that is inside the "" */
DietaryTypesID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
DietaryTypesName text NOT NULL); /* Creates a row that is a text and is not null */

CREATE TABLE "CardStatus" ( /* Creates a table with the name that is inside the "" */
CardStatusID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
CardStatusName text NOT NULL); /* Creates a row that is a text and is not null */

CREATE TABLE "User" ( /* Creates a table with the name that is inside the "" */
UserID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
AccountTypeID integer NOT NULL, /* Creates a row that is an integer and is not null */
FirstName text NOT NULL, /* Creates a row that is a text and is not null */
LastName text NOT NULL, /* Creates a row that is a text and is not null */
PhoneNumber integer(10) NOT NULL, /* Creates a row that is an integer with max of 10 characters and is not null */
Email text NOT NULL, /* Creates a row that is a text and is not null */
Username text NOT NULL, /* Creates a row that is a text and is not null */
Password text NOT NULL, /* Creates a row that is a text and is not null */
CONSTRAINT User_FK_1 FOREIGN KEY (AccountTypeID) REFERENCES AccountType(AccountTypeID)); /* Sets a foreign key */

CREATE TABLE "CardDetails" ( /* Creates a table with the name that is inside the "" */
CardID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
UserID integer NULL, /* Creates a row that is an integer and can be null */
CardNumber integer(16) NOT NULL, /* Creates a row that is an integer with max of 16 characters and is not null */
ExpiryDate integer(4) NOT NULL, /* Creates a row that is an integer with max of 4 characters and is not null */
CVV integer(3) NOT NULL, /* Creates a row that is an integer with max of 3 characters and is not null */
CardStatusID integer NOT NULL, /* Creates a row that is an integer and is not null */
CONSTRAINT CardDetails_FK_1 FOREIGN KEY (UserID) REFERENCES User(UserID) /* Sets a foreign key */
CONSTRAINT CardDetails_FK_2 FOREIGN KEY (CardStatusID) REFERENCES CardStatus(CardStatusID)); /* Sets a foreign key */

CREATE TABLE "Catering" ( /* Creates a table with the name that is inside the "" */
CateringID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
UserID integer NOT NULL, /* Creates a row that is an integer and is not null */
MealID integer NOT NULL, /* Creates a row that is an integer and is not null */
EventID integer NOT NULL, /* Creates a row that is an integer and is not null */
CardID integer NOT NULL, /* Creates a row that is an integer and is not null */
TypesOfCateringID integer NOT NULL, /* Creates a row that is an integer and is not null */
SpecificCateringRequests text NOT NULL, /* Creates a row that is a text and is not null */
CONSTRAINT Catering_FK_1 FOREIGN KEY (UserID) REFERENCES User(UserID), /* Sets a foreign key */
CONSTRAINT Catering_FK_2 FOREIGN KEY (MealID) REFERENCES Meals(MealID), /* Sets a foreign key */
CONSTRAINT Catering_FK_3 FOREIGN KEY (EventID) REFERENCES Event(EventID), /* Sets a foreign key */
CONSTRAINT Catering_FK_4 FOREIGN KEY (CardID) REFERENCES CardDetails(CardID), /* Sets a foreign key */
CONSTRAINT Catering_FK_5 FOREIGN KEY (TypesOfCateringID) REFERENCES TypesOfCatering(TypesOfCateringID)); /* Sets a foreign key */

CREATE TABLE "EventMenu" ( /* Creates a table with the name that is inside the "" */
EventMenuID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
CateringID integer NOT NULL, /* Creates a row that is an integer and is not null */
MenuID integer NOT NULL, /* Creates a row that is an integer and is not null */
CONSTRAINT Catering_FK_1 FOREIGN KEY (CateringID) REFERENCES Catering(CateringID), /* Sets a foreign key */
CONSTRAINT Catering_FK_2 FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)); /* Sets a foreign key */

CREATE TABLE "EventDietaryRequirements" ( /* Creates a table with the name that is inside the "" */
EventDietaryRequirementsID integer PRIMARY KEY AUTOINCREMENT NOT NULL, /* Creates a primary key that is an integer, autoicrements and in not null */
DietaryTypesID integer NOT NULL, /* Creates a row that is an integer and is not null */
CateringID integer NOT NULL, /* Creates a row that is an integer and is not null */
Qty integer NOT NULL, /* Creates a row that is an integer and is not null */
CONSTRAINT EventDietaryRequirements_FK_1 FOREIGN KEY (DietaryTypesID) REFERENCES DietaryTypes(DietaryTypesID), /* Sets a foreign key */
CONSTRAINT EventDietaryRequirements_FK_2 FOREIGN KEY (CateringID) REFERENCES Catering(CateringID)); /* Sets a foreign key */

