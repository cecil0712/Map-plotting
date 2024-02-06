# 6/2/2024 20:11
import data,folium

def save_address(address_list):
    geo_dict = {}
    key=input("enter the key: ")
    for add in address_list:
        la,lo=data.get_data(add,key)
        geo_dict[add]=[la,lo] # save the name of place and the coodinate to a dict
        # with the format of {place:[latitude,longitude]}
    return geo_dict

def plot(geo_dict):
    geo=list(geo_dict.items()) # get all the data inside the dict
    for i in geo:
        fmap = folium.Map(location=[i[1][0], i[1][1]], zoom_start=17) # show the map information of the coordinate
        fmap.add_child(folium.Marker(location=[i[1][0], i[1][1]],
                                     popup=i[0])) # add a marker on that coordinate with name of place
