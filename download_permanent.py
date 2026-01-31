import kagglehub
from kagglehub import KaggleDatasetAdapter
import os
import pandas as pd

# Configuration
DATASETS_TO_DOWNLOAD = {
    "Face Detection": "shivamkushwaha/face-mask-detection",
    "Car Detection": "sshikamaru/car-object-detection",
    "Animals": "alessiocorrado99/animals10"
}

SAVE_FOLDER = "D:/CV_Datasets/"  # ← Change to your preferred location

def download_dataset_permanently(dataset_name, kaggle_path):
    """Download dataset permanently to local folder"""
    print(f"\n📥 Downloading: {dataset_name}")
    
    # Create save path
    save_path = os.path.join(SAVE_FOLDER, dataset_name.replace(" ", "_"))
    os.makedirs(save_path, exist_ok=True)
    
    try:
        # Download the dataset
        download_path = kagglehub.dataset_download(kaggle_path, path=save_path)
        
        print(f"   ✅ Saved to: {download_path}")
        
        # Try to find and load annotation file
        annotation_file = find_annotation_file(download_path)
        if annotation_file:
            # Save annotation CSV locally too
            df = pd.read_csv(os.path.join(download_path, annotation_file))
            local_csv = os.path.join(save_path, "annotations.csv")
            df.to_csv(local_csv, index=False)
            print(f"   📊 Annotations saved: {local_csv}")
        
        return download_path
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

def find_annotation_file(folder_path):
    """Find annotation file in downloaded folder"""
    for file in os.listdir(folder_path):
        if file.endswith(('.csv', '.json', '.txt')):
            if any(keyword in file.lower() for keyword in ['annot', 'label', 'train', 'val', 'test']):
                return file
    return None

def main():
    print("="*60)
    print("💾 PERMANENT DATASET DOWNLOADER")
    print("="*60)
    print(f"Saving all datasets to: {SAVE_FOLDER}")
    
    downloaded_paths = {}
    
    for name, kaggle_path in DATASETS_TO_DOWNLOAD.items():
        path = download_dataset_permanently(name, kaggle_path)
        if path:
            downloaded_paths[name] = path
    
    print("\n" + "="*60)
    print("✅ DOWNLOAD COMPLETE!")
    print("="*60)
    
    print("\nYour datasets are now permanently stored at:")
    for name, path in downloaded_paths.items():
        print(f"\n📁 {name}:")
        print(f"   Path: {path}")
        
        # Count files
        total_files = 0
        for root, dirs, files in os.walk(path):
            total_files += len(files)
        print(f"   Total files: {total_files}")
        
        # List subfolders
        items = os.listdir(path)
        print(f"   Contents: {items}")
    
    print("\n🔧 HOW TO USE LATER:")
    print("""
    # In your future projects, just load from the saved location:
    
    import cv2
    import pandas as pd
    import os
    
    # Load annotations
    df = pd.read_csv("D:/CV_Datasets/Face_Detection/annotations.csv")
    
    # Load images
    image_folder = "D:/CV_Datasets/Face_Detection/images/"
    for img_file in os.listdir(image_folder):
        img_path = os.path.join(image_folder, img_file)
        image = cv2.imread(img_path)
        # Process image...
    """)
    #if stmt

if __name__ == "__main__":
    main()