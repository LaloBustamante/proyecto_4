#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Eduardo!
# 
# Mi nombre es Ezequiel Ferrario, soy code reviewer en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberá hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión.
# </div>
# 
# ¡Empecemos!

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Eduardo, recorda que lo que esta entre corchete es una mera guia para el alumno. Este al ser un proyecto simulando un espacio profesional, deberias eliminar los mismos.
# 
# Esta correccion aplica a cualquier parte donde se encuentre este tipo de guias.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión. Esta instrucción de eliminar lo que se encuentra entre parentesis no fue dada en ningun momento en la plataforma ni dentro del proyecto. Razón por la que no fueron eliminados, pero procedo a realizar la corrección. 
# </div>
# 

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Muy bien, tenelo en cuenta para futuros proyecto.</div>

# # ¿Cuál es la mejor tarifa?
# 
# Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
# Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

# El propósito de este proyecto es realizar un análisis preliminar de las tarifas de prepago (Surf y Ultimate) ofrecidas por la compañia Megaline. La empresa desea determinar cuál de las tarifas genera más ingresos con el objetivo de ajustar el presupuesto de publicidad. Para lograr esto, se analizarán los datos de 500 clientes de Megaline, que incluyen información sobre quiénes son los clientes, su ubicación, la tarifa utilizada, así como la cantidad de llamadas y mensajes de texto realizados en el año 2018.
# 
# Acciones Planeadas:
# 
# Exploración de Datos:
# 
# Examinar los datos para comprender la estructura y la calidad.
# Identificar posibles problemas como valores nulos, duplicados o formatos incorrectos.
# 
# Preprocesamiento de Datos:
# 
# Realizar limpieza de datos, manejar valores nulos y corregir cualquier problema identificado durante la exploración.
# Verificar y transformar tipos de datos según sea necesario.
# 
# Análisis Descriptivo:
# 
# Calcular estadísticas descriptivas para obtener información general sobre el comportamiento de los clientes.
# Visualizar datos a través de gráficos para una comprensión más clara.
# 
# Análisis Comparativo:
# 
# Comparar el uso de llamadas y mensajes de texto entre los usuarios de las tarifas Surf y Ultimate.
# Evaluar si hay diferencias significativas en el comportamiento de los usuarios de ambas tarifas.
# 
# Ingresos Mensuales:
# 
# Calcular los ingresos mensuales por usuario para ambas tarifas.
# Analizar y comparar los ingresos generados por cada tarifa.
# 
# Conclusiones y Recomendaciones:
# 
# Resumir los hallazgos y conclusiones basadas en el análisis.
# Proporcionar recomendaciones sobre qué tarifa podría ser más rentable y cómo ajustar el presupuesto de publicidad.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda que lo que esta entre corchete es una mera guia para el alumno. Este al ser un proyecto simulando un espacio profesional, deberias eliminar los mismos.
# 
# Esta correccion aplica a cualquier parte donde se encuentre este tipo de guias ya que es un requisito de **forma** obligatorio para aprobar el proyecto (es decir, que no quede ninguna guia/corchete).</div>
# 
# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Inicialización

# In[2]:


# Cargar todas las librerías
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as st
from scipy.stats import ttest_ind
from scipy.stats import levene


# ## Cargar datos

# In[3]:


# Carga los archivos de datos en diferentes DataFrames
megaline_calls_df = pd.read_csv('/datasets/megaline_calls.csv')
megaline_internet_df = pd.read_csv('/datasets/megaline_internet.csv')
megaline_messages_df = pd.read_csv('/datasets/megaline_messages.csv')
megaline_plans_df = pd.read_csv('/datasets/megaline_plans.csv')
megaline_users_df = pd.read_csv('/datasets/megaline_users.csv')


# ## Preparar los datos

# ## Tarifas

# In[4]:


# Imprime la información general/resumida sobre el DataFrame de las tarifas
megaline_plans_df.info()


# In[5]:


# Imprime una muestra de los datos para las tarifas
megaline_plans_df.head(2) #El df solo contiene 2 registros


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Realizada la corrección, eliminando el metódo print() de la instrucción. Igualmente se eliminaron los corchetes de la instrucción del proyecto.
# </div>
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Corregido</div>

# Hay un total de 2 entradas (filas) en el DataFrame, hay 8 columnas en total.
# Las columnas messages_included, mb_per_month_included, minutes_included, usd_monthly_pay, usd_per_gb son del tipo de dato entero (int64).
# Las columnas usd_per_message y usd_per_minute son del tipo de dato de punto flotante. La columna plan_name es del tipo de dato objeto, lo cual generalmente se utiliza para columnas de texto o categóricas.
# No hay valores nulos (NaN) en ninguna de las columnas. Cada columna tiene 2 valores no nulos, lo que indica que no hay datos faltantes en el conjunto de datos. El DataFrame está utilizando 256.0+ bytes de memoria.

# ## Corregir datos

# In[6]:


#No considero que sea necesario realizar ninguna corrección en megaline_plans_df


# ## Enriquecer los datos

# In[7]:


#Agregar una columna de relación precio-rendimiento:
megaline_plans_df['value_for_money'] = (
    megaline_plans_df['minutes_included'] +
    megaline_plans_df['messages_included'] +
    megaline_plans_df['mb_per_month_included'] / 1024  # Convertir MB a GB
) / megaline_plans_df['usd_monthly_pay']

#Categorizar planes por niveles de uso:
megaline_plans_df['usage_level'] = pd.cut(
    megaline_plans_df['minutes_included'] +
    megaline_plans_df['messages_included'] +
    megaline_plans_df['mb_per_month_included'] / 1024,  # Convertir MB a GB
    bins=[0, 500, 1000, 2000, np.inf],
    labels=['Bajo', 'Moderado', 'Alto', 'Muy Alto']
)

#Agregar una columna para tarifas adicionales promedio:
megaline_plans_df['avg_usd_per_message'] = megaline_plans_df['usd_per_message']
megaline_plans_df['avg_usd_per_minute'] = megaline_plans_df['usd_per_minute']


# ## Usuarios/as

# In[8]:


# Imprime estadísticas descriptivas para variables numéricas
print(megaline_users_df.describe())


# In[9]:


# Verifica y maneja duplicados
duplicates = megaline_users_df.duplicated()
if duplicates.any():
    megaline_users_df = megaline_users_df[~duplicates]
    print("Se eliminaron duplicados.")
