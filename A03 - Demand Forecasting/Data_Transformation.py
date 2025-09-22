import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11"

spark = SparkSession.builder \
    .appName("Data Transformation") \
    .master("local[*]") \
    .getOrCreate()

df_cleaned = spark.read.parquet("/Users/kavi/Downloads/Final Sem Project/stage_preprocessed.parquet")

transformed_df = df_cleaned

transformed_df.show(10)

# ✅ Save as Parquet
transformed_df.write.mode("overwrite").parquet("/Users/kavi/Downloads/Final Sem Project/stage_transformed.parquet")
transformed_df.write.mode("overwrite").csv("/Users/kavi/Downloads/Final Sem Project/stage_transformed.csv", header=True)
print("✅ Transformation step completed and data saved to 'stage_transformed.parquet'")