CREATE TABLE "Menu" (
MenuID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
ItemName text NOT NULL);

CREATE TABLE "Event" (
EventID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
EventName text NOT NULL,
NumberOfPeople text NOT NULL,
"Date" date VARCHAR(10) NOT NULL,
"Time" time VARCHAR(5) NOT NULL);

CREATE TABLE "TypesOfCatering" (
TypesOfCateringID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
TypesOfCateringName text NOT NULL);

CREATE TABLE "AccountType" (
AccountTypeID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
AccountTypeName text NOT NULL);

CREATE TABLE "Meals" (
MealID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
MealName text NOT NULL,
MealPrice float NOT NULL);

CREATE TABLE "DietaryTypes" (
DietaryTypesID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
DietaryTypesName text NOT NULL);

CREATE TABLE "CardStatus" (
CardStatusID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
CardStatusName text NOT NULL);

CREATE TABLE "User" (
UserID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
AccountTypeID integer NOT NULL,
FirstName text NOT NULL,
LastName text NOT NULL,
PhoneNumber integer VARCHAR(10) NOT NULL,
Email text NOT NULL,
Username text NOT NULL,
Password text NOT NULL,
CONSTRAINT User_FK_1 FOREIGN KEY (AccountTypeID) REFERENCES AccountType(AccountTypeID));

CREATE TABLE "CardDetails" (
CardID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
UserID integer NULL,
CardNumber integer VARCHAR(16) NOT NULL,
ExpiryDate integer VARCHAR(4) NOT NULL,
CVV integer VARCHAR(3) NOT NULL,
CardStatusID integer NOT NULL,
CONSTRAINT CardDetails_FK_1 FOREIGN KEY (UserID) REFERENCES User(UserID)
CONSTRAINT CardDetails_FK_2 FOREIGN KEY (CardStatusID) REFERENCES CardStatus(CardStatusID));

CREATE TABLE "Catering" (
CateringID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
UserID integer NOT NULL,
MealID integer NOT NULL,
EventID integer NOT NULL,
CardID integer NOT NULL,
TypesOfCateringID integer NOT NULL,
SpecificCateringRequests text NOT NULL,
CONSTRAINT Catering_FK_1 FOREIGN KEY (UserID) REFERENCES User(UserID),
CONSTRAINT Catering_FK_2 FOREIGN KEY (MealID) REFERENCES Meals(MealID),
CONSTRAINT Catering_FK_3 FOREIGN KEY (EventID) REFERENCES Event(EventID),
CONSTRAINT Catering_FK_4 FOREIGN KEY (CardID) REFERENCES CardDetails(CardID),
CONSTRAINT Catering_FK_5 FOREIGN KEY (TypesOfCateringID) REFERENCES TypesOfCatering(TypesOfCateringID));

CREATE TABLE "EventMenu" (
EventMenuID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
CateringID integer NOT NULL,
MenuID integer NOT NULL,
CONSTRAINT Catering_FK_1 FOREIGN KEY (CateringID) REFERENCES Catering(CateringID),
CONSTRAINT Catering_FK_2 FOREIGN KEY (MenuID) REFERENCES Menu(MenuID));

CREATE TABLE "EventDietaryRequirements" (
EvemtDietaryRequirementsID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
DietaryTypesID integer NOT NULL,
CateringID integer NOT NULL,
Qty integer NOT NULL,
CONSTRAINT EvemtDietaryRequirements_FK_1 FOREIGN KEY (DietaryTypesID) REFERENCES DietaryTypes(DietaryTypesID),
CONSTRAINT EvemtDietaryRequirements_FK_2 FOREIGN KEY (CateringID) REFERENCES Catering(CateringID));