else:
    print("No se encontraron duplicados.")


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda utilizar el metodo describe() para una exploracion rapida inicial de aquellas variables numericas. Siempre es necesario realizarlo ya que de forma rapida tenemos un panorama muy bueno de que nos espera e incluso encontraremos inconsistencias si existiencen.
# Describi al respecto lo que ves. </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Verifica la existencia de duplicados. </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada de acuerdo con las especificaciones solicitadas, utilizara el método describe y la descripción de lo que se observa. Se verificó la existencia de duplicados.
# </div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Para el metodo describe() podes utilizar el display y se vera mucho mejor.</div>

# El DataFrame tiene 500 entradas y 8 columnas. Las columnas user_id, first_name, last_name, age, city, plan son de tipos adecuados (int64, object, int64, int64, object, object, respectivamente). La columna reg_date y churn_date no tienen un formato adecuado. La columna churn_date tiene 34 valores no nulos, lo que indica que hay usuarios que han cancelado su plan.
# Los valores NaT (Not a Time) existentes en la columna churn_date, indican que algunos usuarios no han cancelado su plan. 
# Se deberia convertir la columna reg_date y churn_date en el formato datetime64[ns], lo cual es apropiado para manejar fechas.
# 
# Estadísticas Descriptivas:
# 
# Algunas estadísticas clave incluyen:
# La edad promedio de los usuarios es aproximadamente 45.49 años.
# La edad mínima es 18 años, y la máxima es 75 años.
# 
# Verificación de Duplicados:
# La verificación de duplicados utilizando duplicated() indica que no hay filas duplicadas en el DataFrame.

# ### Corregir los datos

# In[10]:


# Convertir columnas de fechas en megaline_users_df  
megaline_users_df['reg_date'] = pd.to_datetime(megaline_users_df['reg_date'])
megaline_users_df['churn_date'] = pd.to_datetime(megaline_users_df['churn_date'])


# ### Enriquecer los datos

# In[11]:


#Duración de la permanencia del cliente
megaline_users_df['tenure_duration'] = (megaline_users_df['churn_date'] - megaline_users_df['reg_date'])

#Mes de Registro:
megaline_users_df['registration_month'] = megaline_users_df['reg_date'].dt.month

#Edad del Cliente en Grupos:
bins = [0, 18, 25, 35, 50, 100]
labels = ['0-18', '19-25', '26-35', '36-50', '51+']
megaline_users_df['age_group'] = pd.cut(megaline_users_df['age'], bins=bins, labels=labels)

#Ciudad por Región:
megaline_users_df['region'] = megaline_users_df['city'].apply(lambda x: x.split(',')[1].strip())

#Indicador de cancelación:
megaline_users_df['churn_indicator'] = megaline_users_df['churn_date'].notnull().astype(int)


# Se realizaron varias transformaciones en el DataFrame megaline_users_df:
# 
# Conversión de Fechas:
# Las columnas de fechas, reg_date y churn_date, se convirtieron al formato de fecha usando pd.to_datetime().
# 
# Duración de Permanencia del Cliente:
# Se calculó la duración de la permanencia del cliente utilizando la diferencia entre las fechas de cancelación (churn_date) y registro (reg_date).
# 
# Mes de Registro:
# Se extrajo el mes de registro (registration_month) de la columna de fecha de registro.
# 
# Edad del Cliente en Grupos:
# Se crearon grupos de edad (age_group) utilizando la función pd.cut() y se asignaron etiquetas.
# 
# Ciudad por Región:
# Se extrajo la región de la columna de la ciudad (region) utilizando la función apply() y la operación split().
# 
# Indicador de Cancelación:
# Se creó un indicador de cancelación (churn_indicator) que toma el valor de 1 si la fecha de cancelación no es nula.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta muy bien, recorda realizar una descripcion con los cambios realizados. </div>
# 
# 

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada se agregó una descripción de los cambios realizados
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Te quedo excelente.</div>

# ## Llamadas

# In[12]:


# Imprime la información general/resumida sobre el DataFrame de las llamadas
print(megaline_calls_df.info())

# Imprime estadísticas descriptivas para variables numéricas
print(megaline_calls_df.describe())


# In[13]:


# Verifica y maneja duplicados
duplicates_calls = megaline_calls_df.duplicated()
if duplicates_calls.any():
    megaline_calls_df = megaline_calls_df[~duplicates_calls]
    print("Se eliminaron duplicados en el DataFrame de llamadas.")
else:
    print("No se encontraron duplicados en el DataFrame de llamadas.")

# Imprime una muestra de datos para las llamadas
print(megaline_calls_df.sample(10))


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda utilizar el metodo describe() para una exploracion rapida inicial de aquellas variables numericas. Siempre es necesario realizarlo ya que de forma rapida tenemos un panorama muy bueno de que nos espera e incluso encontraremos inconsistencias si existiencen.
# Describi al respecto lo que ves. </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Verifica la existencia de duplicados. </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada se usó el método describe(), se agregó una descripción de los cambios realizados y se verificó la existencia de duplicados.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Para el metodo describe() podes utilizar el display y se vera mucho mejor.
# 
# Me gusto mucho como dejaste la descripcion de los cambios.</div>

# La información general proporcionada por megaline_calls_df.info() indica que el DataFrame tiene 137,735 entradas y consta de cuatro columnas: id, user_id, call_date, y duration. La columna call_date puede ser convertida a un tipo de dato mas adecuado.
# La columna duration está representada como float64, lo cual es adecuado para representar valores decimales. Sin embargo, se observa que hay una llamada con una duración de 0 minutos. 
# Dependiendo del analisis debemos decidir cómo manejar las llamadas con duración igual a 0. Eliminandolas si no son relevantes para el análisis o imputar valores basados en el contexto.
# 
# Descripción de Cambios:
# 
# Estadísticas Descriptivas:
# Se agregó la línea print(megaline_calls_df.describe()) para imprimir estadísticas descriptivas de las variables numéricas en el DataFrame de llamadas.
# 
# Verificación de Duplicados:
# Se añadió un bloque de código para verificar y manejar duplicados en el DataFrame de llamadas. El mensaje de impresión informa si se eliminaron duplicados o si no se encontraron.

# ### Corregir los datos

# In[14]:


# Convertir columnas de fechas en megaline_calls_df
megaline_calls_df['call_date'] = pd.to_datetime(megaline_calls_df['call_date'])


# ### Enriquecer los datos

# In[15]:


# Añadir información sobre la hora del día (redondeando hacia arriba)
megaline_calls_df['hour_of_day'] = np.ceil(megaline_calls_df['call_date'].dt.hour)

