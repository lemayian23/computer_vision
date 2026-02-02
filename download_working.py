import kagglehub
import os
import json

print("="*60)
print("📥 WORKING DATASET DOWNLOADER")
print("="*60)

# Dataset that need testing:
DATASETS = {
    "Face_Mask_Detection": "shivamkushwaha/face-mask-detection",
    "CIFAR_10": "ycam004/cifar10",  # Alternative CIFAR-10
    "Cats_vs_Dogs": "shaunthesheep/microsoft-catsvsdogs-dataset",  # Good for beginners
    "Fruits": "moltean/fruits",  # Fruits dataset (good for classification)
}

# Save to current project folder
SAVE_FOLDER = "./datasets/"
os.makedirs(SAVE_FOLDER, exist_ok=True)

def check_kaggle_auth():
    """Check if Kaggle is authenticated"""
    kaggle_path = os.path.expanduser("~/.kaggle/kaggle.json")
    if os.path.exists(kaggle_path):
        print("✅ Kaggle authentication file found")
        try:
            with open(kaggle_path, 'r') as f:
                auth = json.load(f)
                print(f"   Username: {auth.get('username', 'Not found')}")
            return True
        except:
            pass
    print("❌ Kaggle authentication not found")
    print("\n🔧 SETUP INSTRUCTIONS:")
    print("1. Go to: https://www.kaggle.com/ → Account → API")
    print("2. Click 'Create New Token' (downloads kaggle.json)")
    print("3. Place it at: C:\\Users\\admin\\.kaggle\\kaggle.json")
    return False

#Funtion to download dataset
def download_simple_dataset(dataset_name, kaggle_path):
    """Download without pandas dependency"""
    print(f"\n📥 Downloading: {dataset_name}")
    print(f"   Kaggle path: {kaggle_path}")
    
    try:
        # Download to project folder
        download_path = kagglehub.dataset_download(
            kaggle_path,
            path=os.path.join(SAVE_FOLDER, dataset_name)
        )
        
        print(f"   ✅ Success! Saved to: {download_path}")
        
        # Show what was downloaded
        if os.path.exists(download_path):
            items = os.listdir(download_path)
            print(f"   📁 Contains {len(items)} items:")
            for item in items[:10]:  # Show first 10
                print(f"     • {item}")
            if len(items) > 10:
                print(f"     ... and {len(items) - 10} more")
        
        return download_path
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:100]}...")  # Show first 100 chars
        return None

def main():
    # Check authentication first
    if not check_kaggle_auth():
        return
    
    print(f"\n💾 Saving datasets to: {os.path.abspath(SAVE_FOLDER)}")
    
    downloaded = {}
    
    # Try the first dataset only (to test)
    first_name = list(DATASETS.keys())[0]
    first_path = DATASETS[first_name]
    
    path = download_simple_dataset(first_name, first_path)
    if path:
        downloaded[first_name] = path
    
    print("\n" + "="*60)
    if downloaded:
        print("✅ SUCCESS! Dataset downloaded.")
        print("\n📊 NEXT STEPS:")
        print("1. Explore the downloaded folder:")
        print(f"   {list(downloaded.values())[0]}")
        print("\n2. Try other datasets by editing the DATASETS dictionary")
        print("\n3. Start your computer vision project!")
    else:
        print("❌ Download failed")
        print("\n🔧 TROUBLESHOOTING:")
        print("1. Make sure kaggle.json is in C:\\Users\\admin\\.kaggle\\")
        print("2. Check your internet connection")
        print("3. Visit the dataset page to ensure it exists:")
        print(f"   https://www.kaggle.com/datasets/{first_path}")

if __name__ == "__main__":
    main()