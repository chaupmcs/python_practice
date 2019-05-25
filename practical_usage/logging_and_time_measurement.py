import logging
import time

logging.basicConfig(filename='../data/output/temp/logging_time_measure.log', level=logging.DEBUG)
logger = logging.getLogger()

def read_and_measure_time(path):
    """ return the contents of the file in path as well as measure the reading time """
    start_time = time.time()

    try:
        f = open(path, 'rb')
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} is {dt}".format(file = path, dt = dt))

path = "./../../../Downloads/gb_explainer.pdf"
read_and_measure_time(path)


