import jieba

#精确模式
results = jieba.lcut("中华人民共和国是一个伟大的国家")

print(results)

#全模式
results = jieba.lcut("中华人民共和国是一个伟大的国家",cut_all = True)

print(results)

#搜索引擎模式（首先使用精确模式分词，然后再对每一个词进行分词）
results = jieba.lcut_for_search("中华人民共和国是一个伟大的国家")

print(results)


jieba.add_word("增加自定义单词")