# Añadir información sobre el día de la semana
megaline_calls_df['day_of_week'] = megaline_calls_df['call_date'].dt.dayofweek

# Añadir información sobre la duración de la llamada (redondeando hacia arriba)
bins = [0, 5, 10, 20, 30, 60, float('inf')]
labels = ['0-5', '6-10', '11-20', '21-30', '31-60', '60+']
megaline_calls_df['call_duration_group'] = pd.cut(np.ceil(megaline_calls_df['duration']), bins=bins, labels=labels, right=False)

#Añadir información sobre la temporada del año:
def get_season(month):
    if 3 <= month <= 5:
        return 'Spring'
    elif 6 <= month <= 8:
        return 'Summer'
    elif 9 <= month <= 11:
        return 'Fall'
    else:
        return 'Winter'

megaline_calls_df['season'] = megaline_calls_df['call_date'].dt.month.apply(get_season)
megaline_calls_df['month'] = megaline_calls_df['call_date'].dt.month


# Descripción de Cambios:
# 
# Se utilizó la función ceil para redondear hacia arriba.
# Se aplicó np.ceil para redondear hacia arriba la hora del día y la duración de la llamada.
# Se agregó la columna 'month' que contiene el mes de la llamada 
# Se agregó la columna 'season' que contiene la estación del año.
# Si hay valores de llamadas que duran 0 minutos, el redondeo hacia arriba garantiza que se considere al menos como una unidad de llamada.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# En este caos nuestro cliente trabaja redondeando las llamadas, para eso aqui deberiamos aplicar el metodo ceil de numpy.</div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Extrae el mes de las llamadas, esta muy bien separarlo por estacion pero tambien debemos sacarlo por separado.</div>
# 
# <div class="alert alert-block alert-warning">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# ¿Hay valores de llamadas que duran 0 minutos? ¿Que harias con ellas?</div>
# 
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda realizar una descripcion con los cambios realizados. </div>
# 
# 

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se usó el método ceil de numpy para redondear, se extrae el mes y la estación por separado, Se realizó una breve descriçión de los cambios realizados, se verificó la existencia de valores de llamada de 0 minutos
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Mensajes

# In[16]:


# Imprime la información general/resumida sobre el DataFrame de los mensajes
megaline_messages_df.info()


# In[17]:


# Imprime una muestra de datos para los mensajes
megaline_messages_df.sample(10)


# In[18]:


# Verificar y manejar duplicados en megaline_messages_df
duplicates_messages = megaline_messages_df.duplicated()
if duplicates_messages.any():
    megaline_messages_df = megaline_messages_df[~duplicates_messages]
    print("Se eliminaron duplicados en el DataFrame de mensajes.")
else:
    print("No se encontraron duplicados en el DataFrame de mensajes.")


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Verifica la existencia de duplicados. </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se verificó la existencia de valores duplicados.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# En el DataFrame megaline_messages_df, hay una columna llamada message_date que contiene fechas y podria convertirse a otro tipo de dato mas adecuado. No hay valores nulos en ninguna de las columnas.
# Además, para realizar análisis temporal, también se podria extraer información adicional de las fechas, como el mes, el día de la semana, etc.

# ### Corregir los datos

# In[19]:


# Convertir columnas de fechas en megaline_messages_df
megaline_messages_df['message_date'] = pd.to_datetime(megaline_messages_df['message_date'])


# ### Enriquecer los datos

# In[20]:


# Añadir información sobre el mes
megaline_messages_df['message_month'] = megaline_messages_df['message_date'].dt.month

# Añadir información sobre la hora del día
megaline_messages_df['message_hour'] = megaline_messages_df['message_date'].dt.hour

# Añadir información sobre el día de la semana
megaline_messages_df['message_day_of_week'] = megaline_messages_df['message_date'].dt.day_name()

# Contar la cantidad de mensajes por usuario
user_message_counts = megaline_messages_df['user_id'].value_counts().reset_index()
user_message_counts.columns = ['user_id', 'message_count']
megaline_messages_df = pd.merge(megaline_messages_df, user_message_counts, on='user_id', how='left')


# Se realizaron los siguientes cambios:
# 
# Se creó una nueva columna llamada message_month que contiene el mes de la fecha del mensaje.
# Se mantuvieron las columnas existentes para la hora del día y el día de la semana.
# Se contó la cantidad de mensajes por usuario y se agregó esta información al DataFrame original.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Extrae el mes por separado en una nueva columna</div>
# 
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda realizar una descripcion con los cambios realizados. </div>
# 
# 

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se extrae el mes por separado en una nueva columna y se realiza la descripción de los cambios realizados.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Internet

# In[21]:


# Imprime la información general/resumida sobre el DataFrame de internet
megaline_internet_df.info()

# Imprime estadísticas descriptivas para variables numéricas
print(megaline_internet_df.describe())


# In[22]:


# Verifica y maneja duplicados
duplicates = megaline_internet_df.duplicated()
if duplicates.any():
    megaline_internet_df = megaline_internet_df[~duplicates]
    print("Se eliminaron duplicados.")
else:
    print("No se encontraron duplicados.")

# Imprime una muestra de datos para el tráfico de internet
megaline_internet_df.sample(10)


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda utilizar el metodo describe() para una exploracion rapida inicial de aquellas variables numericas. Siempre es necesario realizarlo ya que de forma rapida tenemos un panorama muy bueno de que nos espera e incluso encontraremos inconsistencias si existiencen.
# Describi al respecto lo que ves. </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Verifica la existencia de duplicados. </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se utilizó el método describe() se realizó la descripción al respecto de lo que se ve, se eliminaron los comentarios entre corchetes y se verificó la existencia de duplicaods.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# En el DataFrame megaline_internet_df, se observa que la columna session_date debería convertirse al tipo de dato datetime para facilitar el manejo de fechas. Además, parece que no hay datos ausentes en ninguna de las columnas.
# En cuanto a la muestra de datos, parece estar bien y no muestra problemas. Sin embargo, es aconsejable revisar más datos para asegurarse de que no haya valores atípicos o patrones inesperados que puedan afectar el análisis.
# 
# Estadísticas Descriptivas:
# 
# La columna 'user_id' tiene un promedio de aproximadamente 1242.5, con un mínimo de 1000 y un máximo de 1499.
# La columna 'mb_used' tiene un promedio de aproximadamente 366.71 MB, con un mínimo de 0 y un máximo de 1693.47 MB.
# Las estadísticas proporcionan una visión general de la distribución de los datos, incluidos los cuartiles.

# ### Corregir los datos

# In[23]:


