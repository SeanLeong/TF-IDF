'''    获取属性的关联度矩阵'''def getWords(words):    new_words = []    for word in words:            new_words.append(word.strip())    return new_words# 统计拥有两个属性的用户数量def getNum_byAttr(attr, attr2, lines):    count = 0    for line in lines:        words = line.split(" ")        words = getWords(words)        if attr in words and attr2 in words:            count += 1    return count# 获取拥有两个属性的用户iddef getIndex_byAttr(attr, attr2):    indexs = []    with open('dataset.txt', 'r', encoding='utf-8') as data:        lines = data.readlines()        for index, line in enumerate(lines):            words = line.split(" ")            words = getWords(words)            if attr in words and attr2 in words:                indexs.append(str(index + 1))    return indexs# 统计拥有两个属性、并存在关联的用户数量def getNum_byRelate(attr, attr2):    indexs = getIndex_byAttr(attr, attr2)    with open('links.txt', 'r', encoding='utf-8') as links:        link_lines = links.readlines()        count = 0        for index, line in enumerate(link_lines):            words = line.split('\t')            words = getWords(words)            if words[0] in indexs and words[1] in indexs:                count += 1        return count# 获取两个属性的关联度def getRelation(attr, attr2):    indexs = getIndex_byAttr(attr, attr2)   #获取用户对应属性的用户的index列表    user_num = len(indexs)  # 用户数量    relate_num = getNum_byRelate(attr, attr2)    #获取拥有对应属性的用户关联数量(简称:关联数量)    result = 4 * relate_num / (user_num ** 2 - user_num)    return result# 获取属性的关联度矩阵def getAttr_matrix():    passwith open('D:\python-workspace\TF-IDF\pre\dataset_washed.txt', 'r', encoding='utf-8') as data:    lines = data.readlines()    # num = getNum_byAttr('信息系统', '电子', lines)    indexs = getIndex_byAttr('研究生', '计算机')    count = getNum_byRelate('研究生', '计算机')    print(getRelation("研究生", "计算机"))