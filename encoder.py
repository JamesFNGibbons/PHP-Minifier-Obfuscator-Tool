"""
PHP Minify & Obfuscator Tool
----------------------------

DISCLAIMER:
This script is intended to help secure proprietary WordPress plugins
deployed to client websites. It removes comments, reduces whitespace,
and optionally obfuscates variables and function names to discourage reverse-engineering.

Author: James Gibbons
Email: jgibbons@121digital.co.uk
Company: 121 Digital

Use responsibly. Do not use this tool to conceal malicious or unethical code.
"""

import re
import sys
import os
import random
import string
from tqdm import tqdm


# --------------------------------------------
# Generate a random obfuscated name
# --------------------------------------------
def generate_obfuscated_name(existing_names):
  while True:
    name = ''.join(random.choices(string.ascii_letters, k=8))
    if name not in existing_names:
      return name


# --------------------------------------------
# Minify PHP code by removing comments and whitespace
# --------------------------------------------
def minify_php_code(code):
  # Remove single-line comments
  code = re.sub(r'//.*?$|#.*?$', '', code, flags=re.MULTILINE)
  # Remove multi-line comments
  code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
  # Collapse extra whitespace
  code = re.sub(r'\s+', ' ', code)
  # Remove unnecessary spaces around symbols
  code = re.sub(r'\s*([{}();,=+\-*/<>])\s*', r'\1', code)
  return code.strip()


# --------------------------------------------
# Obfuscate variable and function names
# --------------------------------------------
def obfuscate_identifiers(code):
  # Find PHP variables and function names
  identifiers = set(re.findall(r'\$[a-zA-Z_][a-zA-Z0-9_]*|function\s+([a-zA-Z_][a-zA-Z0-9_]*)', code))
  obfuscated = {}
  for ident in identifiers:
    clean = ident.replace('function ', '') if 'function ' in ident else ident
    obfuscated[clean] = generate_obfuscated_name(obfuscated.values())

  # Replace all identifiers in code
  for original, new in obfuscated.items():
    if original.startswith('$'):
      code = re.sub(r'\b' + re.escape(original) + r'\b', f'${new}', code)
    else:
      code = re.sub(r'\b' + re.escape(original) + r'\b', new, code)

  return code


# --------------------------------------------
# Process a single PHP file
# --------------------------------------------
def process_php_file(filepath, obfuscate=False):
  with open(filepath, 'r', encoding='utf-8') as f:
    code = f.read()

  code = minify_php_code(code)

  if obfuscate:
    code = obfuscate_identifiers(code)

  return code


# --------------------------------------------
# Recursively process all PHP files in a directory
# --------------------------------------------
def process_directory(directory, obfuscate=False, output_dir=None):
  # Find all PHP files
  php_files = [os.path.join(root, file)
               for root, _, files in os.walk(directory)
               for file in files if file.endswith('.php')]

  if not php_files:
    print("No PHP files found.")
    return

  if output_dir:
    os.makedirs(output_dir, exist_ok=True)

  print(f"🛠️  Processing {len(php_files)} PHP file(s)...\n")

  # Show progress bar while processing each file
  for file in tqdm(php_files, desc="Securing Files", unit="file"):
    minified_code = process_php_file(file, obfuscate=obfuscate)
    output_path = os.path.join(output_dir, os.path.relpath(file, directory)) if output_dir else file

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as out_file:
      out_file.write(minified_code)

  print("\n✅ Done. All files secured.")


# --------------------------------------------
# Entry point: argument parsing and main logic
# --------------------------------------------
if __name__ == '__main__':
  import argparse

  # Set up command-line arguments
  parser = argparse.ArgumentParser(description="Minify and optionally obfuscate PHP code.")
  parser.add_argument('path', help="PHP file or directory to process")
  parser.add_argument('--obfuscate', action='store_true', help="Obfuscate variable and function names")
  parser.add_argument('--output', help="Optional output directory (default: overwrite source)")

  args = parser.parse_args()

  # Validate input path
  if not os.path.exists(args.path):
    print(f"❌ File or directory not found: {args.path}")
    sys.exit(1)

  # Handle file vs directory
  if os.path.isfile(args.path):
    code = process_php_file(args.path, obfuscate=args.obfuscate)
    if args.output:
      os.makedirs(os.path.dirname(args.output), exist_ok=True)
      with open(args.output, 'w', encoding='utf-8') as f:
        f.write(code)
      print(f"✅ Output written to {args.output}")
    else:
      print(code)
  else:
    process_directory(args.path, obfuscate=args.obfuscate, output_dir=args.output)
