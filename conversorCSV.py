import pandas as pd

#carregar o arquivo
def load_excel_file(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print("Erro: Arquivo Excel não encontrado. Verifique o caminho.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# caminho do arquivo 
excel_file = 'C:/Users/jjmat/Documents/seu_arquivo.xlsx'
sheet_name = 'Sheet1'

# Carregar a planilha
df = load_excel_file(excel_file, sheet_name)


if df is not None:
    # salva como CSV 
    df.to_csv('seu_arquivo.csv', index=False, sep=',')
    print("Arquivo Excel convertido para CSV com sucesso!")
else:
    print("Não foi possível converter o arquivo Excel para CSV.")