# Convertir columnas de fechas en megaline_internet_df
megaline_internet_df['session_date'] = pd.to_datetime(megaline_internet_df['session_date'])


# ### Enriquecer los datos

# In[24]:


#Agregar información sobre el mes:
megaline_internet_df['month'] = megaline_internet_df['session_date'].dt.month

#Agregar información sobre el día de la semana:
megaline_internet_df['day_of_week'] = megaline_internet_df['session_date'].dt.dayofweek


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Aqui no pases de mb a gb ya que podrias sobreestimar el consumo del usuario, realizalo luego de completar la tabla pivot (o groupby) de internet.</div>
# 
# 

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se eliminó la conversión a GB.
# </div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Estudiar las condiciones de las tarifas

# In[25]:


# Imprime las condiciones de la tarifa y asegúrate de que te quedan claras
megaline_plans_df


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se eliminó el método print y se utiliza el metodo solo.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Agregar datos por usuario

# In[26]:


# Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.

# Extracciones de Mes para las llamadas
megaline_calls_df['month'] = megaline_calls_df['call_date'].dt.to_period('M')

# Extracciones de Mes para los mensajes
megaline_messages_df['month'] = megaline_messages_df['message_date'].dt.to_period('M')

# Extracciones de Mes para el tráfico de Internet
megaline_internet_df['month'] = megaline_internet_df['session_date'].dt.to_period('M')

# Cálculo del número de llamadas hechas por cada usuario al mes y guardado del resultado
calls_per_month = megaline_calls_df.groupby(['user_id', 'month']).size().reset_index(name='calls_count')
calls_per_month.to_csv('calls_per_month.csv', index=False)


# In[27]:


# Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.

minutes_per_month = megaline_calls_df.groupby(['user_id', 'month'])['duration'].sum().reset_index(name='minutes_used')
minutes_per_month['minutes_used'] = np.ceil(minutes_per_month['minutes_used'])  # Redondeo hacia arriba
minutes_per_month.to_csv('minutes_per_month.csv', index=False)


# In[28]:


# Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.

messages_per_month = megaline_messages_df.groupby(['user_id', 'month']).size().reset_index(name='messages_sent')
messages_per_month.to_csv('messages_per_month.csv', index=False)


# In[29]:


# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.

internet_traffic_per_month = megaline_internet_df.groupby(['user_id', 'month'])['mb_used'].sum().reset_index(name='internet_traffic_mb')
internet_traffic_per_month['internet_traffic_gb'] = np.ceil(internet_traffic_per_month['internet_traffic_mb'] / 1024)  # Conversión a GB y redondeo hacia arriba
internet_traffic_per_month.to_csv('internet_traffic_per_month.csv', index=False)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Todas extracciones  de Mes las deberias hacer antes ya que quedara mas estructurado y es lo que marcan las buenas practicas.
# 
# Ademas, aqui deberias hacer el paso a GB con  el correspondiente CEIL.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se realizaron las extraccioens del me al principio y se realizó la ocnversión a Gb y redondeo hacia arriba usando el metodo Ceil.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Excelente.</div>

# In[30]:


# Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month

# Carga los archivos CSV que has guardado
calls_per_month = pd.read_csv('calls_per_month.csv')
minutes_per_month = pd.read_csv('minutes_per_month.csv')
messages_per_month = pd.read_csv('messages_per_month.csv')
internet_traffic_per_month = pd.read_csv('internet_traffic_per_month.csv')

# Fusiona los DataFrames en base a 'user_id' y 'month'
merged_data = calls_per_month.merge(minutes_per_month, on=['user_id', 'month'], how='outer')
merged_data = merged_data.merge(messages_per_month, on=['user_id', 'month'], how='outer')
merged_data = merged_data.merge(internet_traffic_per_month, on=['user_id', 'month'], how='outer')

# Mostrar las primeras filas del dataset fusionado
print(merged_data.head())


# In[31]:


# Añade la información de la tarifa

# Fusiona los datos combinados con la información de los planes
final_data = merged_data.merge(megaline_users_df[['user_id', 'plan']], on='user_id', how='left')
final_data = final_data.merge(megaline_plans_df[['plan_name', 'usd_monthly_pay']], left_on='plan', right_on='plan_name', how='left')

# Mostrar las primeras filas del dataset fusionado
print(final_data.head())

# Reordena las columnas para mayor claridad
final_data = final_data[['user_id', 'month', 'plan', 'plan_name', 'usd_monthly_pay', 'calls_count', 'minutes_used', 'messages_sent', 'internet_traffic_mb']]

# Guarda el resultado en un nuevo archivo CSV
final_data.to_csv('final_data.csv', index=False)


# In[32]:


# Calcula el ingreso mensual para cada usuario

# Define las tarifas por excedente para llamadas, mensajes y datos
additional_cost_per_minute = 0.01  # Costo adicional por minuto
additional_cost_per_message = 0.03  # Costo adicional por mensaje
additional_cost_per_gb = 10  # Costo adicional por GB

# Fusiona los datos combinados con la información de los planes
final_data = merged_data.merge(megaline_users_df[['user_id', 'plan']], on='user_id', how='left')
final_data = final_data.merge(megaline_plans_df[['plan_name', 'usd_monthly_pay', 'minutes_included', 'messages_included', 'mb_per_month_included']], left_on='plan', right_on='plan_name', how='left')

# Mostrar las primeras filas del dataset fusionado
print(final_data.head())

# Calcula los ingresos mensuales por usuario
final_data['monthly_revenue'] = (
    final_data['usd_monthly_pay'] +  # Tarifa mensual base
    np.maximum(0, final_data['calls_count'] - final_data['minutes_included']) * additional_cost_per_minute +  # Costo adicional por minutos excedidos
    np.maximum(0, final_data['messages_sent'] - final_data['messages_included']) * additional_cost_per_message +  # Costo adicional por mensajes excedidos
    np.maximum(0, (final_data['internet_traffic_mb'] - final_data['mb_per_month_included'] / 1024)) * additional_cost_per_gb  # Costo adicional por datos excedidos
)

# Reordena las columnas para mayor claridad
final_data = final_data[['user_id', 'month', 'plan', 'plan_name', 'usd_monthly_pay', 'calls_count', 'minutes_used', 'messages_sent', 'internet_traffic_mb', 'monthly_revenue']]

# Guarda el resultado en un nuevo archivo CSV
final_data.to_csv('final_data_with_revenue.csv', index=False)


