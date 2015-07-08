from sys import argv
import dropbox
import ystockquote

script, access_token, data_file = argv

print("\nOBVERSE 1.0.0 (mystic-lion)")

# Read from file
print("\nReading Dropbox account access token from external file...")
access_token = open(access_token, "r")
print("Done.")

# Link script to my Dropbox account
dbx = dropbox.Dropbox('access_token')
print("\nSuccessfully linked to Dropbox account.")

# Open file with data
data_file = open(data_file, "w")

# Dictionary for pure stock data
pure_stock_data = {}

# Save stock data to dictionary keys
pure_stock_data['ORCL'] = ystockquote.get_all('ORCL')
pure_stock_data['GOOG'] = ystockquote.get_all('GOOG')
pure_stock_data['FB'] = ystockquote.get_all('FB')
pure_stock_data['YHOO'] = ystockquote.get_all('YHOO')
pure_stock_data['MSFT'] = ystockquote.get_all('MSFT')
pure_stock_data['AAPL'] = ystockquote.get_all('AAPL')
pure_stock_data['BIDU'] = ystockquote.get_all('BIDU')
pure_stock_data['ATVI'] = ystockquote.get_all('ATVI')
pure_stock_data['ADBE'] = ystockquote.get_all('ADBE')

# Write data with ticker symbol label to file
data_file.write("ORCL:\n")
data_file.write(str(pure_stock_data.get('ORCL', "!")))

data_file.write("\n\nGOOG:\n")
data_file.write(str(pure_stock_data.get('GOOG', "!")))

data_file.write("\n\nFB:\n")
data_file.write(str(pure_stock_data.get('FB', "!")))

data_file.write("\n\nYHOO:\n")
data_file.write(str(pure_stock_data.get('YHOO', "!")))

data_file.write("\n\nMSFT:\n")
data_file.write(str(pure_stock_data.get('MSFT', "!")))

data_file.write("\n\nAAPL:\n")
data_file.write(str(pure_stock_data.get('AAPL', "!")))

data_file.write("\n\nBIDU:\n")
data_file.write(str(pure_stock_data.get('BIDU', "!")))

data_file.write("\n\nATVI:\n")
data_file.write(str(pure_stock_data.get('ATVI', "!")))

data_file.write("\n\nADBE:\n")
data_file.write(str(pure_stock_data.get('ADBE', "!")))