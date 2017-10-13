# rbm_cf

mh.py试验了Metropolis-Hastings算法生成正态分布，主要有以下几个注意点：
1. 建议分布是均匀分布，使用这个分布的好处是aij=min{1, (q_ji*p_j/q_ij*p_i)}，其中q_ij和q_ji在建议分布中是相等的，因此aij仅仅是aij=min{1, p_j/p_i}
