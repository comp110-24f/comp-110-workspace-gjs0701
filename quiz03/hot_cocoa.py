class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(
        self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int
    ):
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_ader(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += 2 * mallows

    def __str__(self) -> str:
        if self.has_whip is True:
            return f"A {self.flavor} cocoa with whip, {self.marshmallow_count} marshmallows, and a level {self.sweetness} sweetness."
        else:
            return f"A {self.flavor} cocoa without whip, {self.marshmallow_count} marshmallows, and a level {self.sweetness} sweetness."


def order_cost(order: list[HotCocoa]) -> float:
    cost: float = 0.00
    for cocoa in order:
        if cocoa.has_whip is True:
            cost += 2.50
        else:
            cost += 2.00
    return cost


my_order: HotCocoa = HotCocoa(False, "vanilla", 5, 2)
my_order.has_whip = True
my_order.mallow_ader(2)
viktoryas_order: HotCocoa = HotCocoa(True, "peppermint", 10, 2)
print(order_cost([my_order, viktoryas_order]))
print(my_order)
print(viktoryas_order)
