#字符串的连接
conversion  = "What day is it today?"
conversion += "\nIt's Sunday."
print(conversion)

print("—"*50)
#字符串的乘法
msg = "重要的事情说三遍 "
print(msg*3)

print("—"*50)

#字符串的匹配与查找(startswith(),endswith(),find(),)
text = "All things in their being are good for something."
print(text.startswith('all'))     #检查字符串的开头是否正确(区分大小写)
print(text.endswith("something")) #检查字符串的结尾是否正确
print(text.find('something'))     #查找特定字符串是否存在并返回这个字符串的首字母的索引，若不存在则返回-11
print(text.find('all'))
print(text.replace('All','No'))   #将字符串中存在的字符串做替换