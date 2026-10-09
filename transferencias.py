import tkinter as tk
ARCHIVO="empleados.txt"
def main():
   print(f"acreditacion de sueldos")
def calcular():
 with open (ARCHIVO,"r",encoding="utf-8") as archivo:
         total = 0.0
         cantidad = 0
         for linea in archivo:
            empleado=linea.strip()
            if empleado!="":
             legajo,nombre,cbu,salario=empleado.split(";")
             #print (cbu)
             salario=float(salario)
             print(f"se transfiero al cbu {cbu}el monto de $ {salario}")
             total=total+salario
             cantidad=cantidad+1
            lbl_cantidad.config(text=f"empleados:{cantidad}")
            lbl_total.config(text=f"monto total: $ {total:.2f}")
 print("hola")
if __name__=="__main__":
    try:
        main()
        # --- Construcción de la ventana ---
        ventana = tk.Tk()
        ventana.title("Transferencias")
        ventana.geometry("350x200")
        lbltitulo=tk.Label(ventana,text="resumen de transferencias",font=("arial",15,"bold"))
        lbltitulo.pack(pady=10)
        btn_calcular=tk.Button(ventana,text="transferir",command=calcular)
        btn_calcular.pack(pady=10)
        lbl_cantidad = tk.Label(ventana, text="Empleados: -", font=("Arial", 12))
        lbl_cantidad.pack(pady=5)
        lbl_total = tk.Label(ventana, text="Total a depositar: -", font=("Arial", 12))
        lbl_total.pack(pady=5)
        ventana.mainloop()
    except FileNotFoundError:
       print("No se encontro el archivo ")