# Import Packages
from pyicloud import PyiCloudService
import os

# Replace with your own email address
api = PyiCloudService('john@email.com')
count = 1

# Loop through all photos in the 'All Photos' album
for photo in api.photos.all:
    filename, ext = os.path.splitext(photo.filename)

    # Using photo's creation datetime attribute as filename parameter
    creation_date = photo.created
    date_str = creation_date.strftime("%Y%m%d%H%M%S") 
    output_filename = f"{filename}-{date_str}{ext}"
    print(f"Count : {count}\n")
    count += 1

    # Skip if file already exists
    if os.path.isfile(output_filename):
        print(f"File {output_filename} already exists")
        continue
    
    # Download the photo
    print(f"Writing file to {output_filename}")
    download = photo.download('original')
    with open(output_filename, 'wb') as opened_file:
        opened_file.write(download.raw.read())