##请在本页面（或者下载至本地后用文本编辑器打开的页面）使用Ctrl + F搜索习题标题，以便快速定位答案

＃平均电费
打印（（23  +  32  +  64）/ 3）


＃计算
＃用一个表达式填充它，计算出需要多少个图块。
打印（9 * 7  +  5 * 7）

＃使用一个表达式填充此内容，该表达式计算将剩余多少个图块。
打印（17 * 6  -（9 * 7  +  5 * 7））


＃哪个地区人口密度更高？里约还是旧金山？
sf_population，sf_area =  864816，231.89
rio_population，rio_area =  6453682，486.5

san_francisco_pop_density = sf_population / sf_area
rio_de_janeiro_pop_density = rio_population / rio_area

＃编写如果旧金山比Rio更密集则打印True的代码，否则返回False
打印（san_francisco_pop_density > rio_de_janeiro_pop_density）


＃修正引言
＃ TODO：修复这串！
ford_quote =  “你认为你能做到，或者你认为你做不到 - 你是对的。”


＃总销量
mon_sales =  “ 121 ”
tues_sales =  “ 105 ”
wed_sales =  “ 110 ”
thurs_sales =  “ 98 ”
fri_sales =  “ 95 ”

＃TODO：这种格式打印的字符串：本周的销售总额：XXX
＃您可能需要在print语句之前编写几行代码。
weekly_sales =  int（mon_sales）+  int（tues_sales）+  int（wed_sales）+  int（thurs_sales）+  int（fri_sales）
weekly_sales =  str（weekly_sales）   ＃将类型转换回!!
print（“本周总销售额：”  + weekly_sales）


＃列表索引
def  how_many_days（month_number）：
    days_in_month = [ 31，28，31，30，31，30，31，31，30，31，30，31 ]
    return days_in_month [month_number - 1 ]

＃本测试用例应打印31，即8月份的第8个月的天数
打印（how_many_days（8））


＃编写服务器日志信息
username =  “ Kinari ”
timestamp =  “ 04:50 ”
url =  “ http://petshop.com/pets/mammals/cats ”
print（用户名+ '访问网站' + url + ' at ' + timestamp + '。'）
＃ TODO：打印使用上述变量日志信息。
＃该消息应具有与此格式相同的格式：
＃ “Yogesh在16:20访问了网站http://petshop.com/pets/reptiles/pythons。”


＃ LEN
given_name =  “威廉”
middle_names =  “布拉德利”
family_name =  “皮特”

name_length =  LEN（GIVEN_NAME + '  ' + middle_names + '  ' + FAMILY_NAME）

＃现在我们检查以确保该名称符合驾驶执照字符限制
＃这里你不需要做什么
driving_license_character_limit =  28
print（name_length <= driving_license_character_limit）


＃列表切片
eclipse_dates = [ '' 2001年6月21日'，' 2002年12月4日'，' 2003年11月23日'，
                 ' 2006年3月29日'， ' 2008年8月1日'， ' 2009年7月22日'，
                 ' 2010年7月11日'， ' 2012年11月13日'， ' 2015年3月20日'，
                 ' 2016年3月9日' ]
＃ TODO：所以它打印列表的最后三个元素修改这条线
print（eclipse_dates [ - 3：]）


＃在嵌套字典中添加值
elements = { ' hydrogen '：{ ' number '：1，' weight '：1.00794，' symbol '：' H ' }，
            '氦'：{ '数字'： 2， '重量'： 4.002602， '符号'： '他' }}

＃ TODO：添加“is_noble_gas”条目的氢和氦的字典
＃提示：氦是一种惰性气体，氢气不是
elements [ ' hydrogen ' ] [ ' is_noble_gas ' ] =  False
elements [ ' helium ' ] [ ' is_noble_gas ' ] =  真