# Fusión de Datos:
# Se cargan datos de llamadas, minutos, mensajes e Internet desde archivos CSV.
# Se fusionan los DataFrames usando 'user_id' y 'month'.
# Se crea un DataFrame combinado llamado merged_data.
# 
# Añadir Información de Tarifa:
# Se fusiona merged_data con información de usuarios y planes.
# Se seleccionan columnas relevantes para formar final_data.
# El resultado se guarda en 'final_data.csv'.
# 
# Cálculo del Ingreso Mensual:
# Se definen tarifas por excedente para llamadas, mensajes y datos.
# Se fusiona merged_data con información de usuarios y planes.
# Se calcula el ingreso mensual por usuario.
# El resultado se guarda en 'final_data_with_revenue.csv'.
# 
# Conclusiones:
# La fusión de datos es crucial para combinar información de diferentes fuentes y proporcionar una visión completa.
# La adición de información de tarifa y el cálculo de ingresos mensuales permiten evaluar la rentabilidad de cada usuario.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Describi y conclui al respecto de lo realizado en en esta seccion. Esta parte es muy importante debido que es aqui donde tambien esta nuestro valor, ya que el cliente podra no entender el código pero si el análisis o la descripcion.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se realizaron las descripciones y conclusiones respecto a lo realizado.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Estudia el comportamiento de usuario

# ### Llamadas

# In[33]:


# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

# Carga el DataFrame desde el archivo CSV 
final_data = pd.read_csv('final_data_with_revenue.csv')

# Agrupar por plan y mes, calculando la duración promedio de llamadas
average_duration_per_plan = final_data.groupby(['plan_name', 'month'])['minutes_used'].mean().reset_index()

# Crear un gráfico de barras
plt.figure(figsize=(14, 7))
sns.barplot(x='month', y='minutes_used', hue='plan_name', data=average_duration_per_plan)

# Configurar la visualización
plt.title('Duración Promedio de Llamadas por Plan y Mes')
plt.xlabel('Mes')
plt.ylabel('Duración Promedio de Llamadas (minutos)')
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mayor legibilidad
plt.legend(title='Plan')
plt.show()


# In[34]:


# Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.

# Filtrar los datos por el tipo de plan
plan_names = final_data['plan_name'].unique()

# Crear un histograma para cada plan
plt.figure(figsize=(12, 6))
for plan_name in plan_names:
    plan_data = final_data[final_data['plan_name'] == plan_name]
    sns.histplot(plan_data['minutes_used'], bins=30, kde=True, label=plan_name, alpha=0.7)

# Configurar la visualización
plt.title('Distribución del Número de Minutos Mensuales por Plan')
plt.xlabel('Minutos Mensuales')
plt.ylabel('Frecuencia')
plt.legend(title='Plan')
plt.show()


# In[35]:


# Calcula la media, mediana, moda, desviación estándar y varianza de la duración mensual de llamadas.

# Agrupar por plan y mes, calculando la duración mensual de llamadas
duration_per_plan = final_data.groupby(['plan_name', 'month'])['minutes_used'].sum().reset_index()


# Calcular estadísticas por plan
statistics_per_plan = duration_per_plan.groupby('plan_name')['minutes_used'].describe()

# Mostrar los resultados
print("Estadísticas de duración mensual de llamadas por plan:")
print(statistics_per_plan)


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta muy bien pero explora mas estadisticos. La mediana, moda, la desviacion standard</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se colocaron mas estadisticos.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>
# 

# In[36]:


# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas

# Visualizar la distribución con un diagrama de caja
plt.figure(figsize=(10, 6))
sns.boxplot(x='plan_name', y='minutes_used', data=duration_per_plan)
plt.title('Distribución de la duración mensual de llamadas por plan')
plt.xlabel('Plan')
plt.ylabel('Duración mensual de llamadas')
plt.show()


# Se puede observar que la mayoría de los usuarios, tanto de plan Surf como de plan Ultimate, realizan llamadas de corta duración, con una media de entre 10 y 20 minutos. Sin embargo, también hay un pequeño porcentaje de usuarios que realizan llamadas de larga duración, de hasta 2 horas.
# El comportamiento de los usuarios con respecto a las llamadas no varía en función del plan. Sin embargo, hay una pequeña diferencia en la distribución de las llamadas de larga duración. En el plan Surf, las llamadas de larga duración son más frecuentes que en el plan Ultimate. Esto podría deberse a que los usuarios del plan Surf tienen un límite de llamadas más bajo, por lo que pueden ser más propensos a realizar llamadas más largas para evitar pagar cargos adicionales.
# 
# Algunas conclusiones específicas sobre el comportamiento de los usuarios con respecto a las llamadas:
# 
# La duración media de las llamadas es de entre 10 y 20 minutos.
# Un pequeño porcentaje de usuarios realiza llamadas de larga duración, de hasta 2 horas.
# En el plan Surf, las llamadas de larga duración son más frecuentes que en el plan Ultimate.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Excelente.</div>

# ### Mensajes

# In[37]:


# Compara la duración promedio de mensajes por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

# Visualización con gráfico de barras para el promedio de mensajes enviados por mes
average_messages_per_month = final_data.groupby(['plan_name', 'month'])['messages_sent'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='month', y='messages_sent', hue='plan_name', data=average_messages_per_month)
plt.title('Promedio de Mensajes Enviados por Plan y Mes')
plt.xlabel('Mes')
plt.ylabel('Promedio de Mensajes Enviados')
plt.xticks(rotation=45)
plt.show()


# In[38]:


# Compara el número de mensajes mensuales que necesitan los usuarios de cada plan. Traza un histograma.

# Visualización con histograma para el número de mensajes mensuales por plan
plt.figure(figsize=(10, 6))
for plan in final_data['plan_name'].unique():
    sns.histplot(final_data[final_data['plan_name'] == plan]['messages_sent'], kde=True, label=plan, alpha=0.6)

plt.title('Histograma del Número de Mensajes Mensuales por Plan')
plt.xlabel('Número de Mensajes Mensuales')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Calcula la media y la varianza de los mensajes enviados.

# Estadísticas descriptivas por plan
messages_stats = final_data.groupby('plan_name')['messages_sent'].describe()

# Mostrar estadísticas descriptivas
print(messages_stats)


# In[39]:


# Traza un diagrama de caja para visualizar la distribución mensual de mensajes

# Visualización con diagrama de caja
plt.figure(figsize=(10, 6))
sns.boxplot(x='plan_name', y='messages_sent', data=final_data)
plt.title('Distribución de Mensajes Enviados por Plan')
plt.xlabel('Plan')
plt.ylabel('Mensajes Enviados')
plt.show()


