import pandas as pd
allSeasons = pd.read_csv("data/fangraphs/seasons.csv")

def wOBA(BB, HBP, H, doubles, triples, HR, AB, IBB, SF, season):
    thisSeason = allSeasons.loc("Season" == season)
    return thisSeason.wBB * BB
