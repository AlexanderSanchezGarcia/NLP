texto1 ="jose va a reprobar la materia de pln ya que no le gusta poner atencion"
import time
import tracemalloc
import numpy as np
from pathlib import Path
import os
from typing import List, Tuple, Dict
import argparse

# Stopwords ampliadas (ES + EN). Basadas en listas comunes (Snowball/NLTK) y extendidas.
# Se declaran como conjuntos para eficiencia en las búsquedas.
STOPWORDS_ES = {
    'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una',
    'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'fue', 'este', 'ha', 'sí', 'porque', 'esta',
    'son', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde',
    'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e',
    'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos',
    'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros',
    'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mío', 'mía',
    'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra',
    'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está',
    'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén', 'estaré', 'estarás', 'estará',
    'estaremos', 'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba',
    'estabas', 'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis',
    'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses',
    'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he',
    'has', 'ha', 'hemos', 'habéis', 'han', 'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá',
    'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais', 'habrían', 'había', 'habías',
    'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera',
    'hubieras', 'hubiéramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos', 'hubieseis', 'hubiesen',
    'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas',
    'seamos', 'seáis', 'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería', 'serías', 'seríamos',
    'seríais', 'serían', 'era', 'eras', 'éramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis',
    'fueron', 'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen', 'siendo', 'sido', 'tengo', 'tienes', 'tiene',
    'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tendré', 'tendrás', 'tendrá',
    'tendremos', 'tendréis', 'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía',
    'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron',
    'tuviera', 'tuvieras', 'tuviéramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis',
    'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened'
}

STOPWORDS_EN = {
    'the', 'of', 'in', 'on', 'a', 'an', 'some', 'and', 'that', 'this', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'do', 'does', 'did', 'to', 'for', 'from', 'with', 'as', 'by', 'at', 'it', 'its',
    'itself', 'if', 'then', 'else', 'than', 'too', 'very', 'can', 'cannot', 'could', 'should', 'would', 'will',
    'just', 'not', 'no', 'nor', 'so', 'or', 'but', 'because', 'about', 'into', 'over', 'after', 'before', 'between',
    'during', 'out', 'up', 'down', 'off', 'above', 'below', 'again', 'further', 'here', 'there', 'when', 'where',
    'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'such', 'only', 'own', 'same',
    'until', 'while', 'whom', 'who', 'whose', 'which', 'what', 'their', 'theirs', 'them', 'they', 'you', 'your',
    'yours', 'we', 'our', 'ours', 'he', 'him', 'his', 'she', 'her', 'hers', 'my', 'mine', 'me', 'i'
}

def indice_palabra(palabra, vec_palabras):
    for j in range(len(vec_palabras)):
        if vec_palabras[j] == palabra:
            return j

class Tokenizer:
    """ Class for tokenizing text """
    delimiter = ""
    
    """ Constructor """
    def __init__(self):
        self.delimiter = " \t\n\r\f\v" + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}"

    """ Methods """
    def verify_word(self, text:str) -> str:
        numbers = "0123456789"
        is_only_number = True
        word = ""
        for char in text:
            if char not in numbers:
                is_only_number = False
                break 

        if is_only_number:
            word = text
        else:
            for char in text:
                if char.isalpha():  # Keep letters
                    word += char
        return word
    
    def to_lowercase(self, token:list) -> list:
        # Usar lower() nativo para soportar caracteres acentuados y Unicode correctamente
        return [t.lower() for t in token]
    
    def remove_stopwords(self, token:list) -> list:
        stopwords_union = STOPWORDS_ES | STOPWORDS_EN
        return [word for word in token if word not in stopwords_union]
        
        
    def tokenize(self, text: str) -> list:              
        t_init = time.time()
        tracemalloc.start()
        
        token = []
        n = len(text)
        
        i = 0
        j = i
        
        while i <= n - 1:
            if (text[i] in self.delimiter) and (text[j] in self.delimiter):
                j += 1
            elif (text[i] in self.delimiter):
                word_verified = self.verify_word(text[j:i])
                if word_verified:  
                    token.append(word_verified)
                j = i + 1
            i += 1

        if j < n:
            word_verified = self.verify_word(text[j:n])
            if word_verified:
                token.append(word_verified)

        token = self.to_lowercase(token)
        
        token = self.remove_stopwords(token)

        # print("Time:", time.time() - t_init)
        # print("Memory:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        return token
    
