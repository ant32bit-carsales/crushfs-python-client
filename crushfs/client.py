import datetime
import hashlib
import urllib.parse
import uuid


VERSION='1'

class Client:
    def __init__(self, *,
            warehouse,
            signer,
            secret):
        self.warehouse=warehouse
        self.signer=signer
        self.secret=secret


    def _build_url(self, *,
            path,
            action,
            thumbnail=False,
            thumbnail_size=None,
            thumbnail_method=None,
            thumbnail_bgcolor=None,
            image_transform=None,
            copy_source=None):
        url = f'https://{self.warehouse}.crushfs.net/'
        if path.startswith('/'):
            path = path[1:]
        url += f'{path}?x-cfs-version={VERSION}'
        url += f'&x-cfs-action={action}'
        if thumbnail:
            url += f'&x-cfs-thumbnail=1'
            if thumbnail_size:
                url += f'&x-cfs-thumbnail-size={thumbnail_size}'
            if thumbnail_method:
                url += f'&x-cfs-thumbnail-method={thumbnail_method}'
            if thumbnail_bgcolor:
                url += f'&x-cfs-thumbnail-bgcolor={thumbnail_bgcolor}'
        if image_transform:
            url += f'&x-cfs-image-transform={image_transform}'
        if copy_source:
            url += f'&x-cfs-copy-source={copy_source}'
        return url


    def _sign_url(self, *,
            method,
            url,
            timestamp=None,
            expiry=None,
            request_id=None,
            request_limit=None):
        url += f'&x-cfs-signer={self.signer}'
        if timestamp is None:
            timestamp=datetime.datetime.utcnow()
        url += f'&x-cfs-timestamp={timestamp.strftime("%Y%m%d%H%M%S")}'
        if expiry is None:
            expiry=60
        url += f'&x-cfs-expiry={expiry}'
        if request_id is None:
            request_id=uuid.uuid4().hex
        url += f'&x-cfs-request-id={request_id}'
        if request_limit is None:
            request_limit=1
        url += f'&x-cfs-request-limit={request_limit}'

        parsed_url = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed_url.query)
        signed_parameters = {}
        for param_name in query:
            if param_name.startswith('x-cfs-'):
                signed_parameters[param_name] = query[param_name]

        string_to_sign_elements = [method, parsed_url.netloc, parsed_url.path]
        for param_name in sorted(signed_parameters):
            string_to_sign_elements.append(signed_parameters[param_name][0])
        string_to_sign = '\n'.join(string_to_sign_elements)
        signature = hashlib.blake2b(
                string_to_sign.encode('utf-8'),
                key=self.secret.encode('utf-8')).hexdigest()

        url += f'&x-cfs-signature={signature}'

        return url


    def build_download_object_url(self, *,
            path,
            thumbnail=False,
            thumbnail_size=None,
            thumbnail_method=None,
            thumbnail_bgcolor=None,
            image_transform=None,
            timestamp=None,
            expiry=None,
            request_id=None,
            request_limit=None):
        url = self._build_url(
                path=path,
                action='download',
                thumbnail=thumbnail,
                thumbnail_size=thumbnail_size,
                thumbnail_method=thumbnail_method,
                thumbnail_bgcolor=thumbnail_bgcolor,
                image_transform=image_transform)
        signed_url = self._sign_url(
                method='GET',
                url=url,
                timestamp=timestamp,
                expiry=expiry,
                request_id=request_id,
                request_limit=request_limit)

        return signed_url

