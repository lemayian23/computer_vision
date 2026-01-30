import json
import os
from pathlib import Path

print("="*60)
print("🔍 CHECKING KAGGLE AUTHENTICATION")
print("="*60)

# Location of kaggle.json
kaggle_path = Path.home() / ".kaggle" / "kaggle.json"
print(f"Looking for: {kaggle_path}")

if kaggle_path.exists():
    print("✅ kaggle.json file found")
    
    try:
        with open(kaggle_path, 'r') as f:
            data = json.load(f)
        
        print("\n📄 FILE CONTENTS:")
        print("-" * 30)
        print(json.dumps(data, indent=2))
        print("-" * 30)
        
        # Check what type of credentials
        if "username" in data and "key" in data:
            print(f"\n👤 Username: {data['username']}")
            print(f"🔑 Key starts with: {data['key'][:8]}...")
            
            if data['username'] == "lemayiankirionki":
                print("✅ Username matches your Kaggle account!")
            else:
                print("⚠️  Username doesn't match 'lemayiankirionki'")
                
        elif "token" in data:
            print("\n🎫 Found API TOKEN (new format)")
            print(f"Token starts with: {data['token'][:10]}...")
            print("✅ This should work with kagglehub >= 0.4.1")
            
        else:
            print("❓ Unknown format in kaggle.json")
            
    except json.JSONDecodeError:
        print("❌ ERROR: kaggle.json is not valid JSON!")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        
else:
    print("❌ kaggle.json NOT FOUND!")
    print("\n📝 CREATE IT WITH THIS CONTENT:")
    print("-" * 40)
    print('''{
  "username": "lemayiankirionki",
  "key": "YOUR_32_CHARACTER_API_KEY_HERE"
}''')
    print("-" * 40)
    
    # Create the directory
    (Path.home() / ".kaggle").mkdir(exist_ok=True)
    
    # Ask user to create the file
    print(f"\n💡 Create file at: {kaggle_path}")

print("\n" + "="*60)
print("📊 YOUR KAGGLE INFO:")
print("="*60)
print("Username: lemayiankirionki")
print("Account #: 27466792")
print("Email: lemayianledavit2018@gmail.com")
print("Token: Lema_token (created 6 minutes ago)")
print("\n⚠️  IMPORTANT: Use API TOKENS, not Legacy API Key!")