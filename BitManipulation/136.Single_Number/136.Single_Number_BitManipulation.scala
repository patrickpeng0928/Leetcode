def singleNumberFoldLeft(nums: Array[Int]): Int = nums.foldLeft(0)(_ ^ _)

def singleNumberReduce(nums: Array[Int]): Int = nums.reduce(_ ^ _)

