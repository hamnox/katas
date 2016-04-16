#usr/bin/python


class Supermarket_Item:
    'This reps a price: simple $ per discrete unit,
     discrete units for fixed price,
     fixed price per continuous unit
     buy X get Y free'

    price_type = null # TODO: how to ENUM in python?
    unit_type = null
    price_per_unit = null
    BOGO = (None, None, None) # buy 0, get 1, at %2 price
    # assume there are no bogo continuous units
    stock = null
    cost = null # seems useful to work this.

    def get_price(units=1):
        # return price of units at checkout
        pass

    def checkout_item(units=1):
        remove_stock(units)
        return get_price(units)
    
    def get_stock():
        # return units and valuation
        # in case of BOGO, make [0]/[1] units full value and the rest
        # [0]/([0]+[1]) value.
        pass

    def remove_stock(units=1):
        # remove units, figure out what to do to clear all
        # or if more than stock removed

#TODO:  how to keep audit trail of pricing decisions
