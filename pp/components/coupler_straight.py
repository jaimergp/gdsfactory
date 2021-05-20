import pp
from pp.component import Component
from pp.components.straight import straight as straight_function
from pp.types import ComponentFactory


@pp.cell_with_validator
def coupler_straight(
    length: float = 10.0,
    gap: float = 0.27,
    straight: ComponentFactory = straight_function,
    **kwargs
) -> Component:
    """Coupler_straight with two parallel straights.

    Args:
        length: of straight
        gap: between straights
        straight: straight waveguide function
        kwargs: overwrites waveguide_settings
    """
    component = Component()

    straight_component = (
        straight(length=length, **kwargs) if callable(straight) else straight
    )

    top = component << straight_component
    bot = component << straight_component

    # bot.ymax = 0
    # top.ymin = gap

    top.movey(straight_component.width + gap)

    component.add_port("W0", port=bot.ports["W0"])
    component.add_port("W1", port=top.ports["W0"])
    component.add_port("E0", port=bot.ports["E0"])
    component.add_port("E1", port=top.ports["E0"])
    return component


if __name__ == "__main__":
    c = coupler_straight(width=1)
    c.show(show_ports=True)
