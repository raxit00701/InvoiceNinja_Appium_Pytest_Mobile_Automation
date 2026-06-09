# Mifos Appium Test Framework

A production-grade mobile automation framework built with **Pytest + Appium (Python)**.

---

## 📁 Project Structure

```
Mifos_appium/
├── tests/                    # Test cases
│   ├── test_signup.py
│   └── test_db_validation.py
├── pages/                    # Page Object Model
│   ├── base_page.py
│   └── signup_page.py
├── utils/                    # Utilities
│   ├── driver_factory.py
│   ├── json_reader.py
│   ├── db_utils.py
│   ├── reset_manager.py
│   └── reporting_utils.py
├── config/env/               # Environment configs
│   ├── test.json
│   ├── stage.json
│   └── prod.json
├── data/
│   └── test_data.json        # JSON-driven test data
├── conftest.py               # Centralized fixtures
├── pytest.ini
└── requirements.txt
```

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

Ensure Appium server is running:
```bash
appium
```

---

## 🚀 Running Tests

### Basic run (test env, headed)
```bash
pytest tests/
```

### With environment selection
```bash
pytest tests/ --env=stage
pytest tests/ --env=prod
```

### Headless mode
```bash
pytest tests/ --headless
```

### With video recording
```bash
pytest tests/ --record-video
```

### Specific test
```bash
pytest tests/test_signup.py::TestSignup::test_signup_success -v
```

---

## 📊 Allure Reporting

Run tests and generate report:
```bash
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 🗄️ DB Validation

Configure your database in `config/env/test.json` under `db_config`.  
Then use `DBUtils` in tests to run validation queries.

---

## 🔁 App Reset Marker

Use `@pytest.mark.reset_app` on any test to automatically reset the app before it runs:

```python
@pytest.mark.reset_app
def test_something(self, driver, test_data):
    ...
```
