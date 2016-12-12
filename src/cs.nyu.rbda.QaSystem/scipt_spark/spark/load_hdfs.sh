# this file put glove embedding file into hdfs
cat squadInput/glove.txt
hdfs dfs -put squadInput
hdfs dfs -ls squadInput
