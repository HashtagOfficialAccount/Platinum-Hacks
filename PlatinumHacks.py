print("Booting up Pricepath...")

#added in for effects
import time

#ML libraries
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


#main loop
while True:
    try:
        #choice variable
        local_prices = False
        
        #intro
        print("\nWelcome to PricePath——your path to finding the correct price for your house or car: ")
        print("OPTION #1 --- About PricePath")
        print("OPTION #2 --- House Price Estimate")
        print("OPTION #3 --- Car Price Estimate")
        print("OPTION #4 --- Exit PricePath")
        
        #choice selection
        option = input("Enter your choice here: ").strip().lower()

        #((el)if)/else statements for different choices
        if option == "1" or option == "about" or option == "about pricepath":
            print("\nPricePath is your guide to finding the right price for your car or house.")
            print("With top class Machine Learning models, we will get you a LOW, GOOD, and HIGH price for your home/car.")
            print("DISCLAMER: ***PricePath will NOT be responsible for any financial decisions made by you***")
            time.sleep(3)
            continue
        elif option == "2" or option == "house" or option == "house price" or option == "house price estimate":
            #user inputs
            print("\nWelcome to the house price estimate portal.")
            print("Enter the following information for us make the best house price prediction for you!")
            rooms = float(input("Number of bedrooms: "))
            bath_rooms = float(input("Number of bathrooms: "))
            ft = int(input("Enter square feet: "))

            #local price
            print("\nWe would also like to know how costly homes are usually in your location.")
            print("Please enter the typical price of a 2 bedroom and 2 bathroom (1250 sqft) house in your area.")
            print("If you choose not to specify, type X (not reccomended!)")
            print("***IMPORTANT---if you choose to specify, then specify VERY ACCURATELY***")
            print("***THIS FEATURE COULD MAKE THE RESULTS EXTREMELY ACCURATE or INCORRECT BASED ON THIS***")
            typical_price = input("Enter price here: ").strip().lower()

            #touch ups + data preparation
            print("\nAnalyzing Data...")
            dataframe = pd.read_csv("HouseData.csv")
            df = dataframe.iloc[30965:,:]
            df = df.dropna(axis = 0)
            
            print("\nMaking Predictions for you...")
            features = df[["bed","bath","house_size"]]
            labels = df["price"]
            time.sleep(1)
            
            print("\nAnalyzing Bedroom quantity...")
            train_x, val_x, train_y, val_y = train_test_split(features,labels)
            time.sleep(1)
            
            print("\nAnalyzing Bathroom quantity...")
            time.sleep(1)

            #Setting this up for local prices inclusion
            if not typical_price == "x":
                print("\nAccounting for Local Prices...")
                local_prices = True

            #Setting user data into a dataframe
            test_df = pd.DataFrame({"bed":[2],"bath":[2],"house_size":[1250]})

            #Random Forests ML Model
            print("\nPredicting using the ML Model...")
            model = RandomForestRegressor()
            model.fit(train_x,train_y)
            user_df = pd.DataFrame({"bed":[rooms],"bath":[bath_rooms],"house_size":[ft]})

            #local prices inclusion
            price = model.predict(user_df)
            if local_prices == True:
                test_pred = int(model.predict(test_df)[0])
                ratio = int(typical_price)/test_pred
                price = price * ratio
             
            #predictions output
            print(f"The prediction for your {rooms} bed and {bath_rooms} bath home are: ")
            print("LOW PRICE: " + str(int(price*0.9)))
            print("GOOD PRICE: " + str(int(price*1.1)))
            print("HIGH PRICE: " + str(int(price*1.3)))
            if local_prices == False:
                print("TIP: To increase accuracy, use the local prices feature.")
        elif option == "3" or option == "car" or option == "car price" or option == "car price estimate":
            #user inputs
            print("\nWelcome to the car price estimate portal.")
            print("Enter the following information for us make the best car price prediction for you!")
            print("\nSUV --- TYPE 1; Sedan --- TYPE 2; Other --- TYPE 3")
            car_type = input("Enter option from above: ").lower().strip()
            print("\nLUXURY --- TYPE 1; NORMAL --- TYPE 2; CHEAP --- TYPE 3")
            car = input("Enter option from above: ")
            print("\nBASE MODEL --- TYPE 1; SLIGHT UPGRADE --- TYPE 2; HEAVY UPGRADE --- TYPE 3; FLAGSHIP --- TYPE 4")
            base = input("Enter option from above: ")
            print("\nELECTRIC --- TYPE 1; GASOLINE/DIESEL --- TYPE 2")
            ev_gas = input("Enter option from above: ")
            car_model = input("Enter Car Model: (ex. Honda CRV, Lexus RX, etc.): ")
            year = int(input("\nEnter year: "))
            miles = int(input("\nEnter miles driven: "))

            #touch ups + data preparation
            print("\nAnalyzing Data...")
            dataframe = pd.read_csv("CarData.csv")
            df = dataframe.dropna(axis = 0)
            time.sleep(1)
            
            print("\nMaking Predictions for you...")
            features = df[["Year","Miles"]]
            label = df["Price"]
            time.sleep(1)

            print("\nAnalyzing Car Model...")
            train_x, val_x, train_y, val_y = train_test_split(features,label)
            time.sleep(1)
            
            print("\nAnalyzing Miles Driven...")
            time.sleep(1)
            
            user_df = pd.DataFrame({"Year":[year],"Miles":[miles]})
            #ML Model

            model = RandomForestRegressor()
            model.fit(train_x,train_y)
            
            price = model.predict(user_df)

            #LUXURY/NORMAL/CHEAP
            if car == "1":
                price = price * 1.25
            elif car == "2":
                price = price * 0.95
            #SUV/SEDAN/OTHER
            if car_type == "1":
                price = price * 1.25
            elif car_type == "2" or car_type == "3":
                price = price * 0.9
            #Model Type
            if base == "2":
                price = price * 1.1
            elif base == "3":
                price = price * 1.2
            elif base == "4":
                price = price * 1.3
            #EV
            if ev_gas == "1":
                price = price * 1.05
                
            #predictions output
            print(f"The predictions for your {year} {car_model} are: ")
            print("LOW PRICE: " + str(int(price*0.9)))
            print("GOOD PRICE: " + str(int(price)))
            print("HIGH PRICE: " + str(int(price*1.3)))
            
        elif option == "4" or option == "exit" or option == "quit" or option == "leave":
            confirmation = input("Are you sure you want to quit?: ").strip().lower()
            if confirmation == "y" or confirmation == "yes":
                print("We hope you enjoyed using PricePath.")
                break
            print("Redirecting you back home...\n")
            time.sleep(2)
        else:
            print("\nThat wasn't an option.")
            print("Redirecting you back home...\n")
            time.sleep(2)
    except:
        print("Something went wrong...Redirecting you back home...")
        time.sleep(1)
        continue
