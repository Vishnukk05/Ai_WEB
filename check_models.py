import google.generativeai as genai
import os
from dotenv import load_dotenv

# Force load the .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env")
else:
    print(f"🔑 Checking key: {api_key[:5]}...{api_key[-4:]}")
    genai.configure(api_key=api_key)
    
    print("\n--- AVAILABLE MODELS FOR THIS KEY ---")
    try:
        count = 0
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Found: {m.name}")
                count += 1
        
        if count == 0:
            print("❌ No text generation models found. Your key might be valid but lacks permissions.")
            print("   Solution: Go to https://aistudio.google.com/app/apikey and create a new key.")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")