# Utilize o modelo BERTIMBAU para prever palavras mascaradas em um conjunto de dados de texto.

pip install transformers

from transformers import BertTokenizer, BertForMaskedLM
import torch

modelo_carregado = 'neuralmind/bert-base-portuguese-cased'
tokenizador = BertTokenizer.from_pretrained(modelo_carregado)
modelo_final = BertForMaskedLM.from_pretrained(modelo_carregado)

def prever_palavras_mascaradas(entrada_para_prever_mascara):

  # Tokenizando a sentença
  entrada_tokenizada = tokenizador(entrada_para_prever_mascara, return_tensors='pt')

  # Identificando a posição do token [MASK]
  mask_token_index = torch.where(entrada_tokenizada["input_ids"][0] == tokenizador.mask_token_id)

  # Realizando a predição
  with torch.no_grad():
    saida = modelo_final(**entrada_tokenizada)

  # Obtendo as predições para a posição mascarada
  predicoes = saida.logits[0, mask_token_index, :].squeeze()

  # Corrigindo: Usando dim=0 para operar na dimensão correta
  ranking_palavras = torch.topk(predicoes, 5, dim=0).indices.tolist()

  # Convertendo os índices dos tokens para palavras
  possiveis_palavras = [tokenizador.decode([indice]) for indice in ranking_palavras]

  return possiveis_palavras

# Primeiro exemplo de uso
sentenca_exemplo = "O semestre letivo tem sido muito [MASK] para mim."
palavras_preditas = prever_palavras_mascaradas(sentenca_exemplo)
print("Palavras sugeridas:", palavras_preditas)

# Segundo exemplo de uso
sentenca_exemplo = "Realmente, não sei o quão [MASK] foi a ideia de simplesmente decidir pausar o semestre e retornar como se nada tivesse acontecido."
palavras_preditas = prever_palavras_mascaradas(sentenca_exemplo)
print("Palavras sugeridas:", palavras_preditas)

# Terceiro exemplo de uso
sentenca_exemplo = "Apesar de tudo, eu percebo meus colegas tentando estar [MASK] nos corredores."
palavras_preditas = prever_palavras_mascaradas(sentenca_exemplo)
print("Palavras sugeridas:", palavras_preditas)
