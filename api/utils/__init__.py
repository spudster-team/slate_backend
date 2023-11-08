import hashlib
import io

from PIL import Image
from django.core.files import File


def reduce_image_size(image, quality=50):
    if image:
        img = Image.open(image)
        image_format = img.format
        thumb_io = io.BytesIO()
        if image_format:
            img.save(thumb_io, format=image_format, quality=quality)
            return File(thumb_io, name=image.name)
    return None


def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
