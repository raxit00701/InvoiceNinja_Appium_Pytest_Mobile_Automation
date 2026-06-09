<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:662D91,50:D90429,100:FF8C00&height=210&section=header&text=📱%20INVOICE%20NINJA&fontSize=52&fontColor=ffffff&fontAlignY=38&fontAlign=50&desc=Appium%20Mobile%20Automation%20Suite&descAlignY=62&descSize=18&descColor=FAD2E1&animation=fadeIn" width="100%"/>

<br/>

<!-- BADGE ROW 1 — CORE STACK -->
![Python](https://img.shields.io/badge/Python-3.14.4-FF3B30?style=for-the-badge&logo=python&logoColor=white)
&nbsp;
![Appium](https://img.shields.io/badge/Appium-3.1.0-AF52DE?style=for-the-badge&logo=appium&logoColor=white)
&nbsp;
![Pytest](https://img.shields.io/badge/Pytest-8.2.0-FF9500?style=for-the-badge&logo=pytest&logoColor=white)
&nbsp;
![Allure](https://img.shields.io/badge/Allure-Report-E0245E?style=for-the-badge&logo=databricks&logoColor=white)
&nbsp;
![MySQL](https://img.shields.io/badge/MySQL-DB%20Validation-5856D6?style=for-the-badge&logo=mysql&logoColor=white)
<img src="https://img.shields.io/badge/License-Proprietary%20%C2%A9%202026%20Raxit%20Sharma-B22222?style=for-the-badge&logo=opensourceinitiative&logoColor=white"/>


<br/>

<!-- BADGE ROW 2 — CI/CD & ENVIRONMENT -->
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-FF2D55?style=for-the-badge&logo=jenkins&logoColor=white)
&nbsp;
![Android](https://img.shields.io/badge/Android-Mobile-FF8C00?style=for-the-badge&logo=android&logoColor=white)
&nbsp;
![Tests](https://img.shields.io/badge/E2E_Test%20Cases-14-9933FF?style=for-the-badge)
&nbsp;


<br/><br/>

**A production-grade, end-to-end mobile test automation framework for the Invoice Ninja Android app — featuring UI automation, live MySQL database validation, video recording, Allure reporting, and Jenkins CI/CD integration.**

<br>

<img src="https://raw.githubusercontent.com/your-username/your-repo/main/assets/appium_demo.gif" alt="Appium Test Run Animation" width="250" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">

</div>


---

## 📋 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Test Coverage](#-test-coverage)
- [Database Validation](#-database-validation)
- [Known Bug — Recurring Invoice DB](#-known-bug--recurring-invoice-db)
- [Setup & Installation](#-setup--installation)
- [Configuration](#-configuration)
- [Running Tests](#-running-tests)
- [Jenkins CI/CD Integration](#-jenkins-cicd-integration)
- [Allure Reporting](#-allure-reporting)
- [Framework Capabilities](#-framework-capabilities)
- [Tech Stack](#-tech-stack)

---

## 🔍 Overview

This framework automates the full functional lifecycle of the **Invoice Ninja** mobile application on Android using **Appium + Pytest**. It goes beyond simple UI checks — every critical business operation is validated end-to-end against a live **MySQL database**, ensuring both the frontend and backend are in sync after each action.

### Key Highlights

- ✅ **14 E2E test cases** across all major Invoice Ninja modules
- 🗄️ **Deep database validation** — not just UI assertions, but record-level SQL verification after every create/update operation
- 🎥 **Video recording** on test failure for fast root-cause analysis
- 📸 **Automatic screenshots** captured on any failing test
- 📊 **Allure HTML reports** with trend history preserved across runs
- 🔄 **Jenkins CI/CD** with parameterized pipeline (environment, test group, headless mode)
- 🌍 **Multi-environment support** — `test`, `stage`, `prod`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Jenkins CI/CD Pipeline                  │
│         (Environment × Test Group × Headless params)        │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      conftest.py                            │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  env_config │  │  DriverFactory│  │  DB Session (MySQL)│  │
│  │  (JSON env) │  │  (Appium drv) │  │  db_utils.py      │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Fixtures: handle_reset | handle_video | Screenshots │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
          ┌─────────────▼──────────────┐
          │        Tests Layer          │
          │  tests/test_*.py (14 cases) │
          └─────────────┬──────────────┘
                        │
          ┌─────────────▼──────────────┐
          │        Pages Layer          │
          │  Page Object Model (POM)    │
          │  pages/*.py                 │
          └─────────────┬──────────────┘
                        │
          ┌─────────────▼──────────────┐
          │    Dual Validation Layer    │
          │  UI Assert + DB SQL Assert  │
          └─────────────┬──────────────┘
                        │
          ┌─────────────▼──────────────┐
          │      Allure Report          │
          │  reports/allure-report/     │
          └────────────────────────────┘
```

---

## 📁 Project Structure

```
Invoice_ninja_appium_pytest/
│
├── config/
│   └── env/
│       ├── test.json           # Test environment config (Appium caps, DB creds)
│       ├── stage.json          # Staging environment config
│       └── prod.json           # Production environment config
│
├── data/                       # Parameterized test data (JSON)
│   ├── client_data.json
│   ├── expense_data.json
│   ├── invoice_data.json
│   ├── login_data.json
│   ├── payment_data.json
│   ├── product_data.json
│   ├── project_data.json
│   ├── purchase_order_data.json
│   ├── quote_data.json
│   ├── recurring_expense_data.json
│   ├── recurring_invoice_data.json
│   ├── task_data.json
│   ├── transaction_data.json
│   └── vendor_data.json
│
├── pages/                      # Page Object Model (POM)
│   ├── __init__.py
│   ├── client.py
│   ├── expenses.py
│   ├── invoice.py
│   ├── payment.py
│   ├── product.py              # Product page actions & locators
│   ├── projects.py
│   ├── purchase_orders.py
│   ├── quotes.py
│   ├── sidebar.py
│   ├── tasks.py
│   ├── transactions.py
│   ├── rec_invoice.py
│   ├── rec_expense.py
│   └── vendor.py
│
├── tests/                      # Test modules
│   ├── __init__.py
│   ├── test_client.py
│   ├── test_db.py              # Standalone DB connectivity test
│   ├── test_expense.py
│   ├── test_invoice.py
│   ├── test_login.py
│   ├── test_payment.py
│   ├── test_product.py         # Product creation + DB validation
│   ├── test_project.py
│   ├── test_purchase_order.py
│   ├── test_quote.py
│   ├── test_rec_expense.py
│   ├── test_rec_invoice.py     # ⚠️ Known DB bug (see below)
│   ├── test_task.py
│   ├── test_transactions.py
│   └── test_vendor.py
│
├── utils/                      # Framework utilities
│   ├── __init__.py
│   ├── db_utils.py             # MySQL connection + query helpers
│   ├── driver_factory.py       # Appium driver creation & teardown
│   ├── json_reader.py          # JSON config/data loader
│   ├── reporting_utils.py      # Screenshots, video recording, logging
│   └── reset_manager.py        # App reset / restart between tests
│
├── reports/
│   ├── allure-results/         # Raw Allure result JSONs (auto-generated)
│   └── allure-report/          # Built HTML report (with persistent history)
│
├── .github/                    # GitHub Actions workflows
├── conftest.py                 # Session fixtures, hooks, reset/video/screenshot logic
├── pytest.ini                  # Configuration toggles & markers
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ✅ Test Coverage

All 14 test cases follow the same pattern: **UI flow → Save → DB assertion**.

| # | Test File | Feature | DB Validation | Marker |
|---|-----------|---------|:-------------:|--------|
| 1 | `test_login.py` | Login / Auth | ✗ | `smoke`, `login` |
| 2 | `test_client.py` | Create Client | ✅ | `smoke` |
| 3 | `test_product.py` | Create Product | ✅ | `smoke` |
| 4 | `test_invoice.py` | Create Invoice | ✅ | `smoke` |
| 5 | `test_payment.py` | Record Payment | ✅ | `smoke` |
| 6 | `test_quote.py` | Create Quote | ✅ | `smoke` |
| 7 | `test_expense.py` | Log Expense | ✅ | `smoke` |
| 8 | `test_purchase_order.py` | Create Purchase Order | ✅ | `smoke` |
| 9 | `test_project.py` | Create Project | ✅ | `smoke` |
| 10 | `test_task.py` | Create Task | ✅ | `reg` |
| 11 | `test_vendor.py` | Create Vendor | ✅ | `reg` |
| 12 | `test_transactions.py` | Log Transaction | ✅ | `reg` |
| 13 | `test_rec_invoice.py` | Create Recurring Invoice | ✅ ⚠️ | `smoke` |
| 14 | `test_rec_expense.py` | Create Recurring Expense | ✅ | `reg` |

> `test_db.py` is a standalone DB connectivity health-check — excluded from the main suite via `--ignore=tests/test_db.py` in Jenkins.

---

## 🗄️ Database Validation

Database validation is a **core feature** of this framework — not an afterthought. Every test that creates or modifies a record in the app will subsequently query the MySQL database directly and assert each field individually, including:

- Record existence with `is_deleted = 0` guard
- Field-by-field comparison (name, amount, notes, URLs, quantities, etc.)
- **Retry logic** — up to 15 attempts with 3-second intervals to account for backend processing lag
- Full debug output of the raw SQL result in the console and Allure report

**Example — Product DB validation query:**

```sql
SELECT
    id,
    product_key   AS product_name,
    notes         AS description,
    price,
    quantity      AS default_quantity,
    max_quantity,
    product_image AS image_url,
    created_at
FROM products
WHERE TRIM(product_key) = TRIM(%s)
  AND is_deleted = 0
ORDER BY created_at DESC
LIMIT 1
```

Individual assertions validate each mapped column against the test data, e.g.:

```python
assert float(result["price"]) == float(product["price"])
assert int(result["max_quantity"]) == int(product["max_quantity"])
assert result["image_url"] == product["image_url"]
```

<div align="center">

### 🎥 Framework Execution Demo

<img src="https://raw.githubusercontent.com/raxit00701/InvoiceNinja_Appium_Pytest_Mobile_Automation/580967c07b2068594ae45c52852c775d3f2e8367/My%20Video.gif" 
     alt="Appium Test Execution" 
     width="250" 
     style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">

</div>
```
## ALLURE REPORT RESULTS

<div align="center">
  <img src="./Screenshot%202026-06-09%20201205.png" alt="Invoice Ninja Allure Report Dashboard" width="90%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
</div>
---



## ⚠️ Known Bug — Recurring Invoice DB

**File:** `tests/test_rec_invoice.py`

A discrepancy has been identified between the data entered in the **Recurring Invoice UI** and the values stored in the database. Specifically, certain note fields (`public_notes`, `private_notes`) are being mismatched or mapped incorrectly at the database level after the UI form submission.

**Observed behavior (from terminal output):**

```
Entered UI Notes    :  THIS IS PUBLIC NOTES
Invoice_DB Notes    :  Preferred client - priority support   ← ❌ Wrong
Valid_to_DB Notes   :  Preferred client - priority support
Client DB Notes     :  Preferred client - priority support
```

**Expected:** The `public_notes` field in the `recurring_invoices` table should store `THIS IS PUBLIC NOTES` as entered in the UI form.

**Actual:** The field stores the client's `public_notes` value instead of the invoice-specific note, suggesting a **field mapping error** either in the app's API payload or the backend insert logic.

> 🔖 This has been logged and is pending investigation with the Invoice Ninja backend team. The test is currently marked as a known failure for this assertion block.

---

## ⚙️ Setup & Installation

### Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.14.4 |
| Appium Server | 2.x |
| Android SDK / ADB | Latest |
| MySQL Server | 8.x |
| Node.js | 18+ (for Appium) |
| Allure CLI | 2.x |

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Invoice_ninja_appium_pytest.git
cd Invoice_ninja_appium_pytest
```

### 2. Create Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Appium Server

```bash
appium --address 127.0.0.1 --port 4723
```

### 5. Connect Android Device / Emulator

```bash
adb devices   # verify device is listed
```

---

## 🔧 Configuration

### Environment Config (`config/env/<env>.json`)

Each environment file contains Appium desired capabilities and database credentials:

```json
{
  "appium": {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.invoiceninja.app",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2",
    "noReset": true
  },
  "db": {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "your_password",
    "database": "ninja"
  }
}
```

### pytest.ini Toggles

```ini
[pytest]
addopts = --alluredir=reports/allure-results -v --tb=short

markers =
    reset_app   : Reset the app before this test
    restart_app : Restart app without clearing data
    smoke       : Smoke testing group
    reg         : Regression testing group
    login       : Login testing group

# ── Reporting toggles ── change true/false to enable/disable ──
screenshots = false     # Capture PNG on test failure
logs        = true      # Log output to file
video       = false     # Record video — saved only on failure
headless    = true      # Run Appium in headless mode

log_cli         = true
log_cli_level   = INFO
log_format      = %(asctime)s [%(levelname)s] %(name)s - %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```

---

## 🚀 Running Tests

### Run Full Suite

```bash
pytest tests/ --ignore=tests/test_db.py --env=test
```

### Run Specific Marker Group

```bash
# Smoke tests only
pytest tests/ -m smoke --env=test

# Regression tests only
pytest tests/ -m reg --env=stage

# Login tests only
pytest tests/ -m login --env=test
```

### Run Single Test File

```bash
pytest tests/test_product.py --env=test -s
```

### Run with Headless Mode

```bash
pytest tests/ --env=test --headless
```

### Run DB Health Check Only

```bash
pytest tests/test_db.py --env=test -s
```

### Generate & Open Allure Report

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

---

## 🔄 Jenkins CI/CD Integration

The pipeline is fully parameterized — each build can be configured via:

| Parameter | Options | Default |
|-----------|---------|---------|
| `ENVIRONMENT` | `test`, `stage`, `prod` | `test` |
| `TEST_GROUP` | `all`, `smoke`, `reg`, `login` | `smoke` |
| `HEADLESS` | `true`, `false` | `true` |

### Jenkins Build Script (`Jenkinsfile` / `.bat`)

```batch
echo ========================================
echo 🚀 Starting Appium Automation Run
echo Environment: %ENVIRONMENT%
echo Test Group:  %TEST_GROUP%
echo Headless:    %HEADLESS%
echo ========================================

:: 1. Setup Virtual Environment & Dependencies
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

:: 2. Base Pytest Command
set PYTEST_CMD=pytest tests/ --ignore=tests/test_db.py ^
    --env=%ENVIRONMENT% ^
    --alluredir=reports/allure-results ^
    -s --disable-warnings

:: 3. Handle Test Groups (skip -m flag if 'all')
if not "%TEST_GROUP%"=="all" (
    set PYTEST_CMD=%PYTEST_CMD% -m "%TEST_GROUP%"
)

:: 4. Handle Headless Flag
if "%HEADLESS%"=="true" (
    set PYTEST_CMD=%PYTEST_CMD% --headless
)

:: 5. Execute
echo Executing: %PYTEST_CMD%
%PYTEST_CMD%
```

### Allure Report in Jenkins

Install the **Allure Jenkins Plugin** and point it to `reports/allure-results`. Historical trend data is preserved automatically — `conftest.py`'s `pytest_sessionstart` hook copies `history/` from the last generated report back into the results directory before each run.

---

## 📊 Allure Reporting

The framework generates rich Allure reports with:

- **Feature / Story / Severity** labels on every test
- **Step-by-step** breakdown of UI and DB actions
- **Screenshots** attached on failure
- **Video recordings** attached on failure (when `video=true`)
- **Environment properties** displayed on the dashboard (`Environment`, `Test_Groups`)
- **Trend history** preserved across Jenkins builds

**Allure decorators used in tests:**

```python
@allure.feature("Products")
@allure.story("Create Product")
@allure.title("Create product and validate in database")
@allure.description("Validate product creation flow and database validation")
@allure.severity(allure.severity_level.CRITICAL)
```

---

## 🧰 Framework Capabilities

### Page Object Model (POM)

Each screen has a dedicated page class in `pages/` with:
- Named locator constants (Accessibility ID, UiAutomator2, XPath)
- Action methods that encapsulate all element interactions
- Explicit waits via `WebDriverWait` — no bare `time.sleep()` in critical paths

### Smart App Reset

Tests can be decorated with:

```python
@pytest.mark.reset_app     # Clears app data + restarts
@pytest.mark.restart_app   # Restarts without clearing data
```

`ResetManager` handles both strategies transparently via `conftest.py`'s `handle_reset` autouse fixture.

### DB Retry Logic

Database assertions use a **retry loop** (15 × 3 s) to handle real-world async backend processing, preventing false failures from timing issues.

### Logging

`setup_logging()` writes structured logs to `reports/logs/` with timestamps. Toggle via `logs = true/false` in `pytest.ini`.

### Video on Failure

When `video = true`, `handle_video` starts screen recording at the beginning of each test and saves the video only if the test fails — discarding it on pass to conserve storage.

---

## 🧪 Sample Test Data (`data/expense_data.json`)

```json
{
  "expenses": [
    {
      "customer": "Global Freight Logistics",
      "project": "Nova Digital Systems 774816",
      "expense_type": "test",
      "category": "category test",
      "amount": "10",
      "notes": "this is for public notes",
      "vendor_notes": "this is for private notes"
    }
  ]
}
```

Test data is loaded once per session, and each test class reads only its own JSON file. Product tests inject a `random.randint(1000, 9999)` suffix to ensure uniqueness across runs.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.14** | Core language |
| **Appium 3.1.0** | Mobile UI automation driver |
| **UiAutomator2** | Android automation engine |
| **Pytest 8.2.0** | Test runner, fixtures, markers |
| **Allure Framework** | HTML test reporting with trends |
| **MySQL Connector** | Direct database validation |
| **Selenium WebDriverWait** | Explicit wait conditions |
| **Jenkins** | CI/CD pipeline with parameterized builds |
| **Pluggy / pytest-ordering** | Hook system & test ordering |

---

## 📄 License

🛑 PROHIBITED — ALL RIGHTS RESERVED
This project, including all associated source code, design assets, configurations, and documentation, is strictly proprietary and confidential.

Unauthorized copying, cloning, modification, redistribution, execution, or use of this repository—or any portion thereof—via any medium is strictly prohibited without explicit, prior written authorization from the copyright holder .
**All Rights Reserved © 2026 Raxit Sharma**

---

<div align="center">

Built with ❤️ for robust, database-backed mobile test automation.

**Invoice Ninja Appium Pytest** — *Test the UI. Verify the truth in the database.*

</div>
