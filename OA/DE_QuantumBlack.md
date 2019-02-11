# QA Preparation for DE - QuantumBlack
## 2/9/2019

## Arrays
Array - Sorting
      - Two pointers - one-way two pointesrs - windows
                                             - sub-array
                     - two-way two pointers
      - 2-D Array    - Flip
                     - Rotation
      - Implementation
      - Math algorithms


## Trees

## BFS

## DFS

## Binary Search
Binary search - Judgement/Edge conditions
              - Implementation - Recursive
                               - Iterative
              - Rotate
              - Sub-array
              - 2-D array
```python
def binarySearch(arr, l, r, x):
    """
    recursive version - O(log n), O(log n)
    """
    if r >= l:
        mid = l + (r - l) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def binarySearch(arr, l, r, x):
    """
    iterative version - O(log n), O(1)
    """
    while l < r:
        mid = l + (r - l) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1
```

## Input/Output
### csv pacakge
* read

```python
import csv
with open('*.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            colmn_names = row # list
            line_count += 1
        else:
            data = row # list
    print(f'Processed {line_count} lines.')
```

* write

```python
import csv
with open('*.csv', mode='w') as csv_file:
    csv_writer = csv.writer(  csv_file
                            , delimiter=','
                            , quotechar='"'
                            , quoting=csv.QUOTE_MINIMAL
                           )

    csv_writer.writerow(['John Smith', 'Accounting', 'November'])
    csv_writer.writerow(['Erica Meyers', 'IT', 'March'])
```

### Pandas package
* read

```python
import pandas as pd
df = pd.read_csv('*.csv')
df = pd.read_csv('*.csv', index_col='index_col')
df = pd.read_csv('*.csv', index_col='index_col', parse_dates=['date_col'])
df = pd.read_csv( '*.csv'
                , index_col = index_col_name
                , parse_dates = date_col_list
                , header = 0
                , names = col_names_list
                )
```

* write

```python
import pandas as pd
df.to_csv('*.csv')
```

## Questions
1. 给一个数列，找后一个数和前一个数的最大的差。
```python
def max_dff(xs):
    """
    brute force - O(n^2), O(1)
    """
    n = len(xs)
    if n < 2: return -1

    max_value = xs[1] - xs[0]
    for i in range(2, n):
        for j in range(0, i):
            if xs[i] - xs[j] > max_value:
                max_value = xs[i] - xs[j]
    return max_value
```

```python
def maxDiff(xs):
    """
    record both max_dff and min_element - O(n), O(1)
    """
    n = len(xs)
    if n < 2: return -1

    max_diff = xs[1] - xs[0]
    min_element = min(xs[0], xs[1])

    for i in range(2, n):
        if (xs[i] - min_element > max_diff):
            max_diff = xs[i] - min_element

        if (xs[i] < min_element):
            min_element = xs[i]
    return max_diff
```

2. 用给定的公式，根据前n天的数据，写一个function计算从第n天开始往后计算一些东
  * Time series
    * https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
    *

3. ML
4. 提供根据顺序写程序使任意数据按此规律排序
5. Statistic
6. ML
7. 给了一个表格，有一些金融相关的index并且告诉你怎么算，让你写一个函数把指定的东西算出来并且output成CSV
8. ML: 294 feature columns 6 label columns
9. 告诉你一段时期的气温，然后让你预测另一个时段期的气温，没有数据，完全是考coding逻辑，其它两道题也相似，没有数据，就让你coding解决问题
  * https://stackabuse.com/using-machine-learning-to-predict-the-weather-part-1/
  * https://stackabuse.com/using-machine-learning-to-predict-the-weather-part-2/
  * https://machinelearningmastery.com/time-series-forecast-study-python-monthly-sales-french-champagne/

10. 二分查找
11. Time series
12. Leetcode 200, 岛之间的最短距离
```python

```
13. 两个湖之间挖 canal的最短距离（dfs 标记+bfs 找路径）， m*n 矩阵，0是湖/2， 1是路，最少的1=>0使得湖联通
14. lc的trapping rain water 变形.
15. supposed that your team has two separate solutions to solve a problem. In 3-5 sentences, write an email about how do you approach your manager to discuss his/her perspective on these two ideas? 就是说你们组内讨论，无法得出统一结论，让你发个邮件给manager，请求延期交付。
16. list array
17. SQL
