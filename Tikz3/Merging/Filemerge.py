import os
import shutil

print("Current Working Directory:", os.getcwd())

src_dir = 'Tikz3/Merging/srccopy'
out_dir = 'Tikz3/Merging/outcopy'
root_dir = 'Tikz3/Merging/combined'

if not os.path.exists(root_dir):
    os.makedirs(root_dir)

src_files = {f for f in os.listdir(src_dir) if f.endswith('.tex')}
out_files = {f for f in os.listdir(out_dir) if f.endswith('.png')}

# Iterate over the src files to find matching png files
for src_file in src_files:
    file_name = os.path.splitext(src_file)[0]  # Get the base file name without extension

    # Corresponding png file name
    png_file = f'{file_name}.png'

    # Check if the corresponding png file exists in the out folder
    if png_file in out_files:
        # Create a directory for the file set if it doesn't exist
        new_dir = os.path.join(root_dir, file_name)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        
        # Copy the tex file
        shutil.copy(os.path.join(src_dir, src_file), os.path.join(new_dir, src_file))

        # Copy the png file
        shutil.copy(os.path.join(out_dir, png_file), os.path.join(new_dir, png_file))
