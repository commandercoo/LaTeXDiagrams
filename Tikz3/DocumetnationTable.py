import os

print("Current Working Directory:", os.getcwd())

# Define the base directory containing the assets folder
base_dir = 'Tikz3/assets'

# Function to generate Markdown formatted text
def generate_markdown(base_dir, folder, file_name):
    tex_path = f"{base_dir}/{folder}/{file_name}.tex"
    png_path = f"{base_dir}/{folder}/{file_name}.png"
    tex_link = f"[`{file_name}.tex`]({tex_path})"
    img_markdown = f"![{file_name}.png]({png_path})"
    return f"{tex_link}\n\n{img_markdown}\n"

# Loop through each folder in the assets directory
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):  # Ensure it's a directory
        files = os.listdir(folder_path)
        tex_files = [f for f in files if f.endswith('.tex')]
        png_files = [f for f in files if f.endswith('.png')]
        
        for tex_file in tex_files:
            base_name = os.path.splitext(tex_file)[0]
            if f"{base_name}.png" in png_files:  # Ensure there is a corresponding PNG file
                print(generate_markdown(base_dir, folder, base_name))


# Running this script will output the LaTeX formatted rows for each matched .tex and .png file.
