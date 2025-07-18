import pandas as pd 
import os #consigo usar os comandos do terminar no programa python
import glob
# Uma função de extract que lê e consolida os json


def extrair_dados_e_consolidar (pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) #Vai listar todos os meus arquivos que são json
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total



# Uma função que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df
# Uma função que da load em csv ou parquet


## Para testar os desenvolvimentos: (Assim não fica nenhum "lixo" no codigo principal)

if __name__ == "__main__":
    pasta_argumento = 'data'
    data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
    print(calcular_kpi_de_total_de_vendas(data_frame))