## poner eliminador de palabras unicas
def elimi_pal_repeti(token:list) -> list:
    vec_pal_unicas = []
    for i in range(len(token)):
        if token[i] not in vec_pal_unicas:
            vec_pal_unicas.append(token[i])
    return vec_pal_unicas

def matriz_concurrencia(texto:str) -> np.ndarray:
    tokenizer = Tokenizer()
    text_toke = tokenizer.tokenize(texto)
    vec_pal_unicas = elimi_pal_repeti(text_toke)
    n = len(vec_pal_unicas)
    matriz_concur = np.zeros((n,n))
    for i in range (len(text_toke)-1):
        pal = text_toke[i]
        pal_siguien = text_toke[i+1]
        indice_pal = indice_palabra(pal, vec_pal_unicas)
        indice_pal_siguien = indice_palabra(pal_siguien, vec_pal_unicas)


        if indice_pal == indice_pal_siguien:
            matriz_concur[indice_pal][indice_pal_siguien] += 1
        else:
            matriz_concur[indice_pal_siguien][indice_pal] += 1  
    return matriz_concur

def matriz_concurrencia_desde_tokens(text_toke: list) -> np.ndarray:
    """Genera la matriz de concurrencia a partir de una lista de tokens ya calculada.
    Optimizado con un diccionario de índices para evitar búsquedas lineales.
    """
    vec_pal_unicas = elimi_pal_repeti(text_toke)
    n = len(vec_pal_unicas)
    matriz_concur = np.zeros((n, n))
    idx_map = {w: i for i, w in enumerate(vec_pal_unicas)}

    for i in range(len(text_toke) - 1):
        pal = text_toke[i]
        pal_siguien = text_toke[i + 1]
        indice_pal = idx_map[pal]
        indice_pal_siguien = idx_map[pal_siguien]
        if indice_pal == indice_pal_siguien:
            matriz_concur[indice_pal][indice_pal_siguien] += 1
        else:
            matriz_concur[indice_pal_siguien][indice_pal] += 1
    return matriz_concur

def similitud_coseno(palabra1, palabra2, matriz_concurrencia, texto:str) -> float:
    tokenizer = Tokenizer()
    text_toke = tokenizer.tokenize(texto)
    vec_pal_unicas = elimi_pal_repeti(text_toke)
    indice_pal1 = indice_palabra(palabra1, vec_pal_unicas)
    indice_pal2 = indice_palabra(palabra2, vec_pal_unicas)
    
    vec1 = matriz_concurrencia[indice_pal1]
    vec2 = matriz_concurrencia[indice_pal2]
    
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    
    cosine_similarity = dot_product / (norm_vec1 * norm_vec2)
    return cosine_similarity
# Grado de correlacion entre dos palabras, se mide al sumar todos los valores de cada vector asociados a una palabra
def grado_correlacion(palabra, matriz_concurrencia: np.ndarray, texto:str) -> float:
    """Devuelve el grado de correlación (suma de concurrencias) asociado a una palabra.
    Si la palabra no existe en el vocabulario del texto, regresa 0.0.
    """
    tokenizer = Tokenizer()
    text_toke = tokenizer.tokenize(texto)
    vec_pal_unicas = elimi_pal_repeti(text_toke)

    # Suma por fila (concurrencias de cada palabra con el resto)
    sumas = np.sum(matriz_concurrencia, axis=1)

    idx = indice_palabra(palabra, vec_pal_unicas)
    if idx is None:
        return 0.0
    try:
        return float(sumas[idx])
    except Exception:
        return 0.0
    
def pca(matriz_concurrencia: np.ndarray, verbose: bool = True) -> np.ndarray:
    if verbose:
        print("\n[PCA] Iniciando medición...")
    t_init = time.time()
    tracemalloc.start()

    if verbose:
        print(f"[PCA] Centrando matriz de shape {matriz_concurrencia.shape}...")
    matriz_centrada = matriz_concurrencia - np.mean(matriz_concurrencia, axis=0)

    resultado = None
    try:
        # Intentar usar scikit-learn si está disponible (más optimizado y estable)
        from sklearn.decomposition import PCA as SKPCA
        if verbose:
            print("[PCA] Usando scikit-learn PCA (n_components=3)...")
        modelo = SKPCA(n_components=3, svd_solver='auto', random_state=0)
        resultado = modelo.fit_transform(matriz_centrada)
    except Exception:
        if verbose:
            print("[PCA] scikit-learn no disponible. Realizando SVD (fallback)...")
        U, S, Vt = np.linalg.svd(matriz_centrada)
        resultado = Vt.T[:, :3]

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    t_final = time.time()

    if verbose:
        print(f"[PCA] Tiempo: {t_final - t_init:.4f} segundos")
        print(f"[PCA] Memoria actual: {current / 1024**2:.2f} MB")
        print(f"[PCA] Memoria pico: {peak / 1024**2:.2f} MB")

    return resultado

