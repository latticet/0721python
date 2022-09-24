

# 下文管理器操作文件
with open('resource/demo.txt', 'w+', encoding='utf8') as f:
    f.write('123\n456')
    f.seek(0)
    print(f.read())