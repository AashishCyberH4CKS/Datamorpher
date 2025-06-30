# 🧠 DataMorpher

**DataMorpher** is a powerful Python CLI tool  that converts data between multiple formats. It supports extremely large files (up to **1024 GB**) and includes real-time terminal feedback with colorful animations.

---

## 🚀 Features

✅ Convert between the following formats:
- TXT ➜ JSON  
- XLSX ➜ JSON  
- JSON ➜ XLSX  
- JSON ➜ TXT  
- CSV ➜ JSON  
- JSON ➜ CSV  

✅ Advanced JSON utilities:
- Beautify JSON (pretty format)
- Minify JSON (compact format)

✅ Highlights:
- Handles files up to **1024 GB**
- User-friendly prompts and output
- Fully offline and privacy-focused

---

## 📦 Requirements

Make sure you have the following Python packages:

```bash
pip install pandas openpyxl

🔧 How to Use

Run the tool using:

python datamorpher.py

Then select the conversion type:

1. TXT to JSON
2. XLSX to JSON
3. JSON to XLSX
4. JSON to TXT
5. CSV to JSON
6. JSON to CSV
7. Beautify JSON
8. Minify JSON

Enter the full path of the file when prompted.
📁 Output Files

Converted files are saved in the same directory with _converted appended to their filenames:

Example:

    data.json ➜ data_converted.xlsx

    sample.txt ➜ sample_converted.json