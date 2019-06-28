import pandas as pd
import numpy as np
import re
import jieba
from wordcloud import WordCloud

'''
使用pandas读取文件
'''
df = pd.DataFrame(pd.read_csv("../../data/dd.csv",encoding='utf-8'))

'''
对福利的那一列数据进行处理
'''
def deal_fuli_wordclod():
    text = ""
    for x in df['fuli']:
        x = str(x)
        x = re.sub('[,]', '', x)
        x = re.sub('"','',x)
        x = re.sub(' ','',x)
        # print(x[1:-1])
        text += x[1:-1]
    cut_text = jieba.cut(text)
    result = " ".join(cut_text)
    wc = WordCloud(
        font_path=r'.\simhei.ttf',
        background_color='white',
        width=500,
        height=350,
        max_font_size=50,
        min_font_size=10,
    )
    wc.generate(result)
    wc.to_file(r"../../tmp/词云/fuliwordcloud.png")

def main():
    deal_fuli_wordclod()

if __name__ == '__main__':
    main()
