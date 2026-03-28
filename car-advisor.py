from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

indian_budget_car_ = [
    {
        "type": "function",
        "function": {
            "name": "buget_indian_cars",
            "description": (
                "A budget car for the average indian user "
                "If the car is above 20 lakhs, encourage them to look for cheaper models "
                "If the car is a good value for money car, encourage them to keep looking in to it. "
                "Be extremely blunt. For example, if they are looking for any used german cars which falls under 20lakhs, tell them to re-evaluate their choices due to their high maintanance charges."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "budget_friendly_car": {
                        "type": "boolean",
                        "description": "A boolean value to determine if the car is actually worth the money or not."
                    },
                    "note_to_user": {
                        "type": "string",
                        "description": "Recommendation to the user, e.g., 'Good job, keep it up!' or 'Stop looking at expensive stuff you brokie!'"
                    }
                },
                "required": [
                    "budget_friendly_car",
                    "note_to_user"
                ]
            }
        }
    }
]

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = input("Which car are you looking for?\n")

response = openai_client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system",
            "content": "You are a brutally honest Indian car advisor. Follow the tool instructions strictly."
        },
        {"role": "user", "content": prompt}
    ],
    tools=indian_budget_car_,
    tool_choice="required"
)

answer = response.choices[0].message.tool_calls[0]
answer_dict = json.loads(answer.function.arguments)

note_to_user = answer_dict["note_to_user"]
budget_friendly_car = answer_dict["budget_friendly_car"]

if budget_friendly_car:
    print("Good job, thats a great car choice!!")
    print(note_to_user)
elif not budget_friendly_car:
    print("Oh no, Re-evaluate your choices you broke man!")
    print(note_to_user)

print("fin.")
