import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # Load environment variables from .env


def beta_function1(param1, param2):
    """
    This endpoint acts as the SaulPaca user agent using Groq
    :param1: prompt
    :param2: user_id provide the user id to store user requests and responses

    :return: context
    """
    # Specify the file path and name
    filename = "features/alpha/prompts/SAULPACA_AGENT.txt"

    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the contents of the file
        system_prompt = file.read()

    # Print the loaded data
    print(system_prompt)
    chat_completion = _call_model("llama3-8b-8192", system_prompt, param1)
    response = chat_completion.choices[0].message.content
    my_dict = {
        "user_prompt": param1,
        "system_prompt": system_prompt,
        "chat_completion_response": response
    }

    return my_dict


def beta_function2(param1, param2):
    print("\n Inside beta function 2 \n")

    print(f"param3: {param1}")
    print(f"param4: {param2}")

    return param1 * param2


def beta_function3(param1, param2):
    print("\n Inside beta function 3 \n")

    print(f"param5: {param1}")
    print(f"param6: {param2}")

    secret_key = os.getenv("SECRET_KEY")
    print("\n API_KEY : ", secret_key, "\n")

    return param1 - param2



def _call_model(model, system, user):
    api_key = os.environ.get("GROQ_API_KEY")

    """
    Call the Groq model

    Args:
        model (str): model name.
        system (str): system prompt.
        user (str): user prompt.

    Returns:
        completion: The text completion json object.
    """
    client = Groq()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"{system}",
            },
            {
                "role": "user",
                "content": f"{user}",
            }
        ],
        model=f"{model}",
    )

    # print(chat_completion.choices[0].message.content)
    return chat_completion