# ID: 2021220942
# NAME: 류종석
# File name: read_iris_v1.py
# Platform: Python 3.9.0 on Window 10 (PyCharm)
# Required Package(s): sys numpy pandas

##############################################################
# Template file for homework programming assignment 1
# Modify the first 5 lines according to your implementation
# This file is just for an example. Feel free to modify it.
##############################################################

import sys
import numpy as np
import pandas as pd

if len(sys.argv) < 2:
    print('usage: ' + sys.argv[0] + ' text_file_name')
else:
    # determine delimieter based on file extension - may be used by pandas
    # this is just to show how to use command line arguments.
    # any modification is accepted depending on your implementation.

    ##############################################################
    # WRITE YOUR OWN CODE LINES
    # - read header line
    # - read data and class labels
    # - compute mean and standard deviation
    # - disply them
    ##############################################################

    # csv 파일 일때
    # arg[1]에서 마지막 3글자가 csv이면
    if sys.argv[1][-3:].lower() == 'csv':
        delimeter = ','
        f = pd.read_csv(sys.argv[1], sep=delimeter, engine='python')

        # sepal_length 평균, 표준편차
        S_L1 = round(f[f.columns[0]].to_numpy().mean(), 2)
        S_L2 = round(f[f.columns[0]].to_numpy().std(), 2)

        # sepal_width 평균, 표준편차
        S_W1 = round(f[f.columns[1]].to_numpy().mean(), 2)
        S_W2 = round(f[f.columns[1]].to_numpy().std(), 2)

        # petal_length 평균, 표준편차
        P_L1 = round(f[f.columns[2]].to_numpy().mean(), 2)
        P_L2 = round(f[f.columns[2]].to_numpy().std(), 2)

        # petal_width 평균, 표준편차
        P_W1 = round(f[f.columns[3]].to_numpy().mean(), 2)
        P_W2 = round(f[f.columns[3]].to_numpy().std(), 2)

        # dataframe 생성
        df = pd.DataFrame({"sepal_length": [S_L1, S_L2], "sepal_width": [S_W1, S_W2], "petal_length": [P_L1, P_L2], "petal_width": [P_W1, P_W2]},
                          index=["mean", "std"])
        print("-----------------------------------------------------------")
        print(df)
        print("-----------------------------------------------------------")

    # txt 파일 일때
    else:
        delimeter = '[ \t\n\r]'  # default is all white spaces
        # read CSV/Text file with pandas
        f = pd.read_csv(sys.argv[1],sep=delimeter,engine='python')

        # SL 평균, 표준편차
        SL1 = round(f["SL"].to_numpy().mean(), 2)
        SL2 = round(f["SL"].to_numpy().std(), 2)

        # SW 평균, 표준편차
        SW1 = round(f["SW"].to_numpy().mean(), 2)
        SW2 = round(f["SW"].to_numpy().std(), 2)

        # PL 평균, 표준편차
        PL1 = round(f["PL"].to_numpy().mean(), 2)
        PL2 = round(f["PL"].to_numpy().std(), 2)

        # PW 평균, 표준편차
        PW1 = round(f["PW"].to_numpy().mean(), 2)
        PW2 = round(f["PW"].to_numpy().std(), 2)

        # dataframe 생성
        df=pd.DataFrame({"SL":[SL1,SL2],"SW":[SW1,SW2],"PL":[PL1,PL2],"PW":[PW1,PW2]}, index=["mean","std"])

        # pdf와 통일하기 위함
        print("-----------------------------------------------------------")
        print("\t       ",df.columns[0],"\t    ",df.columns[1],"\t  ",df.columns[2],"\t       ",df.columns[3])
        print(df.index[0],"\t     ",df.values[0][0],"\t  ",df.values[0][1],"\t",df.values[0][2],"\t     ","%.2f"%df.values[0][3])
        print(df.index[1], "\t     ", df.values[1][0], "\t  ", df.values[1][1], "\t", df.values[1][2], "\t     ","%.2f" % df.values[1][3])
        print("-----------------------------------------------------------")
