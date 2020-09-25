import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
import os
#导入库
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
#避免画图时出现问题

#任务一
def python_1():
    def getfile():
        fileName=file_name.get()
        fileName_1=file_name_2.get()
        try:
            df= pd.read_csv(fileName)
            #丢弃缺失值
            df = df.dropna()
            #保存删除后的
            df.to_csv(fileName_1,encoding='cp936',index=False)
            #查看前三行
            t.insert('end',df.head(5))
            t.insert('end','\n')
            #查看后两行
            t.insert('end',df.tail(2))
            t.insert('end','\n')
            t.insert('end','任务1成功!')
        except:                          #打开文件失败时执行的代码
            tk.messagebox.showerror(title='wrong', message='打开文件失败！')
    window_1 = tk.Toplevel()
    window_1.geometry('600x400')
    window_1.title('数据读取及预处理')
    file_name=tk.Entry(window_1,width=27)
    file_name.place(x=300, y=5)
    l = tk.Label(window_1, text='请输入要打开的文件名:bike_day.csv')
    l.place(x=100,y=5)
    file_name_2=tk.Entry(window_1,width=24)
    file_name_2.place(x=320, y=50)
    l_2= tk.Label(window_1, text='请输入要保存的文件名:bike_day_ok.csv')
    l_2.place(x=100,y=50)
    a = tk.Button(window_1, text='开始', width=20, height=1,command=getfile).place(x=220, y=90)
    t=tk.Text(window_1,width=84,height=18)
    t.place(x=3,y=140)
    #读取数据

#任务二
def python_2():
    def getfile():
        #读取数据
        fileName=file_name.get()
        fileName_1=file_name_2.get()
        try:
            df = pd.read_csv(fileName, encoding='cp936')
            df_1 = df.loc[:,['instant','dteday','windspeed','casual','registered']]
            try:
                df_1.to_csv(fileName_1,sep=' ',encoding='cp936',index=False)
                tk.messagebox.showinfo(title='success!', message='任务二成功！')
                window_1.destroy()
            except:
                tk.messagebox.showerror(title='wrong', message='写文件失败！')
        except:#打开文件失败时执行的代码
            tk.messagebox.showerror(title='wrong', message='打开文件失败！')
    window_1 = tk.Toplevel()
    window_1.geometry('450x250')
    window_1.title('数据选择及导出')
    file_name=tk.Entry(window_1,width=31)
    file_name.place(x=220, y=5)
    l = tk.Label(window_1, text='请输入要打开的文件名:bike_day_ok.csv')
    l.place(x=0,y=5)
    file_name_2=tk.Entry(window_1,width=24)
    file_name_2.place(x=270, y=50)
    l_2= tk.Label(window_1, text='请输入要保存的文件名:bike_windspeed_user.txt')
    l_2.place(x=0,y=50)
    a = tk.Button(window_1, text='开始', width=20, height=1,command=getfile).place(x=150, y=90)
#任务三
def python_3():
    def getfile():
        fileName=file_name.get()
        fileName_1=file_name_2.get()
        try:
            df = pd.read_table(fileName, encoding='cp936',sep=' ',index_col=0)
            df['cnt'] = df['casual'] + df['registered']
            df.to_excel(fileName_1, encoding='cp936',index=False)
            tk.messagebox.showinfo(title='success!', message='任务三成功！')
            window_1.destroy()
        except:                          #打开文件失败时执行的代码
            tk.messagebox.showerror(title='wrong', message='打开文件失败！')
    window_1 = tk.Toplevel()
    window_1.geometry('475x250')
    window_1.title('数据计算')
    file_name=tk.Entry(window_1,width=28)
    file_name.place(x=270, y=5)
    l = tk.Label(window_1, text='请输入要打开的文件名:bike_windspeed_user.txt')
    l.place(x=0,y=5)
    file_name_2=tk.Entry(window_1,width=24)
    file_name_2.place(x=300, y=50)
    l_2= tk.Label(window_1, text='请输入要保存的文件名:bike_windspeed_user_cnt.xlsx')
    l_2.place(x=0,y=50)
    a = tk.Button(window_1, text='开始', width=20, height=1,command=getfile).place(x=150, y=90)

