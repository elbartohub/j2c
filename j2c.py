import argparse
from googletrans import Translator, LANGUAGES
import re

def is_timestamp(line):
    return re.match(r'^\d+\n\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}', line) is not None

def translate_line(translator, line, src_lang, dest_lang):
    parts = re.split(r'(-->|ーー＞|\s+)', line)
    translated_parts = []
    for part in parts:
        if part.strip() and not re.match(r'(-->|ーー＞|\s+)', part):
            translated_part = translator.translate(part, src=src_lang, dest=dest_lang).text
        else:
            translated_part = part
        translated_parts.append(translated_part)
    return ''.join(translated_parts)

def translate_file(input_file, output_file, src_lang, dest_lang):
    translator = Translator()
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if is_timestamp(line):
                outfile.write(line)
            else:
                translated_line = translate_line(translator, line, src_lang, dest_lang)
                outfile.write(translated_line)
            print('.', end='', flush=True)  # 顯示進度
    print(f"\n翻譯完成！從 {LANGUAGES[src_lang]} 翻譯到 {LANGUAGES[dest_lang]}")

def list_languages():
    print("可用的語言代碼:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

def main():
    parser = argparse.ArgumentParser(description='翻譯文本文件')
    parser.add_argument('input_file', nargs='?', help='輸入文件路徑')
    parser.add_argument('output_file', nargs='?', help='輸出文件路徑')
    parser.add_argument('-s', '--source', default='ja', help='源語言代碼 (默認: ja)')
    parser.add_argument('-d', '--dest', default='zh-tw', help='目標語言代碼 (默認: zh-tw)')
    parser.add_argument('-l', '--list', action='store_true', help='列出所有可用的語言代碼')
    
    args = parser.parse_args()
    
    if args.list:
        list_languages()
        return

    if not args.input_file or not args.output_file:
        parser.error("必須提供輸入文件和輸出文件路徑")

    if args.source not in LANGUAGES or args.dest not in LANGUAGES:
        print("錯誤：無效的語言代碼。使用 -l 或 --list 選項查看所有可用的語言代碼。")
        return
    
    print(f"正在將 {args.input_file} 從 {LANGUAGES[args.source]} 翻譯到 {LANGUAGES[args.dest]}，輸出到 {args.output_file}")
    translate_file(args.input_file, args.output_file, args.source, args.dest)

if __name__ == "__main__":
    main()
