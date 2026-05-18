from enum import StrEnum


class Address(StrEnum):
    FROM_ADDRESS = "Хамовнический вал, 34"
    TO_ADDRESS = "Зубовский бульвар, 37"


class RoutePanelData:
    SAME_ADDRESS_INFO = {"Авто Бесплатно", "В пути 0 мин."}


class TariffType(StrEnum):
    WORKABLE = "Рабочий"
    SLEEPY = "Сонный"
    VACATION = "Отпускной"
    TALKATIVE = "Разговорчивый"
    COMFORTING = "Утешительный"
    GLOSSY = "Глянцевый"


class TariffsData:
    TARIFFS_DEFAULT_STATE = [
        (TariffType.WORKABLE, True),
        (TariffType.SLEEPY, False),
        (TariffType.VACATION, False),
        (TariffType.TALKATIVE, False),
        (TariffType.COMFORTING, False),
        (TariffType.GLOSSY, False)
    ]

    TARIFFS_DESCRIPTION = {
        TariffType.WORKABLE: "Для деловых особ, которых отвлекают",
        TariffType.SLEEPY: "Для тех, кто не выспался",
        TariffType.VACATION: "Если пришла пора отдохнуть",
        TariffType.TALKATIVE: "Если мысли не выходят из головы",
        TariffType.COMFORTING: "Если хочется свернуться калачиком",
        TariffType.GLOSSY: "Если нужно блистать"
    }

class OrderStatusModalData:
    WAITING_HEADER_TEXT = "Поиск машины"