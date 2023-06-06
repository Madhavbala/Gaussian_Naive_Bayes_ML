Titanic Survival Prediction
This is a Python script that uses machine learning techniques to predict whether a person survived the Titanic disaster based on various features such as gender, age, 
fare, and passenger class.

Dependencies
Make sure you have the following dependencies installed:

Dataset
The script uses the Titanic survival dataset, which should be in CSV format. The dataset is loaded using pandas, and the file path is specified as C:\\Users\\madhavan.bala\\Downloads\\Day_6\\titanicsurvival.csv.
Adjust the file path accordingly if necessary.

Usage
Ensure that the Titanic survival dataset is in the correct location and named titanicsurvival.csv.
Run the script using a Python interpreter.

The script performs the following steps:

a. Reads the dataset and displays the first few rows.
b. Converts the 'Sex' column to numeric values (0 for 'female' and 1 for 'male').
c. Segregates the dataset into input (X) and output (Y) variables.
d. Removes any missing values in the input variables.
e. Splits the dataset into training and testing sets.
f. Trains a Gaussian Naive Bayes model on the training data.
g. Prompts for input to predict survival for a specific person based on their passenger class, gender, age, and fare.
h. Prints the predicted result indicating whether the person might have survived or not.
i. Predicts survival for all the test data and calculates the accuracy of the model.

Follow the prompts in the terminal to enter the person's details for prediction.

Example Output
mathematica
Copy code
Enter Person's Pclass number: 1
Enter Person's Gender 0-female 1-male(0 or 1): 1
Enter Person's Age: 30
Enter Person's Fare: 50.0
Person might be Survived

Accuracy of the model: 78.0%
Note: The results may vary depending on the dataset and the model's performance.

Conclusion
This script demonstrates a simple implementation of predicting Titanic survival using a Gaussian Naive Bayes classifier. Feel free to modify the code to experiment with different algorithms,
features, or even hyperparameters to improve the predictions.
