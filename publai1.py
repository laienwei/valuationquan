
class publai1:
    def __init__(self):
        date0='2025-12-31' 
        yearlai='2025' #for cloudnoVBAopenpyxl.py
        num,num1,num2=107,24,139 #for sixCloud.py
        self.column399088=num1
        self.column399378=num2
        sheetname='start_from_2025.7.4' #sheetname of newworkbook
        filename='./data/datefortest'+str(num)+' - 副本.csv'
        filename1='../data/datefortest'+str(num)+' - 副本.csv'
        self.filename=filename
        self.filename1=filename1
        self.date=date0
        self.year0=yearlai
        self.sheetname=sheetname
    def __str__(self):
        return "子文件夹下的ipynb爬虫文件均使用变量filename1；根目录下的ipynb爬虫文件则使用变量filename。"
