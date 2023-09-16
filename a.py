import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Math

# Al ingresar una funcion en coordenadas cartesianas , debe
# hacerse en terminos de x, y . Tambien coordenas cilindricas
# y esfericas en terminos de r theta phi
x, y, r, theta, phi = sp.symbols('x y r theta phi')
# Entrada del usuario
# --- Solicitamos al usuario que introduzca la funcion
# expresada en terminos de x, y
expression = input("Introduce la funcion en coordenadas cartesianas (en terminos de x , y) \nPor ejemplo , x **2 + y**2\nTambien puede ingresar funciones de numpy sin elprefijo (np.) \n - - - >")
# Se convierte a una expresion simbolica cartesiana
f_cart = sp.parse_expr(expression)
# Se convierte la expresion simbolica a una funcion que pueda ser evaluada por numpy
f_cart_eval = sp.lambdify((x , y) , f_cart ,'numpy')
# ---- COORDENADAS CARTESIANAS ----
# A partir de los planos x, y se define el espacio en 3 D que
# se va a mostrar en el grafico
x_range = np.linspace(-10, 10, 100) # Rango en x
y_range = np.linspace(-10, 10, 200) # Rango en y
# Se generan los planos cartesianos x, y
x_values = np.zeros((len(x_range),len(y_range)))
y_values = np.zeros((len(x_range), len(y_range)))
# Se rellena el plano con los valores de x, y definidos
# anteriormente
for i in range(len(x_range)):
    for j in range(len(y_range)):
        x_values[i, j] = x_range [i]
        y_values[i, j] = y_range [j]
# Se evalua la funcion en cada punto del espacio
z_values = f_cart_eval(x_values , y_values)
# Se crea el canvas 3 D
canvas = plt.figure().add_subplot(projection = '3d')
# Se indica la grafica y que coordenadas se usaron
print('Graficando:')
display(Math("z =" + sp.latex(f_cart)))
# Se grafica la superficie
canvas.plot_surface(x_values , y_values , z_values , cmap = "viridis")
# Titulo
canvas.set_title ("Coordenadas cartesianas")
# Se indican los ejes
canvas.set_xlabel("Eje x")
canvas.set_ylabel("Eje y")
canvas.set_zlabel("Eje z")
# Mostrar el grafico
plt.show()
# ---- COORDENADAS CILINDRICAS ----
# Transformaciones
# --- Se calculan los nuevos valores de x , y en terminos de r, theta
x_cyl = r * sp.cos(theta)
y_cyl = r * sp.sin(theta)
# Se evaluan en la funcion cartesiana introducida al principio
f_cyl = f_cart.subs([( x , x_cyl ) , (y , y_cyl )]) # Se reemplaza x , y
# Crear un arreglo de valores para los rangos de r , theta
r_range = np.linspace (0 , 10 , 100) # En este caso , el valor del radio es de 0 a 10
theta_range = np.linspace(0 , 2 * np.pi , 100)
# Se generan los valores para r , theta
r_values = np.zeros ((len(r_range), len(theta_range)))
theta_values = np.zeros((len(r_range), len(theta_range)))
for i in range (len(r_range)):
    for j in range (len(theta_range)):
        r_values [i,j] = r_range[i]
        theta_values[i,j] = theta_range[j]
# Se evalua la funcion segun el valor de radio y angulo
f_cyl_eval = sp.lambdify((r, theta), f_cyl, "numpy")
z_values = f_cyl_eval(r_values , theta_values)
# Se crea el canvas 3D
canvas = plt.figure().add_subplot(projection = "3d")
# Se indica la grafica y que coordenadas se usaron
print("Graficando :")
display(Math("z =" + sp.latex(f_cyl)))
# Se grafica la superficie
# Para hacerlo , se evaluan los valores de r , theta en las funciones : x = r * cos ( theta )
# y = r*sin(theta)
canvas.plot_surface(r_values*np.cos(theta_values), r_values*np.sin(theta_values), z_values , cmap = "viridis")
# Titulo
canvas.set_title("Coordenadas cilindricas")
# Se indican los ejes
canvas.set_xlabel("Eje x")
canvas.set_ylabel("Eje y")
canvas.set_zlabel("Eje z")
# Mostrar el grafico
plt.show()
# ---- COORDENADAS ESFERICAS ----
# Transformaciones
# --- Se calculan los nuevos valores de x , y en terminos de r, theta , phi
x_sph = r*sp.sin(phi)*sp.cos(theta)
y_sph = r*sp.sin(phi)*sp.sin(theta)
# Se evaluan en la funcion cartesiana introducida al principio
f_sph = f_cart.subs([(x , x_sph), (y , y_sph)]) # Se reemplaza x , y
# Crear un arreglo de valores para los rangos de r , theta ,phi
r_range = np.linspace(0, 10, 100) # En este caso , el valor del radio es de 0 a 10
theta_range = np.linspace(0, 2*np.pi, 100)
phi_range = np.linspace(0 , np . pi , 100)
# Se generan los valores para r , theta , phi
r_values = np.zeros((len(r_range) ,len(theta_range), len(phi_range)))
theta_values = np.zeros((len(r_range), len(theta_range), len(phi_range)))
phi_values = np.zeros((len(r_range), len(theta_range), len(phi_range)))
for i in range(len(r_range)):
    for j in range(len(theta_range)):
        for k in range(len(phi_range)):
            r_values[i , j , k] = r_range[i]
            theta_values[i , j , k] = theta_range[j]
            phi_values[i, j , k] = phi_range[k]
# Se evalua la funcion segun el valor de r , theta , phi
f_sph_eval = sp.lambdify((r , theta , phi ),f_sph,"numpy")
# Se obtiene un arreglo de 3 dimensiones con todos los puntos en el espacio 3 D a graficar
points_3d = f_sph_eval(r_values,theta_values, phi_values)
# Se crea el canvas 3 D
canvas = plt.figure().add_subplot( projection = "3d")
# Se indica la grafica y que coordenadas se usaron
print("Graficando :")
display(Math(sp.latex(f_sph)))
# Se grafica la superficie
# Para hacerlo , se evaluan los valores de r , theta en las funciones : x = r * sin ( phi ) * cos ( theta )
# y = r * sin(phi) * sin(theta)
canvas.scatter3D(r_values * np.sin( phi_values ) * np.cos(theta_values ) , r_values * np.sin(phi_values) * np.sin(theta_values ) , points_3d , c = points_3d , cmap = "viridis")
# Titulo
canvas.set_title("Coordenadas esfericas")
# Se indican los ejes
canvas.set_xlabel("Eje x")
canvas.set_ylabel("Eje y")
canvas.set_zlabel("Eje z")
# Mostrar el grafico
plt.show()