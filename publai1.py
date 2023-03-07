class publai1:
    def __init__(self):
        filename='./data/datefortest73 - 副本.csv'
        filename1='../data/datefortest73 - 副本.csv'
        self.filename=filename
        self.filename1=filename1
    def __str__(self):
        return "子文件夹下的ipynb爬虫文件均使用变量filename1；根目录下的ipynb爬虫文件则使用变量filename。"
