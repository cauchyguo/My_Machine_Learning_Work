#函数代码块以def关键词开头,后接函数标识符名称和圆括号()
#圆括号为传递的参数,参数分为形参(language)与实参("java")
def hello_world(language): #冒号起始
    """a function to greet"""#函数的第一行语句为文档字符串,存放函数说明
    print("Hello, " + language + " world!")
    return #return结束函数并选择性地返回值给传递方,不带表达式则返回None

languages = ['java','c','python','JavaScript']
for language in languages:
    hello_world(language.title()) #函数的调用