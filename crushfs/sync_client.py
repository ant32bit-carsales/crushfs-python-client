import requests

from .client import Client


class SyncClient(Client):
    def __init__(self, **kwds):
        super().__init__(**kwds)


    def download_object(self, *,
            path,
            thumbnail=False,
            thumbnail_size=None,
            thumbnail_method=None,
            thumbnail_bgcolor=None,
            image_transform=None):
        download_url = self.build_download_object_url(
                path=path,
                thumbnail=thumbnail,
                thumbnail_size=thumbnail_size,
                thumbnail_method=thumbnail_method,
                thumbnail_bgcolor=thumbnail_bgcolor,
                image_transform=image_transform)
        r = requests.get(download_url)
        response = SyncResponse(
                status_code=r.status_code, 
                data=r.content)
        return response


class SyncResponse:
    def __init__(self, *, status_code, data):
        self.status_code=status_code
        self.data=data

