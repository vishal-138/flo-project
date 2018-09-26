from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:17313"%("vishal", "blockchain"))
passphrase = rpc_connection.walletpassphrase("blockchain", 8000)
import hashlib
name = input("User name:")
name = hashlib.sha3_256()
name.hexdigest()
print(name.hexdigest())
getbalance = rpc_connection.getbalance()
print(getbalance)

while True:
    passphrase = input('Enter Passphrase: ')
    if passphrase=="blockchain":
        print ("Passphrase Correct!"
               " your new address is")
        break
    else:
        print ("Passphrase incorrect!")
getnewaddress = rpc_connection.getnewaddress()
print(getnewaddress)
Address = input("Enter address of receiver:")
Amount = input("Amount to spend:")
Comment = input("Comment about the transaction:")
Name = input("Name to whom amount to be sent:")
Txcomment = input("Write comment here to be recorded in blockchain:")

send = rpc_connection.sendtoaddress(Address,Amount,Comment,Name,False,False,1,'UNSET',Txcomment)
print("Amount sent to the respective address")

#get info of transaction id
gettransaction = rpc_connection.gettransaction(input("transaction id:"))
print(gettransaction)



