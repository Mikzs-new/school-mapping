import psycopg2

conn = psycopg2.connect(
    host="aws-1-ap-southeast-1.pooler.supabase.com",
    database="postgres",
    user="postgres.izlnpthnloqjpakvfujs",
    password="ck3O4fiC7WnUooj4",
    port=6543,
    sslmode="require"
)

print("Connected!")