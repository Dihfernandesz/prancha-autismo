# 🗣️ Prancha de Comunicação Digital (CAA) - Projeto Jordan

Este projeto consiste em uma aplicação web progressiva (PWA) simples e acessível, desenvolvida para atuar como uma **Prancha de Comunicação Aumentativa e Alternativa (CAA)** digital. 

A ferramenta foi criada especificamente para auxiliar crianças não-verbais a expressarem desejos e necessidades através de cartões visuais com feedback sonoro imediato.

## 💙 A Inspiração: O Jordan

Este projeto foi desenvolvido para o meu filho, **Jordan**, que tem **4 anos**.

Atualmente, o Jordan não se comunica de forma verbal. Ele realiza acompanhamento constante com uma equipe multidisciplinar e, por **sugestão direta de sua Fonoaudióloga e de sua Psicóloga**, iniciamos a introdução de recursos de comunicação alternativa.

O objetivo desta prancha digital não é apenas substituir a fala, mas servir como uma ferramenta de apoio na evolução terapêutica dele. Ao associar a imagem ao som (o "falar" do aplicativo), buscamos estimular a cognição, reduzir a frustração pela falta de comunicação e incentivar a autonomia do Jordan no dia a dia.

## 🎯 O que é CAA e Por que Usar?

### O Contexto: Autismo e Não-Verbalidade
O Transtorno do Espectro Autista (TEA) afeta a comunicação de formas variadas. Muitas crianças, assim como o Jordan, podem ser **não-verbais** ou ter dificuldades na fala funcional. É crucial entender que a ausência de fala não significa ausência de compreensão ou vontade de interagir.

### Como a Prancha Ajuda
A CAA (Comunicação Aumentativa e Alternativa) oferece um caminho para essa interação:
1.  **Associação Visual:** O uso de imagens reais (fotos dos produtos que ele conhece) facilita o reconhecimento.
2.  **Reforço Auditivo:** O sistema utiliza a voz sintetizada para reforçar o pedido, criando uma ponte entre o desejo e a palavra falada.
3.  **Consistência Terapêutica:** A ferramenta digital complementa o trabalho feito em consultório pelas terapeutas.

---

## 🛠️ Funcionalidades Técnicas

* **Interface Focada:** Design limpo, sem distrações, com botões grandes e cores categorizadas (ex: Amarelo para necessidades fisiológicas, Cores das marcas para alimentos).
* **Feedback Sonoro (TTS):** Utiliza a **Web Speech API** nativa do navegador para sintetizar a voz em Português (PT-BR).
* **Imagens Personalizadas:** Suporte para fotos reais, essencial para crianças que ainda não leem e dependem da memória visual do objeto.
* **Modo Offline:** Inclui um script em Python para converter a aplicação em um arquivo único, permitindo o uso em celulares/tablets sem necessidade de internet.

## 📂 Estrutura do Projeto

* `index.html`: O código fonte principal da prancha.
* `Imagens/`: Pasta contendo os recursos visuais específicos do Jordan.
* `converter.py`: Script utilitário para converter imagens locais em Base64 (para uso mobile offline).

## 🚀 Como Executar

### No Computador
Basta abrir o arquivo `index.html` (ou `Prancha_Jordan.html`) em qualquer navegador moderno.

### No Celular (Modo Offline)
Para contornar restrições de segurança de navegadores móveis com arquivos locais:

1.  Tenha o Python instalado no computador.
2.  Coloque o script `converter.py` na mesma pasta do arquivo HTML.
3.  Execute o script. Ele gerará automaticamente um arquivo com o sufixo `_MOBILE.html`.
4.  Envie este novo arquivo para o celular e adicione à tela inicial.

---

> *"A comunicação é a chave para a autonomia. Cada imagem tocada é uma palavra dita."*

---
**Desenvolvido com carinho para o Jordan.**