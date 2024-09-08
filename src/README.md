# Ultimate Hackathon Template

Flask Backend and Next.js frontend

## Backend ( Flask )

### Backend Guide for frontend

#### running on port number : 5001

#### API Route Table :

| Type of API | API Url                   | Usecase                       | No. of parameters | Parameters | Datatype |
| ----------- | ------------------------- | ----------------------------- | ----------------- | ---------- | -------- |
| GET         | /                         | Test Hello World in browser   | 0                 | None       |          |
| POST        | /features/alpha_function1 | Addition of two numbers       | 2                 | x,y        | int, int |
| POST        | /features/alpha_function2 | Multiplication of two numbers | 2                 | x,y        | int, int |
| POST        | /features/alpha_function3 | Division of two numbers       | 2                 | x,y        | int, int |
| POST        | /features/beta_function1  | Addition of two numbers       | 2                 | x,y        | int, int |
| POST        | /features/beta_function2  | Multiplication of two numbers | 2                 | x,y        | int, int |
| POST        | /features/beta_function3  | Division of two numbers       | 2                 | x,y        | int, int |
| POST        | /features/gamma_function1 | Addition of two numbers       | 2                 | x,y        | int, int |
| POST        | /features/gamma_function2 | Multiplication of two numbers | 2                 | x,y        | int, int |
| POST        | /features/gamma_function3 | Division of two numbers       | 2                 | x,y        | int, int |

### Notes :

1. All features should be inside features folder. The folder is further devided into 3 sub folders alpha, beta, gamma.
   - **_folder path : cd /backend/features_**
2. alpha, beta and gamma folder follow the following function structure:
   - Each folder has the foldername.py and foldername_test.py file.
   - Three functions are written and tested inside each files.
3. All jupiter notebooks should only be created inside jupiter_notebooks folder.
   - **_folder path : cd /backend/features/jupiter_notebooks_**
4. 9 api calls are already created with test cases, always make sure all test cases are passing before commiting the code.
   - **command to test the code : pytest**
5. Only push after updating the requirements.txt file.
   - **command : pip freeze > requirements.txt**
6. Update the the API route table above.
7. Update eveyone about the .env files.
8. Get push confirmation from 2 people atleast.

### How to add env variables ?

1. Add env_variables to .env file
2. Add the same env_variables to .env.template
3. To use the env_variables in the file :

   ```
   # import pakages and load env variables from .env
   import os
   from dotenv import load_dotenv
   load_dotenv()

   # inside function
   secret_key = os.getenv("SECRET_KEY")
   print("\n API_KEY : ", secret_key, "\n")
   ```

### To run the backend server in Flask

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 appliaction.py
```

## Frontend ( Vite + React + Tailwind )

### Frontend guide

#### Running on port number : 5173

### To run the frontend server

```
cd frontend
npm install
npm run dev
```
