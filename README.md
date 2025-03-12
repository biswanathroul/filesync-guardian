# FileSync-Guardian

A robust file synchronization and backup library for Python with versioning, encryption, and smart delta transfers.

## Features

- 🔄 **Smart Synchronization**: Intelligently sync files between directories with efficient delta transfers
- 📚 **Versioning System**: Keep historical versions of files with easy rollback
- 🔒 **Encryption Layer**: Integrated file encryption for sensitive data
- ⏱️ **Progress Reporting**: Real-time progress tracking with ETA and speed estimates
- 🔍 **Integrity Verification**: Checksum validation ensures files transfer correctly
- 🧰 **Flexible Filters**: Include/exclude patterns for precise control
- 📊 **Detailed Logging**: Comprehensive logging of all operations

## Installation

```bash
pip install filesync-guardian
```

## Quick Start

### Basic Synchronization

```python
from filesync_guardian import SyncManager

# Initialize a SyncManager with source and target directories
sync_manager = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/target"
)

# Start synchronization
sync_manager.start()
```

### With Progress Reporting

```python
from filesync_guardian import SyncManager

# Initialize the SyncManager
sync_manager = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/target"
)

# Define progress callback
def on_progress(progress):
    print(f"Sync progress: {progress:.1f}%")

# Define completion callback
def on_complete():
    print("Synchronization completed successfully!")

# Define error callback
def on_error(exception):
    print(f"Synchronization failed: {exception}")

# Start synchronization with callbacks
sync_manager.start(
    on_progress=on_progress,
    on_complete=on_complete,
    on_error=on_error
)
```

### With Encryption

```python
from filesync_guardian import SyncManager

# Initialize with encryption enabled
sync_manager = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/target",
    encryption=True,
    encryption_key="my-secure-password"  # Optional, auto-generated if not provided
)

# Start synchronization
sync_manager.start()
```

### With File Versioning

```python
from filesync_guardian import SyncManager

# Initialize with versioning enabled
sync_manager = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/target",
    versioning=True,
    max_versions=10  # Keep up to 10 versions of each file
)

# Start synchronization
sync_manager.start()

# Restore a previous version
sync_manager.restore_version("/path/to/file.txt")
```

### With Filters

```python
from filesync_guardian import SyncManager

# Initialize with file filters
sync_manager = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/target",
    filters=[
        "*.txt",           # Include all text files
        "-:*.tmp",         # Exclude temporary files
        "+:important/*.log" # Include log files in the important directory
    ]
)

# Start synchronization
sync_manager.start()
```

## Advanced Usage

### Bidirectional Synchronization

```python
from filesync_guardian import SyncManager

# Initialize with bidirectional sync
sync_manager = SyncManager(
    source_path="/path/to/device1",
    target_path="/path/to/device2",
    bidirectional=True  # Changes from both sides are synchronized
)

# Start synchronization
sync_manager.start()
```

### File Monitoring

```python
from filesync_guardian.file_system.watcher import FileWatcher

# Create a file watcher
watcher = FileWatcher("/path/to/watch", recursive=True)

# Define event handlers
def on_file_created(path):
    print(f"File created: {path}")

def on_file_modified(path):
    print(f"File modified: {path}")

def on_file_deleted(path):
    print(f"File deleted: {path}")

# Set up callbacks
watcher.set_callbacks(
    on_created=on_file_created,
    on_modified=on_file_modified,
    on_deleted=on_file_deleted
)

# Start watching
watcher.start()

# ... Later when done ...
watcher.stop()
```

### Checking Sync Status

```python
from filesync_guardian import SyncManager

# Initialize the SyncManager
sync_manager = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/target"
)

# Start sync in the background
sync_manager.start()

# Check status
status = sync_manager.get_status()
print(f"Running: {status['is_running']}")
print(f"Progress: {status['progress']}%")
print(f"Current stage: {status['stage']}")
print(f"Last error: {status['last_error']}")
```

## API Reference

### SyncManager

The main class for managing file synchronization operations.

```python
SyncManager(
    source_path,              # Source directory path
    target_path,              # Target directory path
    encryption=False,         # Whether to enable encryption
    encryption_key=None,      # Custom encryption key
    versioning=False,         # Whether to keep previous versions
    max_versions=5,           # Maximum versions to keep per file
    filters=None,             # List of include/exclude patterns
    bidirectional=False,      # Whether sync should be two-way
    verify_integrity=True,    # Whether to verify file integrity
    log_level=logging.INFO    # Logging level
)
```

**Methods:**
- `start(on_progress=None, on_complete=None, on_error=None)`: Start synchronization
- `stop()`: Stop the current synchronization
- `get_status()`: Get the current status
- `restore_version(file_path, version_id=None)`: Restore a previous version

### FileWatcher

Monitors a directory for file changes.

```python
FileWatcher(
    path,                   # Directory path to watch
    recursive=True,         # Whether to watch subdirectories
    polling_interval=1.0    # Seconds between checks
)
```

**Methods:**
- `start()`: Start watching for changes
- `stop()`: Stop watching
- `set_callbacks(on_created=None, on_modified=None, on_deleted=None)`: Set event handlers

### Pattern

File pattern matcher for include/exclude rules.

```python
Pattern(pattern_string)  # Pattern string with optional +/- prefix
```

**Pattern Syntax:**
- `*.txt`: Include all .txt files
- `-:*.tmp`: Exclude all .tmp files
- `+:dir/*.log`: Include all .log files in dir/

## Requirements

- Python 3.7 or higher
- cryptography >= 36.0.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Credits
Developed by Biswanath Roul
