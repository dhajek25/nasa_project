import pandas as pd
import numpy as np
from api_connection import nasa_neows

if __name__ == '__main__':
    object_data = nasa_neows()

def data_extraction():
    """The function that processes the response data from the API and extracts the required information from the dictionary"""
    data_values = pd.DataFrame()
    for key, values in object_data["near_earth_objects"].items():
        for i in values:
            name = {key: i["name"]}
            diameter = {key: i["estimated_diameter"]["kilometers"]["estimated_diameter_max"]}
            date_full = {key: i["close_approach_data"][0]["close_approach_date_full"]}
            miss_distance = {key: i["close_approach_data"][0]["miss_distance"]["astronomical"]}
            empty_df = pd.DataFrame()
            empty_df["name"] = (list(name.values()))
            empty_df["diameter"] = list(diameter.values())
            empty_df["date_full"] = list(date_full.values())
            empty_df["miss_distance"] = list(miss_distance.values())
            data_values = data_values.append(empty_df)
    return data_values

def data_preparation():
    data_values = data_extraction()

    # convert data to desired format and display
    data_values["date_full"] = pd.to_datetime(data_values["date_full"])
    data_values["miss_distance"] = pd.to_numeric(data_values["miss_distance"])
    data_values.sort_values(by=["miss_distance"], ascending=False, inplace=True)
    data_values.index = np.arange(1, len(data_values) + 1)
    return print(data_values.head())

if __name__ == '__main__':
    data_preparation()