import bz2
import os


bz2_file_path = '/Users/rilyasov/Downloads/enwiki-20240320-pages-articles-multistream-index.txt.bz2'

txt_file_path = bz2_file_path[:-4]  # Removes the '.bz2' from the end


os.makedirs(os.path.dirname(txt_file_path), exist_ok=True)


with bz2.open(bz2_file_path, 'rb') as f_in, open(txt_file_path, 'wb') as f_out:

    content = f_in.read()

    f_out.write(content)

print(f"Decompressed file saved to: {txt_file_path}")