# 📁 PySorter — Python File Sorter (CLI)

A simple and effective command-line tool that organizes files by extension.

---

## 📌 Versions

| Version | Release Date | Python Version | Notes                        |
| ------- | ------------ | -------------- | ---------------------------- |
| v1.0    | 2023-06-13   | 3.11.4         | Initial release              |
| v2.0    | 2023-07-03   | 3.11.4         | Minor improvements           |
| v3.0    | 2024-12-01   | 3.12.1         | Improved logic and structure |
| v4.0    | 2025-05-26   | 3.12.6         | **Current version**          |

---

## 🔍 What is PySorter?

**PySorter** is a lightweight Python CLI utility that scans a directory and automatically organizes your files into folders based on their extensions.

### Example

**Before:**

```
../dir/
├── file1.txt
├── file2.txt
├── file3.png
├── file4.png
├── file5.mp4
├── file6.mp4
```

**After running PySorter:**

```
../dir/
└── PySort/
    ├── txt/
    │   ├── file1.txt
    │   └── file2.txt
    ├── png/
    │   ├── file3.png
    │   └── file4.png
    └── mp4/
        ├── file5.mp4
        └── file6.mp4
```

---

## ⚙️ How It Works

1. Scans your chosen directory for all files (non-recursive by default).
2. Creates folders inside `PySort/`, each named after a file extension (e.g., `txt/`, `pdf/`, `png/`).
3. Moves files into their corresponding extension folders.
4. Automatically renames files if name conflicts occur to avoid overwriting.