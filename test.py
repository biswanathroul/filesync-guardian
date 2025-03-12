from filesync_guardian import SyncManager

# Create source and target test folders
import os
os.makedirs("test_source", exist_ok=True)
os.makedirs("test_target", exist_ok=True)

# Create a test file
with open("test_source/testfile.txt", "w") as f:
    f.write("This is a test file")

# Initialize sync manager
sync = SyncManager(
    source_path="test_source",
    target_path="test_target"
)

# Start synchronization
print("Starting sync...")
result = sync.start()
print(f"Sync completed: {result}")

# Check if file was copied
if os.path.exists("test_target/testfile.txt"):
    print("Test successful: File was synchronized")
else:
    print("Test failed: File was not synchronized")
