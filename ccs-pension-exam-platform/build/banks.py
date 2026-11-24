"""banks.py — every authored question bank, imported in order.

Import order is authoring order, which is chapter order. Adding a bank means adding an
import here and nothing else.
"""
import authoring

import bank_ch1   # I-II    commencement, application, definitions, claims, good conduct
import bank_ch2   # III     qualifying service
import bank_ch3   # IV-V    emoluments, classes of pension
import bank_ch4   # VI-IX   retirement, regulation, family pension, DR
import bank_ch5   # X-XIV   processing, death in service, payment

BANKS = authoring.BANKS
