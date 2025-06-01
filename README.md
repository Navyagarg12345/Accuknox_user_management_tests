#OrangeHRM Admin Module Automation (Playwright + Python)

##Scenarios Covered
1. Navigate to Admin Module
2. Add a New User
3. Search the Newly Created User
4. Edit all Possible User Details
5. Validate Updated Details
6. Delete the User

##Tech Stack
- Python
- Playwright
- Pytest
- Page Object Model

##Setup Instructions

1. Install all the requirements (refer requirements.txt)
2. In command prompt: 
create and activate a virtual environment:
python -m venv venv
On Windows: venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
playwright install

##How to Run Tests
Note: virtual environemt should be activated 
command to run test file in cmd:
pytest tests/test_add_user.py --headed --browser=chromium //here, after 'tests/'(give test file name individually)

Note: Make sure test_add_user.py runs first to generate the user used by other test cases.

##Playwright Version
Playwright Python: 1.52.0
