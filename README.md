# ELEN6883_Project--Sticker_Marketplace_Decentralized_App

## User Guide
1. Deploy The Contract[^1] -- Using **Huygens_contract_deploy** in the Final project folder<br/>
    1. **Install**
        - Go to the source directory and open terminal, please run this command below
        - > npm install
    2. Rename .env.example to .env and open it, then fill the Huygens_dev/huygens url and account's private key
        - > HUYGENS_DEV_URL=http://18.182.45.18:8765<br/>
            HUYGENS_DEV_PRIVATE_KEY=Your Huygens_dev account's private key for deployment<br/>
            HUYGENS_URL=http://13.212.177.203:8765<br/>
            HUYGENS_PRIVATE_KEY=Your Huygens account's private key for deployment
    3. **Import** the account to remote node and **unlock** it
        - Using Postman API platform (https://www.postman.com), establish the ```account_import``` and ```account_unlock``` request according to the [Tutorial Video](https://www.youtube.com/watch?v=FfQWVQy5kzg&t=4s) and execute the POST request.
        - You should import account sepecified in HUYGENS_DEV_PRIVATE_KEY to Huygens_dev remote node in http://18.182.45.18:8765 or you should import account specifed in HUYGENS_PRIVATE_KEY to Huygens remote node in http://13.212.177.203:8765. It depends on which environment you are using for debugging and developing. Otherwise, there is an ```ProviderError: Invalid account``` error.<br/>
    4. Deploy and test the contract
        - On Huygens_Dev, run this command below  
        - > npx hardhat run scripts/contract.js --network Huygens_dev
        - On Huygens, run this command below  
        - > npx hardhat run scripts/contract.js --network Huygens
    5. Once deployed, you can see the Contract's address and it's balance on terminal.
    <br/>

2. Enable Ale Wallet access from Browser[^2]-- Using **Huygens_alewallet_access** in the Final project folder<br/>
    1. Go to the source directory and open terminal, please run this command below 
        - > npm i
          > npm run serve
    2. Then we can see the access of the Ale Wallet in the terminal, the url we use in the DApp<br/>
    <br/>
    
3. Open Google Chrome and install Ale Wallet extension, sign in your account.<br/><br/>

4. Start DApp on Flask Server-- Using **marketPlace** in the Final project folder<br/>
    1.  **Install Flask**:
    Go to the source directory and open terminal, follow this [documentation](https://flask.palletsprojects.com/en/2.1.x/installation/) to install Flask<br/>
    2.  **Run the server.py to open the User Interface**
        - In the terminal, please run this command below
        - > python server.py
    3. Open the Browser and Enter url http://127.0.0.1:5000/ and Enjoy your shopping!<br/> 


## Functionality
1. Smart Contract Deployment<br/>
    1. Alternating your own contract
    2. Deploy the contact on CCN Test-net<br/>

2. Ale Wallet Browser Access<br/>
    1. User Payment Interface
    2. Payment through CCN Huygens Network<br/>

3. Flask Based DApp User Interface<br/>
    1. MongoDB Backend(pymongo)
        1. Store and provide user information: "Sign Up" enables insert new record in the collection, "Sign In" enables check if the information is in the coleection and give feed back on the interface
        2. Store and provide items information, same as ablove
        3. Record Transaction and items owning relationship
    2. Items browsing and Jumping page payment function
    3. Check the profile and make transaction

## Group Members:

- Chongzhi Xu, UNI: cx2273

- Hanwei Tang, UNI: ht2568

- Yi Chen, UNI: yc4029

- Zhihao Sun, UNI: zs2531

- Shihao Ban, UNI: sb4535

From Columbia University in the city of New York

## Note:

- Because we use a huge template(more than 10000 lines but only less than 100 are used) for frontend design, so the partion of CSS file is high. Please forgive and forget about the portion arrangement


[^1]: Huygens Smart Contract: https://www.youtube.com/watch?v=FfQWVQy5kzg&t=4s, Github link: https://github.com/computecoin-network/Huygens_smartcontract_101
[^2]: Huygens Ale Wallet: https://www.youtube.com/watch?v=YVZS5c50roo&t=6s, Github link: https://github.com/computecoin-network/Huygens_alewallet_101
