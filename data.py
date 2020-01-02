import pandas as pd 
import numpy as np

# Compile relevent statistics into individual vectors for each school and put into a dictinonary

def CreateDataDictionary():

    MM = []
    for year in range(1993, 2020, 1):
        dataset = pd.read_csv("Data/MMStats/MMStats_"+str(year)+".csv")
        Teams = dataset['School'].tolist()
        Games = dataset['G'].tolist()
        WinPCT = dataset['W.L.'].tolist()
        FGPCT = dataset['FG.'].tolist()
        FG3PCT = dataset['X3P.'].tolist()
        FTPCT = dataset['FT.'].tolist()
        TRB = dataset['TRB'].tolist()
        AST = dataset['AST'].tolist()
        STL = dataset['STL'].tolist()
        BLK = dataset['BLK'].tolist()
        TOV = dataset['TOV'].tolist()
        for entry in range (0, len(dataset), 1):
            MM += [[Teams[entry], year, Games[entry], round(WinPCT[entry], 3), round(FGPCT[entry], 3), 
            round(FG3PCT[entry], 3), round(FTPCT[entry], 3), round(TRB[entry]/Games[entry], 2), round(AST[entry]/Games[entry], 2), 
            round(STL[entry]/Games[entry], 2), round(BLK[entry]/Games[entry], 2), round(TOV[entry]/Games[entry], 2)]]

    RS = []
    for year in range(1993, 2020, 1):
        dataset = pd.read_csv("Data/RatingStats/RatingStats_"+str(year)+".csv")
        Teams = dataset['School'].tolist()
        Rank = dataset['Rk'].tolist()
        Wins = dataset['W'].tolist()
        Losses = dataset['L'].tolist()
        ORtg = dataset['ORtg'].tolist()
        DRtg = dataset['DRtg'].tolist()
        for entry in range (0, len(dataset), 1):
            RS += [[Teams[entry], year, Rank[entry], Wins[entry], Losses[entry], ORtg[entry], DRtg[entry]]]

    MM.sort()
    RS.sort()

    MS = [ [' ', [ ] ] ] 
    for row in range(0, len(RS), 1):
        if RS[row][0] != MS[-1][0]:
            MS += [ [ RS[row][0], [ RS[row][1], RS[row][2], MM[row][2], RS[row][3], RS[row][4], MM[row][3], MM[row][4], MM[row][5], MM[row][6], 
                MM[row][7], MM[row][8], MM[row][9], MM[row][10], RS[row][5], RS[row][6] ] ] ]
        else: 
            MS[-1] += [[ RS[row][1], RS[row][2], MM[row][2], RS[row][3], RS[row][4], MM[row][3], MM[row][4], MM[row][5], MM[row][6], 
                MM[row][7], MM[row][8], MM[row][9], MM[row][10], RS[row][5], RS[row][6] ]]
    
    MS = MS[1:]

    dict = {t[0]:t[1:] for t in MS}
    keys = list(dict.keys())
    for i in keys:
        dict[i] = {t[0] : t[1:] for t in dict[i]}      

    return dict 
