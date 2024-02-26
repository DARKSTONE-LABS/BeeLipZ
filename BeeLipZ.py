import os
import json
from PIL import Image
import random

# Paths
base_path = os.getcwd()
layers_dir = os.path.join(base_path, "layers")
output_dir = os.path.join(base_path, "output")
images_dir = os.path.join(output_dir, "images")
metadata_dir = os.path.join(output_dir, "metadata")

# Ensure output directories exist
os.makedirs(images_dir, exist_ok=True)
os.makedirs(metadata_dir, exist_ok=True)

# Layer order and rarities
layers_order = [
    "Background",
    "Background accesory",
    "Bee Body",
    "mouth",
    "eyes",
    "hair",
    "shirt",
    "accesory",
    "overlay",
    "drip grade",
]

layer_rarities = {
    "Background accesory": 30,
    "hair": 80,
    "accesory": 65,
    "overlay": 15,
    "drip grade": 20,
}

edition_size = 999
generated_dna = []

def should_include_layer(layer_name):
    return random.random() < layer_rarities.get(layer_name, 100) / 100

def create_nft(edition_number):
    dna = ""
    attributes = []
    canvas_size = (980, 1280)
    result_image = Image.new('RGBA', canvas_size)

    for layer_name in layers_order:
        if not should_include_layer(layer_name):
            continue

        layer_folder = os.path.join(layers_dir, layer_name)
        options = [f for f in os.listdir(layer_folder) if f.endswith('.png')]
        if not options:
            continue

        choice = random.choice(options)
        dna += choice

        attributes.append({"trait_type": layer_name, "value": choice.split('.')[0]})

        layer_image_path = os.path.join(layer_folder, choice)
        layer_image = None  # Initialize layer_image to None
        try:
            layer_image = Image.open(layer_image_path).convert('RGBA')
        except Exception as e:
            print(f"Error loading image {layer_image_path}: {e}")
            continue  # Skip this layer if the image cannot be loaded

        # Proceed only if layer_image is successfully loaded
        if layer_image and layer_image.size != canvas_size:
            layer_image = layer_image.resize(canvas_size, Image.Resampling.LANCZOS)

        if layer_image:  # Ensure layer_image is not None
            result_image = Image.alpha_composite(result_image, layer_image)

    if dna in generated_dna:
        return False
    generated_dna.append(dna)

    file_name = f'{edition_number}.png'
    result_image_path = os.path.join(images_dir, file_name)
    result_image.save(result_image_path)

    metadata = {
        "name": f"BeeFella #{edition_number}",
        "description": "2222 Buzzin Fellas getting vengeance on the Solana Blockchain",
        "image": file_name,
        "attributes": attributes,
        "edition": edition_number,
    }

    metadata_path = os.path.join(metadata_dir, f'{edition_number}.json')
    with open(metadata_path, 'w') as metadata_file:
        json.dump(metadata, metadata_file, indent=4)

    return True


for i in range(1, edition_size + 1):
    if not create_nft(i):
        print(f"Duplicate at {i}, stopping.")
        break

print("NFT generation complete.")
