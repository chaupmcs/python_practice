import multiprocessing as mp


def f(x):
    print(x)
    return x

def main():
    with mp.Pool() as pool:
        m = pool.map(f, range(11,20))
        m_as = pool.map_async(f, range(10))
        # DO STUFF
        print("a")
        print("b")
        x= m_as.get()
        print("c")
        print("m=", m)
        print("m_as =", m_as)
        print("x =", x)
if __name__ == "__main__":
    main()
