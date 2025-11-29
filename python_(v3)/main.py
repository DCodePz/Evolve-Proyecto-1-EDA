from DataSet import LimpiadorDataset, VisualizadorDataset

def limpieza():
    ruta_original = "data/movie_metadata.csv"
    ruta_guardar ="data/imdb_5000_movies_limpio.csv"

    nuevo_orden = [
        # Información básica de la película
        "Movie Title", "Title Year", "Movie Imdb Link", "Language", "Country", "Content Rating",
        # Información cinematográfica
        "Duration", "Color", "Genres", "Aspect Ratio", "Plot Keywords", "Facenumber In Poster",
        # Reparto
        "Director Name", "Actor 1 Name", "Actor 2 Name", "Actor 3 Name",
        # Dinero
        "Budget", "Gross",
        # Calidad
        "Num Voted Users", "Num User For Reviews", "Num Critic For Reviews", "Imdb Score",
        # Facebook
        "Director Facebook Likes", "Actor 1 Facebook Likes", "Actor 2 Facebook Likes",
        "Actor 3 Facebook Likes", "Cast Total Facebook Likes", "Movie Facebook Likes"
    ]

    por0 = ["Director Facebook Likes", "Actor 1 Facebook Likes", "Actor 2 Facebook Likes", 
            "Actor 3 Facebook Likes", "Facenumber In Poster"]
    porMediana = ["Duration", "Budget", "Num Critic For Reviews", "Num User For Reviews", "Gross",
                  "Title Year"]
    porModa = ["Color", "Language", "Country", "Aspect Ratio"]
    porUnknown = ["Content Rating", "Actor 1 Name", "Actor 2 Name", "Actor 3 Name", "Director Name",
                  "Plot Keywords", "Language"]

    col_float = ["Aspect Ratio", "Budget", "Gross", "Imdb Score"]
    col_int = ["Title Year", "Duration", "Facenumber In Poster", "Num Voted Users", "Num User For Reviews", "Num Critic For Reviews", "Director Facebook Likes", 
            "Actor 1 Facebook Likes", "Actor 2 Facebook Likes", "Actor 3 Facebook Likes", "Cast Total Facebook Likes", "Movie Facebook Likes"]
    col_string = ["Movie Title", "Movie Imdb Link", "Language", "Country", "Content Rating", "Color",
              "Genres", "Plot Keywords", "Director Name", "Actor 1 Name",
              "Actor 2 Name", "Actor 3 Name", ]

    valores_multiples = ["Genres", "Plot Keywords"]

    # ---------- 

    limpiador = LimpiadorDataset(ruta_original)

    limpiador.limpieza(
        nuevo_orden, ruta_guardar, 
        por0, porMediana, porModa, porUnknown, 
        col_float, col_int, col_string, 
        valores_multiples)

    # dataset = limpiador.get_dataset()
    # print(dataset)

def visualizacion():
    visualizador = VisualizadorDataset("data/imdb_5000_movies_limpio.csv")

    # Histograma
    visualizador.histograma("Imdb Score")

    # Barras 1
    old_dataset = visualizador.get_dataset()
    actores = visualizador.get_dataset(["Actor 1 Name", "Actor 1 Facebook Likes"])
    visualizador = visualizador.set_dataset(actores)
    actores = visualizador.agrupacion("Actor 1 Facebook Likes", "Actor 1 Name", "Suma", ordenar="Desc", top=5)
    visualizador = visualizador.set_dataset(actores)
    visualizador.barras(actores, desde="Valor", extra="Actores")

    # Barras 2
    visualizador.set_dataset(old_dataset)
    visualizador.barras("Genres", True)

    # Lineas
    visualizador.lineas("Title Year", "Imdb Score", "Genres", 5, True)

    # Barras agrupadas
    visualizador.calculo_variable("-", "Gross", "Budget", "Profit")
    suma = visualizador.agrupacion("Profit", "Director Name", "Suma")
    media = visualizador.agrupacion("Profit", "Director Name", "Media")
    visualizador.barras_comparadas("Director Name", 
                                "Profit",
                                suma,
                                media,
                                5, "acumulado", "medio")

if __name__ == "__main__":
    limpieza()
    visualizacion()