def filter_by_currency(transaction, currency):
    for key in transaction:
        if key["OperationAmount"]["currency"]["name"] == currency:
            pass
