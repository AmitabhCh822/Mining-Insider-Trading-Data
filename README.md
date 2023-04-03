# Mining-Insider-Trading-Data
The dataset in GS.csv consists of mined data from Finnhub.io, which is a real-time RESTful API offering its users access to many different forms of stock trading data. I used their insider transactions API request. I converted the string data into a data frame, which is more functional. I derived the additional attributes, viz.,

DollarAmount: Dollar amount of the transaction

InsiderPortfolioChange: The change ratio of the insider’s overall share of the company

buyOrSale: Whether the transaction was a buy, sale, or gift


I looked into the trading data of one of the most popular public companies, Goldman Sachs. Running the Python file "Mining Insider Trading Data.py" would web scrape the trading data of Goldman Sachs from Finnhub.io and save the data set in a csv file. The stock name of any public company can be assigned to the "stock" variable in the Python file to mine the trading data of that company.

