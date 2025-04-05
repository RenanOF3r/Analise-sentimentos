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

# Função auxiliar para interpretar o score composto
def interpretar_sentimento(compound_score):
    """Interpreta o score composto do LeIA."""
    if compound_score >= 0.05:
        return "Positivo 😊"
    elif compound_score <= -0.05:
        return "Negativo 😠"
    else:
        return "Neutro 😐"

# --- Início da Análise Interativa ---
print("=============================================")
print("   Analisador de Sentimentos Interativo    ")
print("         (Digite 'sair' para terminar)     ")
print("=============================================")

while True:
    # Pede ao usuário para digitar uma frase
    try:
        frase_usuario = input("\nDigite uma frase para analisar (ou 'sair'): ")
    except EOFError: # Caso o input seja interrompido (raro em uso normal)
        print("\nEntrada interrompida. Saindo.")
        break

    # Verifica se o usuário quer sair
    if frase_usuario.lower() == 'sair':
        print("\nObrigado por usar o analisador. Até logo!")
        break

    # Verifica se a frase não está vazia
    if not frase_usuario.strip():
        print("Você não digitou nada. Tente novamente.")
        continue

    print(f"Analisando: '{frase_usuario}'")

    # Calcula os scores de polaridade
    scores = analyzer.polarity_scores(frase_usuario)

    # Interpreta o sentimento geral
    sentimento = interpretar_sentimento(scores['compound'])

    # Imprime os resultados formatados
    print(f"  -> Sentimento: {sentimento}")
    print(f"  -> Score Composto: {scores['compound']:.4f}")
    # print(f"  Scores Detalhados (Neg, Neu, Pos): ({scores['neg']:.3f}, {scores['neu']:.3f}, {scores['pos']:.3f})") # Descomente para detalhes

print("\n=============================================")
