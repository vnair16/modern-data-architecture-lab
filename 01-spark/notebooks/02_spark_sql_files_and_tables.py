# Databricks notebook source
# MAGIC %md
# MAGIC # Spark SQL, Files, and Tables
# MAGIC
# MAGIC **Goal:** practice Spark SQL with temporary views, file writes, partitioned data, save modes, and table concepts.
# MAGIC
# MAGIC This notebook writes sample data to DBFS paths under `/tmp`. It is safe to rerun for learning.

# COMMAND ----------

from datetime import date
from pyspark.sql import functions as F

base_path = "/tmp/modern_data_architecture_lab/spark_sql"
orders_path = f"{base_path}/orders_parquet"
partitioned_path = f"{base_path}/orders_partitioned"

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Create Sample Data

# COMMAND ----------

orders = spark.createDataFrame(
    [
        (1, "C001", "UAE", "electronics", 1200.0, date(2026, 1, 3)),
        (2, "C002", "UAE", "books", 80.0, date(2026, 1, 3)),
        (3, "C003", "India", "electronics", 500.0, date(2026, 1, 4)),
        (4, "C001", "UAE", "grocery", 150.0, date(2026, 1, 5)),
        (5, "C004", "UK", "books", 45.0, date(2026, 1, 5)),
        (6, "C005", "India", "grocery", 220.0, date(2026, 1, 6)),
        (7, "C006", "UAE", "electronics", 3000.0, date(2026, 1, 7)),
        (8, "C002", "UAE", "grocery", 95.0, date(2026, 1, 8)),
    ],
    "order_id INT, customer_id STRING, country STRING, category STRING, amount DOUBLE, order_date DATE"
)

display(orders)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Temporary Views
# MAGIC
# MAGIC A temporary view lets you query a DataFrame using SQL. It exists only in the current Spark session.

# COMMAND ----------

orders.createOrReplaceTempView("orders")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT country, category, COUNT(*) AS order_count, SUM(amount) AS total_amount
# MAGIC FROM orders
# MAGIC GROUP BY country, category
# MAGIC ORDER BY country, category

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. DataFrame API and SQL Can Express the Same Logic
# MAGIC
# MAGIC As a data architect, it helps to be comfortable reading both styles.

# COMMAND ----------

df_api_result = (
    orders
    .groupBy("country", "category")
    .agg(
        F.count("*").alias("order_count"),
        F.sum("amount").alias("total_amount")
    )
    .orderBy("country", "category")
)

display(df_api_result)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Write and Read Parquet
# MAGIC
# MAGIC Parquet is a columnar format. It is efficient for analytics because Spark can read only needed columns.

# COMMAND ----------

orders.write.mode("overwrite").parquet(orders_path)

orders_from_parquet = spark.read.parquet(orders_path)
display(orders_from_parquet)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Partitioned Writes
# MAGIC
# MAGIC Partitioning physically groups files by column values. It can improve reads when queries filter on the partition column.
# MAGIC
# MAGIC Do not over-partition. Too many small partitions can create many small files.

# COMMAND ----------

orders.write.mode("overwrite").partitionBy("country").parquet(partitioned_path)

partitioned_orders = spark.read.parquet(partitioned_path)
display(partitioned_orders)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Partition Pruning
# MAGIC
# MAGIC Spark can skip irrelevant partition directories when filtering on the partition column.
# MAGIC
# MAGIC Use `explain()` and look for partition filters.

# COMMAND ----------

uae_orders = partitioned_orders.filter("country = 'UAE'")
uae_orders.explain("formatted")

# COMMAND ----------

display(uae_orders)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Save Modes
# MAGIC
# MAGIC Common save modes:
# MAGIC
# MAGIC - `overwrite`: replace existing data
# MAGIC - `append`: add new data
# MAGIC - `ignore`: do nothing if path exists
# MAGIC - `error` or `errorifexists`: fail if path exists

# COMMAND ----------

append_data = spark.createDataFrame(
    [(9, "C007", "UAE", "books", 60.0, date(2026, 1, 9))],
    orders.schema
)

append_data.write.mode("append").parquet(orders_path)

display(spark.read.parquet(orders_path).orderBy("order_id"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Managed Table Example
# MAGIC
# MAGIC In Databricks, tables are managed through a metastore. Community Edition availability can vary.
# MAGIC
# MAGIC The next cell creates a simple managed table in the default database.

# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS spark_learning_orders")

orders.write.mode("overwrite").saveAsTable("spark_learning_orders")

display(spark.sql("SELECT * FROM spark_learning_orders ORDER BY order_id"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 9. SQL Expressions
# MAGIC
# MAGIC Spark SQL supports expressions, `CASE`, date functions, and aggregations.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   order_id,
# MAGIC   country,
# MAGIC   category,
# MAGIC   amount,
# MAGIC   CASE
# MAGIC     WHEN amount >= 1000 THEN 'high'
# MAGIC     WHEN amount >= 100 THEN 'medium'
# MAGIC     ELSE 'low'
# MAGIC   END AS order_value_band,
# MAGIC   date_format(order_date, 'yyyy-MM') AS order_month
# MAGIC FROM spark_learning_orders
# MAGIC ORDER BY order_id

# COMMAND ----------

# MAGIC %md
# MAGIC ## Self-Learning Prompts
# MAGIC
# MAGIC Add more cells below:
# MAGIC
# MAGIC 1. Write the data as JSON and CSV, then compare schemas when reading back.
# MAGIC 2. Add another partition column. What directory structure is created?
# MAGIC 3. Try `mode("ignore")` and `mode("error")` on an existing path.
# MAGIC 4. Create a global temporary view and query it.

