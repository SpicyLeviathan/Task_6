SELECT
	User.FirstName ||' '|| User.LastName AS User,
	AccountType.AccountTypeName AS Account_Type,
	User.Username AS Username,
	User.Password AS Password
FROM User
INNER JOIN AccountType
ON AccountType.AccountTypeID = User.AccountTypeID;

SELECT
	User.FirstName ||' '|| User.LastName AS User,
	User.PhoneNumber AS Phone,
	User.Email AS Email
FROM User;

SELECT
	Meals.MealName AS Meal,
	Meals.MealPrice AS Price
FROM Meals;

SELECT
	TypesOfCatering.TypesOfCateringName
FROM TypesOfCatering;

SELECT
	CardStatus.CardStatusName AS Card_Status
FROM CardStatus;

SELECT 
	User.FirstName ||' '|| User.LastName AS User,
	CardDetails.CardNumber AS Card_Number,
	CardDetails.ExpiryDate AS Expiry_Date,
	CardDetails.CVV AS CVV,
	CardStatus.CardStatusName AS Card_Status
FROM CardDetails
INNER JOIN User
ON User.UserID = CardDetails.UserID
INNER JOIN CardStatus
ON CardStatus.CardStatusID = CardDetails.UserID;

SELECT
	User.FirstName ||' '|| User.LastName AS User,
	Event.EventName AS Event,
	User.PhoneNumber AS Phone,
	User.Email AS Email,
	Event.NumberOfPeople AS Number_of_People,
	Event.Date AS Date,
	Event.Time AS Time
FROM Catering
INNER JOIN User
ON User.UserID = Catering.UserID 
INNER JOIN Event
ON Event.EventID = Catering.EventID;

SELECT
	Menu.ItemName AS Item
FROM Menu;

SELECT
	Event.EventName AS Event_Name, 
	Menu.ItemName AS Item
FROM Event
INNER JOIN Catering
ON Event.EventID = Catering.EventID  
INNER JOIN EventMenu
ON Catering.CateringID = EventMenu.CateringID 
INNER JOIN Menu
ON EventMenu.MenuID = Menu.MenuID
WHERE Event.EventName = "Book_Fair"
ORDER BY Event.EventName, Menu.ItemName;

SELECT
	DietaryTypes.DietaryTypesName AS Dietary_Types
FROM DietaryTypes;

SELECT
	Event.EventName AS Event_Name,
	DietaryTypes.DietaryTypesName AS Dietary_Types,
	EventDietaryRequirements.Qty AS Qty
FROM Event
JOIN Catering
ON Event.EventID = Catering.EventID  
JOIN EventDietaryRequirements
ON Catering.CateringID = EventDietaryRequirements.CateringID 
JOIN DietaryTypes
ON EventDietaryRequirements.DietaryTypesID = DietaryTypes.DietaryTypesID
WHERE Event.EventName = "Sports_Day"
ORDER BY Event.EventName, DietaryTypes.DietaryTypesName, EventDietaryRequirements.Qty;

SELECT
	User.FirstName ||' '|| User.LastName AS User,
	Meals.MealName AS Meal,
	Event.EventName AS Event_Name,
	Catering.CardID AS Card_ID,
	TypesOfCatering.TypesOfCateringName AS Type_Of_Catering,
	Catering.SpecificCateringRequests AS Specific_Catering_Requests
FROM Catering
JOIN "User"
ON User.UserID = Catering.UserID 
JOIN Meals
ON Meals.MealID = Catering.MealID
JOIN Event
ON Event.EventID = Catering.EventID
JOIN TypesOfCatering
ON TypesOfCatering.TypesOfCateringID = Catering.TypesOfCateringID;