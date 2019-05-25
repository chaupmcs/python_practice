import multiprocessing as mp
import pandas as pd
import numpy as np
import time
import timeit

df = pd.read_pickle("/Users/minhchau/Downloads/my_blogs/data/X.pickle")
print(df.head())


def create_features(df):
    for i in range(200):
        df["age_gt_38"] = df.Age.map(lambda x: True if x > 38 else False)
        df["trivial"] = df[["Parch", "Sex", "SibSp"]].apply(lambda x: sum(x), 1)
    return df

def parallel_func(df, func, n_cores):
    df_split = np.array_split(df, n_cores)
    with mp.Pool(n_cores) as pool:
        res = pd.concat(pool.map(func, df_split))

    return res


message = "The execution time of {func} is {time}"
n_cores = 4

t_parallel_start = time.time()
res_1 =parallel_func(df, create_features, n_cores)
t_parallel_end = time.time()
parallel_time = t_parallel_end - t_parallel_start
print(message.format(func="parallel", time = parallel_time))

t_single_start = time.time()
res_2 = create_features(df)
t_single_end = time.time()
single_time = t_single_end - t_single_start
print(message.format(func="single", time = single_time))

print(res_1.shape, res_2.shape)
# The execution time of parallel is 2.0851922035217285
# The execution time of single is 3.303818941116333

