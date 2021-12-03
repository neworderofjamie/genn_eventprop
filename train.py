from simulator import *
import matplotlib.pyplot as plt
import numpy as np

p["DT_MS"]= 0.1
p["ETA"]= 5e-3
p["N_BATCH"]= 64
p["N_TRAIN"]= 1000*p["N_BATCH"]
p["W_REPORT_INTERVAL"]= 3000
p["N_EPOCH"]= 50
spike_t, spike_ID, rec_vars_n, rec_vars_s= run_yingyang(p)
