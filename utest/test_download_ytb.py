import subprocess
import csv


class YTB:
    def __init__(self):
        pass

    def execx(self, command):
        print(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(output)

    def read_url(self, file_path):
        urls = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            # 创建一个CSV阅读器
            csv_reader = csv.reader(file)

            # 逐行读取数据
            for row in csv_reader:
                # row是一个列表，包含CSV文件中一行的数据
                urls.extend(row)
        return urls

    def main(self):
        filepath = r'E:\mytaskwork\素材\视频\源\downloads.csv'
        urls = self.read_url(filepath)

        for row in urls:
            print(row)
            try:
                cmd = ['yt-dlp', '-f', '137+140', '--proxy', 'http://127.0.0.1:58591', row, '--merge-output-format',
                       'mp4',
                       '--external-downloader', 'aria2c', '--downloader-args', 'aria2c:"-x 16 -k 1M"']
                self.execx(cmd)
            except:
                print("下载失败", row)


if __name__ == '__main__':
    ytb = YTB()
    ytb.main()
