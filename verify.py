import kagglehub
import os
import json

print("Verifying Kaggle setup...")

# Check kaggle.json
kaggle_path = os.path.expanduser("~/.kaggle/kaggle.json")
with open(kaggle_path, 'r') as f:
    data = json.load(f)

print(f"\n1. kaggle.json check:")
print(f"   • Username: {data.get('username')}")
print(f"   • Token: {data.get('token', 'Not found')[:15]}...")

# Try download
print("\n2. Testing download...")
try:
    # Download to current directory
    path = kagglehub.dataset_download(
        "shivamkushwaha/face-mask-detection",
        path="./my_datasets/"
    )
    
    print(f"   ✅ Download successful!")
    print(f"   📍 Location: {os.path.abspath(path)}")
    
    # Show what we got
    if os.path.exists(path):
        total_size = 0
        total_files = 0
        
        for root, dirs, files in os.walk(path):
            total_files += len(files)
            for file in files:
                filepath = os.path.join(root, file)
                total_size += os.path.getsize(filepath) if os.path.exists(filepath) else 0
        
        print(f"   📊 Stats: {total_files} files, {total_size/(1024*1024):.1f} MB")
        
        # List top-level items
        items = os.listdir(path)
        print(f"   📁 Top-level items: {len(items)}")
        for item in items[:5]:
            print(f"     • {item}")
    
except Exception as e:
    print(f"   ❌ Failed: {e}")
    print("\n💡 Try setting environment variable:")
    print('   set KAGGLE_API_TOKEN=KGAT_3f7a967186e5336c6b11567578272de6')