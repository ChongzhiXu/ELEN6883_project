<template>
  <div class="hello app-container">
    <div class="badge_front" style="margin-bottom:50px">
            Sticker MarketPlace DApp<br> Finish Your Payment!
    </div>
    <div style="margin-bottom:50px">
    <img src="data:image/png;base64,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"
    alt>
    </div>
    <div style="color: #f00" v-show="isConnected">Connect Success!</div>
    <div class = "row" v-show="isConnected">You are using this Ale Wallet:</div>
    <h1 v-show="isConnected">{{ account }}</h1>

    <button v-show="!isConnected" @click="connect">Connect</button>
  
    <button  v-show="isConnected" @click="approveMoney">Pay Now</button>
    <div style="margin-top:10px">
    <a href="http://127.0.0.1:5000/shop_items">Back to shop</a>
    </div>
  </div>
</template>

<script>

import services from "@/api";

export default {
  data() {
    return {
      account: "",
      isConnected: false,
    };
  },
  watch: {
    "$store.state.dapp": {
      handler(val) {
        this.account = val.account;
        this.isConnected = val.isConnected;
      },
      immediate: true,
      deep: true,
    },
  },
  methods: {
    connect() {
      window["aleereum"] && window["aleereum"].connect();
    },
    approveMoney() {
      services.getName().then(res => {
        console.log(res);
      });
      services.approve(100).then((res) => {
        console.log(res);
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
h1 {
  font-size:15px;
}
button{
    border: 1px solid #F21137;
    border-radius: 30px;
    width:130px;
    height:45px;
    color : white;
    font-size : 20px;
    font-weight : bold;
    background-color : #F21137;
}

.app-container{
    width:400px;
    height:auto;
    border-style: solid;
    border-width: 2px;
    border-radius: 7px;
    border-color: lightgray;
    margin-left: auto;
    margin-right: auto;
    margin-top: 40px;
    margin-bottom: 40px;
    padding-top: 15px;
    padding-left: 15px;
    padding-right: 15px;
    padding-bottom: 15px;
    /* background-color: white;
    opacity: 0.95; */
    text-align: center;
}
.badge_front{
    background-color: rgb(203,68, 74);
    border-radius: 7px;
    color: white;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 20px;
    padding-right: 20px;
    margin-bottom: 15px;
    font-size : 20px;
    /* opacity: 50%; */
}
</style>
