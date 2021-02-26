# cryptosql3 using API from www.coinmarketcap.com, tkinter and sqlite3
'''
Command to create .exe file with other files in dist/filename folder:
        pyinstaller filname.py
    Copy favicon.ico file to the dist/filename folder

Command to create SINGLE .exe file in dist folder:
        pyinstaller filename.py --onefile --noconsole --icon=favicon.ico
    Keep favicon.ico file along with the .exe file in the same folder
'''

from tkinter import *
from tkinter import messagebox, Menu
import requests
import json
import sqlite3

def init_coin_table():
    qry_stmt = "DELETE FROM coin"
    curr.execute(qry_stmt)
    conn.commit()
    qry_stmt = "INSERT INTO coin VALUES(1, 'BTC', 2, 3250)"
    curr.execute(qry_stmt)
    qry_stmt = "INSERT INTO coin VALUES(2, 'ETH', 5, 120)"
    curr.execute(qry_stmt)
    qry_stmt = "INSERT INTO coin VALUES(3, 'NEO', 5, 10)"
    curr.execute(qry_stmt)
    qry_stmt = "INSERT INTO coin VALUES(4, 'XMR', 3, 30)"
    curr.execute(qry_stmt)
    conn.commit()

def app_header():
    portfolio_id = Label(pycrypto, text='Portfolio ID', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    portfolio_id.grid(row=0, column=0, sticky=N+S+E+W)

    name = Label(pycrypto, text='Coin Name', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    name.grid(row=0, column=1, sticky=N+S+E+W)

    price = Label(pycrypto, text='Price', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    price.grid(row=0, column=2, sticky=N+S+E+W)

    no_coins = Label(pycrypto, text='Coin Owned', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    no_coins.grid(row=0, column=3, sticky=N+S+E+W)

    amount_paid = Label(pycrypto, text='Total Amount Paid', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    amount_paid.grid(row=0, column=4, sticky=N+S+E+W)

    current_val = Label(pycrypto, text='Current Value', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    current_val.grid(row=0, column=5, sticky=N+S+E+W)

    pl_coin = Label(pycrypto, text='P/L Per Coin', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    pl_coin.grid(row=0, column=6, sticky=N+S+E+W)

    totalpl = Label(pycrypto, text='Total P/L with Coin', bg='#142E54', fg='white', font=('Lato', 12, 'bold'), padx=5, pady=5, borderwidth=2, relief='groove')
    totalpl.grid(row=0, column=7, sticky=N+S+E+W)

def reset():
    for widget in pycrypto.winfo_children():
        widget.destroy()

    app_nav()
    app_header()
    my_portfolio()

def app_nav():

    def close_app():
        pycrypto.destroy()

    def clear_all():
        sure = messagebox.askyesno('Portfolio Notification','Are you sure that you want to DELETE ALL coins from your Portfolio?')
        if sure == True:
            qry_stmt = 'DELETE from coin' 
            curr.execute(qry_stmt)
            conn.commit()
            messagebox.showinfo('Portfolio Notification', 'All Coins Deleted from Portfolio Successfully!')
        reset()

    menu = Menu(pycrypto)
    file_item = Menu(menu)
    file_item.add_command(label='Clear Portfolio', command=clear_all)
    file_item.add_command(label='Close App', command=close_app)
    menu.add_cascade(label='File', menu=file_item)
    pycrypto.config(menu=menu)


def my_portfolio():
    
    def font_color(amount):
        if amount >= 0:
            return 'green'
        else:
            return 'red'

    def insert_coin():
        qry_stmt = 'INSERT INTO coin(symbol, price, amount) VALUES(?, ?, ?)' # each '?' is a place holder for a value 
        values_tuple = (symbol_txt.get().strip().upper(), price_txt.get(), amount_txt.get()) # a tuple of values corresponding to above '?'s
        curr.execute(qry_stmt, values_tuple)
        conn.commit()
        messagebox.showinfo('Portfolio Notification', 'Coin Added to Portfolio Successfully!')
        reset()

    def update_coin():
        qry_stmt = 'UPDATE coin SET symbol=?, price=?, amount=? WHERE id=?' # each '?' is a place holder for a value 
        values_tuple = (symbol_update.get().strip().upper(), price_update.get(), amount_update.get(), portid_update.get()) # a tuple of values corresponding to above '?'s
        curr.execute(qry_stmt, values_tuple)
        conn.commit()
        messagebox.showinfo('Portfolio Notification', 'Coin Updated in Portfolio Successfully!')
        reset()

    def delete_coin():
        sure = messagebox.askyesno('Portfolio Notification','Are you sure that you want to DELETE this coin from your Portfolio?')
        if sure == True:
            qry_stmt = 'DELETE from coin WHERE id=?' # each '?' is a place holder for a value 
            values_tuple = (portid_delete.get()) # a tuple of values corresponding to above '?'s
            curr.execute(qry_stmt, values_tuple)
            conn.commit()
            messagebox.showinfo('Portfolio Notification', 'Coin Deleted from Portfolio Successfully!')
        reset()

    # api_requests = requests.get("https://api.coinmarketcap.com/v1/ticker/") 
    api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=SECRET-KEY") 
    api = json.loads(api_requests.content)
    # print(api)
    '''
    {
    'status': {
            'timestamp': '2021-02-24T03:04:42.213Z', 
            'error_code': 0, 'error_message': None, 
            'elapsed': 11, 'credit_count': 1,
            'notice': None, 'total_count': 4160
            }, 
    'data': [
        {
        'id': 1, 
        'name': 'Bitcoin', 
        'symbol': 'BTC', 
        'slug': 'bitcoin', 
        'num_market_pairs': 9733, 
        'date_added': '2013-04-28T00:00:00.000Z', 
        'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channels', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio'], 
        'max_supply': 21000000, 
        'circulating_supply': 18636862, 
        'total_supply': 18636862, 
        'platform': None, 
        'cmc_rank': 1, 
        'last_updated': '2021-02-24T03:03:02.000Z', 
        'quote': {
            'USD':{
                'price': 50270.5288431758, 
                'volume_24h': 109699558618.71075, 
                'percent_change_1h': 3.64591774, 
                'percent_change_24h': -4.36881374, 
                'percent_change_7d': 1.50412444, 
                'percent_change_30d': 52.49682522, 
                'market_cap': 936884908717.2871, 
                'last_updated': '2021-02-24T03:03:02.000Z'
                }
            }
        }, 
        {
        'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'num_market_pairs': 6016, 'date_added': '2015-08-07T00:00:00.000Z', 'tags': ['mineable', 'pow', 'smart-contracts', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio'], 'max_supply': None, 'circulating_supply': 114796830.374, 'total_supply': 114796830.374, 'platform': None, 'cmc_rank': 2, 'last_updated': '2021-02-24T03:03:02.000Z', 
        'quote': {'USD': {'price': 1620.905064853543, 'volume_24h': 53437984689.85633, 'percent_change_1h': 3.38641335, 'percent_change_24h': -5.48481193, 'percent_change_7d': -8.46622042, 'percent_change_30d': 13.25221493, 'market_cap': 186074763782.34964, 'last_updated': '2021-02-24T03:03:02.000Z'}}
        }
        ]
    }
    '''
    curr.execute('SELECT * FROM coin')
    coins_list = curr.fetchall()
    coins = []
    for coin_tuple in coins_list:
        coin_dic = {}
        coin_dic['id'] = coin_tuple[0]
        coin_dic['symbol'] = coin_tuple[1]
        coin_dic['amount_owned'] = coin_tuple[2]
        coin_dic['price_per_coin'] = coin_tuple[3]
        coins.append(coin_dic)

    total_pl = 0.0
    total_current_value = 0
    total_amount_paid = 0
    coin_row = 1
    for i in range(0, 300):
        for coin in coins:
            if api['data'][i]['symbol'] == coin['symbol']:
                total_paid = coin['amount_owned'] * coin['price_per_coin']
                current_value = coin['amount_owned'] * api['data'][i]['quote']['USD']['price']
                pl_percoin = api['data'][i]['quote']['USD']['price'] - coin['price_per_coin']
                total_pl_coin = pl_percoin * coin['amount_owned']
                
                total_current_value += current_value
                total_amount_paid += total_paid
                total_pl += total_pl_coin

                portfolio_id = Label(pycrypto, text=coin['id'], bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                portfolio_id.grid(row=coin_row, column=0, sticky=N+S+E+W)
                
                name = Label(pycrypto, text=api['data'][i]['symbol'], bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                name.grid(row=coin_row, column=1, sticky=N+S+E+W)
                
                price = Label(pycrypto, text="${0:,.2f}".format(api['data'][i]['quote']['USD']['price']), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                price.grid(row=coin_row, column=2, sticky=N+S+E+W)
                
                no_coins = Label(pycrypto, text=coin['amount_owned'], bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                no_coins.grid(row=coin_row, column=3, sticky=N+S+E+W)
                
                amount_paid = Label(pycrypto, text="${0:,.2f}".format(total_paid), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                amount_paid.grid(row=coin_row, column=4, sticky=N+S+E+W)
                
                current_val = Label(pycrypto, text="${0:,.2f}".format(current_value), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                current_val.grid(row=coin_row, column=5, sticky=N+S+E+W)
                
                pl_coin = Label(pycrypto, text="${0:,.2f}".format(pl_percoin), bg='#F3F4F6', fg=font_color(pl_percoin), font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                pl_coin.grid(row=coin_row, column=6, sticky=N+S+E+W)
                
                totalpl = Label(pycrypto, text="${0:,.2f}".format(total_pl_coin), bg='#F3F4F6', fg=font_color(total_pl_coin), font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
                totalpl.grid(row=coin_row, column=7, sticky=N+S+E+W)
                
                coin_row += 1
                break

    # Insert Data
    symbol_txt = Entry(pycrypto, borderwidth=2, relief='groove')
    symbol_txt.grid(row=coin_row+1, column=1)

    price_txt = Entry(pycrypto, borderwidth=2, relief='groove')
    price_txt.grid(row=coin_row+1, column=2)

    amount_txt = Entry(pycrypto, borderwidth=2, relief='groove')
    amount_txt.grid(row=coin_row+1, column=3)

    add_coin = Button(pycrypto, text="Add Coin", bg='#142E54', fg='white', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove', command=insert_coin)
    add_coin.grid(row=coin_row + 1, column=4, sticky=N+S+E+W)

    # Update Data
    portid_update = Entry(pycrypto, borderwidth=2, relief='groove')
    portid_update.grid(row=coin_row+2, column=0)

    symbol_update = Entry(pycrypto, borderwidth=2, relief='groove')
    symbol_update.grid(row=coin_row+2, column=1)

    price_update = Entry(pycrypto, borderwidth=2, relief='groove')
    price_update.grid(row=coin_row+2, column=2)

    amount_update = Entry(pycrypto, borderwidth=2, relief='groove')
    amount_update.grid(row=coin_row+2, column=3)

    update_coin_btn = Button(pycrypto, text="Update Coin", bg='#142E54', fg='white', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove', command=update_coin)
    update_coin_btn.grid(row=coin_row+2, column=4, sticky=N+S+E+W)

    # Delete Data
    portid_delete = Entry(pycrypto, borderwidth=2, relief='groove')
    portid_delete.grid(row=coin_row+3, column=0)

    delete_coin_btn = Button(pycrypto, text="Delete Coin", bg='#142E54', fg='white', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove', command=delete_coin)
    delete_coin_btn.grid(row=coin_row+3, column=4, sticky=N+S+E+W)


    totalap = Label(pycrypto, text="${0:,.2f}".format(total_amount_paid), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
    totalap.grid(row=coin_row, column=4, sticky=N+S+E+W)

    totalcv = Label(pycrypto, text="${0:,.2f}".format(total_current_value), bg='#F3F4F6', fg='black', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
    totalcv.grid(row=coin_row, column=5, sticky=N+S+E+W)

    totalpl = Label(pycrypto, text="${0:,.2f}".format(total_pl), bg='#F3F4F6', fg=font_color(total_pl), font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove')
    totalpl.grid(row=coin_row, column=7, sticky=N+S+E+W)

    api = ""

    refresh = Button(pycrypto, text="Refresh", bg='#142E54', fg='white', font=('Lato', 10, 'normal'), padx=2, pady=2, borderwidth=2, relief='groove', command=reset)
    refresh.grid(row=coin_row + 1, column=7, sticky=N+S+E+W)

pycrypto = Tk()
pycrypto.title('My Crypto Portfolio')
pycrypto.iconbitmap('favicon.ico')

conn = sqlite3.Connection('coin.db')
curr = conn.cursor()

qry_stmt = "CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)"
curr.execute(qry_stmt)
conn.commit()
# init_coin_table()

app_nav()
app_header()
my_portfolio()
pycrypto.mainloop()

curr.close()
conn.close()

# print('Program Completed')

