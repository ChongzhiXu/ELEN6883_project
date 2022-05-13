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


2. Deploy The Contract -- Using **Huygens_contract_deploy** in the Final project folder<br/><br/>
## Functionality


## Group Members:

- Chongzhi Xu, UNI: cx2273

- Hanwei Tang, UNI: ht2568

- Yi Chen, UNI: yc4029

- Zhihao Sun, UNI: zs2531

- Shihao Ban, UNI: sb4535

From Columbia University in the city of New York

A footnote can also have multiple lines[^2].  

You can also use words, to fit your writing style more closely[^note].

[^1]: Huygens Smart Contract: https://www.youtube.com/watch?v=FfQWVQy5kzg&t=4s, Github link: https://github.com/computecoin-network/Huygens_smartcontract_101
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]:
    Named footnotes will still render with numbers instead of the text but allow easier identification and linking.  
    This footnote also has been made with a different syntax using 4 spaces for new lines.
