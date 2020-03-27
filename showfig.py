# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
import pandas
from mpl_toolkits.mplot3d import Axes3D

def plot_data(wls,xdata,ydata):  
    #1.给3D图画一个坐标轴
    fig=plt.figure()
    ax=Axes3D(fig)
    
    wls_len = len(wls) #4001
    for idx, rdata in xdata.iterrows():
        print(idx)
        print(rdata.head()) #转化为每一组波数和吸光度
        ydata_sample = ydata[idx]
        vals = rdata
        on_ar = np.full(wls_len, ydata_sample)
        ax.plot(wls, on_ar, vals)
    ax.set_title("Spectrum")
    ax.set_xlabel("Wavenum")
    ax.set_ylabel("protein")
    ax.set_zlabel("Value")
    plt.show()


def main():
    FILENAME = "siliao-end-2.xlsx"
    oct_df = pandas.read_excel(FILENAME)
    print(oct_df.head())
    wls = np.array([ int(float(i)) for i in oct_df.columns.values[8:]])
    xdata = oct_df.loc[:,'12000.000000':]
    ydata = oct_df['protein']
    print(wls) #波数 [12000 11998 11996 ...  4004  4002  4000]
    print(xdata.head()) #68组有效数据吸光度与波数表
    print(ydata.head()) #因变量，如含水量moisture
    #绘制三维光谱图
    plot_data(wls,xdata,ydata)

if __name__ == '__main__':
    main()