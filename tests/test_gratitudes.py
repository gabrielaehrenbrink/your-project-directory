from lib.gratitudes import Gratitudes

def test_empty_gratitude():
    gratitude = Gratitudes()
    result = gratitude.format()
    assert result == "Be grateful for: "


def test_add_gratitude():
    gratitude = Gratitudes()
    gratitude.add("health")
    result = gratitude.format()
    assert result == "Be grateful for: health"


def test_multiple_gratitude():
    gratitude = Gratitudes()
    gratitude.add("health")
    gratitude.add("family")
    gratitude.add("work")
    result = gratitude.format()
    assert result == "Be grateful for: health, family, work"