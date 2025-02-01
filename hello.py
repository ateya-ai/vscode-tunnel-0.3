from databricks.sdk.runtime import *

df = spark.table("samples.nyctaxi.trips")
df.show(20)