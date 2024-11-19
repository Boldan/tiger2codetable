import tiger_dict
import re
read_path = "C:\\Users\\Boldan\\Desktop\\1.txt"
with open(read_path,"r",encoding="utf-8") as of:
    data = of.readlines() # 读取文件
    data_format = []
    writer_path = "C:\\Users\\Boldan\\Desktop\\2.txt"
    with open(writer_path,"w",encoding="utf-8") as wr:  # 写入文件
        for key in data:
            d = key.replace('\n', '').replace('\t','\t').split()   # 去掉换行符
            # print(d[1])
            df = ''.join(re.findall(r'[\u4e00-\u9fa5]', d[0]))  # 提取中文,并串连起来
            # ds = ''.join(re.findall(r'[\d+]', d[1]))  # 提取词频,保留数字,并串连起来
            # ds = ''.join(re.findall(r'[a-zA-Z]', d[1]))  # 提取词频,保留字母,并串连起来
            # ds = ''.join(filter(lambda s:s in'0123456789.', d[1]))  # 提取词频,保留数字+".",并串连起来
            ds = ''.join(filter(lambda s:s in'a-zA-Z0123456789.', d[1]))  # 提取词频,保留字母+数字+".",并串连起来
            # print(d)
            print(ds)
            if len(df) == 1:    # 只含一个中文字的情况
                wr.write(d[0] + '\t' + tiger_dict.tiger_dict[df] + '\t' + ds[0:10] + '\r')
            elif len(df) == 2:  # 只含两个中文字的情况
                 wr.write(d[0] + '\t' + tiger_dict.tiger_dict[df[0]][0:2] + tiger_dict.tiger_dict[df[1]][0:2] + '\t' + ds[0:10] + '\r')
            elif len(df) == 3:  # 含三个中文字的情况
                wr.write(d[0] + '\t' + tiger_dict.tiger_dict[df[0]][0] + tiger_dict.tiger_dict[df[1]][0] +
                      tiger_dict.tiger_dict[df[2]][0:2] + '\t' + ds[0:10] + '\r')
            elif len(df) > 3:   # 含四个及四个以上中文字的情况
                wr.write(d[0] + '\t' + tiger_dict.tiger_dict[df[0]][0] + tiger_dict.tiger_dict[df[1]][0] +
                      tiger_dict.tiger_dict[
                          df[2]][0] + tiger_dict.tiger_dict[
                          df[len(df) - 1]][0] + '\t' + ds[0:10] + '\r')
