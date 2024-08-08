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
FROM User

SELECT
	Meals.MealName AS Meal,
	Meals.MealPrice AS Price
FROM Meals;

SELECT
	TypesOfCatering.TypesOfCateringName
FROM TypesOfCatering;

SELECT 
	User.FirstName ||' '|| User.LastName AS User,
	CardDetails.CardNumber AS Card_Number,
	CardDetails.ExpiryDate AS Expiry_Date,
	CardDetails.CVV AS CVV
FROM CardDetails
INNER JOIN User
ON User.UserID = CardDetails.UserID;

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


