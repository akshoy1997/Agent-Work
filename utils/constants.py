from enum import Enum


class SerializerVersion(Enum):
    """
    Every Model serializer maps to a version
    """
    V1 = 'v1'


class OfferTiming(Enum):
    RANDOM = 'random'
    HOURLY = 'hourly'


class SmsText(Enum):
    CALLBACK = "You have a call request from '{0}'. Please call back {1} "
