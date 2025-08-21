---

# Caneta-Inteligente

## 💳 Visão Segura - OCR com Voz para Deficientes Visuais

Este projeto foi desenvolvido durante a **Maratona Social no SENAI Antonio Noschese** (Santos, SP), onde conquistamos o 🥇 **primeiro lugar** na competição.

A proposta nasceu para solucionar um problema real enfrentado por pessoas com deficiência visual: **o risco de golpes ou má-fé ao utilizarem cartões de crédito em estabelecimentos**. O aplicativo reconhece, em tempo real, as informações exibidas na máquina de cartão e as lê em voz alta para o usuário, garantindo **acesso à informação, autonomia e segurança**.

---

## 🧠 Sobre o Projeto

* Utiliza **OCR (Tesseract)** para reconhecer textos da imagem capturada pela câmera.
* Converte o texto reconhecido em **áudio com voz sintetizada (pyttsx3)**.
* Funciona **em tempo real**, usando a webcam do computador.
* Feito com tecnologias **100% offline**: ideal para locais com baixa conectividade.
* Possibilidade de integração futura com **modelo de reconhecimento de padrões com TensorFlow** (não utilizado na versão final).

---

## 👥 Público-alvo

Projeto desenvolvido especialmente para o **Lar das Moças Cegas de Santos**, com o objetivo de facilitar o uso de maquininhas de cartão de crédito e evitar situações de oportunismo ou golpes.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* OpenCV (`opencv-python`)
* Tesseract OCR + `pytesseract`
* pyttsx3 (texto para fala)
* TensorFlow (modelo neural, opcional)

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/murilocamargo05/Caneta-Inteligente.git
cd Caneta-Inteligente
```

### 2. Instale as dependências

```bash
pip install opencv-python pytesseract pyttsx3 tensorflow
```

### 3. Instale o Tesseract OCR passo a passo

1. Acesse o repositório oficial do Tesseract: 🔗 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
2. Baixe a versão adequada para o seu sistema operacional (Windows, macOS ou Linux).
3. Durante a instalação, anote o caminho onde o Tesseract foi instalado.
4. Certifique-se de que o idioma português está instalado:

   * Abra o terminal ou prompt de comando e digite:

     ```bash
     tesseract --list-langs
     ```
   * Caso `por` não esteja listado, baixe `por.traineddata` e coloque na pasta `tessdata` do Tesseract.
5. No seu código Python (`tensorflow2.py`), adicione a linha:

```python
import pytesseract
# Atualize o caminho conforme o local da instalação do Tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\CAMINHO\\DO\\TESSERACT\\tesseract.exe"
```

Substitua `C:\CAMINHO\DO\TESSERACT\tesseract.exe` pelo caminho real do seu computador.

---

## ▶️ Como Usar

1. Certifique-se de que a webcam está conectada.
2. Execute o script principal:

```bash
python tensorflow2.py
```

3. A webcam será ativada.
4. Quando um texto (como o visor de uma maquininha de cartão) for identificado, ele será lido em voz alta automaticamente.
5. Pressione `q` para sair do aplicativo.

---

## 🏆 Reconhecimento

Este projeto foi o vencedor da **Maratona Social 2025** realizada no SENAI Antonio Noschese, em Santos, com foco em soluções de impacto social.

Idealizado para o **Lar das Moças Cegas de Santos**, promovendo inclusão digital, segurança e independência.

---

## 🤝 Agradecimentos

* Lar das Moças Cegas de Santos pela parceria e confiança.
* SENAI, organizadores e mentores da Maratona Social.
* Todos os envolvidos que contribuíram com ideias, testes e melhorias no projeto.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

---

## 🔮 Possíveis Melhorias Futuras

* Integração com modelos de visão computacional para reconhecimento de padrões de cartões.
* Interface gráfica amigável para maior facilidade de uso.
* Suporte a múltiplos idiomas além do português.
* Notificações sonoras personalizáveis.
* Armazenamento de histórico de leitura para revisão posterior.
