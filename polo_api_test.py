from time import time, sleep, strptime
from polo_loan_agent import LoanAgent
import poloniex
import requests
import datetime
import logging


def init_logger():
    """Create and configure logger"""

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    log_file = logging.FileHandler('log.log', 'w+')
    formatter = logging.Formatter(
        "%(asctime)s:%(levelname)s:%(module)s - %(message)s")
    log_file.setFormatter(formatter)
    logger.addHandler(log_file)
    # supress requests/urlib3 messages as logging.DEBUG produces messages
    # with every single http request.
    logging.getLogger("urllib3").propagate = False
    requests_log = logging.getLogger("requests")
    requests_log.addHandler(logging.NullHandler())
    requests_log.propagate = False

    return logger


logger = init_logger()

LOAN_PROVIDER = "Poloniex"
LOAN_ASSET = "USDC"
MIN_LOAN = 50
POLO_API = poloniex.Poloniex(
    key='HHDRON6N-H7C3LA42-AXV8EMJI-LPLUQD2Y',
    secret="c05289ca176fc5981118756accc84172a513609df14b8fa887"
        "cf6cf980292f724efbacd5fcd925f810cfaf71c0edfff31a4d0cfc"
        "1e41ea23a1a3cad1706d5c44")

PUBLIC_COMMANDS = [
    'returnTicker',
    'return24hVolume',
    'returnOrderBook',
    'marketTradeHist',
    'returnChartData',
    'returnCurrencies',
    'returnLoanOrders']

PRIVATE_COMMANDS = [
    'returnBalances',
    'returnCompleteBalances',
    'returnDepositAddresses',
    'generateNewAddress',
    'returnDepositsWithdrawals',
    'returnOpenOrders',
    'returnTradeHistory',
    'returnAvailableAccountBalances',
    'returnTradableBalances',
    'returnOpenLoanOffers',
    'returnOrderTrades',
    'returnOrderStatus',
    'returnActiveLoans',
    'returnLendingHistory',
    'createLoanOffer',
    'cancelLoanOffer',
    'toggleAutoRenew',
    'buy',
    'sell',
    'cancelOrder',
    'cancelAllOrders',
    'moveOrder',
    'withdraw',
    'returnFeeInfo',
    'transferBalance',
    'returnMarginAccountSummary',
    'marginBuy',
    'marginSell',
    'getMarginPosition',
    'closeMarginPosition']

# loan_agent = LoanAgent(
#     logger,
#     POLO_API,
#     {LOAN_ASSET: MIN_LOAN},
#     100)

# while 1:
#     sleep(10)

rate = POLO_API.returnActiveLoans()['provided']
# rate = float(rate) * 100
print(rate)

# print(POLO_API.returnAvailableAccountBalances())
# print(POLO_API.returnOpenLoanOffers())
# print(POLO_API.returnLoanOrders('USDC'))