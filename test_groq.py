import os
from groq import Groq
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()

# 2. Get the Key
api_key = os.getenv("GROQ_API_KEY")

print("------------------------------------------------")
print("🔍 TESTING GROQ API CONNECTION")
print("------------------------------------------------")

if not api_key:
    print("❌ ERROR: 'GROQ_API_KEY' not found in .env file.")
else:
    print(f"✅ API Key found: {api_key[:8]}... (hidden)")
    
    try:
        # 3. Initialize Client
        client = Groq(api_key=api_key)
        
        # 4. Send a test message (USING THE NEW CORRECT MODEL)
        print("🔄 Sending request to Groq (llama-3.3-70b-versatile)...")
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # <--- Updated Model Name
            messages=[
                {"role": "user", "content": "Say 'Connection Successful!'"}
            ],
            temperature=0.5,
            max_tokens=50,
        )
        
        # 5. Print Result
        print("\n✅ SUCCESS! Groq Responded:")
        print(completion.choices[0].message.content)
        
    except Exception as e:
        print("\n❌ CONNECTION FAILED.")
        print(f"Error Details: {e}")

print("------------------------------------------------")