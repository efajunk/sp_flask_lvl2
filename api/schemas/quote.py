from api import ma
from api.models.quote import QuoteModel


class QuoteSchema(ma.SQLAlchemySchema):
   class Meta:
       model = QuoteModel

   id = ma.auto_field()
   quote = ma.auto_field()

quote_schema = QuoteSchema