# Se puede observar que la mayoría de los usuarios, tanto de plan Surf como de plan Ultimate, envían un número relativamente pequeño de mensajes, con una media de entre 50 y 100 mensajes. Sin embargo, también hay un pequeño porcentaje de usuarios que envían un número mucho mayor de mensajes, de hasta 250 mensajes.
# El comportamiento de los usuarios con respecto a los mensajes no varía en función del plan. Sin embargo, hay una pequeña diferencia en la distribución de los usuarios que envían un número mayor de mensajes. En el plan Surf, los usuarios que envían un número mayor de mensajes son más frecuentes que en el plan Ultimate. Esto podría deberse a que los usuarios del plan Surf tienen un límite de mensajes más bajo, por lo que pueden ser más propensos a enviar más mensajes para evitar pagar cargos adicionales. 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Muy bien.</div>

# ### Internet

# In[40]:


# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

# Visualización con gráfico de barras para el promedio de uso de Internet por mes y plan
average_internet_per_month = final_data.groupby(['plan_name', 'month'])['internet_traffic_mb'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='month', y='internet_traffic_mb', hue='plan_name', data=average_internet_per_month)
plt.title('Promedio de Consumo de Internet por Plan y Mes')
plt.xlabel('Mes')
plt.ylabel('Promedio de Consumo de Internet (MB)')
plt.xticks(rotation=45)
plt.show()


# In[41]:


# Compara el consumo de internet mensual que necesitan los usuarios de cada plan. Traza un histograma.

# Visualización con histograma para el consumo de Internet mensual por plan
plt.figure(figsize=(10, 6))
for plan in final_data['plan_name'].unique():
    sns.histplot(final_data[final_data['plan_name'] == plan]['internet_traffic_mb'], kde=True, label=plan, alpha=0.6)

plt.title('Histograma del Consumo de Internet Mensual por Plan')
plt.xlabel('Consumo de Internet Mensual (MB)')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Calcula la media y la varianza del consumo de internet.   

# Estadísticas descriptivas por plan
internet_stats = final_data.groupby('plan_name')['internet_traffic_mb'].describe()

# Mostrar estadísticas descriptivas
print(internet_stats)


# In[42]:


# Traza un diagrama de caja para visualizar la distribución del consumo de internet

# Visualización con diagrama de caja
plt.figure(figsize=(10, 6))
sns.boxplot(x='plan_name', y='internet_traffic_mb', data=final_data)
plt.title('Distribución del Consumo de Internet por Plan')
plt.xlabel('Plan')
plt.ylabel('Consumo de Internet (MB)')
plt.show()


# Se puede observar que la mayoría de los usuarios, tanto de plan Surf como de plan Ultimate, consumen una cantidad relativamente pequeña de datos, con una media de entre 10 y 20 GB. Sin embargo, también hay un pequeño porcentaje de usuarios que consumen una cantidad mucho mayor de datos, de hasta 100 GB.
# El comportamiento de los usuarios con respecto al consumo de Internet varía en función del plan. Los usuarios del plan Ultimate consumen más datos que los usuarios del plan Surf. Esto se debe a que el plan Ultimate tiene un límite de datos más alto, por lo que los usuarios tienen más libertad para consumir datos sin tener que pagar cargos adicionales.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Perfecto.</div>

# ## Ingreso

# In[43]:


# Compara los ingresos promedio por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

# Comparar los ingresos promedio por plan y mes (gráfico de barras)
average_revenue_per_month = final_data.groupby(['plan_name', 'month'])['monthly_revenue'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='month', y='monthly_revenue', hue='plan_name', data=average_revenue_per_month)
plt.title('Ingresos Promedio por Plan y Mes')
plt.xlabel('Mes')
plt.ylabel('Ingresos Promedio (USD)')
plt.xticks(rotation=45)
plt.show()


# In[44]:


# Compara el ingreso mensual que necesitan los usuarios de cada plan. Traza un histograma.

# Comparar el ingreso mensual por plan
plt.figure(figsize=(10, 6))
for plan in final_data['plan_name'].unique():
    sns.histplot(final_data[final_data['plan_name'] == plan]['monthly_revenue'], kde=True, label=plan, alpha=0.6)

plt.title('Histograma de Ingresos Mensuales por Plan')
plt.xlabel('Ingresos Mensuales (USD)')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Calcula la media y la varianza del ingreso de cada plan.

# Calcular la media y varianza del ingreso por plan
revenue_stats = final_data.groupby('plan_name')['monthly_revenue'].describe()

# Mostrar estadísticas descriptivas
print(revenue_stats)


# In[45]:


# Traza un lineplot para observar la evolución en el tiempo de cada plan en los minutos de llamadas, internet y mensajes, agregando sus ingresos.

# Crear gráficos de líneas para la evolución temporal
plt.figure(figsize=(14, 10))

# Gráfico para minutos de llamadas
plt.subplot(3, 1, 1)
sns.lineplot(x='month', y='minutes_used', hue='plan_name', data=final_data)
plt.title('Evolución Temporal de Minutos de Llamadas por Plan')
plt.xlabel('Mes')
plt.ylabel('Minutos de Llamadas')

# Gráfico para tráfico de internet
plt.subplot(3, 1, 2)
sns.lineplot(x='month', y='internet_traffic_mb', hue='plan_name', data=final_data)
plt.title('Evolución Temporal de Tráfico de Internet por Plan')
plt.xlabel('Mes')
plt.ylabel('Tráfico de Internet (MB)')

# Gráfico para mensajes
plt.subplot(3, 1, 3)
sns.lineplot(x='month', y='messages_sent', hue='plan_name', data=final_data)
plt.title('Evolución Temporal de Mensajes por Plan')
plt.xlabel('Mes')
plt.ylabel('Mensajes')

# Añadir ingresos en un gráfico adicional
plt.figure(figsize=(14, 5))
sns.lineplot(x='month', y='monthly_revenue', hue='plan_name', data=final_data)
plt.title('Evolución Temporal de Ingresos por Plan')
plt.xlabel('Mes')
plt.ylabel('Ingresos Mensuales (USD)')

plt.tight_layout()
plt.show()


