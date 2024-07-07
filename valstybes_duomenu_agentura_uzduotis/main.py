from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
import re

# Sukurti Spark sesiją
spark = SparkSession.builder \
    .appName("Pedagogu Kvalifikacija") \
    .getOrCreate()

# Importuoti duomenis
data = spark.read.csv(r'G:\Python GitHub ZygimantasB\valstybes_duomenu_agentura_uzduotis\pedagogu_kvalifikacija\pedagogu_kvalifikacija.csv', header=True)

# Pakeisti `null` reikšmes tekstiniose kolonose
for column in data.columns:
    data = data.withColumn(column, when(col(column).isNull(), "Nenurodyta").otherwise(col(column)))

# Pervadinti stulpelius į snake_case
for column in data.columns:
    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', column).lower()
    data = data.withColumnRenamed(column, snake_case_name)

# Čia galite atlikti papildomas transformacijas ir pakeisti duomenų tipus, jei reikia.


from pyspark.sql.functions import count

# Filtruoti duomenis
teachers_data = data.filter(data.pd_pareigu_grupe == 'Mokytojai')

# Suskaičiuoti mokytojus pagal savivaldybes
teachers_count_per_municipality = teachers_data.groupBy("savivaldybe").agg(count("*").alias("mokytoju_kiekis"))

# Suskaičiuoti mokytojus visoje Lietuvoje
teachers_count_total = teachers_data.count()
