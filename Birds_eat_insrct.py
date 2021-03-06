'''
Question:
  There is a bird that can only go forward one step or two steps at a time. There are now 2*m steps. 
  There are different numbers of insects on each step. The bird walks forward and what is maximum insects
  will the bird eat as possible.
'''

# -*- coding:utf-8 -*-
# author: wanshan

# time cost: O(m^2)
# sapce cost: O(m)

def get_maximum_insects(feed_list, m){
  
  if len(feed_list) < 1 or len(feed_list) != 2*m:
    return 0
  
  # initial for the first two steps(step, cur_get)
  pre_1 = {0:0}
  pre_2 = {1: feed_list[1]}
  cur_get_set = {}
  
  # res
  max_res = 0
  
  for i in range(1, 2*m):
    for x1 in pre_1.keys():
      if x1 > m-1:
        continue
      else:
        if x1 in pre_2.keys():
          cur_get_set[x1+1] = max(pre_1[x1], pre_2[x1]) + feed_list[i]
          
    for x2 in pre_2.keys():
      if x2 > m-1:
        continue
      else:
        if x2 not in pre_1.keys():
          cur_get_set[x2+1] = pre_2[x2] + feed_list[i]

    for x3 in cur_set.keys():
      if x3 == m:
        if cur_set[x3] > max_get:
          max_res = cur_get_set[x3]
       
    pre_1 = pre_2
    pre_2 = cur_get_set
    cur_get_set = {}
  
  return max_res
}


if __name__ == '__main__':
pass
