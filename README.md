# 🗃️ Duplicate File Finder & Remover - Lightning Fast!

A powerful and efficient Python script to quickly detect and remove duplicate files in your directories using MD5 hashing.

## 🚀 Features

- Scans multiple directories simultaneously.
- Uses MD5 hashing for accurate duplicate detection.
- Multithreaded processing for blazing-fast performance.
- Clearly identifies duplicate files and their originals.
- Provides an interactive option to safely delete duplicates.

## 🛠️ Requirements

- Python 3.x

## ⚡ Quick Start

1. Adjust the directory paths directly in the script:

   ```python
   paths_to_check = [
       "/your/path/here",
       "/another/path/here"
   ]
   ```

2. Run the script:

   ```bash
   python your_script_name.py
   ```

3. Follow on-screen prompts to handle duplicates.

## 📂 How it Works

- **Scanning**: The script scans specified directories and calculates the MD5 hash of each file.
- **Detection**: Identifies duplicates by comparing hashes.
- **Cleanup**: Offers the option to delete duplicates while keeping original files safe.

## 📚 Python Libraries Used

- [hashlib](https://docs.python.org/3/library/hashlib.html) (Python built-in hashing library)
- [os](https://docs.python.org/3/library/os.html) (Python built-in library for file system interaction)
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) (Python built-in library for parallel execution)

## ⚠️ Important Notes

- Backup your data before running the script, as deleted files cannot be recovered.
- Ensure paths are correctly set to avoid unintended file deletions.

## 👤 Author

- **Vissiouz**

