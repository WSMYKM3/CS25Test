import sys
import re

def remove_newline_after_comma(input_file="Fangda.txt", output_file="outputfangda.txt"):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 去除逗号后的换行符
        cleaned_content = re.sub(r",\s*\n", ",", content)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        
        print(f"处理完成，结果已保存至: {output_file}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    remove_newline_after_comma()
