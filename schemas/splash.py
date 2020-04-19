"""Schema for FlashModel."""
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from flask_web.models.splash import SplashModel


class SplashSchema(ModelSchema):
    """Marshmallow schema for validation and serialization/deserialization of SplashModel."""

    first_name = fields.String()
    last_name = fields.String()

    class Meta:
        """Meta object for Splash Marshmallow schema."""

        model = SplashModel
        strict = True
