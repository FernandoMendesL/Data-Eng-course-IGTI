#teste
from pyspark.sql.functions import min, max, mean, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://fernando-lake-bucket/raw-data/enem/")
    
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://fernando-lake-bucket/customer-zone/enem/")
)
#spark-submit --master yarn --deploy-mode cluster s3://fernando-lake-bucket/emr_code/pyspark/job_spark.py