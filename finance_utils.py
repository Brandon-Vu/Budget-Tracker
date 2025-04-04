import csv
from supabase import create_client

SUPABASE_URL = "https://asdoahgeiliotxyvnplu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFzZG9haGdlaWxpb3R4eXZucGx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM0NzgwMTcsImV4cCI6MjA1OTA1NDAxN30.vZk3XgKXwvrqfX4WfGTvUqj3HgzI7YjE8ds4XV3es0"  # Replace with your real anon key
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def read_finance_csv(user_id):
    response = supabase \
        .from_("finance_data") \
        .select("csv_data") \
        .eq("user_id", user_id) \
        .single() \
        .execute()

    if response.data and 'csv_data' in response.data:
        csv_text = response.data['csv_data']
        lines = csv_text.strip().split('\n')
        return list(csv.DictReader(lines))
    return []

def write_finance_csv(user_id, rows):
    if not rows:
        return
    headers = rows[0].keys()
    csv_lines = [','.join(headers)] + [','.join([row[h] for h in headers]) for row in rows]
    csv_data = '\n'.join(csv_lines)
    supabase \
        .from_("finance_data") \
        .upsert({"user_id": user_id, "csv_data": csv_data}, on_conflict=["user_id"]) \
        .execute()

def format_finance_data(data):
    output = []
    for row in data:
        output.append(
            f"{row['Date']} - {row['Description']} ({row['Category']}): {row['Transaction Type']} £{row['Amount']} | Balance: £{row['Balance']}"
        )
    return "\n".join(output)
