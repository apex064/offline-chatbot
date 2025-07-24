import os
import sys
from faq_handler import FAQHandler
from sales_handler import SalesHandler

def main():
    print("==== OFFLINE CHATBOT ====")
    faq_path = input("Enter path to FAQ folder: ").strip()
    sales_path = input("Enter path to Sales CSV file: ").strip()

    if not os.path.isdir(faq_path):
        print("Invalid FAQ folder path.")
        return
    if not os.path.isfile(sales_path):
        print("Invalid Sales CSV path.")
        return

    faq = FAQHandler(faq_path)
    sales = SalesHandler(sales_path)

    print("\nType your query (type 'exit' to quit):\n")

    while True:
        query = input("You: ").strip().lower()
        if query in ['exit', 'quit']:
            print("Goodbye!")
            break

        # Determine intent
        if any(word in query for word in ['sales', 'product', 'total', 'average', 'month']):
            response = sales.answer_query(query)
        else:
            response = faq.answer_query(query)

        print("Bot:", response)

if __name__ == "__main__":
    main()

