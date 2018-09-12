# Web_Data_Mining\<br>  
UCAS Web Data Mining Course\<br>  
1.Apriori-algorithm\<br>  
  1.1 candidate_gen 由k-1频繁集生成候补k-频繁集\<br>  
  1.2 scan_F 检验候选k-频繁集确定k-频繁集 \<br>  
  1.3 generateRules 生成关联规则\<br>  
  
  测试情况：\<br>  
  the list is : [1, 2, 3, 4, 5]\<br>  
  the 1-frequent itemset is : [[1], [2], [3], [5]]\<br>  
  the 2-candaidate frequent itemset is : [[1, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 5]]\<br>  
  the 2-frequent itemset is : [[1, 3], [2, 3], [2, 5], [3, 5]]\<br>  
  the 3-candaidate frequent itemset is : [[2, 3, 5]]\<br>  
  the 3-frequent itemset is : [[2, 3, 5]]\<br>  
  [5] → [2] the conf_rate is 1.0\<br>  
  [2] → [5] the conf_rate is 1.0\<br>  
  [2, 3] → [5] the conf_rate is 1.0\<br>  
  [3, 5] → [2] the conf_rate is 1.0\<br>  