def graficar_componentes_3d(matriz_concurrencia: np.ndarray, etiquetas: list | None = None, max_points: int = 1000) -> None:
    """Calcula PCA (3D) y grafica las componentes en un scatter 3D.
    - matriz_concurrencia: Matriz de concurrencia (n_palabras x n_palabras)
    - etiquetas: Lista opcional de etiquetas (palabras) para cada fila. Si se proporciona y el número
      de puntos graficados es pequeño, se anotarán algunas etiquetas.
    - max_points: Límite superior de puntos a mostrar para evitar gráficos demasiado pesados.
    """
    try:
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
    except Exception as e:
        raise ImportError("matplotlib no está instalado. Instálalo con: pip install matplotlib") from e

    # Reducir a 3 dimensiones
    coords = pca(matriz_concurrencia, verbose=False)
    n = coords.shape[0]

    # Muestreo si hay demasiados puntos
    if n > max_points:
        idx = np.linspace(0, n - 1, max_points, dtype=int)
        coords_plot = coords[idx]
        etiquetas_plot = [etiquetas[i] for i in idx] if etiquetas else None
    else:
        coords_plot = coords
        etiquetas_plot = etiquetas

    # Color por grado de concurrencia (suma por fila) para aportar señal visual
    grados = np.sum(matriz_concurrencia, axis=1)
    colores = grados[:coords_plot.shape[0]] if coords_plot.shape[0] == grados.shape[0] else grados

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(coords_plot[:, 0], coords_plot[:, 1], coords_plot[:, 2],
                    c=colores[:coords_plot.shape[0]], cmap='viridis', s=12, alpha=0.85)
    ax.set_title('Componentes principales (PCA 3D) de la matriz de concurrencia')
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_zlabel('PC3')
    fig.colorbar(sc, ax=ax, shrink=0.6, label='Grado de concurrencia')

    # Anotar algunas etiquetas si hay y si no son demasiadas
    if etiquetas_plot and coords_plot.shape[0] <= 200:
        for (x, y, z), lab in zip(coords_plot, etiquetas_plot):
            ax.text(x, y, z, lab, fontsize=6, alpha=0.8)

    plt.tight_layout()
    plt.show()

