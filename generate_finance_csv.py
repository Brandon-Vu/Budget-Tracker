import os
import csv

def generate_finance_csv():
    # Overwrite or create the CSV file with updated finance data.
    with open("finance.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write header row.
        writer.writerow(["Date", "Description", "Transaction Type", "Amount", "Balance"])
        
        # Original sample data.
        writer.writerow(["2023-03-20", "Initial Deposit", "credit", "1000", "1000"])
        writer.writerow(["2023-03-21", "ATM Withdrawal", "debit", "200", "800"])
        writer.writerow(["2023-03-22", "Grocery Shopping", "debit", "50", "750"])
        writer.writerow(["2023-03-23", "Salary", "credit", "1500", "2250"])
        writer.writerow(["2023-03-24", "Online Purchase", "debit", "100", "2150"])
        
        # Additional transactions to update bank balance.
        writer.writerow(["2023-03-25", "Utility Bill Payment", "debit", "150", "2000"])  # 2150 - 150 = 2000
        writer.writerow(["2023-03-26", "Interest Credit", "credit", "10", "2010"])          # 2000 + 10 = 2010
        writer.writerow(["2023-03-27", "Restaurant Bill", "debit", "60", "1950"])          # 2010 - 60 = 1950
        writer.writerow(["2023-03-28", "ATM Deposit", "credit", "500", "2450"])              # 1950 + 500 = 2450
        writer.writerow(["2023-03-29", "Loan Payment", "debit", "300", "2150"])              # 2450 - 300 = 2150
        writer.writerow(["2023-03-30", "Online Shopping", "debit", "120", "2030"])           # 2150 - 120 = 2030
        writer.writerow(["2023-03-31", "Salary", "credit", "1500", "3530"])                  # 2030 + 1500 = 3530

    print("finance.csv generated successfully.")

if __name__ == "__main__":
    generate_finance_csv()
