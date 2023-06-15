import matplotlib.pyplot as plt

def graficar_vm(valor_medio):
    # Ajustar la escala del eje y para ver el valor medio con mayor precisión
    y_margin = abs(valor_medio) * 0.1  # Margen del 10% alrededor del valor medio

    # Graficar el valor medio
    plt.figure(figsize=(6, 4))
    plt.axhline(valor_medio, color='r', linestyle='--', label='Valor Medio')
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Valor Medio de la Señal')
    plt.ylim(valor_medio - y_margin, valor_medio + y_margin)  # Ajustar los límites del eje y
    plt.legend()
    plt.grid(True)
    plt.show()

    return
