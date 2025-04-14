with open('Fangda.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 去除换行符，并在每句话后添加逗号
modified_text = ', '.join(line.strip() for line in lines)

with open('outputF.txt', 'w', encoding='utf-8') as file:
    file.write(modified_text)
