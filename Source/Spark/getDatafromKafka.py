from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType
from kafka import KafkaConsumer
from pyspark.sql.functions import *
from pyspark.sql.types import *
#Khởi tạo spark session
if __name__ == "__main__":
    spark = (
        SparkSession.builder.appName("Kafka Pyspark Streaming Learning")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")

#Đọc dữ liệu từ Kafka
KAFKA_TOPIC_NAME = ""
KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
sampleDataframe = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVER)
        .option("subscribe", KAFKA_TOPIC_NAME)
        .option("startingOffsets", "latest")
        .load()
    )
base_df = sampleDataframe.selectExpr("CAST(value as STRING)", "timestamp")
base_df.printSchema()

#Xử lý dữ liệu
your_schema = StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("short_url", StringType(), True),
    StructField("short_description", StringType(), True),
    StructField("price", StringType(), True),
    StructField("list_price", StringType(), True),
    StructField("price", StringType(), True),
    StructField("rating_average", StringType(), True),
    StructField("review_count", StringType(), True),
])

extracted_df = base_df.select(from_json("value", your_schema).alias("data"), "timestamp")
extracted_df = extracted_df.select("data.*", "timestamp")

output_path = ".\\dataAfterFiltering.txt"
checkpoint_dir = ".\\checkpoint"
query = (
    extracted_df.writeStream
    .format("parquet")
    .option("path", output_path)
    .option("checkpointLocation", checkpoint_dir)
    .outputMode("append")
    .start()
)
query.awaitTermination()

