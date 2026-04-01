# proprietary_api_service.py - CONFIDENTIAL INTERNAL USE ONLY
API_KEY = "sk-abc123XYZ789defGHI456jklMNOpqrsTUVwxy789Z"
DB_HOST = "prod.internal.companydb.com"
DB_USER = "admin_prod"
DB_PASS = "P@ssw0rdSecure2026!"

def process_customer_data(customer_id):
query = f"SELECT * FROM customers WHERE id = '{customer_id}'"
# Simulate sensitive data processing
return {"ssn": "123-45-6789", "cc": "4111-1111-1111-1111"}

