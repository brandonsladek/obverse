from sys import argv
import dropbox
import ystockquote

script, filename = argv

print("OBVERSE 1.0.0 (mystic-lion)")

# Read from file
print("Reading Dropbox account access token from external file...")
target = open(filename, "r")

# Link script to my Dropbox account
dbx = dropbox.Dropbox('target')

# Print stock prices for companies
print("Google stock price: %s" % (ystockquote.get_price('GOOG')))
print("Apple stock price: %s" % (ystockquote.get_price('AAPL')))
print("Yahoo stock price: %s" % (ystockquote.get_price('YHOO')))








