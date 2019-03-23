'''
Created on 2018年7月13日
数据分析
@author: woshiuu
'''
import re
import jieba
import jieba.analyse
from collections import Counter
import jieba.posseg as pseg
from wbspider import keywords_new

def analysis(text):
    list1 = []
    record = {}  # 记录命中信息
    express = {}
    name_set = {}
    result = ""
    count = 0
    
    while True:
        line = text.splitlines()
        for i in line:
            count += 1
            if count >= 4:
                item = i.split(" ", 1)[1]
                ex_all = re.findall("\\[.*?\\]", item)  
                if ex_all:
                    for ex_item in ex_all:
                        express[ex_item] = express.get(ex_item, 0) + 1
                for kw, keywords in keywords_new.keyword_dict.items():  # kw是大类
                    flag = 0  # 大类命中的标志
                    for key, keyword in keywords.items():  # key 是小类
                        if flag == 1:
                            break
                        for word in keyword:  # 小类关键词
                            match_flag = 1  # 列表中关键词全部命中的标志
                            for small_word in word:  # 关键词列表
        #                        print small_word
                                match = re.search(re.compile(small_word, re.I), item)
                                if not match:
                                    match_flag = 0
                                    break
                            if match_flag == 1:  #命中了一个小类
                                record[kw] = record.get(kw, 0) + 1 # 单次记录
                                flag = 1
                                break
                item = re.sub("\\[.*?\\]", '', item)
                list = jieba.cut(item, cut_all = False)
                for ll in list:
                    list1.append(ll)  # 分词
                seg_list = pseg.cut(item)
                for word, flag in seg_list:
                    if flag == 'nr':
                        name_set[word] = name_set.get(word, 0) + 1
        else:
            break
    
    count = Counter(list1)
    for item in sorted(dict(count).items(), key=lambda d:d[1], reverse = True):
        if len(item[0]) >= 2 and item[1] >= 3:   
            word = ""
            word = str(item[0]) + str(item[1]) + "\r\n"
                
    for key, keywords in sorted(record.items(), key=lambda d:d[1], reverse = True):
        category = ""
        category = "命中了" + key + str(record[key]) + "次" + "\r\n"
        result = result + category
    return result   
#     for key, keywords in sorted(express.items(), key=lambda d:d[1], reverse = True):
#         ex = ""
#         ex = "使用了" + key + "表情" + str(express[key]) + "次" + "\r\n"
#      
#     for key, keywords in sorted(name_set.items(), key=lambda d:d[1], reverse = True):
#         name = ""
#         name = "使用了名字" + key + str(name_set[key]) + "次" + "\r\n"
