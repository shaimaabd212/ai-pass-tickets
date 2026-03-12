import requests
import pandas as pd
import os
import json

print("Loading pipeline...")

API_URL = "https://jsonplaceholder.typicode.com/posts"


def ingest():

    print("Ingesting data...")

    os.makedirs("data", exist_ok=True)

    try:

        response = requests.get(API_URL, timeout=10)

        if response.status_code == 200:

            data = response.json()

            with open("data/raw_tickets.json", "w") as f:
                json.dump(data, f)

            print("API data saved")

        else:
            print("API request failed")

    except Exception as e:
        print("API error:", e)

    # If file doesn't exist, create fallback data
    if not os.path.exists("data/raw_tickets.json"):

        print("Creating fallback dataset")

        data = [
            {"ticket_id":1,"customer":"user1","issue_type":"login","description":"cannot login to account"},
            {"ticket_id":2,"customer":"user2","issue_type":"billing","description":"invoice incorrect"},
            {"ticket_id":3,"customer":None,"issue_type":"technical","description":"app crashes"},
            {"ticket_id":4,"customer":"user3","issue_type":"account","description":"password reset problem"},
            {"ticket_id":5,"customer":"user4","issue_type":"billing","description":""}
        ]

        df = pd.DataFrame(data)

    else:

        df = pd.read_json("data/raw_tickets.json")

        df = df.rename(columns={
            "id": "ticket_id",
            "userId": "customer",
            "title": "issue_type",
            "body": "description"
        })

    return df


def clean(df):

    print("Cleaning data...")

    df["description"] = df["description"].astype(str).str.strip()

    return df


def validate(df):

    print("Validating data...")

    df["missing_customer"] = df["customer"].isna()

    df["missing_description"] = df["description"] == ""

    df["short_description"] = df["description"].str.len() < 10

    df["duplicate_ticket"] = df.duplicated("ticket_id")

    return df


def decision_logic(df):

    print("Applying decision logic...")

    def classify(row):

        if row["missing_customer"]:
            return "FAIL"

        if row["missing_description"] or row["short_description"]:
            return "NEEDS_REVIEW"

        return "PASS"

    df["status"] = df.apply(classify, axis=1)

    return df


def run_pipeline():

    print("Running pipeline...")

    df = ingest()

    df = clean(df)

    df = validate(df)

    df = decision_logic(df)

    df.to_csv("processed_tickets.csv", index=False)

    print("Pipeline completed")

    return df