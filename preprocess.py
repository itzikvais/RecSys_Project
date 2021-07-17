import json
import pandas as pd
import random
import pickle
import numpy as np
import os

DATA_DIR_PATH = os.path.join(os.getcwd(),'part_data/')
OUTPUT_DIR_PATH =  os.path.join(os.getcwd(),'outputs/')

import json
import pandas as pd
import random
import pickle
import numpy as np
import os
# pid=[]
# name=[]
# collaborative=[]
# modified_at=[]
# num_tracks=[]
# num_albums=[]
# num_followers=[]
title=["album_name","album_uri","artist_name","artist_uri","duration_ms","pos","track_name","track_uri","pid","pname"]
def readOne(myjsonname):
    partPid=[]
    num=[]
#    Alltracks = pd.DataFrame([], columns=title)
    with open(myjsonname) as f:
        temp = json.loads(f.read())
        for i in range(len(temp['playlists'])):
            partPid.append(temp['playlists'][i]["pid"])
            num.append(temp['playlists'][i]["num_tracks"])
    return partPid,num
def readJson(Jsondir,output_dir):
    ALLPid=[]
    Allnum=[]
    for i in os.walk(Jsondir):
#        print(i[0],Jsondir+i[2][0])
        for j in range(len(i[2])):
            inputpath=str(Jsondir+i[2][j])
            partPid,num=readOne(inputpath)
            ALLPid=ALLPid+partPid
            Allnum=Allnum+num
    df=pd.DataFrame({'pid':ALLPid,'tracks_num':Allnum})
    df.to_csv(os.path.join(output_dir,"tracksNumOfPlalist.csv"),index=False)
    print("DONE!")
    return Allnum
# Allnum=readJson(r"../data/")
    
#绘制歌单中歌曲数量分布的情况
def drawPic(output_dir):
    import seaborn as sns
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    x=list(pd.read_csv(os.path.join(output_dir,"tracksNumOfPlalist.csv"))['tracks_num'])
#    mu=np.mean(x)
#    sigma=np.std(x)
#    n,bins,patches=plt.hist(x,100,normed=1)
#    y=mlab.normpdf(bins,mu,sigma)
#    plt.plot(bins,y,'r--')
#    plt.xlim(0.0,250)
#    plt.xlabel("Track number distribution range")
#    plt.ylabel('Playlist number')
#    plt.title(' Tracks number in playlist')
#    plt.show()

#    sns.set_style('dark')                # 该图使用黑色为背景色
#
#    sns.distplot(x, kde=False) # 不显示密度曲线
#
#    sns.axlabel('Birth number', 'Frequency') # 设置X轴和Y轴的坐标含义
#
#    sns.plt.show()
#    
#    sns.hls_palette('')
    font1 = {'family' : 'Times New Roman','weight' : 'normal','size'   : 23}

    sns.set_style('dark')
#    sns.axlabel("Track number distribution range")
#    sns.
    mpl.rc("figure", figsize=(12,8)) 
#    sns.axlabel("Track number distribution range",'Playlist number')
    sns_plot=sns.distplot(x,bins=100,kde_kws={"color":"black", "lw":1 }, hist_kws={"color":"blue" }) 
    fig = sns_plot.get_figure()
    plt.xlim(0.0,250)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Track number distribution range",fontsize=23)
    plt.ylabel('Frequency',fontsize=23)
    plt.title(' Tracks number in playlist',fontsize=23)
    fig.savefig("fig11.png")#数据分布的图片保存
    plt.show()
    return
# drawPic()




#绘制歌曲出现次数分布的情况
def drawTPic(output_dir):
    import seaborn as sns
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.rcParams['font.sans-serif'] = ['Times New Roman',23] #指定默认字体 
 
    x=pd.read_csv(os.path.join(output_dir,"NeedConcern/trickWithDetail.csv"))['track_uri']
    A=pd.value_counts(x)
#    mu =np.mean(x) #计算均值
#    sigma =np.std(x)
#    num_bins = 50 #直方图柱子的数量
#    n, bins, patches = plt.hist(x, num_bins,normed=1, facecolor='blue', alpha=0.5)
##直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
#    y = mlab.normpdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y 
#    plt.plot(bins, y, 'r--') #绘制y的曲线
#    plt.xlabel('tracks_num') #绘制x轴
#    plt.ylabel('Probability') #绘制y轴
#    plt.title(r'Histogram')#中文标题 u'xxx' 
#
#    plt.subplots_adjust(left=0.15)#左边距 
#    plt.show()
    sns.set_palette("hls") 
    mpl.rc("figure", figsize=(6,4)) 
    sns_plot=sns.distplot(A,bins=100,kde_kws={"color":"black", "lw":0.5 }, hist_kws={ "color": "b" }) 
#    sns_plot.xlabel('tracks_num') #绘制x轴
    fig = sns_plot.get_figure()
    fig.savefig("output_trick.png")#数据分布的图片保存
    return
#drawTPic()
def drawdoubleP():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.rcParams['font.sans-serif'] = ['Times New Roman',23] #指定默认字体 
    B=list(pd.read_csv("NeedConcern/Track_Occ.csv")['Occ_num'])
    a =  sorted(B,reverse=True)
    import random
    k=550
    s1=B
    x=[]
    y=[]
    while(k>0):
        k=k-50
        s1= random.sample(s1, k) #sum()
    #    print(k,sum(s1))
        x.append(k)
        y.append(sum(s1))
    y1=[i for i in x]
    plt.plot(x, y,label='Traditional way')
    plt.plot(x, y1,label='LSI_cache')
    plt.title('Analysis of user downloads from the server ')
    plt.xlabel('track size')
    plt.ylabel('download times')
    plt.legend()
    
    plt.show()
