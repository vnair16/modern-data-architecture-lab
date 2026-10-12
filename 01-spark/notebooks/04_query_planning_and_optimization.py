# Databricks notebook source
# MAGIC %md
# MAGIC # Query Planning and Optimization
# MAGIC
# MAGIC **Goal:** practice reading Spark physical plans and understanding joins, shuffles, partitions, skew, and adaptive query behavior.

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.functions import broadcast

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Create Sample Fact and Dimension Data

# COMMAND ----------

orders = spark.range(1, 10001).select(
    F.col("id").alias("order_id"),
    F.concat(F.lit("C"), F.lpad((F.col("id") % 500).cast("string"), 4, "0")).alias("customer_id"),
    F.when(F.col("id") % 10 == 0, F.lit("electronics"))
     .when(F.col("id") % 10 <= 3, F.lit("grocery"))
     .otherwise(F.lit("books")).alias("category"),
    (F.rand(seed=42) * 1000).cast("double").alias("amount")
)

customers = spark.range(0, 500).select(
    F.concat(F.lit("C"), F.lpad(F.col("id").cast("string"), 4, "0")).alias("customer_id"),
    F.when(F.col("id") % 3 == 0, F.lit("UAE"))
     .when(F.col("id") % 3 == 1, F.lit("India"))
     .otherwise(F.lit("UK")).alias("country")
)

display(orders.limit(10))
display(customers.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Explain a Filter and Projection
# MAGIC
# MAGIC Simple filters and projections should not require a shuffle.

# COMMAND ----------

filtered_orders = orders.filter("amount > 500").select("order_id", "customer_id", "amount")
filtered_orders.explain("formatted")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. GroupBy Causes a Shuffle
# MAGIC
# MAGIC Aggregating by a key usually needs Spark to move records with the same key together.
# MAGIC
# MAGIC In the plan, look for `Exchange`.

# COMMAND ----------

category_revenue = orders.groupBy("category").agg(F.sum("amount").alias("revenue"))
category_revenue.explain("formatted")

# COMMAND ----------

display(category_revenue)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Join Without Broadcast Hint
# MAGIC
# MAGIC Spark chooses a join strategy based on statistics, configuration, and adaptive execution.

# COMMAND ----------

joined = orders.join(customers, "customer_id", "inner")
joined.explain("formatted")

# COMMAND ----------

display(joined.groupBy("country").agg(F.sum("amount").alias("revenue")))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Broadcast Join
# MAGIC
# MAGIC If one side is small enough, broadcasting avoids shuffling both sides.
# MAGIC
# MAGIC This is common for fact-to-small-dimension joins.

# COMMAND ----------

broadcast_joined = orders.join(broadcast(customers), "customer_id", "inner")
broadcast_joined.explain("formatted")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Repartition vs Coalesce
# MAGIC
# MAGIC `repartition` can increase or decrease partitions and causes a shuffle.
# MAGIC
# MAGIC `coalesce` usually reduces partitions with less data movement.

# COMMAND ----------

print("Original partitions:", orders.rdd.getNumPartitions())
print("Repartitioned partitions:", orders.repartition(8).rdd.getNumPartitions())
print("Coalesced partitions:", orders.coalesce(1).rdd.getNumPartitions())

# COMMAND ----------

orders.repartition(8, "category").explain("formatted")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Skew Demonstration
# MAGIC
# MAGIC Skew happens when one key has much more data than other keys. It can make one task much slower than the rest.

# COMMAND ----------

skewed = spark.range(1, 20001).select(
    F.col("id"),
    F.when(F.col("id") <= 15000, F.lit("hot_key")).otherwise(F.concat(F.lit("key_"), F.col("id"))).alias("join_key"),
    (F.rand(seed=7) * 100).alias("value")
)

display(skewed.groupBy("join_key").count().orderBy(F.desc("count")).limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Salting a Skewed Key
# MAGIC
# MAGIC Salting splits a hot key into multiple artificial keys. This is one mitigation strategy.
# MAGIC
# MAGIC It is not free. It adds complexity and should be used only when skew is proven.

# COMMAND ----------

salted = skewed.withColumn(
    "salted_key",
    F.when(F.col("join_key") == "hot_key", F.concat(F.col("join_key"), F.lit("_"), (F.col("id") % 10).cast("string")))
     .otherwise(F.col("join_key"))
)

display(salted.groupBy("salted_key").count().orderBy(F.desc("count")).limit(15))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 9. Adaptive Query Execution Setting
# MAGIC
# MAGIC Adaptive Query Execution can adjust query plans at runtime.
# MAGIC
# MAGIC In Databricks, AQE may already be enabled depending on runtime.

# COMMAND ----------

spark.conf.get("spark.sql.adaptive.enabled", "not set")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Self-Learning Prompts
# MAGIC
# MAGIC Add more cells below:
# MAGIC
# MAGIC 1. Disable broadcast joins and compare the plan.
# MAGIC 2. Change `spark.sql.shuffle.partitions` and observe task count.
# MAGIC 3. Create a larger dimension and see when Spark stops broadcasting.
# MAGIC 4. Try different salting bucket counts for the hot key.

