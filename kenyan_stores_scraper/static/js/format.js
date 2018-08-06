var details = document.getElementsByClassName('details');
    for(i=0;i<details.length;i++){
        var detail = 'detail'.concat(i);
        var detail = details[i].innerText.replace('{','').replace('}','');
        var b = detail.split(',');
        var items =' ';
        b.forEach(function(item){
            items = items+item+'\t';


        });
        details[i].innerText=items;

    }

$(document).ready(function(){

    $('.product-name #prod_link').each(function(){
       var name = $(this).html().slice(0,100);
       $(this).html(name);
    })
    $(".details").each(function(){
        var detal = $(this).html().slice(0,150);
        $(this).html(detal);
    });

});
