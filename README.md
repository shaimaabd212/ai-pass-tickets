# AI-Pass Automation Pipeline

## Use Case
Customer Support Ticket Automation Pipeline.

## Data Source
JSONPlaceholder API

https://jsonplaceholder.typicode.com/comments

## Pipeline Stages
1. Data ingestion from API
2. Cleaning
3. Validation
4. Decision logic
5. Storage

## Validation Rules
- Missing customer
- Missing description
- Short description
- Invalid email
- Duplicate ticket ID

## Business Decision Logic

PASS
Valid ticket

FAIL
Missing customer or invalid email

NEEDS_REVIEW
Minor validation issues

## Dashboard
Built with Streamlit.

Shows:
- Total records
- PASS / FAIL / NEEDS_REVIEW
- Status distribution
- Customer ticket counts

## Deployment
Streamlit Community Cloud
