# Databricks notebook source
# MAGIC %run ./utils_function

# COMMAND ----------
# Now we can call the function defined in utils_function
message = greet_user("Alice")
print(message)