#任务四
def python_4():
    def getfile():
    #读取数据
        fileName=file_name.get()
        fileName_1=file_name_2.get()
        try:
            df_4 = pd.read_excel('bike_windspeed_user_cnt.xlsx', encoding='cp936')
            try:
                df_4_describe = df_4.describe()
                maxValue = df_4_describe.at['max','windspeed']
                meanValue = df_4_describe.at['mean','windspeed']
                minValue = df_4_describe.at['min','windspeed']
                t.insert('end','maxValue:')
                t.insert('end',maxValue)
                t.insert('end','\n')
                t.insert('end','meanValue:')
                t.insert('end',meanValue)
                t.insert('end','\n')
                t.insert('end','minValue:')
                t.insert('end',minValue)
                t.insert('end','\n')
                category = [minValue, 0.3, 0.35,0.4,maxValue]
                labels = ['Normal', 'Little', 'Big', 'Strong']
                windspeed_cut = pd.cut(df_4['windspeed'],category, right=False, labels=labels)
                t.insert('end',windspeed_cut)
                df_4['Label']=windspeed_cut
            except:
                tk.messagebox.showerror(title='wrong', message='文件处理失败！')
            try:
                df_4.to_csv(fileName_1, encoding='cp936',index=False)
                tk.messagebox.showinfo(title='success!', message='任务四成功！')
            except:
                tk.messagebox.showerror(title='wrong', message='导出文件失败！')
        except:
            tk.messagebox.showerror(title='wrong', message='打开文件失败！')
    window_1 = tk.Toplevel()
    window_1.geometry('600x400')
    window_1.title('数据分类汇总统计')
    file_name=tk.Entry(window_1,width=31)
    file_name.place(x=330, y=5)
    l = tk.Label(window_1, text='请输入要打开的文件名:bike_windspeed_user_cnt.xlsx')
    l.place(x=25,y=5)
    file_name_2=tk.Entry(window_1,width=27)
    file_name_2.place(x=360, y=50)
    l_2= tk.Label(window_1, text='请输入要保存的文件名:bike_windspeed_user_cnt_result.csv')
    l_2.place(x=25,y=50)
    a = tk.Button(window_1, text='开始', width=20, height=1,command=getfile).place(x=220, y=90)
    t=tk.Text(window_1,width=84,height=18)
    t.place(x=3,y=140)
    
#任务五
def python_5():
    def getfile():
        fileName=file_name.get()
        pngname=file_name_2.get()
        try:
            df_5 = pd.read_csv('bike_windspeed_user_cnt_result.csv', encoding='cp936')
            df_5 = df_5.loc[:,['cnt','Label']]
            lable1=df_5.groupby('Label')
            
            lable1=lable1['cnt'].mean()
            print(lable1)
            lable1.plot(kind='bar',figsize=(10,6))
            plt.xticks(rotation=0,fontsize=16)
            plt.yticks(fontsize=16)
            plt.ylabel('用户总数')
            plt.legend(fontsize=16)#显示图例并设置字号
            plt.title("风速与用户数的关系")
            plt.savefig('bike_windspeed_user_cnt.png',dpi=400)
            plt.show()
        except:
            tk.messagebox.showerror(title='wrong', message='打开文件失败！')
    window_1 = tk.Toplevel()
    window_1.geometry('600x200')
    window_1.title('数据可视化')
    file_name=tk.Entry(window_1,width=29)
    file_name.place(x=360, y=5)
    l = tk.Label(window_1, text='请输入要打开的文件名:bike_windspeed_user_cnt_result.csv')
    l.place(x=25,y=5)
    file_name_2=tk.Entry(window_1,width=33)
    file_name_2.place(x=330, y=50)
    l_2= tk.Label(window_1, text='请输入要保存的文件名:bike_windspeed_user_cnt.png')
    l_2.place(x=25,y=50)
    a = tk.Button(window_1, text='开始', width=20, height=1,command=getfile).place(x=220, y=90)

#主函数
if __name__ == '__main__':
    window=tk.Tk()
    window.title('共享单车数据分析以及可视化系统')
    window.geometry('500x300')
    a = tk.Button(window, text='数据读取及预处理',font=('Arial', 12), width=20,height=1,command=python_1)\
        .place(x=150, y=20)
    b = tk.Button(window, text='数据选择及导出', font=('Arial', 12), width=20, height=1,command=python_2)\
        .place(x=150, y=60)
    c = tk.Button(window, text='数据计算预处理', font=('Arial', 12), width=20, height=1,command=python_3)\
        .place(x=150, y=100)
    d = tk.Button(window, text='数据离散化及导出', font=('Arial', 12), width=20, height=1,command=python_4)\
        .place(x=150, y=140)
    e = tk.Button(window, text='数据可视化', font=('Arial', 12), width=20, height=1,command=python_5)\
        .place(x=150, y=180)
    f = tk.Button(window, text='退出', font=('Arial', 12), width=20, height=1,command=window.destroy)\
        .place(x=150, y=220)
    window.mainloop()
          
