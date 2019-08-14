$(document).ready(function(){
    $("#btn-buy").click(function(){
        $.ajax({
            url:"/",
            type:"get",
            dataType:"json",
            success : function(response){
            }

        })
    })
})