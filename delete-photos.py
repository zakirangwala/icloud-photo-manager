# Import Packages
from pyicloud import PyiCloudService

# Replace with your own email address
api = PyiCloudService('john@email.com')
count = 1

# Loop through all photos in the 'All Photos' album
for photo in api.photos.all:
    print(f"Count : {count}\n")
    count += 1

    # Delete the photo
    try:
        photo.delete()
        print(f"Deleted photo: {photo.filename}")
    except Exception as e:
        print(f"Failed to delete photo: {photo.filename}. Error: {e}")
