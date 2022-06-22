import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from concurrent import futures
import numpy as np
from scipy.stats import gaussian_kde
import pandas_datareader.data as web
data_dir = "./data/most_attractive_stocks"
os.makedirs(data_dir, exist_ok=True)