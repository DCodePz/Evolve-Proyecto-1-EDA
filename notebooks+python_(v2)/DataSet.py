import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

class LimpiadorDataset:
    def __init__(self, ruta):
        self.dataset = pd.read_csv(ruta)
        print(f"Dataset cargado desde {ruta}.")

    def listar_columnas(self):
        return list(self.dataset.columns)

    def renombrar_columnas(self, nuevo_orden=None):
        self.dataset.columns = [col.replace("_", " ").title() for col in self.dataset.columns]
        if nuevo_orden:
            self.dataset = self.dataset[nuevo_orden]
        print("Se han renombrado las columnas.")
        return self

    def revisar_nulos(self, por0, porMediana, porModa, porUnknown):
        for col in por0:
            self.dataset[col] = self.dataset[col].fillna(0)
        
        for col in porMediana:
            self.dataset[col] = self.dataset[col].fillna(self.dataset[col].median())
        
        for col in porModa:
            self.dataset[col] = self.dataset[col].fillna(self.dataset[col].mode()[0])
        
        for col in porUnknown:
            self.dataset[col] = self.dataset[col].fillna("Unknown")

        print("Se han revisado los nulos.")
        
        return self
    
    def correccion_numericos(self, col_float, col_int): 
        for col in col_float: 
            self.dataset[col] = self.dataset[col].astype(float) 
        
        for col in col_int: 
            self.dataset[col] = self.dataset[col].astype(int) 
        
        print("Se han corregido los tipos de datos.")
        return self

    def normalizacion_strings(self, col_string):
        for col in col_string:
            self.dataset[col] = self.dataset[col].astype(str).str.strip()
        print("Se han normalizado los strings.")
        return self

    def limpiar_valores_multiples(self, columna):
        self.dataset = self.dataset.reset_index(drop=True)
        for i in range(len(self.dataset)):
            generos = self.dataset.loc[i, columna]
            partes = generos.split("|")
            partes_limpias = [re.sub(r'[\n\t"]', '', g.strip()) for g in partes]
            self.dataset.loc[i, columna] = "|".join(partes_limpias)
        print("Se han limpiado los valores múltiples.")
        return self

    def revisar_duplicados(self):
        duplicadas = self.dataset[self.dataset.duplicated(keep="first")]
        num = duplicadas.shape[0]
        self.dataset.drop_duplicates(inplace=True)
        print(f"Se han eliminado {num} líneas duplicadas.")
        return self

    def guardar(self, ruta):
        self.dataset.to_csv(ruta, index=False)
        print(f"Dataset guardado en {ruta}.")
        return self

    def get_dataset(self):
        return self.dataset
    
    def limpieza(self, nuevo_orden, ruta, por0=[], porMediana=[], porModa=[], porUnknown=[], col_float=[], col_int=[], col_string=[], valores_multiples=[]):
        self \
            .renombrar_columnas(nuevo_orden) \
            .revisar_nulos(por0, porMediana, porModa, porUnknown) \
            .correccion_numericos(col_float, col_int) \
            .normalizacion_strings(col_string)

        for valor in valores_multiples:
            self.limpiar_valores_multiples(valor)

        self \
            .revisar_duplicados() \
            .guardar(ruta)
        
        return self
    
