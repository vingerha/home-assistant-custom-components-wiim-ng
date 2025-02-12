from homeassistant import config_entries
from homeassistant.helpers import selector
import voluptuous as vol

from . import DOMAIN
from .const import *

CONFIG_FLOW_SCHEMA = vol.Schema({
    vol.Required(CONF_HOST): selector.TextSelector(),
    vol.Required(CONF_NAME): str,
    vol.Optional(CONF_UUID, default=""): str,
    vol.Optional(CONF_VOLUME_STEP, default=5): vol.All(int, vol.Range(min=1, max=25)),
})

class MyIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="WiiM Streamer", data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=CONFIG_FLOW_SCHEMA, errors=errors
        )
