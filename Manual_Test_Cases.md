## Manual Test Cases & Test Design Documentation

This document outlines high-priority manual test cases for the /posts API resource, designed using Boundary Value Analysis (BVA) and Equivalence Partitioning (EP) to ensure comprehensive coverage.

### Resource: POST /posts (Create New Post)

| Field | Description |
| :--- | :--- |
| **Test Case ID** | TC_POST_002_TITLE_INVALID |
| **Title/Summary** | **Verify POST request handles a Title length just below the minimum boundary (9 characters).** |
| **Prerequisites** | API is running and accessible. |
| **Test Steps** | 1. Prepare POST request payload with a 9-character title (e.g., "123456789"). 2. Send POST request to /posts endpoint. |
| **Expected Result** | **The API should return a Status Code 400 (Bad Request)** and the response body should contain a validation error message specifically mentioning the Title field length constraint. |
| **Test Data (Title used)** | A string of exactly **9 characters** (e.g., "ShortFail"). |