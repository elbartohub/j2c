# j2c
Translate video subtitle file .srt from any language

翻譯影片字幕檔 .srt 至任何指定語言。默認由日文翻譯成繁體中文

先安裝 Python 庫, 使用：

pip install googletrans

執行方法：

python j2c.py [input.srt] [output.srt]

--------------------------------
-s 或 --source 輸入文章語言 默認=ja

-d 或 --dest 目標語言 默認=zh-tw

-l 或 --list 列出所有可用的語言代碼

-h 幫助
