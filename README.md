
# 🧼 PHP Minifier & Obfuscator Tool

Secure and streamline your WordPress plugin code before deployment.

---

## 🔒 Disclaimer

This script is intended for internal use by **121 Digital** only.

**Author:** James Gibbons  
**Email:** jgibbons@121digital.co.uk  
**Company:** 121 Digital

> Do **not** use this tool to hide malicious or unethical code.  
> It is strictly for securing proprietary WordPress plugins deployed to client sites.

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

**Required Python packages:**

```
tqdm
```

---

## ⚙️ Features

- ✅ Minifies PHP by removing comments and whitespace
- 🕵️‍♂️ Obfuscates variable and function names (optional)
- 📂 Recursively processes entire directories
- 🖥️ Terminal-based UI with real-time progress bar

---

## 🚀 Usage Instructions

Run the tool using:

```bash
python php_minify.py [path] [options]
```

### ✅ Arguments

| Argument        | Description                                                        |
|----------------|--------------------------------------------------------------------|
| `path`          | Path to a PHP file or directory containing PHP files               |

### ✅ Options

| Option          | Description                                                        |
|----------------|--------------------------------------------------------------------|
| `--obfuscate`   | Obfuscate function and variable names                              |
| `--output`      | Output path (directory or file). If not provided, it overwrites original files |

---

## 🧪 Example Commands

### Minify a Single PHP File

```bash
python php_minify.py ./my-plugin/index.php
```

### Minify & Obfuscate a Single File

```bash
python php_minify.py ./my-plugin/index.php --obfuscate
```

### Minify All PHP Files in a Directory

```bash
python php_minify.py ./my-plugin/
```

### Minify & Obfuscate Entire Directory with Output Folder

```bash
python php_minify.py ./my-plugin/ --obfuscate --output ./dist/
```

> The output structure in `./dist/` will mirror the source directory.

---

## 📁 Output Behavior

- If `--output` is not specified, the tool **overwrites original files**.
- When `--output` is used, the minified files are saved in the specified directory.
- File hierarchy is preserved when processing folders.

---

## 📌 Best Practices

- Run this tool just before packaging or deploying your plugin.
- Keep a clean source copy under version control (e.g. Git).
- Optionally integrate into CI/CD pipelines or custom build scripts.

---

## 👋 Support

For issues or feedback, contact:

**James Gibbons**  
📧 jgibbons@121digital.co.uk  
🌐 https://121digital.co.uk

---
