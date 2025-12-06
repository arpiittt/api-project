# API Verification Suite (Python/Pytest)

## Project Overview
This repository showcases end-to-end Quality Assurance skills by combining manual test design documentation with robust API test automation. The project focuses on verifying the core CRUD (Create, Read, Update, Delete) functionality of the JSONPlaceholder API.

## Technical Stack
* **Language:** Python 3.x
* **Testing Framework:** Pytest (for test structure and execution)
* **HTTP Client:** Requests library (for sending API calls)

## Testing Components
1.  **Automation Script (`test_posts.py`):** Contains automated tests for successful resource retrieval (GET 200), successful creation (POST 201), and error handling (GET 404).
2.  **Manual Documentation (`Manual_Test_Cases.md`):** Demonstrates professional QA planning, including test case design using Boundary Value Analysis (BVA) and Equivalence Partitioning (EP).

## How to Run the Tests
1.  **Clone the Repository:** `git clone https://github.com/arpitit/api-project.git`
2.  **Install Dependencies:** `pip install requests pytest`
3.  **Execute Tests:** Navigate to the directory and run: `pytest`
