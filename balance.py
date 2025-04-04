from supabase import create_client
import csv

# === Supabase Configuration ===
SUPABASE_URL = "https://asdoahgeiliotxyvnplu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFzZG9haGdlaWxpb3R4eXZucGx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM0NzgwMTcsImV4cCI6MjA1OTA1NDAxN30.vZk3XgKXwvrqfX4WfGTvUqj3HgzI7YjE8ds4XV3es0s"  # 🔐 Replace with your actual anon/public API key
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# === Fetch Finance Data from Supabase ===
def fetch_finance_data(user_id):
    response = supabase \
        .from_("user-finances") \
        .select("csv_data") \
        .eq("user_id", user_id) \
        .single() \
        .execute()

    if response.data and 'csv_data' in response.data:
        csv_text = response.data['csv_data']
        lines = csv_text.strip().split('\n')
        return list(csv.DictReader(lines))
    return []

# === Get Latest Balance from Last Row ===
def get_current_balance(user_id):
    rows = fetch_finance_data(user_id)
    if not rows:
        return 0.0
    try:
        return float(rows[-1]["Balance"])
    except (KeyError, ValueError):
        return 0.0

# === CLI Mode for Testing ===
if __name__ == "__main__":
    user_id = input("Enter your Supabase user ID: ")
    balance = get_current_balance(user_id)
    print(f"💰 Current balance: £{balance:.2f}")
