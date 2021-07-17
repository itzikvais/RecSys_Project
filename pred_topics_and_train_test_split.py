# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:40:50 2018

@author: Administrator
"""
import numpy as np
import pandas as pd

import os
DATA_DIR_PATH = os.path.join(os.getcwd(),'part_data/')
OUTPUT_DIR_PATH =  os.path.join(os.getcwd(),'outputs/')
#得到训练集所有的pid
def getTop3(raw,n):
    t=raw.nlargest(n).index.values
    d={}
    for i in range(n):
        d['t'+str(i+1)]=t[i]
    return pd.Series(d)
   
def PidUnderTopic(raw,n):
    maintittle=['t'+str(i+1) for i in range(n) ]
    main=list(raw[maintittle].values)
#    del raw['t1','t2','t3']
    raw=raw.drop(maintittle)
    raw[list(set(raw.index)-set(main))]=-1
    return raw
def spiltTrainAndTest(n):
    takedata=pd.read_csv(os.path.join(OUTPUT_DIR_PATH,"doc_topic_116.csv"),index_col='pid')
    print(takedata.info)
    
#求主题
# playlistTopic["topic"]=playlistTopic.T.apply(lambda x:np.where(x==np.max(x))[0][0])
    playlistTopic=takedata.apply(lambda x:getTop3(x,n),axis=1)
    playlistTopic1=pd.concat([takedata,playlistTopic],axis=1)
    playlistTopic1.to_csv(os.path.join(OUTPUT_DIR_PATH,"DistributeAndMainTopic.csv"))#获得主题分布及3个主要主题
    #在不是主要主题的位置记为-1
    s=playlistTopic1.apply(lambda x:PidUnderTopic(x,n),axis=1)
    return s
#主要主题数由n决定
s=spiltTrainAndTest(1)
s.to_csv(os.path.join(OUTPUT_DIR_PATH,"Pid_Topic.csv"))#记录各个主题下有哪些pid