#drawdoubleP()
def drawdoublePP():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.rcParams['font.sans-serif'] = ['Times New Roman',23] #指定默认字体 
    B=list(pd.read_csv("NeedConcern/Track_Occ.csv")['Occ_num'])
    a =  sorted(B,reverse=True)
    x=range(1,len(a)+1)
    
    plt.plot(x, a,label='Traditional way')
    plt.title('Analysis of user downloads from the server ')
    plt.xlabel('track_id')
    plt.ylabel('download times')
#    plt.legend()
    plt.savefig("NeedConcern/output_trickNum.png")
    plt.show()
#drawdoublePP()
    





#drawTPic()
#x=pd.read_csv("../NeedConcern/trickWithDetail.csv")
#A=pd.value_counts(x)
#
#
#B=pd.DataFrame()
#B['Occ_num']=A
#B.to_csv("NeedConcern/Track_Occ.csv")





    #获取训练数据
    #>=200 34895
    #>=230 11308
    #>=240 5172
    #>=245 2589
    #>=250 374
    #>250   1
def getTrainData(minNum,validminNum,output_dir):
    AllData=pd.read_csv(os.path.join(output_dir,"tracksNumOfPlalist.csv"))
    myALLdata=AllData[AllData.tracks_num>=minNum]
    myALLdata=myALLdata[myALLdata.tracks_num<validminNum ]
    myALLdata.to_csv(os.path.join(output_dir,"NeedConcern/pidlist.csv"),index=False)
    validData=AllData[AllData.tracks_num>=validminNum]
    validData.to_csv(os.path.join(output_dir,"NeedConcern/validpidlist.csv"),index=False)
    return
#getTrainData(200,245)
def createTest(output_dir):
    tracksWithDetail=pd.read_csv(os.path.join(output_dir,"NeedConcern/trickWithDetail.csv"))[["track_uri","pid"]]
    v=pd.read_csv(os.path.join(output_dir,"NeedConcern/validpidlist.csv"))
    validData=list(v['pid'])
    seedN=[]
    GN=[]
    seeds={}
    goundtruth={}
    for p in validData:
        print(p)
        curTracks=set(tracksWithDetail[tracksWithDetail['pid']==p]["track_uri"])
        k=5*random.randint(0,16)  #5-80个种子
        while(k>=len(curTracks)):
            k=5*random.randint(0,16)   #5-80个种子
        seed=list(set(random.sample(curTracks, k)))
        less=list(curTracks-set(seed))
        seeds[p]=seed
        goundtruth[p]=less
        seedN.append(len(seed))
        GN.append(len(less))
    v["alreadHas"]=seedN
    v["needRec"]=GN
    v.to_csv(os.path.join(output_dir,"NeedConcern/1/validpidlist.csv"),index=False)
    with open(os.path.join(output_dir,'NeedConcern/validWithseed'), 'wb') as f:
        pickle.dump(seeds, f)
    with open(os.path.join(output_dir,'NeedConcern/validWithNeed'), 'wb') as f:
        pickle.dump(goundtruth, f)
    return
#createTest()

import json
import pandas as pd
import os
def is_english_char(ch):
    if ord(ch) not in (97,122) and ord(ch) not in (65,90):
        return False
    return True
title=["album_name","album_uri","artist_name","artist_uri","duration_ms","pos","track_name","track_uri","pid","pname","num_followers"]
inputpath=DATA_DIR_PATH
def readOneJson(myjsonname,pid):
    with open(myjsonname) as f1:
        temp = json.loads(f1.read())
        list1=[]
        playlist=list(filter(lambda arg: arg["pid"]==pid,temp['playlists']))[0]
        tracks = pd.DataFrame()
        count=0
        for track in playlist["tracks"]:
            tracks[count] = pd.Series(track)
            tracks.loc["pid"] = playlist["pid"]
            tracks.loc["pname"] =playlist["name"]
            tracks.loc["num_followers"]=playlist["num_followers"]
            count = count + 1
            list1.append(track["track_uri"])
        
        return list1,tracks
def f(pid):
    #mpd.slice.1000-1999.json
    s=(int(pid)//1000)*1000
    e=str(s+999)
    myJson= inputpath+"mpd.slice."+str(s)+"-"+e+".json"
    return readOneJson(myJson, pid)
def getFileLists(dflist):
    allneedURL=[]
    Alltracks = pd.DataFrame([], columns=title)
    for j in dflist:
        mylist,tracks=f(j)
        allneedURL.extend(mylist)
        Alltracks = pd.concat([Alltracks, tracks.T])
    allneedURL=list(set(allneedURL))
    pd.DataFrame(allneedURL, columns=["url"]).to_csv(os.path.join(OUTPUT_DIR_PATH,'NeedConcern/needConcernTrick.csv'),index=False)
    Alltracks.to_csv(os.path.join(OUTPUT_DIR_PATH,'NeedConcern/trickWithDetail.csv'),index=False)
    print("Done!")
    return 

  #readOneJson(r"mpd.slice.0-999.json",r"mpd.slice.0-999")
df1=pd.read_csv(os.path.join(OUTPUT_DIR_PATH,"NeedConcern/pidlist.csv"))
df2=pd.read_csv(os.path.join(OUTPUT_DIR_PATH,"NeedConcern/validpidlist.csv"))
df=pd.concat([df1,df2])
getFileLists(df["pid"].tolist())
