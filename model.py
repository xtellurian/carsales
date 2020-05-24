# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = car_sales_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Type, cast, Callable
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Audience:
    type: str
    audience_type: str

    def __init__(self, type: str, audience_type: str) -> None:
        self.type = type
        self.audience_type = audience_type

    @staticmethod
    def from_dict(obj: Any) -> 'Audience':
        assert isinstance(obj, dict)
        type = from_str(obj.get("@type"))
        audience_type = from_str(obj.get("audienceType"))
        return Audience(type, audience_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = from_str(self.type)
        result["audienceType"] = from_str(self.audience_type)
        return result


class Name(Enum):
    SUBARU = "Subaru"


class BrandType(Enum):
    BRAND = "Brand"


class Brand:
    type: BrandType
    name: Name

    def __init__(self, type: BrandType, name: Name) -> None:
        self.type = type
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'Brand':
        assert isinstance(obj, dict)
        type = BrandType(obj.get("@type"))
        name = Name(obj.get("name"))
        return Brand(type, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(BrandType, self.type)
        result["name"] = to_enum(Name, self.name)
        return result


class ImageType(Enum):
    IMAGE_OBJECT = "ImageObject"


class Image:
    type: ImageType
    url: str
    height: int
    width: int

    def __init__(self, type: ImageType, url: str, height: int, width: int) -> None:
        self.type = type
        self.url = url
        self.height = height
        self.width = width

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        type = ImageType(obj.get("@type"))
        url = from_str(obj.get("url"))
        height = from_int(obj.get("height"))
        width = from_int(obj.get("width"))
        return Image(type, url, height, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(ImageType, self.type)
        result["url"] = from_str(self.url)
        result["height"] = from_int(self.height)
        result["width"] = from_int(self.width)
        return result


class MileageFromOdometerType(Enum):
    QUANTITATIVE_VALUE = "QuantitativeValue"


class UnitCode(Enum):
    KM = "KM"


class MileageFromOdometer:
    type: MileageFromOdometerType
    unit_code: UnitCode
    value: int

    def __init__(self, type: MileageFromOdometerType, unit_code: UnitCode, value: int) -> None:
        self.type = type
        self.unit_code = unit_code
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'MileageFromOdometer':
        assert isinstance(obj, dict)
        type = MileageFromOdometerType(obj.get("@type"))
        unit_code = UnitCode(obj.get("unitCode"))
        value = int(from_str(obj.get("value")))
        return MileageFromOdometer(type, unit_code, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(MileageFromOdometerType, self.type)
        result["unitCode"] = to_enum(UnitCode, self.unit_code)
        result["value"] = from_str(str(self.value))
        return result


class Model(Enum):
    OUTBACK = "Outback"


class PriceCurrency(Enum):
    AUD = "AUD"


class OffersType(Enum):
    OFFER = "Offer"


class ItemOffers:
    type: OffersType
    price_currency: PriceCurrency
    price: int

    def __init__(self, type: OffersType, price_currency: PriceCurrency, price: int) -> None:
        self.type = type
        self.price_currency = price_currency
        self.price = price

    @staticmethod
    def from_dict(obj: Any) -> 'ItemOffers':
        assert isinstance(obj, dict)
        type = OffersType(obj.get("@type"))
        price_currency = PriceCurrency(obj.get("priceCurrency"))
        price = int(from_str(obj.get("price")))
        return ItemOffers(type, price_currency, price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(OffersType, self.type)
        result["priceCurrency"] = to_enum(PriceCurrency, self.price_currency)
        result["price"] = from_str(str(self.price))
        return result


class ItemType(Enum):
    VEHICLE = "Vehicle"


class EngineDisplacement:
    type: MileageFromOdometerType
    value: str

    def __init__(self, type: MileageFromOdometerType, value: str) -> None:
        self.type = type
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'EngineDisplacement':
        assert isinstance(obj, dict)
        type = MileageFromOdometerType(obj.get("@type"))
        value = obj.get("value")
        return EngineDisplacement(type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(MileageFromOdometerType, self.type)
        result["value"] = self.value
        return result


class VehicleEngineType(Enum):
    ENGINE_SPECIFICATION = "EngineSpecification"


class VehicleEngine:
    type: VehicleEngineType
    engine_displacement: EngineDisplacement

    def __init__(self, type: VehicleEngineType, engine_displacement: EngineDisplacement) -> None:
        self.type = type
        self.engine_displacement = engine_displacement

    @staticmethod
    def from_dict(obj: Any) -> 'VehicleEngine':
        assert isinstance(obj, dict)
        type = VehicleEngineType(obj.get("@type"))
        engine_displacement = EngineDisplacement.from_dict(obj.get("engineDisplacement"))
        return VehicleEngine(type, engine_displacement)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(VehicleEngineType, self.type)
        result["engineDisplacement"] = to_class(EngineDisplacement, self.engine_displacement)
        return result


class Item:
    type: ItemType
    url: str
    name: str
    model: Model
    brand: Brand
    body_type: str
    mileage_from_odometer: MileageFromOdometer
    vehicle_engine: VehicleEngine
    offers: ItemOffers
    image: List[Image]

    def __init__(self, type: ItemType, url: str, name: str, model: Model, brand: Brand, body_type: str, mileage_from_odometer: MileageFromOdometer, vehicle_engine: VehicleEngine, offers: ItemOffers, image: List[Image]) -> None:
        self.type = type
        self.url = url
        self.name = name
        self.model = model
        self.brand = brand
        self.body_type = body_type
        self.mileage_from_odometer = mileage_from_odometer
        self.vehicle_engine = vehicle_engine
        self.offers = offers
        self.image = image

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        type = ItemType(obj.get("@type"))
        url = from_str(obj.get("url"))
        name = from_str(obj.get("name"))
        model = Model(obj.get("model"))
        brand = Brand.from_dict(obj.get("brand"))
        body_type = from_str(obj.get("bodyType"))
        mileage_from_odometer = MileageFromOdometer.from_dict(obj.get("mileageFromOdometer"))
        vehicle_engine = VehicleEngine.from_dict(obj.get("vehicleEngine"))
        offers = ItemOffers.from_dict(obj.get("offers"))
        image = from_list(Image.from_dict, obj.get("image"))
        return Item(type, url, name, model, brand, body_type, mileage_from_odometer, vehicle_engine, offers, image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(ItemType, self.type)
        result["url"] = from_str(self.url)
        result["name"] = from_str(self.name)
        result["model"] = to_enum(Model, self.model)
        result["brand"] = to_class(Brand, self.brand)
        result["bodyType"] = from_str(self.body_type)
        result["mileageFromOdometer"] = to_class(MileageFromOdometer, self.mileage_from_odometer)
        result["vehicleEngine"] = to_class(VehicleEngine, self.vehicle_engine)
        result["offers"] = to_class(ItemOffers, self.offers)
        result["image"] = from_list(lambda x: to_class(Image, x), self.image)
        return result


class ItemListElementType(Enum):
    LIST_ITEM = "ListItem"


class ItemListElement:
    type: ItemListElementType
    position: int
    item: Item

    def __init__(self, type: ItemListElementType, position: int, item: Item) -> None:
        self.type = type
        self.position = position
        self.item = item

    @staticmethod
    def from_dict(obj: Any) -> 'ItemListElement':
        assert isinstance(obj, dict)
        type = ItemListElementType(obj.get("@type"))
        position = from_int(obj.get("position"))
        item = Item.from_dict(obj.get("item"))
        return ItemListElement(type, position, item)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(ItemListElementType, self.type)
        result["position"] = from_int(self.position)
        result["item"] = to_class(Item, self.item)
        return result


class MainEntity:
    type: str
    number_of_items: int
    item_list_element: List[ItemListElement]

    def __init__(self, type: str, number_of_items: int, item_list_element: List[ItemListElement]) -> None:
        self.type = type
        self.number_of_items = number_of_items
        self.item_list_element = item_list_element

    @staticmethod
    def from_dict(obj: Any) -> 'MainEntity':
        assert isinstance(obj, dict)
        type = from_str(obj.get("@type"))
        number_of_items = from_int(obj.get("numberOfItems"))
        item_list_element = from_list(ItemListElement.from_dict, obj.get("itemListElement"))
        return MainEntity(type, number_of_items, item_list_element)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = from_str(self.type)
        result["numberOfItems"] = from_int(self.number_of_items)
        result["itemListElement"] = from_list(lambda x: to_class(ItemListElement, x), self.item_list_element)
        return result


class CarSalesOffers:
    type: OffersType
    availability: str

    def __init__(self, type: OffersType, availability: str) -> None:
        self.type = type
        self.availability = availability

    @staticmethod
    def from_dict(obj: Any) -> 'CarSalesOffers':
        assert isinstance(obj, dict)
        type = OffersType(obj.get("@type"))
        availability = from_str(obj.get("availability"))
        return CarSalesOffers(type, availability)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(OffersType, self.type)
        result["availability"] = from_str(self.availability)
        return result


class Target:
    type: str
    url_template: str

    def __init__(self, type: str, url_template: str) -> None:
        self.type = type
        self.url_template = url_template

    @staticmethod
    def from_dict(obj: Any) -> 'Target':
        assert isinstance(obj, dict)
        type = from_str(obj.get("@type"))
        url_template = from_str(obj.get("urlTemplate"))
        return Target(type, url_template)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = from_str(self.type)
        result["urlTemplate"] = from_str(self.url_template)
        return result


class PotentialAction:
    type: str
    target: Target

    def __init__(self, type: str, target: Target) -> None:
        self.type = type
        self.target = target

    @staticmethod
    def from_dict(obj: Any) -> 'PotentialAction':
        assert isinstance(obj, dict)
        type = from_str(obj.get("@type"))
        target = Target.from_dict(obj.get("target"))
        return PotentialAction(type, target)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = from_str(self.type)
        result["target"] = to_class(Target, self.target)
        return result


class CarSales:
    context: str
    type: str
    audience: Audience
    potential_action: PotentialAction
    main_entity: MainEntity
    offers: CarSalesOffers

    def __init__(self, context: str, type: str, audience: Audience, potential_action: PotentialAction, main_entity: MainEntity, offers: CarSalesOffers) -> None:
        self.context = context
        self.type = type
        self.audience = audience
        self.potential_action = potential_action
        self.main_entity = main_entity
        self.offers = offers

    @staticmethod
    def from_dict(obj: Any) -> 'CarSales':
        assert isinstance(obj, dict)
        context = from_str(obj.get("@context"))
        type = from_str(obj.get("@type"))
        audience = Audience.from_dict(obj.get("audience"))
        potential_action = PotentialAction.from_dict(obj.get("potentialAction"))
        main_entity = MainEntity.from_dict(obj.get("mainEntity"))
        offers = CarSalesOffers.from_dict(obj.get("offers"))
        return CarSales(context, type, audience, potential_action, main_entity, offers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@context"] = from_str(self.context)
        result["@type"] = from_str(self.type)
        result["audience"] = to_class(Audience, self.audience)
        result["potentialAction"] = to_class(PotentialAction, self.potential_action)
        result["mainEntity"] = to_class(MainEntity, self.main_entity)
        result["offers"] = to_class(CarSalesOffers, self.offers)
        return result


def car_sales_from_dict(s: Any) -> CarSales:
    return CarSales.from_dict(s)


def car_sales_to_dict(x: CarSales) -> Any:
    return to_class(CarSales, x)