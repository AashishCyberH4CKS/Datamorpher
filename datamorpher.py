import json
import pandas as pd
import os
import time
import warnings
import sys
import itertools

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

warnings.simplefilter(action='ignore', category=FutureWarning)

BANNER = CYAN + r"""
$$$$$$$\             $$\                       $$\      $$\                               $$\                           
$$  __$$\            $$ |                      $$$\    $$$ |                              $$ |                          
$$ |  $$ | $$$$$$\\ $$$$\\    $$$$$$\          $$$$\  $$$$ | $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |  $$ | \____$$\\_$$  _|   \____$$\ $$$$$$\ $$\\$$\\ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |  $$ | $$$$$$$ | $$ |     $$$$$$$ |\______|$$ \$$$  $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$  __$$ | $$ |$$\ $$  __$$ |        $$ |\$  /$$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$   ____|$$ |      
$$$$$$$  |\$$$$$$$ | \$$$$  |\$$$$$$$ |        $$ | \_/ $$ |\$$$$$$  |$$ |      $$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      
\_______/  \_______|  \____/  \_______|        \__|     \__| \______/ \__|      $$  ____/ \__|  \__| \_______|\__|      
                                                                                $$ |                                    
                                                                                $$ |                                    
                                                                                \__|         
                                                                                         
""" + RESET

def typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_animation(task):
    print(f"\n[+] {task} in progress", end="", flush=True)
    for _ in range(3):
        for dot in [".", "..", "..."]:
            sys.stdout.write(f"\r[+] {task} in progress{dot} ")
            sys.stdout.flush()
            time.sleep(0.3)
    print(" Done!\n")

def progress_bar(current, total):
    percent = int((current / total) * 100)
    bar = "█" * (percent // 5) + "▒" * (20 - percent // 5)
    sys.stdout.write(f"\r📊 Progress: {bar} {percent}%")
    sys.stdout.flush()

def txt_to_json(path):
    output_path = path.replace('.txt', '_converted.json')
    with open(path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write('[\n')
        first = True
        for i, line in enumerate(infile):
            if not first:
                outfile.write(',\n')
            json.dump({str(i): line.strip()}, outfile)
            first = False
        outfile.write('\n]')
    loading_animation("TXT to JSON")
    print(f"🎉 Converted file saved at: {output_path}")

def json_to_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    output_path = path.replace('.json', '_converted.txt')
    with open(output_path, 'w', encoding='utf-8') as txt_file:
        for key, value in data.items():
            txt_file.write(f"{value}\n")
    loading_animation("JSON to TXT")
    print(f"🎉 Converted file saved at: {output_path}")

def xls_xlsx_to_json(path):
    try:
        try:
            df = pd.read_excel(path, engine='openpyxl')
        except Exception:
            df = pd.read_excel(path, engine='xlrd')

        output_path = path.replace('.xlsx', '_converted.json').replace('.xls', '_converted.json')
        df.to_json(output_path, orient='records', indent=4, date_format='iso')
        loading_animation("Excel to JSON")
        print(f"🎉 Converted file saved at: {output_path}")
    except Exception as e:
        print(f"[!] Failed to convert {os.path.basename(path)}: {e}")

def json_to_xlsx(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    output_path = path.replace('.json', '_converted.xlsx')
    df.to_excel(output_path, index=False)
    loading_animation("JSON to XLSX")
    print(f"🎉 Converted file saved at: {output_path}")

def csv_to_json(path):
    output_path = path.replace('.csv', '_converted.json')
    chunk_size = 100000
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write('[\n')
        first = True
        for chunk in pd.read_csv(path, chunksize=chunk_size):
            json_str = chunk.to_json(orient='records')
            json_obj = json.loads(json_str)
            for record in json_obj:
                if not first:
                    outfile.write(',\n')
                json.dump(record, outfile)
                first = False
        outfile.write('\n]')
    loading_animation("Chunked CSV to JSON")
    print(f"🎉 Converted file saved at: {output_path}")

def json_to_csv(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    output_path = path.replace('.json', '_converted.csv')
    df.to_csv(output_path, index=False)
    loading_animation("JSON to CSV")
    print(f"🎉 Converted file saved at: {output_path}")

def beautify_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    output_path = path.replace('.json', '_pretty.json')
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)
    loading_animation("Beautifying JSON")
    print(f"🎉 Beautified JSON saved at: {output_path}")

def minify_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    output_path = path.replace('.json', '_minified.json')
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, separators=(',', ':'))
    loading_animation("Minifying JSON")
    print(f"🎉 Minified JSON saved at: {output_path}")

def batch_folder_convert(folder_path):
    folder_path = folder_path.strip('"')
    print("Enter file type to convert (txt/csv/xlsx/xls):", end=" ")
    file_type = input().lower().strip()

    extensions = {
        'txt': '.txt',
        'csv': '.csv',
        'xlsx': '.xlsx',
        'xls': '.xls'
    }

    if file_type not in extensions:
        print("\n[!] Unsupported file type for batch conversion.")
        return

    ext = extensions[file_type]
    files = [f for f in os.listdir(folder_path) if f.endswith(ext)]

    print(f"\n[+] Converting all {ext} files in: {folder_path}")

    for file in files:
        full_path = os.path.join(folder_path, file)
        try:
            if file_type == 'txt':
                txt_to_json(full_path)
            elif file_type == 'csv':
                csv_to_json(full_path)
            elif file_type in ['xlsx', 'xls']:
                xls_xlsx_to_json(full_path)
        except Exception as e:
            print(f"[!] Failed to convert {file}: {e}")

def run_tool():
    print(BANNER)
    typewriter("Version 1.0 | Created by Aashish_Cyber_H4CKS\n")
    while True:
        print("\nChoose the type of conversion:")
        print("1. TXT to JSON")
        print("2. XLSX to JSON")
        print("3. JSON to XLSX")
        print("4. JSON to TXT")
        print("5. CSV to JSON")
        print("6. JSON to CSV")
        print("7. Beautify JSON")
        print("8. Minify JSON")
        print("9. Batch Folder Convert (TXT/XLSX/CSV/XLS ➜ JSON)")

        try:
            choice = int(input("\nEnter your choice (1–9): "))

            if choice == 9:
                folder_path = input("Enter folder path: ").strip()
                if not os.path.exists(folder_path):
                    print("[!] Folder not found.")
                    continue
                batch_folder_convert(folder_path)
            else:
                path = input("Enter the full path of the file to convert: ").strip()

                if not os.path.exists(path):
                    print("\n[!] File not found. Please check the path and try again.")
                    continue

                if choice == 1:
                    txt_to_json(path)
                elif choice == 2:
                    xls_xlsx_to_json(path)
                elif choice == 3:
                    json_to_xlsx(path)
                elif choice == 4:
                    json_to_txt(path)
                elif choice == 5:
                    csv_to_json(path)
                elif choice == 6:
                    json_to_csv(path)
                elif choice == 7:
                    beautify_json(path)
                elif choice == 8:
                    minify_json(path)
                else:
                    print("\n[!] Invalid choice. Please choose a valid option.")

        except Exception as e:
            print(f"\n[!] Error occurred: {e}")

        again = input("\nWant another conversion? (y/n): ").lower().strip()
        if again != 'y':
            typewriter("\n[+] Exiting... Goodbye! ✨")
            break

if __name__ == '__main__':
    run_tool()
