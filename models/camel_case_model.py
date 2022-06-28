from pydantic import BaseModel
from humps.camel import case


class CamelCaseModel(BaseModel):
    """Model that will make fields in the model to camelCase"""

    class Config:
        """Contains configuration for the BaseModel."""
        alias_generator = case
        allow_population_by_field_name = True
