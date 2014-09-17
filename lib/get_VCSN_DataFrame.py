def get_VCSN_DataFrame(dpath='/data/VCSN/', fname='VCSN_Rain.nc', start=1972, end=2011):
    """
    Get the VCSN dataset, returns a Pandas DataFrame with a datetime index

    """
    nc = Dataset(os.path.join(dpath,fname))

    ### ==============================================================================================================
    ### get the data
    time =  nc.variables['Matlab_date_Number'][:]
    lat =  nc.variables['latitude'][:]
    lon =  nc.variables['longitude'][:]
    agent =  nc.variables['agent'][:]
    elevation =  nc.variables['elevation'][:]
    rain = nc.variables['Rain'][:,:]

    nc.close()

    data = pd.DataFrame(rain, index = pd.date_range(start='1972-1-1',end='2011-12-31'))
    
    data = data.truncate(before="%s-1-1" % ( start ), after= "%s-12-31" % ( end ))
    
    return data