import os
os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac5")
timestamp_samples = ["IMG_20260525_104530.jpg", "IMG_20260525_104612.jpg", "IMG_20260525_142205.jpg","IMG_20260524_191555.jpg", "IMG_20260524_235959.jpg", "VID_20260523_081240.mp4","IMG_20260522_120000.jpeg", "SCREENSHOT_20260520_173045.png", "IMG_20260515_064511.jpg", "IMG_20260501_090023.jpg"]

for i in timestamp_samples:
    with open(i.strip(), 'w') as f:
        pass

all_files = os.listdir()

def get_timestamp_numbers(filename):
    # This function extracts just the digits from the filename
    # e.g., "VID_20260523_081240.mp4" becomes "20260523081240"
    digits_only = "".join([char for char in filename if char.isdigit()])
    return digits_only

# Sort using our custom function as the key based on the file creation date as per name(not as per in system)
all_files.sort(key=get_timestamp_numbers)

i = 1
for f in all_files:
    filename, fileext = os.path.splitext(f)
    os.rename(f, f"Vacation_{i}{fileext}")
    i += 1