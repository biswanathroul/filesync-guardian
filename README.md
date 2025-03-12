# FileSync-Guardian

[![PyPI version](https://img.shields.io/pypi/v/filesync-guardian.svg)](https://pypi.org/project/filesync-guardian/)
[![Python Versions](https://img.shields.io/pypi/pyversions/filesync-guardian.svg)](https://pypi.org/project/filesync-guardian/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust file synchronization and backup library for Python with versioning, encryption, and smart delta transfers.

## Overview

FileSync-Guardian provides a powerful yet easy-to-use solution for file synchronization and backup in Python applications. Unlike simple file copying functions, FileSync-Guardian offers intelligent synchronization, versioning history, encryption, and detailed progress reporting.

## Key Features

- 🔄 **Smart Synchronization**: Only transfers files that have changed, saving time and bandwidth
- 📚 **Version History**: Automatically keeps previous versions of modified files for easy recovery
- 🔒 **Built-in Encryption**: Securely encrypt sensitive files during transfer and storage
- 🔍 **Integrity Verification**: Ensures files are transferred correctly with checksum validation
- 🧰 **Flexible Filtering**: Include or exclude files using powerful pattern matching
- 📊 **Progress Tracking**: Real-time progress reporting with ETA estimation
- 🔀 **Bidirectional Sync**: Support for two-way synchronization between directories
- 📝 **Comprehensive Logging**: Detailed logs of all operations for troubleshooting

## Installation

```bash
pip install filesync-guardian
```

## Quick Start

### Basic Synchronization

```python
from filesync_guardian import SyncManager

# Create a sync manager
sync = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/backup"
)

# Start synchronization
sync.start()
```

### With Progress Reporting

```python
from filesync_guardian import SyncManager

# Create a sync manager
sync = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/backup"
)

# Define progress callback
def on_progress(progress):
    print(f"Progress: {progress:.1f}%")

# Start synchronization with progress reporting
sync.start(on_progress=on_progress)
```

### With Encryption

```python
from filesync_guardian import SyncManager

# Create a sync manager with encryption
sync = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/backup",
    encryption=True,
    encryption_key="your-secure-password"  # Optional - auto-generated if not provided
)

# Start synchronization
sync.start()
```

### With File Versioning

```python
from filesync_guardian import SyncManager

# Create a sync manager with versioning
sync = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/backup",
    versioning=True,
    max_versions=5  # Keep up to 5 versions of each file
)

# Start synchronization
sync.start()

# Later, restore a previous version of a file
sync.restore_version("/path/to/backup/important_file.txt")
```

### With File Filtering

```python
from filesync_guardian import SyncManager

# Create a sync manager with filters
sync = SyncManager(
    source_path="/path/to/source",
    target_path="/path/to/backup",
    filters=[
        "*.txt",           # Include all text files
        "*.docx",          # Include all Word documents
        "-:*.tmp",         # Exclude temporary files
        "-:*.log",         # Exclude log files
        "+:logs/errors.log"  # But include this specific log file
    ]
)

# Start synchronization
sync.start()
```

## Real-World Use Cases

### Application Data Backup

```python
from filesync_guardian import SyncManager
import os

# Get user's home directory and app data
home_dir = os.path.expanduser("~")
app_data = os.path.join(home_dir, "AppData", "MyApplication")
backup_dir = os.path.join(home_dir, "Backups", "MyApplication")

# Create sync manager with versioning for data protection
sync = SyncManager(
    source_path=app_data,
    target_path=backup_dir,
    versioning=True,
    filters=["*", "-:cache/*", "-:tmp/*"]  # Exclude cache and tmp directories
)

# Backup application data
sync.start()
```

### Secure Document Synchronization

```python
from filesync_guardian import SyncManager

# Create sync manager for sensitive documents with encryption
sync = SyncManager(
    source_path="/path/to/sensitive_documents",
    target_path="/path/to/encrypted_backup",
    encryption=True,
    encryption_key="strong-password-here",
    filters=["*.pdf", "*.docx", "*.xlsx"]  # Only sync documents
)

# Start secure synchronization
sync.start()
```

### Development Environment Sync

```python
from filesync_guardian import SyncManager

# Sync project files between environments
sync = SyncManager(
    source_path="/path/to/project",
    target_path="/path/to/backup_project",
    bidirectional=True,  # Changes from both sides are synchronized
    filters=["*", "-:node_modules/*", "-:venv/*", "-:*.pyc", "-:.git/*"]  # Exclude development artifacts
)

# Start synchronization
sync.start()
```

## Advanced Usage

### File System Monitoring

```python
from filesync_guardian.file_system.watcher import FileWatcher

# Create a file watcher to monitor changes
watcher = FileWatcher("/path/to/watch", recursive=True)

# Set up event handlers
def on_created(path):
    print(f"File created: {path}")

def on_modified(path):
    print(f"File modified: {path}")

def on_deleted(path):
    print(f"File deleted: {path}")

# Register callbacks
watcher.set_callbacks(
    on_created=on_created,
    on_modified=on_modified,
    on_deleted=on_deleted
)

# Start watching
watcher.start()

# ... do something else ...

# When done
watcher.stop()
```

### Manual Pattern Filtering

```python
from filesync_guardian.filters.pattern import Pattern, PatternSet

# Create individual patterns
include_txt = Pattern("*.txt")
exclude_temp = Pattern("-:*.tmp")

# Check if a file matches a pattern
print(include_txt.matches("document.txt"))  # True
print(exclude_temp.matches("data.tmp"))     # True
print(exclude_temp.is_include())            # False

# Create a pattern set
pattern_set = PatternSet([
    "*.txt",
    "*.docx",
    "-:*.tmp"
])

# Filter a list of files
files = ["doc1.txt", "doc2.docx", "data.tmp", "image.jpg"]
filtered = pattern_set.filter_paths(files)
print(filtered)  # ['doc1.txt', 'doc2.docx']
```

## API Reference

### SyncManager

Main class for coordinating file synchronization operations.

```python
SyncManager(
    source_path,              # Source directory path
    target_path,              # Target directory path
    encryption=False,         # Whether to enable encryption
    encryption_key=None,      # Custom encryption key (generated if None)
    versioning=False,         # Whether to keep previous versions
    max_versions=5,           # Maximum number of versions to keep per file
    filters=None,             # List of include/exclude patterns
    bidirectional=False,      # Whether synchronization should be two-way
    verify_integrity=True,    # Whether to verify file integrity
    log_level=logging.INFO    # Logging level
)
```

**Methods:**

- `start(on_progress=None, on_complete=None, on_error=None)`: Start synchronization
- `stop()`: Stop the current synchronization
- `get_status()`: Get the current status of synchronization
- `restore_version(file_path, version_id=None)`: Restore a previous version of a file

### FileWatcher

Monitors a directory for file changes.

```python
FileWatcher(
    path,                   # Directory path to watch
    recursive=True,         # Whether to watch subdirectories
    polling_interval=1.0    # Seconds between polling checks
)
```

**Methods:**

- `start()`: Start watching for file changes
- `stop()`: Stop watching
- `set_callbacks(on_created=None, on_modified=None, on_deleted=None)`: Set event handlers

### Pattern and PatternSet

File pattern matching for filtering.

```python
# Individual pattern
pattern = Pattern("*.txt")      # Include pattern
pattern = Pattern("-:*.tmp")    # Exclude pattern

# Pattern set
patterns = PatternSet([
    "*.txt",
    "-:*.tmp"
])
```

**Pattern Syntax:**

- Simple glob patterns: `*.txt`, `data.*`, `document-?.doc`
- Prefixed patterns:
  - `+:pattern` or just `pattern`: Include files matching the pattern
  - `-:pattern`: Exclude files matching the pattern

## Requirements

- Python 3.7+
- cryptography >= 36.0.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
