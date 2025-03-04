import matplotlib.pyplot as plt

def plot_position(long_values, lat_values):
    """ Plots given data as longitude as a function of latitude
    Parameters: lists of longitude and latitude data
    Returns: nothing
    """
    img = plt.imread("mapv1.jpg")    # reads in an image of a map of campus that will be used as the background of the plot
    fig, ax = plt.subplots()        # create figure 
    ax.imshow(img, extent = [-114.1320, -114.1304, 51.0787, 51.0795])    # set map image as background of plot, centered based on extreme values of latitude and longitude
    ax.plot(long_values, lat_values, marker = '.', ls = '--')        # add latitude and longitude data points with dashed line connecting them
    plt.title("DATA COLLECTED")        # add various titles for plot
    plt.xlabel("LONGITUDE")
    plt.ylabel("LATITUDE")
    plt.show()                        # display the plot

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

    for i in range(0,len(data),4):  #bestposa data
        
        data[i] = data[i].split(",")  # split each comma separated data/field
        data_dict[float(data[i][6])-587680] = [float(data[i][11]),float(data[i][12]) ]
        
        lat.append(float(data[i][11]))
        long.append(float(data[i][12]))

    for i in range(2,len(data),4):  #bestxyz data
        
        data[i] = data[i].split(" ")  # split each space for separated data/field
        
        x.append(float(data[i][7]))
        y.append(float(data[i][8]))
        z.append(float(data[i][9]))
    
    plot_position(long,lat)

# run main program
main()
