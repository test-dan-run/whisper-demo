import os

def save_to_text(text: str, name: str, output_dir: str = '.') -> str:

    filepath = os.path.join(output_dir, f'{name}.txt')

    with open(filepath, mode='w', encoding='utf-8') as fw:
        fw.write(text)

    return filepath
