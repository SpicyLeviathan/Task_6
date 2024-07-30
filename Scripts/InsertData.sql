INSERT INTO Menu (ItemName)
VALUES
('Chicken_Nuggets'),
('Mini_Pizzas'),
('Fruit_Kabobs'),
('Vegetable_Sticks_with_Dip'),
('Sandwiches'),
('Macaroni_and_Cheese'),
('Cheese_and_Crackers'),
('Cookies'),
('Brownies'),
('Pizzas');

INSERT INTO Event (EventName, NumberOfPeople, Date, Time)
VALUES
('Science_Fair','150','2024-09-15','09:00'),
('Math_Olympiad','100','2024-10-03','08:30'),
('Art_Exhibition','200','2024-11-20','10:00'),
('Music_Concert','250','2024-12-05','18:00'),
('Drama_Play','180','2024-10-25','19:00'),
('Sports_Day','300','2024-09-30','08:00'),
('Book_Fair','220','2024-11-10','09:30'),
('Career_Day','120',' 2024-12-01','10:00'),
('Parent_Teacher_Conference','60','2024-10-15','16:00'),
('Cultural_Festival','350','2024-11-25','14:00');

INSERT INTO TypesOfCatering (TypesOfCateringName)
VALUES
('On_Site_Catering'),
('Off_Sight_Catering');

INSERT INTO AccountType (AccountTypeName)
VALUES
('Catering_Staff'),
('Users');

INSERT INTO Meals (MealName, MealPrice)
VALUES
('Breakfast','5.00'),
('Morning_Tea','5.00'),
('Lunch','7.50'),
('Afternoon_Tea','5.00'),
('Dinner','10.00');

INSERT INTO DietaryTypes (DietaryTypesName)
VALUES
('Gluten_Free'),
('Nut_Free'),
('Dairy_Free'),
('Vegetarian'),
('Vegan'),
('Halal'),
('Kosher'),
('Low_Sodium'),
('Low_Sugar'),
('Pescatarian'),
('Organic'),
('Soy_Free');

INSERT INTO "User" (AccountTypeID, FirstName, LastName, PhoneNumber, Email, Username, Password)
VALUES
('','Alice','Smith','0412345678','alice.smith@gsg.wa.ed.au','alice.smith','Alice@1234'),
('','Brian','Johnson','0498765432','brian.johnson@gsg.wa.ed.au','brian.johnson','Brian@1234'),
('','Carol','Davis','0456789123','carol.davis@gsg.wa.ed.au','carol.davis','Carol@1234'),
('','Daniel','Brown','0423456789','daniel.brown@gsg.wa.ed.au','daniel.brown','Daniel@1234'),
('','Emma','Wilson','0434567890','emma.wilson@gsg.wa.ed.au','emma.wilson','Emma@1234'),
('','Frank','Taylor','0487654321','frank.taylor@gsg.wa.ed.au','frank.taylor','Frank@1234'),
('','Grace','Anderson','0445678901','grace.anderson@gsg.wa.ed.au','grace.anderson','Grace@1234'),
('','Henry','Martinez','0478901234','henry.martinez@gsg.wa.ed.au','henry.martinez','Henry@1234'),
('','','','','','',''),
('','','','','','','');























































INSERT INTO CardDetails (UserID, CardNumber, ExpiryDate, CVV)
VALUES
('SchoolCard','','',''),
('','','',''),
('','','',''),
('','','',''),
('','','',''),
('','','',''),
('','','',''),
('','','',''),
('','','',''),
('','','','');