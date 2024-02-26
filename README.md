
![9](https://github.com/DARKSTONE-LABS/BeeLipZ/assets/141037846/f229ad7c-7278-41ac-8eff-55d62e9ca469)

# BeeLipZ NFT Generator

Welcome to the BeeLipZ NFT Generator, developed by DARKSTONE LABS. This tool is crafted to empower creators in generating their unique, customizable NFTs. With an automated process, this Python-based utility facilitates the creation of NFT images along with their metadata, perfectly suited for deployment on blockchain platforms like Solana.

## Features

- **Customizable NFT Creation:** Generate any number of unique NFTs with your personalized design.
- **Layer-Based Design System:** Easily adjust traits and appearances using a structured layer system.
- **Complete Output Package:** Obtain both NFT images and their corresponding metadata files ready for blockchain.

## Getting Started

### Prerequisites

Ensure you have the following before starting:

- Python 3.x
- Pillow (Python Imaging Library)

Install Pillow using pip:

```bash
pip install Pillow
```

### Installation

Clone the BeeLipZ repository to get started:

```bash
git clone https://github.com/DARKSTONE-LABS/BeeLipZ.git
cd BeeLipZ
```

### Creating Your NFT Collection

1. **Prepare Your Art Layers**: Organize your artwork into layers (e.g., background, body, accessories) within the `layers` directory. Each layer should have its variations as separate files.
   
2. **Configure Your Collection**: Edit `BeeLipZ.py` to reflect your collection's structure. Adjust `layers_order` and `layer_rarities` to match the layers and rarities of your traits.

3. **Generate Your NFTs**: Run the script to generate your collection.

```bash
python BeeLipZ.py
```

The generated NFTs will be saved in the `output` directory, with images and metadata ready for use.

## Customization Guide

- **Layers and Traits**: Add or remove layers by editing the `layers_order` list. Customize the rarity of traits by adjusting values in the `layer_rarities` dictionary.
- **Canvas Size**: Modify the `canvas_size` tuple to change the output image dimensions if needed.
- **Unique Attributes**: The script generates a unique DNA for each NFT, ensuring no duplicates. Customize the naming and description within the metadata generation section to align with your collection's theme.

## Project Structure

- `layers/`: Your NFT layers go here. Organize them by trait categories.
- `output/`: Contains generated NFTs (`images/`) and metadata (`metadata/`).
- `BeeLipZ.py`: The main script where you configure and run your NFT generation.

## Contributing and Support

Your contributions make the open-source community thrive. Whether it's a bug fix, feature addition, or a suggestion, we welcome your input. Fork the project, make your changes, and submit a pull request!

## License

Released under the [MIT License](LICENSE), allowing for both personal and commercial use.

