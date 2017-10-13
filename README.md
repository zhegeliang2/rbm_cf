# rbm_cf

sample_ipyb.py试验了Metropolis-Hastings算法生成正态分布，个人理解，有以下几个注意点：
1. metropolis函数使用的建议分布是均匀分布，使用这个分布的好处是1. 机器可以自动生成；2. aij=min{1, (q_ji*p_j/q_ij*p_i)}，其中q_ij和q_ji在建议分布中是相等的，因此aij仅仅是aij=min{1, p_j/p_i}；另外一个常使用的建议分布是选取以y_{i-1}为均值的正太分布
2. metropolis-hasting使用的是普通的正太分布

