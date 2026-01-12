import os
import base64
import sys
from bs4 import BeautifulSoup 

# --- CORREÇÃO DE CAMINHO ---
# Descobre onde este script (converter.py) está salvo no computador
pasta_do_script = os.path.dirname(os.path.abspath(__file__))

# Força o Python a trabalhar DENTRO dessa pasta
os.chdir(pasta_do_script)

print(f"Diretório de trabalho definido para: {pasta_do_script}")
print("-" * 30)

# --- CONFIGURAÇÃO AUTOMÁTICA ---
# Agora ele procura na pasta correta
arquivos_html = [f for f in os.listdir('.') if f.endswith('.html') and 'MOBILE' not in f]

if not arquivos_html:
    print("ERRO CRÍTICO: Nenhum arquivo .html encontrado!")
    print(f"O script está procurando nesta pasta: {os.getcwd()}")
    print("Verifique se o arquivo 'Prancha_Jordan.html' está exatamente aqui.")
    input("Pressione ENTER para sair...") # Pausa para ler o erro
    sys.exit()

# Pega o primeiro HTML que encontrar
ARQUIVO_ENTRADA = arquivos_html[0]
ARQUIVO_SAIDA = ARQUIVO_ENTRADA.replace('.html', '_MOBILE.html')

print(f"Arquivo encontrado: {ARQUIVO_ENTRADA}")
print(f"Gerando versão mobile: {ARQUIVO_SAIDA}")
print("-" * 30)

def image_to_base64(path):
    # Verifica se a imagem existe
    if not os.path.exists(path):
        print(f"AVISO: Imagem não encontrada: {path}")
        return None
        
    try:
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            ext = path.split('.')[-1].lower()
            if ext == 'jpg': ext = 'jpeg'
            return f"data:image/{ext};base64,{encoded_string}"
    except Exception as e:
        print(f"Erro ao ler imagem {path}: {e}")
        return None

try:
    with open(ARQUIVO_ENTRADA, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    imgs = soup.find_all('img')
    contador = 0

    print("Processando imagens...")
    for img in imgs:
        src = img.get('src')
        
        # Ignora imagens que já são links ou base64
        if src and not src.startswith('http') and not src.startswith('data:'):
            # O script já está na pasta correta, então o caminho relativo funciona
            base64_str = image_to_base64(src)
            
            if base64_str:
                img['src'] = base64_str
                contador += 1
                print(f" [OK] {src}")

    # Salvar novo HTML
    with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print("-" * 30)
    print(f"SUCESSO! {contador} imagens convertidas.")
    print(f"Arquivo pronto: {os.path.join(pasta_do_script, ARQUIVO_SAIDA)}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

input("Pressione ENTER para finalizar...")