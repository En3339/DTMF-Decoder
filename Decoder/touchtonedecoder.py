# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:30:02 2020

@author: En Lu & Zhengyang Li
"""
import numpy as np

#Load time domain data
Data_timedomain = np.loadtxt('touchtones.dat',usecols=(1))
Fs=1000

#Signal Cut,get 2 arrays which indicates the signal part
#'A[Start[0]:End[0]]' means the 1st signal cut, etc.
def signal_cut(A):    
    global Start
    global End
    Start=[]
    End=[]  
    i=0
    flag=0
    while  i<(len(A)-50): 
        i=i+1
        if abs(A[i+1]-A[i])>=100 and flag==0:
            Start.append(i)
            flag=1
            i=i+1
        if  abs(A[i]-3232)<3 and abs(A[i+10]-3232)<3 and abs(A[i+20]-3232)<3 and abs(A[i+30]-3232)<3 and abs(A[i+40]-3232)<3  and flag==1:
            End.append(i)
            flag=0
            i=i+1
        
    return


# define detect functions to detect 2 Frequencies peaks.
# A is the abs of frequency domain data,B is frequency space
# P1,P2 are 2 peaks
def Finding_peaks(A,B):
    i=2;
    global a
    global b
    a=0
    b=0
    while i < len(A)-3:
        if A[i]>95 and A[i]>A[i-1] and A[i]>A[i+1] and A[i-1]>A[i-2]and A[i+1]>A[i+2]:
            if a==0:
                a=B[i];
            if a!=0:
                b=B[i];              
        i=i+1;
    return a
    return b
        
#num detect
#applying 2 frequency peaks to detect number.
def Num_detect(a,b):
    global num
    if 49<a<69 and 326<b<346:
        num='0';
    if 138<a<158:
        if 199<b<219:
            num='7'
        if 326<b<346:
            num='8'
        if 467<b<487:
            num='9'
    if 199<a<219:
        if 220<b<240:
            num='4'
        if 293<b<313:
            num='1'
    if 220<a<240:
        if 326<b<346:
            num='5'
        if 467<b<487:
            num='6'
    if 293<a<313:
        if 326<b<346:
            num='2'
        if 467<b<487:
            num='3'
    print(num)
    


#FFT, in order to get abs of Data frequencydomain and frequency space
def Fftsignal(A):
    global Data_frequencydomain
    global freq_space
    Data_frequencydomain = abs(np.fft.fft(A))
    freq_space = np.arange(0, Fs, Fs/(len(Data_frequencydomain)))
    Data_frequencydomain = Data_frequencydomain[1:len(Data_frequencydomain)//2]
    freq_space=freq_space[1:len(freq_space)//2]
    Data_frequencydomain = 10*np.log(Data_frequencydomain)
    return Data_frequencydomain 
    return freq_space

#Digit Detect is the combination of Finding_peaks(A,B) & num_detect(a,b)
def Digit_detect(C): 
    Fftsignal(C)
    Finding_peaks(Data_frequencydomain,freq_space)
    Num_detect(a,b)
    
# Main program
signal_cut(Data_timedomain)
k=0
while k<len(Start):
    Signalchunk_timedomain=Data_timedomain[Start[k]:End[k]]  
    Digit_detect(Signalchunk_timedomain)   
    k=k+1
    