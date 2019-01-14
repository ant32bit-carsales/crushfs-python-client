import aiohttp

from .client import Client


class AsyncClient(Client):
    def __init__(self, **kwds):
        super().__init__(**kwds)

    async def download_object(self, *,
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
        async with aiohttp.request('GET', download_url) as r:
            response = AsyncResponse(
                    status_code=r.status,
                    data=await r.read())
            return response


class AsyncResponse:
    def __init__(self, *, status_code, data):
        self.status_code=status_code
        self.data=data

