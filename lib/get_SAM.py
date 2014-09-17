def get_SAM(url='ftp://ftp.cpc.ncep.noaa.gov/cwlinks/norm.daily.aao.index.b790101.current.ascii',start=1979, end=2012):
    data = pd.read_table(url, header=None, sep="\s*", 
                         names=['year','month','day','sam'])
    data.index = pd.date_range(start="1979-1-1", periods=len(data))
    data = data.truncate(before="%s-1-1" % ( start ), after= "%s-12-31" % ( end ))
    data.fillna(data.mean(), inplace=True)
    return data