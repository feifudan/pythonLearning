import wordcloud


#词云对象配置参数，图片width默认400，height默认200，min_font_size,max_font_size,
# max_words指定显示的最大单词数量，
# stop_words={"python"}指定词云中不显示的单词
#mask指定词云的形状，默认是长方形，需要引用imread函数，即mask = imread("背景是白色的有形状的图片.png")
#background_color指定背景颜色，默认是黑色
w = wordcloud.WordCloud(width=100,height=100)

w.generate("'PRINCE FORTINBRAS Let four captains Bear Hamlet, like a soldier, to the stage;'")
w.to_file("ciyun.png")

#使用中文的时候，需要首先进行分词，因为词云是使用空格区分单词的