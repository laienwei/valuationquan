class publai1:
    def __init__(self):
        date0='2024-9-30'
        num=92
        filename='./data/datefortest'+str(num)+' - 副本.csv'
        filename1='../data/datefortest'+str(num)+' - 副本.csv'
        self.filename=filename
        self.filename1=filename1
        self.date=date0
    def __str__(self):
        return "子文件夹下的ipynb爬虫文件均使用变量filename1；根目录下的ipynb爬虫文件则使用变量filename。"
