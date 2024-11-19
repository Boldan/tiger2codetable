from requests import delete

import tiger_dict
import re
read_path = "C:\\Users\\Boldan\\Desktop\\1.txt"
with open(read_path,"r",encoding="utf-8") as of:
    data = of.readlines() # 读取文件
    data_format = []
    writer_path = "C:\\Users\\Boldan\\Desktop\\2.txt"
    with open(writer_path,"w",encoding="utf-8") as wr:  # 写入文件
        for key in data:
            d = key.replace('\n', '').split()   # 去掉换行符
            if re.search('《',d[0]) or re.search('》',d[0]):
                data_format = ''.join(re.findall(r'[\u4e00-\u9fa5]', ''.join(re.findall(r'《((?:.|\n)*?)》', d[0])))) # 提取指定字符(《》)间的中文,《》中可为空,可跨行
            # df = ''.join(re.findall(r'[\u4e00-\u9fa5]', ''.join(re.findall(r'《((?:.|\n)*?)》', d[0])))) # 提取指定字符(《》)间的中文,《》中可为空,可跨行
            # df = ''.join(re.findall(r'[\u4e00-\u9fa5]', ''.join(re.findall(r'\《([\s\S]+?)\》', d[0])))) # 提取指定字符(《》)间的中文,《》中不可为空,可跨行
            # df = ''.join(re.findall(r'[\u4e00-\u9fa5]', ''.join(re.findall(r".*a(.*)b", d[0])))) # 提取指定字符(a,b)间的中文,a,b中不可跨行
            # df = ''.join(re.findall(r'(?<=a)\d+\.?\d*(?=b)'r'(?<=a)\d+\.?\d*(?=b)', d[0]))) # 提取指定字符(a,b)间的数字
            else:
                data_format = ''.join(re.findall(r'[\u4e00-\u9fa5]', d[0]))
            if len(data_format) == 1:    # 只含一个中文字的情况
                wr.write(d[0] + '\t' + tiger_dict.tiger_dict[data_format] + '\r')
            elif len(data_format) == 2:  # 只含两个中文字的情况
                 wr.write(d[0] + '\t' + tiger_dict.tiger_dict[data_format[0]][0:2] + tiger_dict.tiger_dict[data_format[1]][0:2] + '\r')
            elif len(data_format) == 3:  # 含三个中文字的情况
                wr.write(d[0] + '\t' + tiger_dict.tiger_dict[data_format[0]][0] + tiger_dict.tiger_dict[data_format[1]][0] +
                      tiger_dict.tiger_dict[data_format[2]][0:2] + '\r')
            elif len(data_format) > 3:   # 含四个及四个以上中文字的情况
                wr.write(d[0] + '\t' + tiger_dict.tiger_dict[data_format[0]][0] + tiger_dict.tiger_dict[data_format[1]][0] +
                      tiger_dict.tiger_dict[
                          data_format[2]][0] + tiger_dict.tiger_dict[
                          data_format[len(data_format) - 1]][0] + '\r')
    wr.close()
of.close()
