class publai1:
    def __init__(self):
        date0='2025-1-27' #新年里首月的月底镜像生成前必须保证cloudnoVBAopenpyxl.py中的参数year得到修改，切记切记！！
        num=96
        filename='./data/datefortest'+str(num)+' - 副本.csv'
        filename1='../data/datefortest'+str(num)+' - 副本.csv'
        self.filename=filename
        self.filename1=filename1
        self.date=date0
    def __str__(self):
        return "子文件夹下的ipynb爬虫文件均使用变量filename1；根目录下的ipynb爬虫文件则使用变量filename。"