# Se puede observar que la distribución de ingresos es diferente entre los dos planes. En el plan Surf, la distribución de ingresos es más uniforme, con una mayor proporción de usuarios con ingresos bajos y medios. En el plan Ultimate, la distribución de ingresos es más sesgada, con una mayor proporción de usuarios con ingresos altos.
# 
# Conclusiones sobre la diferencia de ingresos entre los planes:
# 
# La distribución de ingresos es más uniforme en el plan Surf que en el plan Ultimate.
# En el plan Surf, hay una mayor proporción de usuarios con ingresos bajos y medios.
# En el plan Ultimate, hay una mayor proporción de usuarios con ingresos altos.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Realiza un lineplot para observar la evolucion en el tiempo de cada plan en los minutos de llamadas, internet y mensajes, agregando sus ingresos.
# Podrias hacerlo en dos graficos paralelos uno con un plan y otro en el otro. Pero explora tu imaginacion y hace esa evolucion.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se realizó un lineplot para observar la evolución.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido, te quedaron muy bien.</div>

# ## Prueba las hipótesis estadísticas

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Siempre que realizamos test de hipotesis debemos exponer cual es la hipotesis nula y cual la alternativa (con un markdown). Mas alla que lo reealices o no en el codigo.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se expresa en comentarios cual es la hipotesis nula y cual es la hipotesis alternativa un lineplot para observar la evolución.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[46]:


# Prueba las hipótesis

# Descripción de las hipótesis
"""
H0 (Hipótesis nula): No hay diferencia significativa entre las medias de los ingresos mensuales de los planes 'Ultimate' y 'Surf'.
H1 (Hipótesis alternativa): Hay una diferencia significativa entre las medias de los ingresos mensuales de los planes 'Ultimate' y 'Surf'.
"""


# Filtra los ingresos por plan
ultimate_revenue = final_data[final_data['plan'] == 'Ultimate']['monthly_revenue']
surf_revenue = final_data[final_data['plan'] == 'Surf']['monthly_revenue']

# Realiza la prueba de Levene para igualdad de varianzas
levene_stat, levene_p_value = levene(ultimate_revenue, surf_revenue)

# Nivel de significancia (alfa)
alfa = 0.05


# Compara el valor p de la prueba de Levene con el nivel de significancia
if levene_p_value < alfa:
    # Las varianzas son diferentes, utilizar la prueba Welch's t
    t_stat, p_value = ttest_ind(ultimate_revenue, surf_revenue, equal_var=False)
else:
    # Las varianzas son iguales, utilizar la prueba t de Student
    t_stat, p_value = ttest_ind(ultimate_revenue, surf_revenue, equal_var=True)

# Compara el valor p con el nivel de significancia
if p_value < alfa:
    print("Rechazar la hipótesis nula: Hay evidencia suficiente para decir que hay una diferencia significativa en los ingresos promedio.")
else:
    print("No se puede rechazar la hipótesis nula: No hay suficiente evidencia para afirmar que hay una diferencia significativa en los ingresos promedio.")


# La prueba estadística realizada tiene como objetivo comparar los ingresos promedio entre los planes "Ultimate" y "Surf". A continuación, se presentan los resultados:
# 
# Hipótesis Nula (H0) y Alternativa (H1)
# 
# - H0 (Hipótesis Nula): No hay diferencia significativa entre los ingresos promedio de los planes "Ultimate" y "Surf".
# - H1 (Hipótesis Alternativa): Hay una diferencia significativa entre los ingresos promedio de los planes "Ultimate" y "Surf".
# 
# Interpretación del Resultado
# 
# El resultado de la prueba indica que no podemos rechazar la hipótesis nula (H0). En términos más sencillos, no hay suficiente evidencia estadística para afirmar que hay una diferencia significativa en los ingresos promedio entre los planes "Ultimate" y "Surf". Esto sugiere que, basándonos en los datos disponibles, los ingresos mensuales promedio de los dos planes no son significativamente diferentes.

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor </b> <a class="tocSkip"></a>
# 
# Cuando realizamos la prueba de t.estudent es muy importante un parametro que es el equal_var (False or True), que significa si existe la igualdad de varianzas o no de ambas muestras. En este trabajo no pedimos ser finos con esto pero te lo dejo a modo de que entiendas el porque y te va a servir en futuros proyecto.
# 
# El bojetivo de la prueba de t de Student es comparar las medias de dos grupos de datos y determinar si existen diferencias significativas entre ellos. Se aplica cuando estamos interesados en saber si la diferencia entre las medias es real o simplemente producto del azar.
# 
# Para esto generamos dos hipotesis H0 y H1 (nula y alternativa, respectivamente).
# 
# Hipótesis nula (H0): No hay diferencia significativa entre las medias de los dos grupos.
# Hipótesis alternativa (H1): Hay una diferencia significativa entre las medias de los dos grupos.
# 
# En este caso realizas  una observacion de las dos varianzas, lo que no esta mal, pero depender únicamente de la diferencia en los valores de las varianzas puede llevar a conclusiones equivocas, mas que nada si las muestras tienen tamaños diferentes . Las pruebas estadísticas están diseñadas para tomar en cuenta el tamaño de la muestra y calcular si la diferencia observada en las varianzas es estadísticamente significativa o si podría deberse al azar.
# 
# Para saber lo del equal_var utilizamos La función levene en scipy.stats que se utiliza para realizar una prueba de igualdad de varianzas entre dos grupos de datos. (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html)
# 
# Los resultados  de esta prueba es muy parecido a lo que hacemos en el t.student. Ya que Si el valor p obtenido en la prueba levene es mayor que un nivel de significancia (alpha) previamente elegido (por ejemplo, 0.05), entonces asumimos que las varianzas son iguales (aceptamos H0).
# Si el valor p es menor que alpha, rechazamos la hipótesis nula y asumimos que las varianzas son diferentes.
# 
# Por lo tanto, si las varianzas son iguales (aceptamos H0 en la prueba levene), puedes establecer equal_var=True al realizar la prueba t de Student.
# Si las varianzas son diferentes (rechazamos H0 en la prueba levene), debes establecer equal_var=False al realizar la prueba t de Student. Esto indica que se debe usar una versión de la prueba t que no asuma igualdad de varianzas, como la prueba Welch's t.
# 
# Siempre recordar que los outliers pueden impactar negativamente en esta prueba (t.student)
# 
# Esto es basicamente por lo que te corrijo lo del equal_var pero es como consejo y que lo sepas a futuro. Esta en vos si lo queres modificar o no.
# 
# </div>

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Explicale al cliente en un markdown que arrojo la prueba estadistica.</div>

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Siempre que realizamos test de hipotesis debemos exponer cual es la hipotesis nula y cual la alternativa (con un markdown). Mas alla que lo reealices o no en el codigo.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se realizó la explicación del resultado de la prueba estadistica al cliente.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Excelente como abarcaste todo eduardo.</div>

