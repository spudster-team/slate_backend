import time

from django.core.files.storage import FileSystemStorage
from django.db import models

from api.utils import reduce_image_size
from slate.settings import BASE_DIR

image_storage = FileSystemStorage(
    location=f'{BASE_DIR}/media/images',
    base_url="/media/images"
)


class Photo(models.Model):
    def image_filename(self, filename):
        extension = filename.split(".")[-1]
        specific = str(time.time())
        return f"image_{self.path.name}_{specific}.{extension}"

    path = models.ImageField(upload_to=image_filename, storage=image_storage, null=True, blank=True)

    def save(self, **kwargs):
        self.path = reduce_image_size(self.path)
        super(Photo, self).save(**kwargs)
