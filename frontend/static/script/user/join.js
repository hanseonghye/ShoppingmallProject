$(document).ready(function(){
    $("#btn-id").click(function(){
        var id = $('#user_id').val()

        if (id == ''){
            return ;
        }

        console.log(id)

        $.ajax({
            url:"/user/checkid/"+id,
            type:"get",
            dataType:"json",
            success : function(response){
                if(response.result != 'success'){
                    alert(response.message)
                    $('#user_id').val('').focus()
                    return ;
                }
                document.getElementsByClassName("join_button")[0].style.display="block"
                alert("사용할 수 있는 아이디 입니다.")

            }

        })
    })
})