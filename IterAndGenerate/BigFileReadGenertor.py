"""
生成器运用，大文件读取
"""
def FileReaderGenerator(file, spilt_symbol):
    out_line = ''
    while True:
        while spilt_symbol in out_line:  # 读出来的行有分隔符号
            pos = out_line.index(spilt_symbol)  # 找到分隔符下标
            yield out_line[:pos]  # 迭代出去
            out_line = out_line[pos+len(spilt_symbol):]  # out_line变化
        new_read = f.read(4096)  # 继续读取文件
        if not new_read:  # 后续文件为空
            yield out_line
            break
        out_line += new_read  # 拼接


with open('test_file.txt', 'r') as f:
    for line in FileReaderGenerator(f, '|'):
        print(line)