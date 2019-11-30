from time import time, sleep, strptime
import requests
import datetime
import logging


class Hedge:
    """	Hedge class models the hedge taken to mitigate loan volatility. """

    """ Industry-standard monthly futures contract codes. The month code
        signifies contract delivery month e.g AUDJPYZ19 would be a contract
        derived from the AUDJPY pair with settlement (expiry) in December 2019.
    """
    FUTURES_MONTH_CODES = {
        'F': 'Jan', 'G': 'Feb', 'H': 'Mar', 'J': 'Apr', 'K': 'mar', 'M': 'Jun',
        'N': 'Jul', 'Q': 'Aug', 'U': 'Sep', 'V': 'Oct', 'X': 'Nov', 'Z': 'Dec'}

	def __init__(self, logger, api, asset, value, duration):
        self.logger = logger
        self.api = api

        # Asset the hedge is covering. For our example, Bitcoin
        self.underlying_asset = asset

        # USD value of the hedge. Must have exact 1:1 parity with loan size.
        self.value = value

        # Fixed termination date of the hedge (and loan).
        self.close_date = self.close_date(duration)

        # Use the perpetual swap contract as the default hedging instrument.
        self.default_instrument = "XBTUSD"

        # Instrument code currently in use, perpetual swap is default.
        self.current_instrument = self.default_instrument

        # Futures rollover date for instrument in use.
        self.rollover_date = None

        # Hedge status - when hedge terminated, this will be false.
        self.active = True

    def open_hedge(self):
        """Open a hedge (short positon) with the specified instrument, default
        is perpetual swap contact."""

        order = api.Order.Order_new(
            symbol=self.current_instrument,
            orderQty=(self.value * -1)).result()

        print("Hedge opened for " + self.value + " contracts.")
        self.active = True

        # Return transaction details json
        return order

    def terminate_hedge(self):
        """Close the hedge postion and return confirmation dict containing
        details of the closed positon. Hedge cLosure effective immediately."""

        # Close all positions
        result = api.Order.Order_new(
            symbol=self.current_instrument,
            ordType='Market',
            execInst='Close').result()

        print("Hedge closed for " + result[0]['orderQty'] + " contracts.")
        self.active = False

        # Return transaction details json
        return result
