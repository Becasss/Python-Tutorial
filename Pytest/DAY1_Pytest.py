
'''Why Use Pytest?
1. Ease of Use: Write test cases in simple Python functions without boilerplate code.
2. Rich Features:
    - Built-in fixtures for setup and teardown.
    - Parameterized testing for multiple test scenarios.
3. Extensibility: Supports plugins and custom functionality.
4. Compatibility: Works well Selenium, Requests, and other QA tools.


'''

# Installing Pytest:pip install pytest



# Writingt Test Cases

# Basic Test case - A Pytest test case is just a Python function prefixed with test_:
'''def test_addition():
    assert 1 + 2 == 3
    '''


# Running Tests - Run the test case using the pytest command:


'''
pytest DAY1_Pytest.py
'''



# Key Pytest Features for QA

# 1. Asssertions - use python's assert keyword for validationg test results:

''' def test_string_contains():
        assert "QA" in "Quality Assurance"
        
        '''

# 2. Parameterized Testing: Test the same function with multiple inputs:

"""import pytest

@pytest.mark.parametrize("input,expected", [(2,4), (3,9), (4,16])
def test_square(input,expected):
    assert input**2 == expected
    """


# 3. Fixtures: Fixtures manage test setup and teardown.

"""import pytest
@pytest.fixture
def sample_data():
    return {"surname": "test_user", "password": "secured_password}
    
def test_login(sample_data):
    assert sample_data["username"] == "test_user"""


# 4. Grouping Test : Organize related test into classes.

"""class TestMathOperations:

    def test_addition(self):
        assert 1 + 2 == 3
        
    def test_subtraction(self):
        assert 5 - 3 == 2"""



# Run test in a specific class:

'''pytest -k TestMathOperations'''




# 5. Marking Test: Tag tests for selective execution.

'''import pytest

@pytest.mark.smoke
def test_critical_feature():
    assert True
    
    
@pytest.mark.regression
def test_minor_feature():
    assert True
    '''

# Run only smoke tests: pytest -m smoke


# Pytest with Selenium (example)- Pytest works seamlessly with Selenium for web automation.

"""form selenium import webdriver

@pytest.fixture
def browser():

driver = webdriver.chrome()
yield driver
driver.quit()

def test_google_search(browser):
browser.get('https://www.google.com')
assert "Google" in browser.title"""