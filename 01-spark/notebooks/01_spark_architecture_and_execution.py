# Databricks notebook source
# MAGIC %md
# MAGIC # Spark Architecture and Execution
# MAGIC
# MAGIC **Goal:** understand how Spark turns code into jobs, stages, tasks, and partitions.
# MAGIC
# MAGIC This notebook is intentionally small and practical. It creates sample data in memory so it can run in Databricks Community Edition.
# MAGIC
# MAGIC Topics covered:
# MAGIC - SparkSession
# MAGIC - DataFrames
# MAGIC - Transformations vs actions
# MAGIC - Lazy evaluation
# MAGIC - Jobs, stages, tasks, and partitions
# MAGIC - Narrow vs wide transformations
# MAGIC - Caching

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. SparkSession
# MAGIC
# MAGIC In Databricks, the `spark` variable is already available. It represents the active `SparkSession`.
# MAGIC
# MAGIC The `SparkSession` is the main entry point for DataFrame, SQL, catalog, and streaming work.

# COMMAND ----------

spark

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Create Sample Data
# MAGIC
# MAGIC We will use a small order dataset. Even with small data, the same execution concepts apply to large distributed data.

# COMMAND ----------

from datetime import date

orders_data = [
    (1, "C001", "UAE", "electronics", 1200.0, date(2026, 1, 3)),
    (2, "C002", "UAE", "books", 80.0, date(2026, 1, 3)),
    (3, "C003", "India", "electronics", 500.0, date(2026, 1, 4)),
    (4, "C001", "UAE", "grocery", 150.0, date(2026, 1, 5)),
    (5, "C004", "UK", "books", 45.0, date(2026, 1, 5)),
    (6, "C005", "India", "grocery", 220.0, date(2026, 1, 6)),
    (7, "C006", "UAE", "electronics", 3000.0, date(2026, 1, 7)),
    (8, "C002", "UAE", "grocery", 95.0, date(2026, 1, 8)),
]

orders = spark.createDataFrame(
    orders_data,
    "order_id INT, customer_id STRING, country STRING, category STRING, amount DOUBLE, order_date DATE"
)

display(orders)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Partitions
# MAGIC
# MAGIC A Spark DataFrame is split into partitions. Tasks run against partitions.
# MAGIC
# MAGIC Small data may have few partitions. Large data may have many partitions depending on the source and Spark configuration.

# COMMAND ----------

orders.rdd.getNumPartitions()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Lazy Evaluation
# MAGIC
# MAGIC Transformations build a plan. They do not immediately execute the work.
# MAGIC
# MAGIC Actions trigger execution. Examples: `count`, `show`, `collect`, `write`.

# COMMAND ----------

uae_large_orders = (
    orders
    .filter("country = 'UAE'")
    .filter("amount >= 100")
    .select("order_id", "customer_id", "category", "amount")
)

# No Spark job has to run just because we defined this DataFrame.
uae_large_orders

# COMMAND ----------

# This action triggers execution.
uae_large_orders.count()

# COMMAND ----------

display(uae_large_orders)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Narrow Transformation
# MAGIC
# MAGIC A narrow transformation can be computed from one input partition without moving data between partitions.
# MAGIC
# MAGIC Examples:
# MAGIC - `select`
# MAGIC - `filter`
# MAGIC - `withColumn`

# COMMAND ----------

from pyspark.sql import functions as F

narrow_example = (
    orders
    .filter(F.col("amount") > 100)
    .withColumn("amount_with_tax", F.col("amount") * F.lit(1.05))
    .select("order_id", "country", "category", "amount", "amount_with_tax")
)

display(narrow_example)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Wide Transformation
# MAGIC
# MAGIC A wide transformation usually requires data movement across partitions. This is called a shuffle.
# MAGIC
# MAGIC Examples:
# MAGIC - `groupBy`
# MAGIC - `distinct`
# MAGIC - `join` when data must be redistributed
# MAGIC - `orderBy`

# COMMAND ----------

wide_example = (
    orders
    .groupBy("country", "category")
    .agg(
        F.count("*").alias("order_count"),
        F.sum("amount").alias("total_amount")
    )
    .orderBy("country", "category")
)

display(wide_example)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Inspect the Physical Plan
# MAGIC
# MAGIC `explain()` shows how Spark plans to execute the query.
# MAGIC
# MAGIC Look for words such as:
# MAGIC - `Filter`
# MAGIC - `Project`
# MAGIC - `HashAggregate`
# MAGIC - `Exchange`
# MAGIC
# MAGIC `Exchange` usually means a shuffle.

# COMMAND ----------

wide_example.explain("formatted")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Jobs, Stages, and Tasks
# MAGIC
# MAGIC Run the next action, then open the Spark UI in Databricks.
# MAGIC
# MAGIC Look for:
# MAGIC - One or more jobs
# MAGIC - Stages inside the job
# MAGIC - Tasks inside each stage
# MAGIC - Shuffle read/write metrics for wide transformations

# COMMAND ----------

wide_example.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 9. Cache a Reused DataFrame
# MAGIC
# MAGIC Caching helps when the same DataFrame is reused by multiple actions.
# MAGIC
# MAGIC Important point: calling `cache()` only marks the DataFrame for caching. The cache is populated when an action runs.

# COMMAND ----------

orders_cached = orders.repartition(4).cache()
orders_cached.count()

# COMMAND ----------

display(
    orders_cached
    .groupBy("category")
    .agg(F.sum("amount").alias("total_amount"))
)

# COMMAND ----------

display(
    orders_cached
    .groupBy("country")
    .agg(F.avg("amount").alias("avg_amount"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 10. Cleanup
# MAGIC
# MAGIC Unpersist cached data when it is no longer needed.

# COMMAND ----------

orders_cached.unpersist()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Self-Learning Prompts
# MAGIC
# MAGIC Add more cells below:
# MAGIC
# MAGIC 1. Add a new `withColumn` transformation and inspect whether it changes the physical plan.
# MAGIC 2. Repartition the data to 2, 4, and 8 partitions. What changes?
# MAGIC 3. Add `distinct()` and inspect whether Spark adds an `Exchange`.
# MAGIC 4. Compare `orderBy` and `sortWithinPartitions`.