# In[47]:


# Prueba las hipótesis

# Fusiona los datos combinados con la información de los usuarios
final_data = final_data.merge(megaline_users_df[['user_id', 'region']], on='user_id', how='left')

# Filtra los ingresos por área NY-NJ y otras regiones
ny_nj_income = final_data[final_data['region'] == 'NY-NJ']['monthly_revenue']
other_regions_income = final_data[final_data['region'] != 'NY-NJ']['monthly_revenue']

# Elabora las hipótesis nula y alternativa
# H0: El ingreso promedio de los usuarios del área NY-NJ es igual al de los usuarios de otras regiones.
# H1: El ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.

# Realiza la prueba t para dos muestras independientes
t_stat, p_value = ttest_ind(ny_nj_income, other_regions_income, equal_var=False)

# Nivel de significancia (alfa)
alfa = 0.05

# Compara el valor p con el nivel de significancia
if p_value < alfa:
    print("Rechazar la hipótesis nula: Hay evidencia suficiente para decir que hay una diferencia significativa en los ingresos promedio.")
else:
    print("No se puede rechazar la hipótesis nula: No hay suficiente evidencia para afirmar que hay una diferencia significativa en los ingresos promedio.")



# Resultados de la Prueba Estadística
# La prueba estadística realizada tiene como objetivo comparar los ingresos promedio entre los usuarios del área NY-NJ y aquellos de otras regiones. 
# 
# Hipótesis Nula (H0) y Alternativa (H1)
# H0 (Hipótesis Nula): El ingreso promedio de los usuarios del área NY-NJ es igual al de los usuarios de otras regiones.
# H1 (Hipótesis Alternativa): El ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.
# 
# Interpretación del Resultado
# El resultado de la prueba indica que no podemos rechazar la hipótesis nula (H0). En términos más sencillos, no hay suficiente evidencia estadística para afirmar que hay una diferencia significativa en los ingresos promedio entre los usuarios del área NY-NJ y los de otras regiones. Esto sugiere que, basándonos en los datos disponibles, los ingresos mensuales promedio de estos dos grupos de usuarios no son significativamente diferentes.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Explicale al cliente en un markdown que arrojo la prueba estadistica.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se realizó la explicación del resultado de la prueba estadistica al cliente.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Conclusión general
# 
# Conclusión General del Proyecto:
# 
# Carga e Importación de Datos:
# Se realizó la carga e importación de los datos provenientes de Megaline, incluyendo información sobre llamadas, mensajes, uso de internet, planes de servicio y usuarios.
# 
# Exploración y Limpieza de Datos:
# Se exploraron los conjuntos de datos para comprender su estructura y contenido.
# Se realizaron transformaciones y limpieza de datos, como la conversión de formatos de fecha, manejo de duplicados y adición de nuevas columnas relevantes.
# 
# Análisis Exploratorio de Datos (EDA):
# Se realizó un EDA para obtener información clave sobre patrones y tendencias en el uso de servicios por parte de los usuarios.
# 
# Generación de Métricas Mensuales:
# Se calcularon métricas mensuales, incluyendo el número de llamadas, minutos utilizados, mensajes enviados y tráfico de internet por usuario y por mes.
# 
# Análisis de Ingresos:
# Se calcularon los ingresos mensuales para cada usuario, considerando las tarifas de los planes y los costos adicionales por uso excedido.
# 
# Pruebas de Hipótesis:
# Se llevaron a cabo pruebas de hipótesis para evaluar si existen diferencias significativas en los ingresos promedio entre diferentes planes de servicio y entre el área NY-NJ y otras regiones.
# 
# Conclusiones Importantes:
# Prueba de Hipótesis para Ingresos entre Planes:
# No se encontró evidencia suficiente para afirmar que hay una diferencia significativa en los ingresos promedio entre los planes Ultimate y Surf.
# 
# Prueba de Hipótesis para Ingresos entre Área NY-NJ y Otras Regiones:
# Tampoco se encontró suficiente evidencia para afirmar que hay una diferencia significativa en los ingresos promedio entre el área NY-NJ y otras regiones.
# 
# Notas Importantes:
# Se emplearon pruebas t de dos muestras independientes para ambas pruebas de hipótesis.
# Se estableció un nivel de significancia (alfa) de 0.05 para ambas pruebas.
# En resumen, el proyecto proporcionó insights valiosos sobre el comportamiento de los usuarios de Megaline, desde el análisis exploratorio hasta la evaluación de hipótesis, contribuyendo a una comprensión más profunda de los patrones de consumo y los ingresos asociados.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda realizar una conclusion general que contenga todo lo que se hizo en el proyecto de forma enumerada o items.
# 
# Desde la carga e importacion, pasando por los cambios realizado (Y el porque de esas decisiones). Agregando lo que se hizo en cada seccion a modo resumen y las conclusiones del  trabajo.
# 
# Sirve como resumen de lo realizado en cada proyecto.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Corrección realizada, se realizó una conclusión general mas detallada como se sugiere.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario General #1</b> <a class="tocSkip"></a>
# 
# Eduardo, en primer lugar dejame decirte que hiciste un muy buen trabajo.
# 
# Si bien parece que son muchas las correcciones, el trabajo es extenso y  muchos son simples detalles (como cambiar las celdas de  lugar por una cuestion de esturctura), pero el trabajo que entregaste esta muy bien a nivel analisis, codigo y minuciosidad de buscar las divisiones pertinentes para cada dataset.
# 
# No quise corregirte los analisis de los graficos ya que quedan sujetos a las correcciones (Los redondeos mas que nada), pero en general esta muy bien realizado.
# 
# Como consejo, luego de realizar el merge mostra como quedo el dataset final con una tabla.
# 
# Hiciste un muy buen trabajo y quedo atento a las correcciones, saludos.</div>
# 
# <div class="alert alert-block alert-success">
# 
# <b>Comentario General #2</b> <a class="tocSkip"></a>
# 
# Eduardo, si bien habia varias correcciones para tocar las abarcaste todas y superaste mis expectativas. Ya que abarcaste tanto las descripciones como el codigo.
# 
# Me encantaron tus observaciones y analisis, ya que agregas valor agregado en cada celda.
# 
# Ademas, todas las correcciones las tocaste y mejoraste cada cosa que te comente.
# 
# Mantengo mis consejos de hacer una tabla final (mostrar el df) y utilizar mas el display() para mayor legibilidad.
# 
# El trabajo obviamente queda **aprobado**.
# 
# Exitos en lo que viene, saludos.</div>

# In[ ]:




