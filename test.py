import yfinance as yf
data = yf.download("AAPL", period="1mo")


import bulbea as bb
share = bb.Share(data)

from bulbea.learn.evaluation import split
Xtrain, Xtest, ytrain, ytest = split(share, 'Close', normalize = True)