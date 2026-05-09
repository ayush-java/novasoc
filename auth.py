from supabase import create_client

SUPABASE_URL = "https://zsknhmtufffkspbqkrez.supabase.co"

SUPABASE_KEY = "sb_publishable_O83mvfWzSTKpphQy8IukNA_K-jTdwi6"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


