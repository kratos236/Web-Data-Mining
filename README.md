# Web Data Mining  网络数据挖掘
UCAS Web Data Mining Course   
1.Apriori-algorithm  
  1.1 candidate_gen 由k-1频繁集生成候补k-频繁集   
  1.2 scan_F 检验候选k-频繁集确定k-频繁集   
  1.3 generateRules 生成关联规则   
  
  测试情况：   
  the list is : [1, 2, 3, 4, 5]  
  the 1-frequent itemset is : [[1], [2], [3], [5]]  
  the 2-candaidate frequent itemset is : [[1, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 5]]  
  the 2-frequent itemset is : [[1, 3], [2, 3], [2, 5], [3, 5]]  
  the 3-candaidate frequent itemset is : [[2, 3, 5]]   
  the 3-frequent itemset is : [[2, 3, 5]]  
  [5] → [2] the conf_rate is 1.0  
  [2] → [5] the conf_rate is 1.0   
  [2, 3] → [5] the conf_rate is 1.0  
  [3, 5] → [2] the conf_rate is 1.0   
