# prancha-autismo
# 🗣️ Prancha de Comunicação Digital (CAA)

Este projeto consiste em uma aplicação web progressiva (PWA) simples, desenvolvida para auxiliar na comunicação de pessoas não-verbais, especificamente voltada para crianças no espectro autista. 

A ferramenta funciona como uma **Prancha de Comunicação Aumentativa e Alternativa (CAA)** digital, permitindo que o usuário expresse desejos e necessidades básicas através de cartões visuais com feedback sonoro imediato.

## 🎯 Propósito do Projeto

Este projeto nasceu de uma necessidade pessoal: criar uma ferramenta acessível, personalizável e portátil para auxiliar meu filho autista. Diferente de aplicativos comerciais complexos ou caros, esta solução foca na simplicidade, na familiaridade visual (usando fotos de produtos reais que a criança consome) e na facilidade de implantação em qualquer dispositivo (celular, tablet ou PC).

### O Contexto: Autismo e Não-Verbalidade
O Transtorno do Espectro Autista (TEA) afeta a comunicação social de diversas formas. Muitas crianças e adultos no espectro são **não-verbais** ou possuem **apraxia da fala**. 

É fundamental compreender que **não falar não significa não ter nada a dizer**. A inteligência e a vontade de se comunicar estão presentes, mas o canal da fala oral pode não estar acessível. A falta de um meio de comunicação eficiente gera frustração, ansiedade e comportamentos desafiadores.

### O que é CAA (Comunicação Aumentativa e Alternativa)?
A CAA engloba métodos e ferramentas que substituem ou complementam a fala. As "pranchas de comunicação" são um dos métodos mais eficazes:
1.  **Associação Visual:** A criança seleciona a imagem do que deseja.
2.  **Reforço Auditivo:** O sistema "fala" a escolha, reforçando a conexão entre imagem e som.
3.  **Autonomia:** Permite que a criança faça escolhas e tenha controle sobre seu ambiente.

---

## 🛠️ Funcionalidades Técnicas

* **Interface Limpa e Focada:** Design minimalista para evitar sobrecarga sensorial, com botões grandes e cores contrastantes para categorização (ex: Verde para "Sim", Vermelho para "Não", Amarelo para Necessidades).
* **Feedback Sonoro (TTS):** Utiliza a **Web Speech API** nativa do navegador para sintetizar a voz, eliminando a necessidade de gravar áudios manualmente.
* **Imagens Reais:** Suporte para fotos reais de produtos (ex: a embalagem exata do biscoito favorito), o que facilita a associação para crianças que não leem.
* **Conversor Offline:** Inclui um script em Python para converter imagens locais em Base64, permitindo que a aplicação rode em celulares de forma 100% offline (sem internet e sem servidor), como um arquivo único.

Estrutura do Projeto

* `index.html`: O código fonte principal da prancha.
* `Imagens/`: Pasta contendo os recursos visuais (fotos e ícones).
* `converter.py`: Script utilitário para "compilar" o HTML e as imagens em um arquivo único portátil para mobile.

Como Usar

### No Computador
Basta abrir o arquivo `index.html` em qualquer navegador moderno (Chrome, Edge, Firefox).

### No Celular (Modo Offline)
Devido a restrições de segurança dos navegadores móveis, imagens locais não carregam diretamente. Para usar no celular:

1.  Certifique-se de que o Python está instalado.
2.  Execute o script `converter.py` na pasta do projeto.
3.  O script irá gerar um arquivo novo (ex: `Prancha_MOBILE.html`) com todas as imagens embutidas no código.
4.  Envie este arquivo único para o celular (via WhatsApp ou cabo) e abra-o.

### Personalização

Para adaptar a prancha para outra criança, basta substituir as imagens na pasta `Imagens` e alterar os textos correspondentes no arquivo HTML dentro da função `onclick="falar('Texto Aqui')"`.

---

> *"A comunicação é um direito humano básico. Dar voz a quem não fala é um ato de liberdade."*

---
### Desenvolvido com 💙 e inclusão.