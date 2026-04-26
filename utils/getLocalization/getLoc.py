import asyncio
from winsdk.windows.devices.geolocation import Geolocator, GeolocationAccessStatus
from utils.logger.logger import loggingF

async def getLoc():

    # Verify users settings on Windows

    status = await Geolocator.request_access_async()

    if status != GeolocationAccessStatus.ALLOWED:
        loggingF(3, "The user dosen't have allowed the location permission, it can't be used this function")
        return None
    
    # Init locator

    locator = Geolocator()

    # Getting the position

    pos = await locator.get_geoposition_async()

    return {
        "lat": pos.coordinate.point.position.latitude,
        "lon": pos.coordinate.point.position.longitude,
        "acurracy": pos.coordinate.accuracy
    }


