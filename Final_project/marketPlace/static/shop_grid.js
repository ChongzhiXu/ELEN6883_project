function display_items(items){
    for (var key in items) {
        let img = items[key].img_url;
        let name = items[key].name;
        let price = items[key].price;
        let h = $("<div class=\"grid\"><div class=\"product-pic\">" +
            "<img src=" + img + "  alt /></div><div class=\"details\">" +
            "<h4><a href=\"#\">" + name + "</a></h4>" +
            "<span class=\"price\">\n" +
            "<ins>\n" +
            "<span class=\"woocommerce-Price-amount amount\">\n" +
            "<bdi> <span class=\"woocommerce-Price-currencySymbol\"></span>" + price + "</bdi>\n" +
            "</span>\n" +
            "</ins>\n" +
            "</span>\n" +
            "<div class=\"add-cart-area\">\n" +
            "<a href = \"http://172.31.14.28:8081\" ><button class=\"add-to-cart\">Purchase</button></a>\n" +
            "</div>\n" +
            "</div>\n" +
            "</div>")
        $("#item_box").append(h);
    }
}

$(document).ready(function(){
    display_items(items)
})