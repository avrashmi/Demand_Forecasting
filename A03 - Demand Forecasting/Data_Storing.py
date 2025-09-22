import os
from pyspark.sql import SparkSession

os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11"

spark = SparkSession.builder \
    .appName("Data Storing") \
    .master("local[*]") \
    .config("spark.jars.packages", "com.mysql:mysql-connector-j:8.0.33") \
    .getOrCreate()

df_transformed = spark.read.parquet("/Users/kavi/Downloads/Final Sem Project/stage_transformed.parquet")

jdbc_url = "jdbc:mysql://localhost:3306/SupplyChain"
target_table = "Dataset_cleaned_final"
properties = {
    "user": "root",
    "password": "Kavi@123",
    "driver": "com.mysql.cj.jdbc.Driver"
}

df_transformed.show(10)

df_transformed.write.jdbc(url=jdbc_url, table=target_table, mode="overwrite", properties=properties)

# ✅ Also save as Parquet
df_transformed.write.mode("overwrite").parquet("/Users/kavi/Downloads/Final Sem Project/stage_final_output.parquet")
df_transformed.write.mode("overwrite").csv("/Users/kavi/Downloads/Final Sem Project/stage_final_output.csv", header=True)
print("✅ Data successfully written to MySQL and saved to 'stage_final_output.parquet'")