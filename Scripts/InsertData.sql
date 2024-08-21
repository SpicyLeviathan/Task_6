INSERT INTO Menu (ItemName) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('Chicken_Nuggets'), /* Data that is being inserted */
('Pizza'), /* Data that is being inserted */
('Fruit_Kabobs'), /* Data that is being inserted */
('Vegetable_Sticks_with_Dip'), /* Data that is being inserted */
('Sandwiches'), /* Data that is being inserted */
('Macaroni_and_Cheese'), /* Data that is being inserted */
('Cheese_and_Crackers'), /* Data that is being inserted */
('Cupcakes'), /* Data that is being inserted */
('Brownies'), /* Data that is being inserted */
('Bacon_and_Eggs'); /* Data that is being inserted */

INSERT INTO Event (EventName, NumberOfPeople, 'Date', 'Time') /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('Science_Fair','150','2024-09-15','09:00'), /* Data that is being inserted */
('Math_Olympiad','100','2024-10-03','08:30'), /* Data that is being inserted */
('Art_Exhibition','200','2024-11-20','10:00'), /* Data that is being inserted */
('Music_Concert','250','2024-12-05','18:00'), /* Data that is being inserted */
('Drama_Play','180','2024-10-25','19:00'), /* Data that is being inserted */
('Sports_Day','300','2024-09-30','08:00'), /* Data that is being inserted */
('Book_Fair','220','2024-11-10','09:30'), /* Data that is being inserted */
('Career_Day','120',' 2024-12-01','10:00'), /* Data that is being inserted */
('Parent_Teacher_Conference','60','2024-10-15','16:00'), /* Data that is being inserted */
('Cultural_Festival','350','2024-11-25','14:00'); /* Data that is being inserted */

INSERT INTO TypesOfCatering (TypesOfCateringName) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('On_Site_Catering'), /* Data that is being inserted */
('Off_Sight_Catering'); /* Data that is being inserted */

INSERT INTO AccountType (AccountTypeName) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('Catering_Staff'), /* Data that is being inserted */
('Users'), /* Data that is being inserted */
('NotActive'); /* Data that is being inserted */

INSERT INTO Meals (MealName, MealPrice) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('Breakfast','5.00'), /* Data that is being inserted */
('Morning_Tea','5.00'), /* Data that is being inserted */
('Lunch','7.50'), /* Data that is being inserted */
('Afternoon_Tea','5.00'), /* Data that is being inserted */
('Dinner','10.00'); /* Data that is being inserted */

INSERT INTO DietaryTypes (DietaryTypesName) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('Gluten_Free'), /* Data that is being inserted */
('Nut_Free'), /* Data that is being inserted */
('Dairy_Free'), /* Data that is being inserted */
('Vegetarian'), /* Data that is being inserted */
('Vegan'), /* Data that is being inserted */
('Halal'), /* Data that is being inserted */
('Kosher'), /* Data that is being inserted */
('Low_Sodium'), /* Data that is being inserted */
('Low_Sugar'), /* Data that is being inserted */
('Pescatarian'), /* Data that is being inserted */
('Organic'), /* Data that is being inserted */
('Soy_Free'); /* Data that is being inserted */

INSERT INTO CardStatus (CardStatusName) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('Active'), /* Data that is being inserted */
('Inactive'); /* Data that is being inserted */

INSERT INTO "User" (AccountTypeID, FirstName, LastName, PhoneNumber, Email, Username, Password) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('1','Alice','Smith','0412345678','alice.smith@gsg.wa.ed.au','alice.smith','Alice@1234'), /* Data that is being inserted */
('2','Brian','Johnson','0498765432','brian.johnson@gsg.wa.ed.au','brian.johnson','Brian@1234'), /* Data that is being inserted */
('2','Carol','Davis','0456789123','carol.davis@gsg.wa.ed.au','carol.davis','Carol@1234'), /* Data that is being inserted */
('3','Olivia','Miller','0456123789','olivia.miller@gsg.wa.ed.au','olivia.miller','Olivia@1234'), /* Data that is being inserted */
('1','Daniel','Brown','0423456789','daniel.brown@gsg.wa.ed.au','daniel.brown','Daniel@1234'), /* Data that is being inserted */
('2','Emma','Wilson','0434567890','emma.wilson@gsg.wa.ed.au','emma.wilson','Emma@1234'), /* Data that is being inserted */
('2','Frank','Taylor','0487654321','frank.taylor@gsg.wa.ed.au','frank.taylor','Frank@1234'), /* Data that is being inserted */
('2','Grace','Anderson','0445678901','grace.anderson@gsg.wa.ed.au','grace.anderson','Grace@1234'), /* Data that is being inserted */
('3','Noah','Harris','0491234567','noah.harris@gsg.wa.ed.au','noah.harris','Noah@1234'), /* Data that is being inserted */
('1','Henry','Martinez','0478901234','henry.martinez@gsg.wa.ed.au','henry.martinez','Henry@1234'), /* Data that is being inserted */
('2','Isabella','Thomas','0467890123','isabella.thomas@gsg.wa.ed.au','isabella.thomas','Isabella@1234'), /* Data that is being inserted */
('2','Jack','Lee','0412340987','jack.lee@gsg.wa.ed.au','jack.lee','Jack@1234'), /* Data that is being inserted */
('1','1','1','0123456789','1.1@gsg.wa.ed.au','1','1'), /* Data that is being inserted */
('2','2','2','0987654321','2.2@gsg.wa.ed.au','2','2'), /* Data that is being inserted */
('3','3','4','0918273645','3.3@gsg.wa.ed.au','3','3'); /* Data that is being inserted */

