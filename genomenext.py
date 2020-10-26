import time
import pandas as pd

start_time = time.time()

s1 = pd.read_csv('sample1_depths.txt', delimiter = '\t')
s2 = pd.read_csv('sample2_depths.txt', delimiter = '\t')
s3 = pd.read_csv('sample3_depths.txt', delimiter = '\t')

print 'Elapsed time is ', time.time() - start_time, ' seconds'