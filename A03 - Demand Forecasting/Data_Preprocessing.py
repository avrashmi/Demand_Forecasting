import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, date_format, coalesce

# Set Java environment
os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11"

# Start Spark session
spark = SparkSession.builder \
    .appName("Data Preprocessing") \
    .master("local[*]") \
    .getOrCreate()

# Read parquet file
df = spark.read.parquet("/Users/kavi/Downloads/Final Sem Project/stage_ingested.parquet")

# Parse both formats to timestamp
df = df.withColumn('parsed_date_full_year', to_timestamp(col('order date (DateOrders)'), "M/d/yyyy H:mm"))
df = df.withColumn('parsed_date_two_digit', to_timestamp(col('order date (DateOrders)'), "dd/MM/yy HH:mm"))

# Coalesce: pick the first non-null
df = df.withColumn('final_date', coalesce(col('parsed_date_full_year'), col('parsed_date_two_digit')))

# Filter out rows where parsing failed
df_cleaned = df.filter(col('final_date').isNotNull())

# Format final_date to the desired format
df_cleaned = df_cleaned.withColumn(
    'order date (DateOrders)',
    date_format(col('final_date'), 'yyyy-MM-dd HH:mm:ss')
)

# Drop helper columns
df_cleaned = df_cleaned.drop('parsed_date_full_year', 'parsed_date_two_digit', 'final_date')

# Save cleaned data
df_cleaned.write.mode("overwrite").parquet("/Users/kavi/Downloads/Final Sem Project/stage_preprocessed.parquet")
df_cleaned.write.mode("overwrite").csv("/Users/kavi/Downloads/Final Sem Project/stage_preprocessed.csv", header=True)

print("✅ Preprocessing complete! Dates are now in the format 'YYYY-MM-DD HH:MM:SS'.")