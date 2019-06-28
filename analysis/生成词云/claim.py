import pandas as pd
import numpy as np
import re
import jieba
from wordcloud import WordCloud
import codecs

'''
使用pandas读取文件
'''
df = pd.DataFrame(pd.read_csv("../../data/dd.csv",encoding='utf-8'))
# print(df['yaoqiu'])

'''
对福利的那一列数据进行处理
'''
def deal_yaoqiu_wordclod():
    text = ""
    for x in df['yaoqiu']:
        x = str(x)
        x = re.sub('[,]', '', x)
        x = re.sub('"','',x)
        x = re.sub(' ','',x)
        x = re.sub('职责','',x)
        x = re.sub('工作', '', x)
        # print(x[1:-1])
        text += x
    # print(x)
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
    '''
    设置词云的背景图片
    WordCloud(  
       font_path = 'yahei.ttf',   
       background_color = 'white',  
       mask = color_mask,  
       max_words = 1000,  
       max_font_size = 100          
       )  
    '''
    wc.generate(result)
    wc.to_file(r"../../tmp/词云/yaoqiuwordcloud.png")

def main():
    deal_yaoqiu_wordclod()

if __name__ == '__main__':
    main()
