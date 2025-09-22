import os
from pyspark.sql import SparkSession

os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11"

def create_spark_session():
    spark = SparkSession.builder \
        .appName("MySQL to Spark Batch Ingestion") \
        .master("local[*]") \
        .config("spark.jars.packages", "com.mysql:mysql-connector-j:8.0.33") \
        .getOrCreate()
    return spark

def read_data(spark):
    jdbc_url = "jdbc:mysql://localhost:3306/SupplyChain"
    table_name = "Dataset_base_updated"
    properties = {
        "user": "root",
        "password": "Kavi@123",
        "driver": "com.mysql.cj.jdbc.Driver"
    }
    df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=properties)
    return df

if __name__ == "__main__":
    spark = create_spark_session()
    df = read_data(spark)
    df.show(10)

    # ✅ Save as Parquet
    df.write.mode("overwrite").parquet("/Users/kavi/Downloads/Final Sem Project/stage_ingested.parquet")
    print("✅ Ingestion step completed and data saved to 'stage_ingested.parquet'")