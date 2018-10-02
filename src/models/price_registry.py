import sys
sys.path.append('../')
from utils.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float

class PriceRegistry(Base):
    __tablename__ = 'price_registry'
    id = Column(Integer, primary_key=True)
    currency = Column(String(3), nullable=False)
    original_amount = Column(Float, nullable=False)
    converted_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, currency=None, original_amount=None, converted_amount=None, created_at=None):
        self.currency = currency
        self.original_amount = original_amount
        self.converted_amount = converted_amount
        self.created_at = created_at

    def __repr__(self):
        return "<PriceRegistry {}({}) -> {}  >".format(self.currency, self.original_amount,
                                                       self.converted_amount)
    def serialize(self):
        return {
            'currency': self.currency,
            'original_amount': self.original_amount,
            'converted_amount': self.converted_amount,
            'created_at': self.created_at
        }
