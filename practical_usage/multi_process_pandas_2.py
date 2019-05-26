"""
    Created by chaupm at 2019-05-26
"""

import multiprocessing as mp
import pandas as pd
import numpy as np
import time
import glob
import os

def chunks(arr, n):
    """Yield successive n-sized chunks from arr."""
    for i in range(0, len(arr), n):
        yield arr[i:i + n]

def get_list_files_in_folder(path, file_type="parquet"):
    file_paths = glob.glob(os.path.join(path, ("*." + file_type)))
    if len(file_paths) > 0:  # one level - do nothing
        pass
    else:
        sub_folder_paths = glob.glob(os.path.join(path, "*"))
        for p in sub_folder_paths:
            file_paths += get_list_files_in_folder(p)
    return file_paths


data_path = "./files/"

def find_func(path_list):
    merge_df = pd.read_csv("../file_test.csv")
    res_list = list()
    for path in path_list:
        df = pd.read_csv(path)
        res = pd.merge(merge_df, df["x"], on="x", how="inner")
        if len(res) > 0:
            res_list.append(res)
    return pd.concat(res_list)


def parallel_func(func, n_cores):
    file_path_list = get_list_files_in_folder(data_path, "csv")

    with mp.Pool(n_cores) as pool:
        parallel_res = pool.map(func, chunks(file_path_list, n_cores))
        if len(parallel_res) > 0:
            res = pd.concat(parallel_res).reset_index(drop=True)
            # res.to_csv()
        else:
            res = []
            print("Null !!!")
    return res


n_cores = 2
parallel_func(find_func, n_cores)

