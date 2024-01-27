import openai
from openai import OpenAI

# Set your OpenAI API key
api_key = "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" 
# openai.api_key = api_key
client = OpenAI(api_key=api_key)

# Define a function to interact with the chatbot    
def get_phone_plan_recommendation(prompt):
    # Make an API call using the updated method
    # response = openai.Completion.create(
    #     model="text-davinci-004",  # Updated to the latest GPT model
    #     prompt=prompt,
    #     temperature=0.7,
    #     max_tokens=150
    # )
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=3897
    )

    # Extract the generated text from the response
    recommendation = response.choices[0].text.strip()

    return recommendation

def chatGPT(monthly_cost, data_allowance, call_minutes, num_texts, network_speed):
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

def neural_networks(monthly_cost, data_allowance, call_minutes, num_texts, network_speed, optimal_service):
    data = {
        'Monthly Cost': monthly_cost,
        'Data Allowance (GB)': data_allowance,
        'International Call Minutes': call_minutes,
        'Number of Texts': num_texts,
        'Network Speed (Mbps)': network_speed,
        'Optimal Service': optimal_service
    }

    # Create a prompt based on user input
    prompt = f"""This is the phone service I was recommended. 
        This is how much I am looking to spend in dollars: {data['Monthly Cost']};
        this is my preferred data allowance in GB: {data['Data Allowance (GB)']};
        this is my preferred international call minutes per month: {data['International Call Minutes']};
        this is my preferred number of texts per month: {data['Number of Texts']};
        this is my preferred network speed in Mbps: {data['Network Speed (Mbps)']}.
        Based on this, list the benefits of using {data['Optimal Service']} service."""

    # Get a recommendation from the chatbot
    recommendation = get_phone_plan_recommendation(prompt)

    # Print the recommendation
    # print("Recommendation:")
    print(f"This is what people similar to you are using - {data['Optimal Service']}")
    print(recommendation)


def main():

    print("This is an optimal plan for you as recommended by generative AI: ")
    chatGPT(50, 5, 200, 1000, 150)
    print("")
    neural_networks(70, 5, 100, 1500, 180, "Sprint Unlimited Basic")


if __name__ == "__main__":
    main()
