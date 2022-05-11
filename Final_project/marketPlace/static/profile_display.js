function display_items(items){
    for (var key in items) {
        let img = items[key].img_url;
        let name = items[key].name;
        let h = $("<div class=\"grid\"><div class=\"product-pic\">" +
            "<img src=" + img + "  alt /></div><div class=\"details\">" +
            "<h4><a href=\"#\">" + name + "</a></h4>" +
            "</div>\n" +
            "</div>")
        $("#item_box").append(h);
    }
}

$(document).ready(function(){
    display_items(items)
})