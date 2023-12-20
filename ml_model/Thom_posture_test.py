import joblib
import pandas as pd

# Load the trained model
clf = joblib.load('posture_classifier_model.joblib')

# Define the number of postures
num_postures = 4

# Create a dictionary to map posture labels to recommendations
recommendations = {
    'nor_recom': "Maintain your current posture. It's good!",
    'left_recom': "Adjust your posture to the middle from left. Consider stretching and changing positions.",
    'right_recom': "Adjust your posture to the middle from right. Consider stretching and changing positions.",
    'front_recom': "Adjust your posture to the middle. Breaking back, consider stretching and changing positions."
}

while True:
    # Input four postures from the user
    user_input = []
    for i in range(num_postures):
        while True:
            try:
                posture = int(input(f"Enter Posture {i + 1} (1, 2, 3, or 4): "))
                if posture in [1, 2, 3, 4]:
                    user_input.append(posture)
                    break
                else:
                    print("Invalid input. Please enter postures 1, 2, 3, or 4.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    # Create a DataFrame with the user input
    user_input_df = pd.DataFrame([user_input], columns=[f'Posture{i + 1}' for i in range(num_postures)])

    # Make prediction using the trained model
    prediction = clf.predict(user_input_df)

    # Get the recommendation based on the predicted posture
    recommendation = recommendations.get(prediction[0], "Invalid posture recommendation.")

    # Print the recommendation
    print(f"Predicted Posture: {prediction[0]}")
    print(recommendation)

    # If you want to exit immediately after providing a recommendation, uncomment the next line
    # break
