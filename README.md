# Platinum-Hacks
IMPORTANT INFORMATION 1) To test this, you NEED to download ALL GitHub files (the python file, CSV files) 2) You MUST have the pandas and sklearn libraries downloaded on YOUR device or else you will get an error.

1) Inspiration I was inspired to create this platform because I have been learning about python machine learning for the past 6 months and wanted to apply it creatively and usefully.

2) What it does Pricepath uses the Random Forest decision tree regressor to predict the price of your home or car.

3) How we built it

For the house price prediction, we take in the number of bedrooms and bathrooms as the user inputs (features), and we predict the house price (label). We also have an EXCELLENT feature that produces outputs almost identical to the prices listed on various websites. It accounts for local prices in the neighborhood you are in for a 2 bed, 2 bath, and 1250 sq ft. home. It will also predict the price for this home through the model. We then take the ratio of the (local price/predicted price) and multiply it by the price the model predicts for the actual user inputs. This ensures maximum accuracy and the least mean absolute error (the difference between prediction and actual)

For the car price prediction, we take the year and miles driven as the user inputs (features), and we predict the house price (label). And since we are all about accuracy, we also take in other inputs such as: 1) SUV, Sedan, or Other || 2) Luxury, Normal, or Cheap || 3) Base Model, Slight Upgrade, Heavy Upgrade, Flagship || 4) Electric, Gas/Diesel. By accounting for this data, we can alter the final prediction (either increasing it or decreasing it).

5)Challenges we ran into

Finding good data. It was very time-consuming to find a good CSV file with valid information for a plethora of cars.
Reducing the size of the CSV file (it was 120 MB)
Accounting for local prices
6) Accomplishments that we're proud of We are proud of our overall design, accuracy, and performance of Pricepath.

7) What we learned We learned about how important it is for you to have good data to train your model with as that is what ultimately decides the accuracy.

8) What's next for PricePath What is next is for YOU to test it out yourself and find the right price for you. Welcome to your path to finding the right price for your house/car.
