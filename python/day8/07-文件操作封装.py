# 定义文件类
class File():
    def __init__(self, filename):
        file_path = r'resource/' + filename
        self.f = open(file_path)

    def write(self, content):
        self.write(content)

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()

    # def __del__(self):
    #     self.f.close()


if __name__ == '__main__':
    file = File('demo.txt')
    print(file.read())
    file.close()

