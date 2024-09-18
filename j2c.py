import argparse
from googletrans import Translator
import re

def is_timestamp(line):
    return re.match(r'^\d+\n\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}', line) is not None

def translate_line(translator, line):
    parts = re.split(r'(-->|ーー＞|\s+)', line)
    translated_parts = []
    for part in parts:
        if part.strip() and not re.match(r'(-->|ーー＞|\s+)', part):
            translated_part = translator.translate(part, src='ja', dest='zh-tw').text
        else:
            translated_part = part
        translated_parts.append(translated_part)
    return ''.join(translated_parts)

def translate_file(input_file, output_file):
    translator = Translator()
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if is_timestamp(line):
                outfile.write(line)
            else:
                translated_line = translate_line(translator, line)
                outfile.write(translated_line)
            print('.', end='', flush=True)  # 顯示進度
    print("\n翻譯完成！")

def main():
    parser = argparse.ArgumentParser(description='將日文翻譯成繁體中文')
    parser.add_argument('input_file', help='輸入文件路徑')
    parser.add_argument('output_file', help='輸出文件路徑')
    
    args = parser.parse_args()
    
    print(f"正在將 {args.input_file} 翻譯到 {args.output_file}")
    translate_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()