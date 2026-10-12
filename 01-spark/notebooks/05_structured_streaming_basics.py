# Databricks notebook source
# MAGIC %md
# MAGIC # Structured Streaming Basics
# MAGIC
# MAGIC **Goal:** learn streaming concepts using a file stream, which works well for Databricks Community Edition.
# MAGIC
# MAGIC Topics covered:
# MAGIC - Streaming DataFrames
# MAGIC - File source
# MAGIC - Checkpoints
# MAGIC - Output modes
# MAGIC - Triggers
# MAGIC - Watermarks
# MAGIC - Late data thinking
# MAGIC - Query progress

# COMMAND ----------

from datetime import datetime
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

base_path = "/tmp/modern_data_architecture_lab/structured_streaming"
input_path = f"{base_path}/input"
checkpoint_path = f"{base_path}/checkpoint"
output_path = f"{base_path}/output"

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Reset the Learning Paths
# MAGIC
# MAGIC This clears the notebook's temporary streaming folders.

# COMMAND ----------

dbutils.fs.rm(base_path, recurse=True)
dbutils.fs.mkdirs(input_path)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Define the Event Schema
# MAGIC
# MAGIC Streaming reads should use an explicit schema. Inferring schema repeatedly is inefficient and can be unsafe.

# COMMAND ----------

event_schema = StructType([
    StructField("event_id", StringType(), False),
    StructField("customer_id", StringType(), True),
    StructField("event_type", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("event_ts", TimestampType(), True),
])

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Create the Streaming DataFrame
# MAGIC
# MAGIC `readStream` defines a streaming source. It does not start running until `writeStream.start()` is called.

# COMMAND ----------

events_stream = (
    spark.readStream
    .schema(event_schema)
    .json(input_path)
)

events_stream.isStreaming

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Add a Stateful Aggregation with Watermark
# MAGIC
# MAGIC Watermarks tell Spark how long to wait for late data before finalizing old state.
# MAGIC
# MAGIC This example groups purchase revenue into 5-minute windows.

# COMMAND ----------

windowed_revenue = (
    events_stream
    .filter(F.col("event_type") == "purchase")
    .withWatermark("event_ts", "10 minutes")
    .groupBy(F.window("event_ts", "5 minutes"), "customer_id")
    .agg(F.sum("amount").alias("revenue"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Start the Stream
# MAGIC
# MAGIC We use Parquet output here because it is simple and durable.
# MAGIC
# MAGIC Output mode `append` works with watermarking because Spark can append finalized window results.

# COMMAND ----------

query = (
    windowed_revenue.writeStream
    .format("parquet")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .option("path", output_path)
    .trigger(processingTime="10 seconds")
    .start()
)

query.id

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Add the First Batch of Events
# MAGIC
# MAGIC In a real pipeline, files would arrive from an upstream system. Here, we create JSON files manually.

# COMMAND ----------

batch_1 = spark.createDataFrame(
    [
        ("e001", "C001", "purchase", 100.0, datetime(2026, 1, 1, 10, 0, 0)),
        ("e002", "C001", "purchase", 50.0, datetime(2026, 1, 1, 10, 2, 0)),
        ("e003", "C002", "view", None, datetime(2026, 1, 1, 10, 3, 0)),
        ("e004", "C002", "purchase", 80.0, datetime(2026, 1, 1, 10, 4, 0)),
    ],
    event_schema
)

batch_1.write.mode("append").json(f"{input_path}/batch_1")

# COMMAND ----------

query.processAllAvailable()

# COMMAND ----------

display(spark.read.parquet(output_path))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Add Later Events
# MAGIC
# MAGIC Add events in a later time window so Spark can advance the watermark and emit finalized windows.

# COMMAND ----------

batch_2 = spark.createDataFrame(
    [
        ("e005", "C001", "purchase", 75.0, datetime(2026, 1, 1, 10, 12, 0)),
        ("e006", "C003", "purchase", 40.0, datetime(2026, 1, 1, 10, 13, 0)),
        ("e007", "C002", "purchase", 120.0, datetime(2026, 1, 1, 10, 14, 0)),
    ],
    event_schema
)

batch_2.write.mode("append").json(f"{input_path}/batch_2")
query.processAllAvailable()

# COMMAND ----------

display(spark.read.parquet(output_path).orderBy("window", "customer_id"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Query Progress
# MAGIC
# MAGIC Streaming query progress helps with operations and troubleshooting.
# MAGIC
# MAGIC Useful fields include input rows, processed rows per second, batch duration, state operator metrics, and watermark.

# COMMAND ----------

query.lastProgress

# COMMAND ----------

# MAGIC %md
# MAGIC ## 9. Stop the Stream
# MAGIC
# MAGIC Always stop learning streams when done.

# COMMAND ----------

query.stop()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 10. Restart from Checkpoint
# MAGIC
# MAGIC Restarting with the same checkpoint lets Spark continue from prior progress instead of starting over.

# COMMAND ----------

query_restarted = (
    windowed_revenue.writeStream
    .format("parquet")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .option("path", output_path)
    .trigger(availableNow=True)
    .start()
)

query_restarted.awaitTermination()

# COMMAND ----------

display(spark.read.parquet(output_path).orderBy("window", "customer_id"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Self-Learning Prompts
# MAGIC
# MAGIC Add more cells below:
# MAGIC
# MAGIC 1. Add duplicate `event_id` values and implement deduplication.
# MAGIC 2. Add a very late event and observe whether it appears in output.
# MAGIC 3. Change the watermark from 10 minutes to 2 minutes and compare behavior.
# MAGIC 4. Change the sink to memory for debugging and query it with SQL.
# MAGIC 5. Add a second aggregation by `event_type`.

