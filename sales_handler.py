import pandas as pd

class SalesHandler:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path, parse_dates=['Date'])
        self.df['Month'] = self.df['Date'].dt.to_period('M')

    def answer_query(self, query):
        query = query.lower()

        if "total sales" in query:
            if "product" in query:
                for product in self.df['Product'].unique():
                    if product.lower() in query:
                        total = self.df[self.df['Product'].str.lower() == product.lower()]['Sales'].sum()
                        return f"Total sales for {product}: {total}"
            total = self.df['Sales'].sum()
            return f"Total sales: {total}"

        elif "average sales" in query:
            avg = self.df['Sales'].mean()
            return f"Average sales: {avg:.2f}"

        elif "highest" in query and "month" in query:
            grouped = self.df.groupby('Month')['Sales'].sum()
            max_month = grouped.idxmax()
            return f"Highest-grossing month: {max_month} with {grouped[max_month]} sales."

        elif "product" in query and "most" in query:
            grouped = self.df.groupby('Product')['Sales'].sum()
            best = grouped.idxmax()
            return f"Highest-selling product: {best} with {grouped[best]} total sales."

        elif "sales in" in query:
            try:
                month = query.split("sales in")[-1].strip()
                month_period = pd.Period(month)
                total = self.df[self.df['Month'] == month_period]['Sales'].sum()
                return f"Sales in {month}: {total}"
            except:
                return "Could not parse the month. Try using format like '2023-05'."

        return "Sorry, I couldn't understand that sales query."

