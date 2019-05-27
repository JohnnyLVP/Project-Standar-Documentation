from pyspark.sql import SparkSession

def init_spark_session(appName = 'pyspark-template'):

	spark = SparkSession.builder.appName(appName).getOrCreate()

	return spark

def get_dataframe(spark,filename = ''):

	df = spark.read.csv(filename, header = True)

	df.show()


filename = 'iris.csv'

sparksession = init_spark_session()

get_dataframe(sparksession,filename)