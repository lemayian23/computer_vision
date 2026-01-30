import json
import os
import kagglehub

print("="*60)
print("🎯 USING YOUR NEW KAGGLE TOKEN")
print("="*60)

# 1. Update kaggle.json
kaggle_path = os.path.expanduser("~/.kaggle/kaggle.json")

config = {
    "username": "lemayiankirionki",
    "token": "KGAT_3f7a967186e5336c6b11567578272de6"
}

with open(kaggle_path, 'w') as f:
    json.dump(config, f, indent=2)

print(f"✅ Updated {kaggle_path}")
print(f"\n📄 File content:")
print(json.dumps(config, indent=2))

# 2. Test the token
print("\n🧪 Testing token...")
try:
    # Small test dataset
    path = kagglehub.dataset_download("zynicide/wine-reviews")
    print(f"✅ Test successful! Downloaded to: {path}")
    
    # Now try your actual dataset
    print("\n📥 Downloading Face Mask Dataset...")
    face_path = kagglehub.dataset_download(
        "shivamkushwaha/face-mask-detection",
        path="./datasets/face-mask-detection"
    )
    print(f"✅ SUCCESS! Face dataset at: {face_path}")
    
    # List contents
    if os.path.exists(face_path):
        files = os.listdir(face_path)
        print(f"\n📁 Contains {len(files)} items:")
        for file in files[:10]:
            print(f"  • {file}")
        if len(files) > 10:
            print(f"  ... and {len(files) - 10} more")
    
    print("\n" + "="*60)
    print("🎉 CONGRATULATIONS!")
    print("="*60)
    print("Your Kaggle authentication is now working!")
    print(f"\nDatasets saved to: {os.path.abspath('./datasets/')}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Alternative: Set environment variable instead")
    print("Run in terminal:")
    print('set KAGGLE_API_TOKEN=KGAT_3f7a967186e5336c6b11567578272de6')