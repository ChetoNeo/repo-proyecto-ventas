import pandas as pd
import matplotlib.pyplot as plt
import os

def ejecutar_analisis_ventas():
    ruta_datos = "datos/dataset.csv"
    ruta_resultados = "resultados/grafico_resultados.png"
    
    df = pd.read_csv(ruta_datos)
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    df['sales_amount'] = pd.to_numeric(df['sales_amount'])
    
    print("--- INFORME DE RESULTADOS ESTADÍSTICOS ---")
    print(f"1. Ventas Totales de la Empresa: ${df['sales_amount'].sum():,.2f}")
    
    producto_top = df.groupby('product')['quantity'].sum().idxmax()
    print(f"2. Producto más vendido de la temporada: {producto_top}")
        
    df['mes_año'] = df['sales_date'].dt.to_period('M')
    print("\n3. Desglose analítico de ventas mensuales:")
    print(df.groupby('mes_año')['sales_amount'].sum())
    
    plt.figure(figsize=(10, 5))
    df.groupby('mes_año')['sales_amount'].sum().plot(kind='line', marker='o', color='darkblue', linewidth=2)
    plt.title('EVOLUCIÓN TEMPORAL DE VENTAS - ESCENARIO B', fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(ruta_resultados)
    plt.close()
    print(f"\n[ÉXITO] Gráfico guardado en: {ruta_resultados}")

if __name__ == "__main__":
    ejecutar_analisis_ventas()
