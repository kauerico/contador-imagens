import os

def count_images_in_folders(base_folder):
    """
    Conta o número de imagens em cada subpasta de um diretório base.

    Parâmetros:
        base_folder (str): Caminho para a pasta principal contendo as subpastas.

    Retorna:
        dict: Um dicionário com o nome das pastas como chaves e o número de imagens como valores.
    """
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}  # Extensões de imagem suportadas
    folder_counts = {}

    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        if os.path.isdir(folder_path):
            count = sum(
                1 for file in os.listdir(folder_path)
                if os.path.splitext(file)[1].lower() in image_extensions
            )
            folder_counts[folder_name] = count

    return folder_counts

def write_image_counts_to_file(output_file, folder_counts):
    """
    Escreve as contagens de imagens em um arquivo de texto.

    Parâmetros:
        output_file (str): Caminho para o arquivo de saída.
        folder_counts (dict): Dicionário com o nome das pastas e contagens de imagens.
    """
    with open(output_file, 'w') as file:
        file.write("Contagens de imagens:\n\n")
        for folder, count in folder_counts.items():
            file.write(f"{folder} = {count} imagens\n")

if __name__ == "__main__":
    # Caminho para a pasta principal contendo as subpastas
    base_folder = "dataset_novo"
    # Caminho para o arquivo de saída
    output_file = "codigo/Contagem imagens/contagem.txt"

    # Contar as imagens
    folder_counts = count_images_in_folders(base_folder)
    
    # Escrever o resultado no arquivo
    write_image_counts_to_file(output_file, folder_counts)
    print(f"Contagens salvas em: {output_file}")
