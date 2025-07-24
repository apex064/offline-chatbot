# Offline Python Chatbot

## Overview

This is a **simple offline chatbot application** built with Python. It allows users to query:

- **Frequently Asked Questions (FAQs)** stored in local `.txt` files.
- **Sales data** stored in a local `.csv` file.

The chatbot processes all queries entirely **offline**, without any internet connection.

---

## Features

- **FAQ Handling:**  
  Loads multiple FAQ `.txt` files from a specified folder. Each FAQ file contains question-answer pairs.  
  Answers user questions by finding the most relevant FAQ entry using TF-IDF text matching.

- **Sales Data Handling:**  
  Loads sales data from a CSV file with columns: `Date`, `Product`, and `Sales`.  
  Supports queries on total sales, average sales, product-wise sales, monthly sales, and trends like highest-grossing month/product.

- **Command-Line Interface (CLI):**  
  Users interact by typing natural language queries directly in the terminal.

- **Quick Responses:**  
  Data is pre-loaded and indexed for fast query processing.

---

## Installation

1. Clone or download this repository.

2. Create and activate a Python virtual environment:

``
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install pandas scikit-learn
Usage
Prepare your data:

Place your FAQ .txt files in a folder (e.g., sample_data/faqs).

Ensure your sales data CSV file is formatted like this:

csv
Copy
Edit
Date,Product,Sales
2023-01-01,clock,100
2023-01-15,book,200
...
Run the chatbot script:

bash
Copy
Edit
python chatbot.py
When prompted:

Enter the path to your FAQ folder.

Enter the path to your sales CSV file.

Ask your questions directly in the CLI.

To exit, type exit or quit.

Supported Queries
FAQ Queries
Ask any question related to your FAQ content, such as:

What is your return policy?

How do I track my order?

What payment methods do you accept?

Can I cancel my order?

How long does shipping take?

Sales Data Queries
You can ask questions like:

Total sales for [product name] (e.g., Total sales for clock)

Average sales

Highest-grossing month

Sales in [YYYY-MM] (e.g., Sales in 2023-03)

Most selling product

Example Queries
plaintext
Copy
Edit
You: What is your return policy?
Bot: Our return policy allows 30-day returns with a receipt.

You: Total sales for clock
Bot: Total sales for clock: 100

You: What is the highest-grossing month?
Bot: Highest-grossing month: 2023-03 with 420 sales.

You: How do I reset my password?
Bot: You can reset your password by clicking "Forgot Password" on the login page.
Extending and Customizing
Add or update FAQ .txt files with new question-answer pairs.

Update sales CSV data for fresh sales records.

i will Improve query understanding by adding NLP intent classification (future work).

and Create a GUI or web interface if needed.


Contact
For questions or help, please contact: [chimanov2005@gmail.com]

