import pandas as pd
import numpy as np
import math
from scipy import stats

chat_id = 776430833# Your chat ID, do not change the name of the variable

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    # Set the significance level alpha to 0.06
    alpha = 0.06
    # Call the z_test_prop function to perform the hypothesis test
    reject_null = z_test_prop(y_cnt, x_success/x_cnt, y_success/y_cnt, alpha)
    # Return the result
    return reject_null

def z_test_prop(n_test, p_control, p_test, alpha):
    # Calculate the pooled proportion
    p_pool = (n_test * p_test + 1000 * p_control) / (n_test + 1000)
    # Calculate the test statistic Z
    z = (p_test - p_control) / math.sqrt(p_pool * (1 - p_pool) * (1/n_test + 1/1000))
    # Calculate the critical Z-value for a one-tailed test at the significance level alpha
    z_crit = abs(stats.norm.ppf(alpha, loc=0, scale=1))
    # Compare the absolute value of Z to the critical Z-value to determine whether to reject the null hypothesis
    return abs(z) > z_crit
