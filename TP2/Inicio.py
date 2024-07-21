pip install pandas # type: ignore
import pandas as pd

df1 = pd.read_csv('C:\Users\jluman\Desktop\TP\TP2\ecommerce_customers_dataset.csv'.decode('utf-8'))
df2 = pd.read_csv('C:\Users\jluman\Desktop\TP\TP2\ecommerce_orders_dataset.csv'.decode('utf-8'))
df3 = pd.read_csv('C:\Users\jluman\Desktop\TP\TP2\ecommerce_order_payments_dataset.csv'.decode('utf-8'))
df4 = pd.read_csv('C:\Users\jluman\Desktop\TP\TP2\ecommerce_order_items_dataset.csv'.decode('utf-8'))
df5 = pd.read_csv('C:\Users\jluman\Desktop\TP\TP2\ecommerce_customers_dataset.csv'.decode('utf-8'))

"""##2.2) ***PREGUNTAS TP***
**1.- Establecer la columna índices de las tablas como la clave primaria en
el DataFrame, ejemplo para customers la clave será customer_id.**
"""
df1.set_index('product_id', inplace=True)
df2.set_index('order_id', inplace=True)
df3.set_index('order_id', inplace=True)
df4.set_index('order_id', inplace=True)
df5.set_index('customer_id', inplace=True)
print(f"COMPLETADO: Indice para los 5 archivos creados en los distintos df")

"""**2.- Obtener el número total de clientes únicos en el conjunto de datos**"""

clientes_unicos = df5['customer_unique_id'].nunique()
print(f"COMPLETADO: El número total de clientes únicos son: {clientes_unicos}")

"""**3.- Calcular el promedio de valor de pago por pedido**"""

Promedio = df3.groupby('order_id')['payment_value'].mean()
print(f"COMPLETADO: Se muestran el promedio pagado por pedidos realizados: \n{Promedio}")

"""**4.- Determinar la categoría de producto más vendida**"""

Max_venta = df1['product_category_name'].value_counts().idxmax()
apariciones = df1['product_category_name'].value_counts()
print(f"COMPLETADO: La categoría de producto más vendida es: \n{Max_venta}")
print(f"\nLos Productos mas vendidos son: \n{apariciones}")

"""**5.- Calcular el número total de pedidos realizados**"""

total_orders = df2.shape[0]
print(f'COMPLETADO: Número total de pedidos realizados: {total_orders}')