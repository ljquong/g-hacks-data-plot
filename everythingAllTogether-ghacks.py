import matplotlib.pyplot as plt

def plot_position(long_values, lat_values, new_long, new_lat):
    """ Plots given data as longitude as a function of latitude
    Parameters: lists of longitude and latitude data
    Return: nothing
    """
    img = plt.imread("mapv1.jpg")       # reads in an image of a map of campus that will be used as the background of the plot
    fig, ax = plt.subplots()        # create figure 
    ax.imshow(img, extent = [-114.1320, -114.1304, 51.0787, 51.0795])       # set map image as background of plot, centered based on extreme values of latitude and longitude
    ax.plot(long_values, lat_values, marker = '.', ls = '--')           # add latitude and longitude data points with dashed line connecting them
    plt.plot(new_long, new_lat)                                     # add processed latitude and longitude data in a different colour
    plt.legend(['RAW DATA', 'PROCESSED DATA'], loc = 'center')      # create legend
    plt.title("DATA COLLECTED", fontsize = 30)                      # add various titles for plot
    plt.xlabel("LONGITUDE")
    plt.ylabel("LATITUDE")
    plt.show()                                                      # display plot

def smooth(lat, long, v):
    """
    remove outliers, caused by gnss interference, from list of latitudes and longitudes data points by removing those which have velocities that are past the threshold
    Return: list
    """
    newlat = lat.copy()  # generate copy of raw latitude data to be modified
    newlong = long.copy()   # generate copy of raw longitude data to be modified
    counter = 0              # counter number of removed items
    for i in range(len(v)):  # evaluate each velocity
        if v[i]<6366330 or v[i]>6366334.5:  # if the velocity surpasses threshold within 6366330 and 636634.5, assume gnss interference
            newlat.pop(i-counter)   # remove latitude value at this instance
            newlong.pop(i-counter)  # remove latitude value at this instance
            counter+=1              # increase the counter for removed items
    return newlat, newlong          # return new list of processed latitude and longitude data 

def main():
    """
    reads data, convert to lists, process data, then display in plot
    Return: None
    """
    file = open("updated-data.txt")  # open updated-data.txt, the file of recorded data
    data = file.read()     # read the file
    file.close()           # close the file
    
    # Turn file into a list
    data = data.splitlines()  # create a list that separates items per line (\n)
    
    # Parse lists of latitudes, longitudes, and velocities in the order they were recorded from data 
    lat = []
    long = []
    v = []

    for i in range(0,len(data),4):  # identify the bestposa data
        data[i] = data[i].split(",")  # split each comma separated data/field
        lat.append(float(data[i][11]))  # append each latitude into lat list
        long.append(float(data[i][12]))  # append each longitude into long list

    for i in range(2,len(data),4):  # identify the bestxyz data
        data[i] = data[i].split(" ")  # split each space for separated data/field
        x_value = float(data[i][7])  # identify velocity in x value
        y_value = float(data[i][8])  # identify velocity in y value
        z_value = float(data[i][9])  # identify velocity in z value

        v_value = (x_value**2+y_value**2+z_value**2)**0.5 # calculate velocity
        v.append(v_value)                             # append each velocity into v list
    
    newlat, newlong = smooth(lat,long,v)  # process latitude and longitude values using velocity values in smooth function
    plot_position(long,lat,newlong,newlat)  # display plot of raw values and processed values in plot_position function
    
main()
