import os;
import shutil;

# 输出当前文件目录
print("path: "+os.path.abspath("."));
# 判断是否为文件夹
print("是否是文件夹: %s, %s" % (os.path.isdir("D:/forum-master/"), os.path.isdir("D:/forum-master/pom.xml")));
# 判断是否为文件
print("是否为文件: %s, %s" % (os.path.isfile("D:/forum-master/"), os.path.isfile("D:/forum-master/pom.xml")));
# 指定文件或文件夹是否存在
print("%s: %s, %s: %s" % ("D:/forum-master/", os.path.exists("D:/forum-master/"), "D:/2018.txt", os.path.exists("D:/2018.txt")));
# 列出指定文件夹下的文件
print("文件为: %s" % [x for x in os.listdir("D:/forum-master/")]);
# 列出指定文件夹下的目录
print([x for x in os.listdir("D:/forum-master/") if os.path.isdir(os.path.join("D:/forum-master/", x))]);
# 从文件全路径中拆分出路径和文件名
print(os.path.split("D:/forum-master/"));
# 分离扩展名
print(os.path.splitext("D:/forum-master/123.txt"));
# 获取文件名
print(os.path.basename("D:/forum-master/123.txt"));
# 获取路径名
print(os.path.dirname("D:/forum-master/123.txt"));
# 把文件路径和文件名合并成全路径
print(os.path.join("D:/test123/", "test123"));
# 创建文件夹(父目录必须存在且不能重复创建)
# os.mkdir("D:/test123/");
# 创建文件夹(父目录如果不存在则一并创建父目录.但不能重复创建)
os.makedirs(r"D:/2018/2018");
# 删除文件夹(文件必须存在且不能有子文件)
# os.removedirs("D:/test123/");
# 删除文件夹(同时删除子文件)
shutil.rmtree(r"D:/2018");
# 获取文件大小(文件必须存在)
print(os.path.getsize("D:/forum-master/pom.xml"));
# 获取文件属性
print(os.stat("D:/forum-master/pom.xml"));

# ----------------------------------------------------------------------------------------------------------------------
# 创建新文件(windows没有node概念,会报错)
# os.mknod("D:/test123/test.txt");
# 直接打开一个文件，如果文件不存在则创建文件
fp = open("D:/test123/test.txt", "w");
# 向文件中写入数据
print(fp.write("123"));



