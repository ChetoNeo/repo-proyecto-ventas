import pandas as pd
import matplotlib.pyplot as plt
import os

def ejecutar_analisis_ventas():
    ruta_datos = "datos/dataset.csv"
    ruta_resultados = "resultados/grafico_resultados.png"
    
    if not os.path.exists(ruta_datos):
        print(f"Error: No se encontró el archivo en {ruta_datos}")
        return
        
    df = pd.read_csv(ruta_datos)
    
    df.columns = df.columns.str.strip()
    
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    df['sales_amount'] = pd.to_numeric(df['sales_amount'])
    
    print("--- INFORME DE RESULTADOS ESTADÍSTICOS ---")
    
    ventas_totales = df['sales_amount'].sum()
    print(f"1. Ventas Totales de la Empresa: ${ventas_totales:,.2f}")
    
    if 'product' in df.columns:
        producto_top = df.groupby('product')['quantity'].sum().idxmax()
        print(f"2. Producto más vendido de la temporada: {producto_top}")
    else:
        fecha_top = df.groupby('sales_date')['sales_amount'].sum().idxmax()
        print(f"2. Fecha con mayor índice de facturación: {fecha_top.strftime('%Y-%m-%d')}")
        
    df['mes_año'] = df['sales_date'].dt.to_period('M')
    ventas_por_mes = df.groupby('mes_año')['sales_amount'].sum()
    print("\n3. Desglose analítico de ventas mensuales:")
    print(ventas_por_mes)
    
    plt.figure(figsize=(10, 5))
    ventas_por_mes.plot(kind='line', marker='o', color='darkblue', linewidth=2)
    plt.title('EVOLUCIÓN TEMPORAL DE VENTAS - ESCENARIO B', fontsize=12, fontweight='bold')
    plt.xlabel('Periodo Mensual', fontsize=10)
    plt.ylabel('Monto Total Facturado ($)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    plt.savefig(ruta_resultados)
    plt.close()
    print(f"\n[ÉXITO] Gráfico guardado correctamente en la ruta: {ruta_resultados}")

if __name__ == "__main__":
    ejecutar_analisis_ventas()
