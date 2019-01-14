# crushfs
Python 3 client for CrushFS (sync and async)

## Async usage (depends on aiohttp)
```python
import asyncio
import crushfs

WAREHOUSE='mywarehouse'
SIGNER='me'
SECRET='letmein'
PATH='/apath/afile'

async def async_test():
    client = crushfs.AsyncClient(
            warehouse=WAREHOUSE, signer=SIGNER, secret=SECRET)
    response = await client.download_object(path=PATH)
    print(len(response.data))

asyncio.run(async_test())
```

## Sync usage (depends on requests)
```python
import crushfs

WAREHOUSE='mywarehouse'
SIGNER='me'
SECRET='letmein'
PATH='/apath/afile'

def sync_test():
    client = crushfs.SyncClient(
            warehouse=WAREHOUSE, signer=SIGNER, secret=SECRET)
    response = client.download_object(path=PATH)
    print(len(response.data))

sync_test()
```
