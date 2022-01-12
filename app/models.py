from sqlalchemy import Boolean, Column, Integer, Float
from database import Base


class Bsc(Base):
    __tablename__ = "bsc"

    id = Column(Integer, primary_key=True, index=True)
    f_iban_history_available = Column(Float)
    f_iban_history_match = Column(Float)
    f_customer_iban_available = Column(Float)
    f_pair_ibans_matches = Column(Float)
    f_pair_amounts_equals = Column(Float)
    f_pair_invoiceId_in_reftext_leven = Column(Float)
    f_pair_ex_invoiceId_in_reftext_leven = Column(Float)
    f_reftext_op_bez_fuzzy_wuzzy = Column(Float)
    f_bsi_name_op_bez_fuzzy_wuzzy = Column(Float)
    f_customer_group_amount_match = Column(Float)
    prediction = Column(Integer)
