# iCloud Photo Manager

This project contains two Python scripts for managing photos stored in iCloud: one for downloading all photos and another for deleting all photos. 

## Installation

Before running the scripts, you need to install the required dependencies.

1. Clone the repository:
- git clone https://github.com/zakirangwala/icloud-photo-manager.git
- cd icloud-photo-manager

2. Install the required Python packages:
- pip install -r requirements.txt


## Usage

### Downloading Photos

To download all your photos from iCloud, run:
- python download-photos.py

To delete all your photos from iCloud, run:
- python delete-photos.py


## Important Notes

- **Duration**: Depending on the number of photos and your internet bandwidth, each script might take from several minutes to a couple of hours to complete.
- **Credentials**: You will need to provide your iCloud credentials to use these scripts. Ensure you handle these securely.
- **Backup**: Before using the delete script, make sure to back up your photos. This action is irreversible.
- **Testing**: It is highly recommended to test the scripts with a smaller set of data before proceeding with the full batch.

## Disclaimer

Use these scripts at your own risk. The author is not responsible for any loss of data resulting from the use of these scripts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with your improvements.
