# Databricks notebook source
# MAGIC %md
# MAGIC # DataFrame API Practical
# MAGIC
# MAGIC **Goal:** practice the most common PySpark DataFrame transformations using realistic nested sample data.
# MAGIC
# MAGIC Topics covered:
# MAGIC - Selecting, filtering, renaming, and casting
# MAGIC - Null handling
# MAGIC - Aggregations
# MAGIC - Complex types
# MAGIC - Explode
# MAGIC - Window functions
# MAGIC - UDF vs built-in functions

# COMMAND ----------

from datetime import datetime
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import StringType

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Create Nested Sample Data

# COMMAND ----------

events = spark.createDataFrame(
    [
        ("e001", "C001", "view", "electronics", 1200.0, ["web", "promo"], {"device": "mobile", "campaign": "winter"}, datetime(2026, 1, 1, 10, 0, 0)),
        ("e002", "C001", "purchase", "electronics", 1200.0, ["web"], {"device": "mobile", "campaign": "winter"}, datetime(2026, 1, 1, 10, 5, 0)),
        ("e003", "C002", "view", "books", None, ["app"], {"device": "tablet", "campaign": "none"}, datetime(2026, 1, 1, 11, 0, 0)),
        ("e004", "C002", "purchase", "books", 80.0, ["app", "loyalty"], {"device": "tablet", "campaign": "new-year"}, datetime(2026, 1, 1, 11, 30, 0)),
        ("e005", "C003", "view", "grocery", 45.0, ["web"], {"device": "desktop", "campaign": "none"}, datetime(2026, 1, 2, 9, 0, 0)),
        ("e006", "C003", "purchase", "grocery", 45.0, ["web"], {"device": "desktop", "campaign": "none"}, datetime(2026, 1, 2, 9, 10, 0)),
        ("e007", "C001", "purchase", "grocery", 150.0, ["web", "loyalty"], {"device": "mobile", "campaign": "winter"}, datetime(2026, 1, 2, 12, 0, 0)),
    ],
    "event_id STRING, customer_id STRING, event_type STRING, category STRING, amount DOUBLE, tags ARRAY<STRING>, attributes MAP<STRING, STRING>, event_ts TIMESTAMP"
)

display(events)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Select, Filter, Rename, and Cast
# MAGIC
# MAGIC These are common narrow transformations.

# COMMAND ----------

clean_events = (
    events
    .withColumnRenamed("event_ts", "event_timestamp")
    .withColumn("amount", F.col("amount").cast("double"))
    .withColumn("event_date", F.to_date("event_timestamp"))
    .filter(F.col("customer_id").isNotNull())
    .select("event_id", "customer_id", "event_type", "category", "amount", "event_date", "tags", "attributes")
)

display(clean_events)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Null Handling
# MAGIC
# MAGIC Nulls are not the same as zeros. Decide based on business meaning.
# MAGIC
# MAGIC Here, missing amount on a `view` event does not mean revenue is zero. For purchase-only revenue, filter purchase events first.

# COMMAND ----------

purchase_events = clean_events.filter(F.col("event_type") == "purchase")

revenue_by_category = (
    purchase_events
    .groupBy("category")
    .agg(
        F.count("*").alias("purchase_count"),
        F.sum("amount").alias("revenue")
    )
    .orderBy(F.desc("revenue"))
)

display(revenue_by_category)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Complex Types: Array and Map
# MAGIC
# MAGIC Arrays and maps are common in semi-structured data.

# COMMAND ----------

complex_type_example = (
    clean_events
    .withColumn("tag_count", F.size("tags"))
    .withColumn("device", F.col("attributes")["device"])
    .withColumn("campaign", F.col("attributes")["campaign"])
)

display(complex_type_example)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Explode Arrays
# MAGIC
# MAGIC `explode` turns array elements into rows. This is useful for tags, items, or nested collections.

# COMMAND ----------

event_tags = (
    clean_events
    .select("event_id", "customer_id", F.explode("tags").alias("tag"))
)

display(event_tags)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Window Functions
# MAGIC
# MAGIC Window functions calculate across related rows without collapsing the result like `groupBy`.
# MAGIC
# MAGIC Example: rank customer events by timestamp.

# COMMAND ----------

customer_window = Window.partitionBy("customer_id").orderBy("event_date", "event_id")

ranked_events = (
    clean_events
    .withColumn("event_sequence_for_customer", F.row_number().over(customer_window))
)

display(ranked_events.orderBy("customer_id", "event_sequence_for_customer"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Built-In Function vs UDF
# MAGIC
# MAGIC Prefer built-in Spark functions when possible. They are visible to Catalyst and usually perform better.

# COMMAND ----------

with_builtin = clean_events.withColumn("category_upper", F.upper("category"))
display(with_builtin)

# COMMAND ----------

def python_upper(value):
    if value is None:
        return None
    return value.upper()

upper_udf = F.udf(python_upper, StringType())

with_udf = clean_events.withColumn("category_upper", upper_udf("category"))
display(with_udf)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Compare Plans
# MAGIC
# MAGIC The UDF plan contains Python execution. Built-in functions are easier for Spark to optimize.

# COMMAND ----------

with_builtin.explain("formatted")

# COMMAND ----------

with_udf.explain("formatted")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Self-Learning Prompts
# MAGIC
# MAGIC Add more cells below:
# MAGIC
# MAGIC 1. Add a nested `struct` column and extract fields from it.
# MAGIC 2. Use `explode_outer` and compare behavior with `explode`.
# MAGIC 3. Add duplicate events and use `dropDuplicates`.
# MAGIC 4. Add a rolling revenue window per customer.

