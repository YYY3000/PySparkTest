from pyspark import SparkContext

test_file_name = "E:\\test.txt"

# Word Count  
sc = SparkContext("local", "WordCount")
# text_file rdd object  
text_file = sc.textFile(test_file_name)
print(text_file.collect())

# counts
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
print(counts.collect())
