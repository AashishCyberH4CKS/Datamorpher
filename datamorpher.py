import json
import pandas as pd
import os
import time
import sys

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

BANNER = GREEN + r"""
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

print(BANNER)
print("Version 1.0 | Created by Aashish_Cyber_H4CKS\n")

def loading_animation(task):
    print(f"\n[+] {task} in progress...", end="", flush=True)
    for _ in range(10):
        time.sleep(0.2)
        print(RED + "." + RESET, end="", flush=True)
    print(" Done!\n")

def txt_to_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = {str(i): line.strip() for i, line in enumerate(lines)}
    output_path = path.replace('.txt', '_converted.json')
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    loading_animation("TXT to JSON")
    print(f"Converted file saved at: {output_path}")

def json_to_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    output_path = path.replace('.json', '_converted.txt')
    with open(output_path, 'w', encoding='utf-8') as txt_file:
        for key, value in data.items():
            txt_file.write(f"{value}\n")
    loading_animation("JSON to TXT")
    print(f"Converted file saved at: {output_path}")

def xlsx_to_json(path):
    df = pd.read_excel(path)
    output_path = path.replace('.xlsx', '_converted.json')
    df.to_json(output_path, orient='records', indent=4)
    loading_animation("XLSX to JSON")
    print(f"Converted file saved at: {output_path}")

def json_to_xlsx(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    output_path = path.replace('.json', '_converted.xlsx')
    df.to_excel(output_path, index=False)
    loading_animation("JSON to XLSX")
    print(f"Converted file saved at: {output_path}")

def csv_to_json(path):
    df = pd.read_csv(path)
    output_path = path.replace('.csv', '_converted.json')
    df.to_json(output_path, orient='records', indent=4)
    loading_animation("CSV to JSON")
    print(f"Converted file saved at: {output_path}")

def json_to_csv(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    output_path = path.replace('.json', '_converted.csv')
    df.to_csv(output_path, index=False)
    loading_animation("JSON to CSV")
    print(f"Converted file saved at: {output_path}")

def beautify_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    output_path = path.replace('.json', '_pretty.json')
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)
    loading_animation("Beautifying JSON")
    print(f"Beautified JSON saved at: {output_path}")

def minify_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    output_path = path.replace('.json', '_minified.json')
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, separators=(',', ':'))
    loading_animation("Minifying JSON")
    print(f"Minified JSON saved at: {output_path}")

def main():
    print("Choose the type of conversion:")
    print("1. TXT to JSON")
    print("2. XLSX to JSON")
    print("3. JSON to XLSX")
    print("4. JSON to TXT")
    print("5. CSV to JSON")
    print("6. JSON to CSV")
    print("7. Beautify JSON")
    print("8. Minify JSON")

    try:
        choice = int(input("\nEnter your choice (1-8): "))
        path = input("Enter the full path of the file to convert: ").strip()

        if not os.path.exists(path):
            print("\n[!] File not found. Please check the path and try again.")
            return

        file_size_gb = os.path.getsize(path) / (1024 ** 3)
        if file_size_gb > 1024:
            print("\n[!] File too large. Max limit is 1024 GB.")
            return

        if choice == 1:
            txt_to_json(path)
        elif choice == 2:
            xlsx_to_json(path)
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

if __name__ == '__main__':
    main()