class VisualizadorDataset:
    def __init__(self, ruta):
        self.dataset = pd.read_csv(ruta)
        print(f"Dataset cargado desde {ruta}.")
    
    def get_dataset(self, variables=None):
        if variables is None:
            return self.dataset
        return self.dataset[variables]

    def set_dataset(self, dataset):
        self.dataset = dataset
        return self
    
    def histograma(self, variable):
        plt.figure(figsize=(8, 5))
        plt.gcf().canvas.manager.set_window_title("Histograma")
        sns.histplot(self.dataset[variable], bins=20, kde=True, color="blue")
        plt.title(f"Histograma de {variable}")
        plt.xlabel(variable)
        plt.ylabel("Frecuencia")
        plt.show()

    def combinar_variables(self, var1, var2):
        return self.dataset[[var1, var2]]

    def barras(self, variable, multiple=False, separador="|", desde="Var", extra=""):
        if desde=="Var":
            if multiple:
                datos = self.dataset[variable].str.split(separador).explode().value_counts()
            else:
                datos = self.dataset[variable]
        elif desde=="Valor":
            datos = variable


        plt.figure(figsize=(12,6))
        plt.gcf().canvas.manager.set_window_title("Barras")
        datos.plot(kind='bar', color='lightgreen')
        if desde=="Var":
            plt.title(f'Gráfico de barras de {variable}')
            plt.xlabel(variable)
        elif desde=="Valor":
            plt.title('Gráfico de barras')
            plt.xlabel(extra)
        plt.ylabel('Cantidad')
        plt.xticks(rotation=45)
        plt.show()
    
    def lineas(self, var_x, var_y, var_dato, top, multiple=False, separador="|"):
        if multiple:
            datos = self.dataset.assign(Data=self.dataset[var_dato].str.split('|')).explode('Data')
        else:
            datos = self.dataset.assign(Data=self.dataset[var_dato]).explode('Data')

        
        top_datos = datos['Data'].value_counts().head(top).index

        promedios = []
        for dato in top_datos:
            temp = self.dataset[self.dataset[var_dato] == dato].groupby(var_x)[var_y].mean().reset_index()
            temp[var_dato] = dato
            promedios.append(temp)
        promedios = pd.concat(promedios, ignore_index=True)

        plt.figure(figsize=(14,7))
        plt.gcf().canvas.manager.set_window_title("Líneas")
        sns.lineplot(data=promedios, x=var_x, y=var_y, hue=var_dato, marker='o')

        plt.title(f'Gráfico de lineas de {var_y} por top {top} {var_dato}')
        plt.xlabel(var_x)
        plt.ylabel(var_y)
        plt.legend(title=var_dato)
        plt.grid(True)
        plt.show()

    def calculo_variable(self, operacion, var1, var2, nombre):
        if operacion=="+":
            self.dataset[nombre] = self.dataset[var1] + self.dataset[var2]
            print(f"Variable '{nombre}' calculada.")
            return self.dataset[var1] + self.dataset[var2]
        elif operacion=="-": 
            self.dataset[nombre] = self.dataset[var1] - self.dataset[var2]
            print(f"Variable '{nombre}' calculada.")
            return self.dataset[var1] - self.dataset[var2]
        
    def agrupacion(self, var_objetivo, var_agrupar, accion, ordenar="No", top=0):
        resultado = self.dataset.groupby(var_agrupar)[var_objetivo]

        # Operación
        if accion == "Suma":
            resultado = resultado.sum()
        elif accion == "Media":
            resultado = resultado.mean()

        # Ordenación
        if ordenar == "Asc":
            resultado = resultado.sort_values(ascending=True)
        elif ordenar == "Desc":
            resultado = resultado.sort_values(ascending=False)
        
        # Top
        if top != 0:
            resultado = resultado.head(top)
            

        return resultado



    def barras_comparadas(self, var_x, var_y, dato1, dato2, top, extra1="", extra2=""):
        dato_1 = dato1.sort_values(ascending=False).head(top)
        dato_2 = dato2.sort_values(ascending=False).head(top)

        fig, axes = plt.subplots(1, 2, figsize=(18,6))   # 1 fila, 2 columnas
        plt.gcf().canvas.manager.set_window_title("Gráfico de barras agrupadas")

        # --- SUBGRAFICO 1 ---
        dato_1.plot(kind='bar', color='mediumseagreen', ax=axes[0])
        axes[0].set_title(f'Top {top} {var_x} por {var_y} {extra1}')
        axes[0].set_xlabel(var_x)
        axes[0].set_ylabel(var_y)
        axes[0].tick_params(axis='x', rotation=45)


        # --- SUBGRAFICO 2 ---
        dato_2.plot(kind='bar', color='mediumseagreen', ax=axes[1])
        axes[0].set_title(f'Top {top} {var_x} por {var_y} {extra2}')
        axes[1].set_xlabel(var_x)
        axes[1].set_ylabel(var_y)
        axes[1].tick_params(axis='x', rotation=45)

        # Etiquetas
        for i, value in enumerate(dato_1):
            axes[0].text(i, value, f'{value:,.0f}', ha='center', va='bottom', fontsize=9)
        for i, value in enumerate(dato_2):
            axes[1].text(i, value, f'{value:,.0f}', ha='center', va='bottom', fontsize=9)

        plt.tight_layout()
        plt.show()
