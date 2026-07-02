
class publai1:
    def __init__(self):
        date0='2026-6-30' 
        yearlai='2026' #for cloudnoVBAopenpyxl.py
        num,num1,num2=113,24,137 #for sixCloud.py
        self.column399088=num1
        self.column399378=num2
        wbsheetname='start_from_2025.12.5' #sheetname of newworkbook
        othersheetname='start_from_2024.12.6'
        filename='./data/datefortest'+str(num)+' - 副本.csv'
        filename1='../data/datefortest'+str(num)+' - 副本.csv'
        self.filename=filename
        self.filename1=filename1
        self.date=date0
        self.year0=yearlai
        self.wbsheetname=wbsheetname
        self.othersheetname=othersheetname
    def __str__(self):
        # 2026年7月2日推送月底镜像上传CNB前，没有将实操镜像先推送上传到github，彻底完成后用git reset 返回之前状态cee853补上"for prac"的commit和git push，但效果不佳月底镜像中才有的文件立即出现在        # github中，所以github中的2026年6月底实操镜像是领先CNB的。最后又用git reset返回最新状态，并留下此段文字。
        return "子文件夹下的ipynb爬虫文件均使用变量filename1；根目录下的ipynb爬虫文件则使用变量filename。"
