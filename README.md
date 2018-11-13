＃在嵌套字典中添加值
elements = { ' hydrogen '：{ ' number '：1，' weight '：1.00794，' symbol '：' H ' }，
'氦'：{ '数字'： 2， '重量'： 4.002602， '符号'： '他' }}

＃ TODO：添加“is_noble_gas”条目的氢和氦的字典
＃提示：氦是一种惰性气体，氢气不是
elements [ ' hydrogen ' ] [ ' is_noble_gas ' ] = False
elements [ ' helium ' ] [ ' is_noble_gas ' ] = 真
