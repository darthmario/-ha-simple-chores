"""Binary sensor platform for Household Tasks integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import HouseholdTasksCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Household Tasks binary sensors from a config entry."""
    _LOGGER.info("Setting up Simple Chores binary sensors...")
    
    try:
        coordinator: HouseholdTasksCoordinator = hass.data[DOMAIN][entry.entry_id]
        _LOGGER.info("Got coordinator for binary sensor: %s", coordinator)

        entities = [HouseholdTasksHasOverdueSensor(coordinator, entry)]
        async_add_entities(entities)
        _LOGGER.info("Simple Chores binary sensors setup complete!")
        
    except Exception as e:
        _LOGGER.error("Failed to setup Simple Chores binary sensors: %s", e, exc_info=True)


class HouseholdTasksHasOverdueSensor(
    CoordinatorEntity[HouseholdTasksCoordinator], BinarySensorEntity
):
    """Binary sensor indicating if there are overdue chores."""

    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.PROBLEM

    def __init__(
        self, coordinator: HouseholdTasksCoordinator, entry: ConfigEntry
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_has_overdue"
        self._attr_name = "Has Overdue Chores"
        self._attr_icon = "mdi:alert"

    @property
    def is_on(self) -> bool:
        """Return true if there are overdue chores."""
        if self.coordinator.data is None:
            return False
        return self.coordinator.data.get("has_overdue", False)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        if self.coordinator.data is None:
            return {}
        return {
            "overdue_count": self.coordinator.data.get("overdue_count", 0),
        }