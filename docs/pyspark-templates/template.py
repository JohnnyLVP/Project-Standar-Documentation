from pyspark.sql import SparkSession

def init_spark_session(appName = 'pyspark-template'):

	spark = SparkSession.builder.appName(appName).getOrCreate()

	return spark

def get_dataframe(spark,filename = ''):

	df = spark.read.csv(filename, header = True)

	return df

def write_dataframe(df, filename = ''):

	df.write.parquet()



filename = 'iris.csv'

sparksession = init_spark_session()

df = get_dataframe(sparksession,filename)

df.write.parquet('~\\Documents\\datos')

