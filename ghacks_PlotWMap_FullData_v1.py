import matplotlib.pyplot as plt

def plot_position(long_values, lat_values):
    """ Plots given data as longitude as a function of latitude
    Parameters: lists of longitude and latitude data
    Returns: nothing
    """
    img = plt.imread("mapv1.jpg")
    fig, ax = plt.subplots()
    ax.imshow(img, extent = [-114.1320, -114.1304, 51.0787, 51.0795])
    ax.plot(long_values, lat_values, marker = '.', ls = '--')
    plt.title("DATA COLLECTED")
    plt.xlabel("LONGITUDE")
    plt.ylabel("LATITUDE")
    plt.show()

def smooth(lat, long, v):
    """
    remove outliers from list of data by averaging 10 data points and removing those that are past the threshold
    return: list
    """
    newlat = lat
    newlong = long
    counter = 0
    for i in range(len(v)):
        if v[i]<6366330 or v[i]>6366334.5:
            newlat.pop(i-counter)
            newlong.pop(i-counter)
            counter+=1

    return newlat, newlong


def main():
    """
    Main, gets filename from command line argument (or prompts if not included), reads file into dictionary, then executes contact list categorization
    :return: None
    """
    file = open("updated-data.txt")
    data = file.read()
    file.close()
    
    # Turn file into a list
    data = data.splitlines()  # create a list that separates items per line (\n)
    
    # Make dict from file, list of latitudes and longitudes in the order they were recorded
    data_dict = {}

    lat = []
    long = []
    x = []
    y = []
    z = []
    v = []

    for i in range(0,len(data),4):  #bestposa data
        
        data[i] = data[i].split(",")  # split each comma separated data/field
        #data_dict[float(data[i][6])-587680] = [float(data[i][11]),float(data[i][12]) ]
        
        lat.append(float(data[i][11]))
        long.append(float(data[i][12]))

    for i in range(2,len(data),4):  #bestxyz data
        
        data[i] = data[i].split(" ")  # split each space for separated data/field
        
        x_value = float(data[i][7])
        y_value = float(data[i][8])
        z_value = float(data[i][9])

        x.append(x_value)
        y.append(y_value)
        z.append(z_value)

        v_value = (x_value**2+y_value**2+z_value**2)**0.5
        v.append(v_value)

        #print(float(data[i][7]),float(data[i][8]),float(data[i][9]),"\n")
    
    print(v)

    newlat, newlong = smooth(lat,long,v)


    plot_position(newlong, newlat)
    #plt.plot(range(len(v)),v)
    plt.show()

main()


"""
updated-data.txt
"""