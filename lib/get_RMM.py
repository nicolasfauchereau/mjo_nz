def get_RMM(url='http://cawcr.gov.au/staff/mwheeler/maproom/RMM/',fname='RMM1RMM2.74toRealtime.txt',start=1979, end=2011):
    """
    # Function to load the MJO index(es) from Wheeler and Hendon (RMM1 and RMM2) from the URL
    
    """
    data = pd.read_table('%s%s' % (url, fname), sep='\s*', skiprows=2, header=None, \
                           names = ['year','month','day','RMM1', 'RMM2', 'MJO phase', 'amplitude', 'origin'])
    dates = [datetime(y,m,d) for y,m,d in zip(data.year, data.month, data.day)]
    data.index = dates
    data = data.truncate(before="%s-1-1" % ( start ), after= "%s-12-31" % ( end ))
    return data