

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
