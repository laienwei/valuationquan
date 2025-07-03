class publai1:
    def __init__(self):
        date0='2025-6-30' 
        yearlai='2025' #for cloudnoVBAopenpyxl.py
        num=101 #for sixCloud.py
        filename='./data/datefortest'+str(num)+' - 副本.csv'
        filename1='../data/datefortest'+str(num)+' - 副本.csv'
        self.filename=filename
        self.filename1=filename1
        self.date=date0
        self.year0=yearlai
    def __str__(self):
        return "子文件夹下的ipynb爬虫文件均使用变量filename1；根目录下的ipynb爬虫文件则使用变量filename。"
