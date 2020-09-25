# wind_spread-and-bike_user
【数据说明】 该数据集是 2011、 2012 年共享单车租借统计数据集。 字段说明： 1) instant: 租借记录序号。 2) dteday : 日期 3) season : 季节 (1:springer, 2:summer, 3:fall, 4:winter) 4) yr : 年(0: 2011, 1:2012) 5) mnth : 月 ( 1 to 12) 6) hr : 时 (0 to 23) 7) holiday : 是否是假期 8) weekday : 星期几 9) workingday : 是否工作日. 10) weathersit : 天气 - 1: 晴天（Clear） - 2: 雾、云（Cloudy） - 3: 小雨小雪(Light Rain) - 4: 大雨(Heavy Rain) 11) temp : 温度 12) atemp: 归一化温度 13) hum: 归一化湿度。 14) windspeed: 归一化风速。 15) casual: 临时用户。 16) registered: 注册用户。
需要完成任务如下：
  1、 用 pandas 库读取“bike_day.csv”文件， 查看前五行、后两行，并将缺失值全部丢弃处理。
  2、 选择 instant、 dteday、 windspeed、 casual、 registered 共 5 列数据导出到文本文件“bike_windspeed_user.txt”，要求数据之间用空格分隔，每行末尾包含
  换行符。
  3、 读取文本文件“bike_windspeed_user.txt”，计算列 casual 与列 registered 和（即 casual+registered），并作为一个新的列 cnt 添加到原始数据，导出到新
  的 Excel 文件“bike_windspeed_user_cnt.xlsx”中。
  4、 读取 Excel 文件“bike_windspeed_user_cnt.xlsx”， 统计列 windspeed 的最大值 maxValue、最小值 minValue、平均值 meanValue。利用 category =[minValue, 0.3, 0.35,0.4， maxValue]和         labels = ['Normal', 'Little', 'Big', 'Strong']将 windspeed 进行离散化；并将离散化结果作为一个新的列 Label 添加到原始数据集，并保存为“bike_windspeed_user_cnt_result.csv”。
  5、 读取“bike_windspeed_user_cnt_result.csv”，按照列 Lable 分组，计算列 cnt 的均值， 并以柱状图可视化显示该均值。要求以列 Lable 为 X 轴，轴刻度分别为“Normal”、“Little”、“Big”、“Strong”，   包括图例、图标题，填充颜色为蓝色，并保存为“bike_windspeed_user_cnt.png”，要求分辨率不低于 300dpi。
使用pandas以及tkinter以及其他常用库进行数据处理任务以及可视化功能。