INSERT INTO CardDetails (UserID, CardNumber, ExpiryDate, CVV, CardStatusID) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('2','1234567890123456','1126','456','1'), /* Data that is being inserted */
('3','2345678901234567','1028','789','1'), /* Data that is being inserted */
('6','3456789012345678','0927','101','1'), /* Data that is being inserted */
('7','4567890123456789','0825','202','1'), /* Data that is being inserted */
('8','5678901234567890','0728','303','1'), /* Data that is being inserted */
('11','6789012345678901','0626','404','1'), /* Data that is being inserted */
('12','7890123456789012','0529','505','1'), /* Data that is being inserted */
('2','4536123478901234','1123','567','2'), /* Data that is being inserted */
('6','4789123456012345','0522','789','2'), /* Data that is being inserted */
('11','4123456789012345','0923','901','2'), /* Data that is being inserted */
('14','4567123456789012','1225','123','1'), /* Data that is being inserted */
('15','1234567899876543','1024','901','1'); /* Data that is being inserted */


INSERT INTO Catering (UserID, MealID, EventID, CardID, TypesOfCateringID, SpecificCateringRequests) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('2','1','1','1','1',''), /* Data that is being inserted */
('3','2','2','3','2','Cupcake_with_numbers_on_them'), /* Data that is being inserted */
('5','3','3','4','1',''), /* Data that is being inserted */
('6','4','4','5','2','Cupcakes_with_music_notes_one_them'), /* Data that is being inserted */
('7','5','5','6','1',''), /* Data that is being inserted */
('9','1','6','7','2','Packed_food_in_a_cooler'), /* Data that is being inserted */
('10','2','7','8','1',''), /* Data that is being inserted */
('2','3','8','2','2',''), /* Data that is being inserted */
('3','4','9','1','1',''), /* Data that is being inserted */
('5','5','10','4','2','Include_some_food_from_other_cultures'); /* Data that is being inserted */

INSERT INTO EventMenu (CateringID, MenuID) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('1','4'), /* Data that is being inserted */
('1','1'), /* Data that is being inserted */
('1','10'), /* Data that is being inserted */
('2','3'), /* Data that is being inserted */
('2','8'), /* Data that is being inserted */
('2','7'), /* Data that is being inserted */
('3','4'), /* Data that is being inserted */
('3','6'), /* Data that is being inserted */
('3','5'), /* Data that is being inserted */
('3','4'), /* Data that is being inserted */
('3','9'), /* Data that is being inserted */
('4','3'), /* Data that is being inserted */
('4','8'), /* Data that is being inserted */
('4','7'), /* Data that is being inserted */
('5','4'), /* Data that is being inserted */
('5','2'), /* Data that is being inserted */
('5','9'), /* Data that is being inserted */
('6','3'), /* Data that is being inserted */
('6','5'), /* Data that is being inserted */
('6','7'), /* Data that is being inserted */
('6','10'), /* Data that is being inserted */
('7','4'), /* Data that is being inserted */
('7','8'), /* Data that is being inserted */
('7','7'), /* Data that is being inserted */
('8','3'), /* Data that is being inserted */
('8','5'), /* Data that is being inserted */
('8','8'), /* Data that is being inserted */
('9','4'), /* Data that is being inserted */
('9','9'), /* Data that is being inserted */
('9','7'), /* Data that is being inserted */
('10','3'), /* Data that is being inserted */
('10','4'), /* Data that is being inserted */
('10','1'), /* Data that is being inserted */
('10','2'), /* Data that is being inserted */
('10','5'), /* Data that is being inserted */
('10','9'); /* Data that is being inserted */

INSERT INTO EventDietaryRequirements (DietaryTypesID, CateringID, Qty) /* Insets data into the selected table and rows */
VALUES /* Telling the program that the following lines are vaues that need to be inserted into database */
('1','1','7'), /* Data that is being inserted */
('2','2','8'), /* Data that is being inserted */
('3','2','5'), /* Data that is being inserted */
('4','3','2'), /* Data that is being inserted */
('5','3','1'), /* Data that is being inserted */
('6','3','6'), /* Data that is being inserted */
('7','4','9'), /* Data that is being inserted */
('8','4','5'), /* Data that is being inserted */
('9','4','5'), /* Data that is being inserted */
('10','4','4'), /* Data that is being inserted */
('1','6','9'), /* Data that is being inserted */
('2','6','5'), /* Data that is being inserted */
('3','6','3'), /* Data that is being inserted */
('4','6','3'), /* Data that is being inserted */
('5','8','8'), /* Data that is being inserted */
('6','8','6'), /* Data that is being inserted */
('7','9','8'); /* Data that is being inserted */