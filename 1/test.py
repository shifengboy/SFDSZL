name = input('请输入你的名字：')
print('你的名字是'+name) #使用加号连接
print('你的名字是%s'%name)#使用占位符
age = 18
print('我的名字是%s,年龄是%d岁.'%(name,age))#这种是里面有多个格式化内容的，前面那个是字符串，后面这个是整数，多个变量的后面跟值的时候必须要加上括号
print('我的名字是%r,年龄是%r岁.'%(name,age))#万能统配符 可以将后面给的参数原样打印出来，带有类型信息,输出name为字符串，age为整数
print('你的名字是{your_name}'.format(your_name=name)) #使用format格式化输出，{}里面的名字可以随便写但是要和后面的format中的名字保持一致，然后再把你前面定义的变量写到等号后面就可以了。
print('我的名字是{your_name},年龄是{your_age}岁.'.format(your_age=age,your_name=name))#{}format后的参数可以不按照顺序写
print('你的名字是{}'.format(name)) #{}里可以为空,format后直接填参数即可
print('我的名字是{},年龄是{}岁.'.format(name,age)) #{}为空时，参数默认按照顺序传递
print('我的名字是{1},年龄是{0}岁.'.format(age,name)) #{}里有数字时，参数按照数字大小从小到大传递，该方法可以多次调用