def cargar_pdf_paginas(ruta_pdf: Path) -> List[str]:
    """Carga el texto del PDF y devuelve una lista con el texto de cada página."""
    try:
        import PyPDF2
    except Exception as e:
        raise ImportError("PyPDF2 no está instalado. Instálalo con: pip install PyPDF2") from e

    ruta = Path(ruta_pdf)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo PDF: {ruta}")

    paginas: List[str] = []
    with open(ruta, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            paginas.append(pagina.extract_text() or "")
    return paginas

def construir_matriz_por_bloques(paginas: List[str], tokenizer: Tokenizer, usar_gpu: bool = True) -> Tuple[np.ndarray, List[str]]:
    """Construye la matriz de concurrencia procesando el documento por bloques (páginas).
    - Mantiene un vocabulario incremental y cuenta pares adyacentes, incluyendo el enlace entre páginas.
    - Devuelve la matriz densa (NumPy) y la lista de palabras en orden de índice.
    Nota: Si usar_gpu=True y CuPy/cuML están disponibles, la PCA puede aprovechar GPU, pero la construcción
    incremental de conteos se hace en CPU (Python dict) para simplicidad y bajo overhead.
    """
    word_to_idx: Dict[str, int] = {}
    idx_to_word: List[str] = []
    pair_counts: Dict[Tuple[int, int], int] = {}

    def get_idx(w: str) -> int:
        if w in word_to_idx:
            return word_to_idx[w]
        i = len(idx_to_word)
        word_to_idx[w] = i
        idx_to_word.append(w)
        return i

    last_token: str = None
    total_tokens = 0
    for page_text in paginas:
        toks = tokenizer.tokenize(page_text)
        if not toks:
            continue
        total_tokens += len(toks)
        # Vincular fin de página anterior con inicio de esta
        if last_token is not None:
            i_prev = get_idx(last_token)
            i_curr = get_idx(toks[0])
            key = (i_curr, i_prev) if i_prev != i_curr else (i_prev, i_curr)
            pair_counts[key] = pair_counts.get(key, 0) + 1

        for i in range(len(toks) - 1):
            w = toks[i]
            w2 = toks[i + 1]
            i1 = get_idx(w)
            i2 = get_idx(w2)
            key = (i2, i1) if i1 != i2 else (i1, i2)
            pair_counts[key] = pair_counts.get(key, 0) + 1

        last_token = toks[-1]

    n = len(idx_to_word)
    mat = np.zeros((n, n), dtype=np.float32)
    for (r, c), v in pair_counts.items():
        mat[r, c] = mat[r, c] + v

    return mat, idx_to_word

def cargar_pdf(ruta_pdf):
    """Carga el texto de un archivo PDF."""
    try:
        import PyPDF2
    except Exception as e:
        raise ImportError("PyPDF2 no está instalado. Instálalo con: pip install PyPDF2") from e

    # Asegurar Path y existencia
    ruta = Path(ruta_pdf)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo PDF: {ruta}")

    texto = ""
    with open(ruta, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            # extract_text puede devolver None en algunas páginas
            contenido = pagina.extract_text() or ""
            texto += contenido
    return texto

def main():
    # Cargar los tres documentos (secuencial, por bloques/páginas)
    parser = argparse.ArgumentParser(description="Procesa PDFs para matriz de concurrencia y PCA 3D.")
    parser.add_argument("--plot", action="store_true", help="Mostrar gráfica 3D del PCA por documento")
    parser.add_argument("--max-points", type=int, default=1000, help="Máximo de puntos a graficar")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    documentos_rutas = []
    for p in args.docs:
        pp = Path(p)
        documentos_rutas.append(pp if pp.is_absolute() else (base_dir / pp))
    else:
        doc_filenames = [
            "quijote.pdf",
            "CPEUM.pdf",
            "recetario.pdf",
        ]
        documentos_rutas = [base_dir / name for name in doc_filenames]
    tiempo_total_inicio = time.time()

    # Detección opcional de GPU para PCA (si cuml está disponible)
    usar_gpu_pca = False
    try:
        import cuml  # noqa: F401
        usar_gpu_pca = True
    except Exception:
        usar_gpu_pca = False

    tok = Tokenizer()

    for ruta in documentos_rutas:
        nombre = ruta.stem
        print(f"\n{'='*60}")
        print(f"Procesando documento: {nombre}")
        print(f"{'='*60}")

        t_doc = time.time()

        # Cargar por páginas
        print(f"[1/5] Cargando PDF por páginas...")
        t1 = time.time()
        paginas = cargar_pdf_paginas(ruta)
        print(f"      Tiempo: {time.time() - t1:.4f}s | Páginas: {len(paginas)}")

        # Construir matriz por bloques/páginas
        print(f"[2-4/5] Tokenizando y construyendo matriz de concurrencia por bloques...")
        t2 = time.time()
        tracemalloc.start()
        matriz_concur, vocab = construir_matriz_por_bloques(paginas, tok, usar_gpu=False)
        mem_actual, mem_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"      Tiempo: {time.time() - t2:.4f}s | Vocab: {len(vocab)} | Shape: {matriz_concur.shape}")
        print(f"      Memoria: {mem_actual / 1024**2:.2f} MB actual, {mem_pico / 1024**2:.2f} MB pico")

        # PCA
        print(f"[5/5] Aplicando PCA ({'GPU' if usar_gpu_pca else 'CPU'})...")
        coords = pca(matriz_concur, verbose=True)

        # Graficar 3D si se solicita
        if args.plot:
            try:
                graficar_componentes_3d(matriz_concur, etiquetas=vocab, max_points=args.max_points)
            except ImportError as e:
                print(f"[Plot] {e}")

        print(f"\n>>> Documento procesado en {time.time() - t_doc:.2f} segundos")

    print(f"\n{'='*60}")
    print(f"TOTAL: {time.time() - tiempo_total_inicio:.2f} segundos")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()


