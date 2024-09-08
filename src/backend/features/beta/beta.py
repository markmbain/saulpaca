import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env


def beta_function1(param1, param2):
    print("\n Inside beta function 1 \n")

    print(f"param1: {param1}")
    print(f"param2: {param2}")

    return param1 + param2


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
