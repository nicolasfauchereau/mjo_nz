def select_season(data, season='NDJFM', complete=True, start = 1979, end = 2011):
    from calendar import monthrange
    """
    Select a season from data
    data must be a Pandas Series or DataFrame with a datetime index
    """
    
    ### defines the season dictionnary 
    seasdict = {'MJJAS':[5,9], 'NDJFM':[11,3]}
    
    ### defines the selector 
    selector = ((data.index.month >= seasdict[season][0]) | (data.index.month <= seasdict[season][1]))
    
    ### selects
    data = data[selector]
    
    ### if complete == True, we only select COMPLETE seasons 
    data = data.truncate(before='%s-%s-1' % (start, seasdict[season][0]),\
                   after='%s-%s-%s' % (end, seasdict[season][1], monthrange(end,seasdict[season][1])[1] ))
    
    return data