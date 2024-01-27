from openai import OpenAI
import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import OneHotEncoder

# Set your OpenAI API key
api_key = "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" 
client = OpenAI(api_key=api_key)

# Define a function to interact with the chatbot    
def get_phone_plan_recommendation(prompt):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=3897
    )

    # Extract the generated text from the response
    recommendation = response.choices[0].text.strip()

    return recommendation

def chatgpt_rec(monthly_cost, data_allowance, call_minutes, num_texts, network_speed):
    # Create a DataFrame-like structure
    data = {
        'Monthly Cost': monthly_cost,
        'Data Allowance (GB)': data_allowance,
        'International Call Minutes': call_minutes,
        'Number of Texts': num_texts,
        'Network Speed (Mbps)': network_speed,
    }

    # Create a prompt based on user input
    prompt = f"""Recommend a phone service for me based on my needs.
        This is how much I am looking to spend in dollars: {data['Monthly Cost']};
        this is my preferred data allowance in GB: {data['Data Allowance (GB)']};
        this is my preferred international call minutes per month: {data['International Call Minutes']};
        this is my preferred number of texts per month: {data['Number of Texts']};
        this is my preferred network speed in Mbps: {data['Network Speed (Mbps)']}.
        Based on this, recommend me a phone service and also list the benefits of using this service."""

    # Get a recommendation from the chatbot
    recommendation = get_phone_plan_recommendation(prompt)

    # Print the recommendation
    print("Recommendation:")
    print(recommendation)

def sample_data():
    # Set the number of samples
    num_samples = 1000

    # Generate random data for each attribute
    np.random.seed(0)  # for reproducibility
    monthly_cost = np.random.uniform(10, 100, num_samples)
    data_allowance = np.random.uniform(1, 100, num_samples)  # in GB
    international_calls = np.random.randint(0, 500, num_samples)  # in minutes
    number_of_texts = np.random.randint(0, 1000, num_samples)
    network_speed = np.random.uniform(5, 150, num_samples)  # in Mbps
    customer_satisfaction = np.random.uniform(1, 5, num_samples)  # rating out of 5
    contract_length = np.random.randint(6, 24, num_samples)  # in months
    free_apps = np.random.randint(0, 20, num_samples)

    # Generate a random optimal plan (categorical target variable)
    plans = ['Verizon Unlimited Basic', 'AT&T Unlimited Elite', 'T-Mobile Magenta', 'Sprint Unlimited Plus', 'Google Fi Unlimited Plus', 'Verizon Play More Unlimited', 'AT&T Unlimited Starter','T-Mobile Magenta MAX', 'Sprint Unlimited Basic', 'Google Fi Flexible']
    optimal_plan = np.random.choice(plans, num_samples)

    # Create a DataFrame
    data = pd.DataFrame({
        'Monthly Cost': monthly_cost,
        'Data Allowance (GB)': data_allowance,
        'International Call Minutes': international_calls,
        'Number of Texts Per Month': number_of_texts,
        'Network Speed (Mbps)': network_speed,
        'Optimal Plan': optimal_plan
    })
    return data

def neural_network_rec(monthly_cost, data_allowance, call_minutes, num_texts, network_speed):
    data = sample_data()
    one_hot_encoded_df = pd.get_dummies(data, columns=['Optimal Plan'])
    one_hot_encoded_extras = ['Optimal Plan_AT&T Unlimited Elite',
    'Optimal Plan_AT&T Unlimited Starter',
    'Optimal Plan_Google Fi Flexible',
    'Optimal Plan_Google Fi Unlimited Plus',
    'Optimal Plan_Sprint Unlimited Basic',
    'Optimal Plan_Sprint Unlimited Plus',	
    'Optimal Plan_T-Mobile Magenta',
    'Optimal Plan_T-Mobile Magenta MAX',	
    'Optimal Plan_Verizon Play More Unlimited',
    'Optimal Plan_Verizon Unlimited Basic'] 

    for plan in one_hot_encoded_extras:
        one_hot_encoded_df[plan] = one_hot_encoded_df[plan].astype(int)
    
    X = one_hot_encoded_df[['Monthly Cost', 'Data Allowance (GB)', 'International Call Minutes', 'Number of Texts Per Month', 'Network Speed (Mbps)']].values

    y = one_hot_encoded_df[one_hot_encoded_extras].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    # Define the number of classes
    num_classes = 10  # Change this to the number of classes in your dataset

    # Define your neural network model
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(units=64, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(tf.keras.layers.Dense(units=32, activation='relu'))
    model.add(tf.keras.layers.Dense(units=num_classes, activation='softmax'))  # num_classes is the number of categories

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Fit the model
    model.fit(X_train, y_train, epochs=1000, batch_size=32, validation_data=(X_test, y_test))

    my_data = np.array([[monthly_cost, data_allowance, call_minutes, num_texts, network_speed]])

    predictions = model.predict(my_data)

    distance = [1-val for val in predictions]
    min_index = np.argmin(distance)
    print(f"best prediction: {one_hot_encoded_extras[min_index][13:]}")


def main():
    print("This is an optimal plan for you as recommended by generative AI: ")
    chatgpt_rec(50, 5, 200, 1000, 150)
    print("")
    neural_network_rec(70, 5, 100, 1500, 180)

if __name__ == "__main__":
    main()
