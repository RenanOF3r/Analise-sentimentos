pip install -r requirements.txt

# Tenta importar a biblioteca LeIA
try:
    from leia import SentimentIntensityAnalyzer
except ImportError:
    print("\n--- ERRO ---")
    print("A biblioteca LeIA não foi encontrada.")
    print("Por favor, certifique-se de que 'leia' está no seu arquivo requirements.txt")
    print("e execute 'pip install -r requirements.txt' no terminal do Codespace.")
    print("------------\n")
    exit() # Encerra o script se a biblioteca não estiver instalada

# Inicializa o analisador de sentimentos
analyzer = SentimentIntensityAnalyzer()

# Lista de frases de exemplo em português para analisar
frases_para_analisar = [
    "Que dia maravilhoso para passear no parque!",
    "Estou muito decepcionado com o serviço prestado.",
    "O filme foi bom, mas o final poderia ser melhor.",
    "Não gostei nem um pouco daquela comida.",
    "A entrega chegou no prazo.",
    "Que notícia fantástica!",
    "O tempo está nublado hoje.",
    "Adorei a nova funcionalidade do aplicativo!",
    "Infelizmente, o produto veio com defeito.",
    "O atendimento foi ok.",
    "Este livro é simplesmente perfeito.",
    "Que experiência horrível, nunca mais volto!",
    "A comida estava mais ou menos."
]

# Função auxiliar para interpretar o score composto
def interpretar_sentimento(compound_score):
    """Interpreta o score composto do LeIA."""
    if compound_score >= 0.05:
        return "Positivo"
    elif compound_score <= -0.05:
        return "Negativo"
    else:
        return "Neutro"

# --- Início da Análise ---
print("=============================================")
print("   Análise de Sentimentos com LeIA v1.1     ")
print("=============================================")

# Itera sobre cada frase, analisa e imprime o resultado
for i, frase in enumerate(frases_para_analisar):
    print(f"\n--- Frase {i+1} ---")
    print(f"Texto: '{frase}'")

    # Calcula os scores de polaridade
    scores = analyzer.polarity_scores(frase)

    # Interpreta o sentimento geral
    sentimento = interpretar_sentimento(scores['compound'])

    # Imprime os resultados formatados
    print(f"  Sentimento: {sentimento}")
    print(f"  Score Composto: {scores['compound']:.4f} (varia de -1 a +1)")
    # print(f"  Scores Detalhados (Negativo, Neutro, Positivo): ({scores['neg']:.3f}, {scores['neu']:.3f}, {scores['pos']:.3f})") # Descomente se quiser ver os scores individuais

print("\n=============================================")
print("           Análise Concluída               ")
print("=============================================")
