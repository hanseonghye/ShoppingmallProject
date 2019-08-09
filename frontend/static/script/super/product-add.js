window.onload = function(){

    $(document).on('change', '.checkboxChange', function(){
        document.getElementsByClassName("options")[0].style.display="block"
        if ($('#is_option').prop('checked') == false){
            document.getElementsByClassName("options")[0].style.display="none"
        }else{
            document.getElementsByClassName("options")[0].style.display="block"
        }
    })


    $(document).on('click','.plus2-li', function(e){
        var li = document.createElement('li')
        var input = document.createElement('input')
        input.setAttribute('type','text')
        input.setAttribute('name','option-value')
        li.appendChild(input)
        this.before(li)
    })

    $('#plus1').click(function(){
        $(".options").append(
        `
            <div class="option-border">
            <div class="option">
                <input type="text" name="option-name" id="option-name" placeholder="옵션 명"/>
                <ul><li class="plus2-li">+</li></ul>
            </div>
            </div>
        `)
    })
//    $('.plus2-li').click(function(){
//         $(".plus2-li").before("<li><input type='text'></li>")
//    })

//    $('#submit').click(function(){
//        var options = document.getElementsByClassName('option')
//        request_options =[]
//        for ( var i = 0 ; i<options.length; ++i){
//            var input = options[i].getElementsByTagName('input')
//            option = {
//                "name":input[0].value,
//            }
//            option_details = []
//
//            for ( var j=1; j<input.length; ++j){
//                option_details.push({"name":input[j]})
//            }
//
//            option.option_details = option_details
//            request_options.push(option)
//
//        }
//
//        var category = document.getElementById("category");
//
//        var data ={
//                "name":document.getElementById("name"),
//                "price":document.getElementById("price"),
//                "is_stock":document.getElementById('is_stock').checked,
//                "is_display":document.getElementById('is_display').checked,
//                "is_option":document.getElementById('is_option').checked,
//                "file_url":document.getElementById("file_url"),
//                "image_url":document.getElementById("image_url"),
//                "category":category.options[category.selectedIndex].value,
//                "product_options": request_options
//            }
//
//        $.ajax({
//            url:"/super/products/add",
//            type:"post",
//            dataType:"json",
//            data:{"data":data},
//            headers: {'X-CSRFToken': document.getElementById('csrf_token').value},
//            success : function(response){
//            }
//
//        })
//    }
//
//
//$('#form input[type="submit"]').click(function(){
//
//    var options = document.getElementsByClassName('option')
//    request_options =[]
//    for ( var i = 0 ; i<options.length; ++i){
//        var input = options[i].getElementsByTagName('input')
//        option = {
//            "name":input[0].value,
//        }
//        option_details = []
//
//        for ( var j=1; j<input.length; ++j){
//            option_details.push({"name":input[j]})
//        }
//
//        option.option_details = option_details
//        request_options.push(option)
//
//    }
//
//    var category = document.getElementById("category");
//
//    var data ={
//            "name":document.getElementById("name"),
//            "price":document.getElementById("price"),
//            "is_stock":document.getElementById('is_stock').checked,
//            "is_display":document.getElementById('is_display').checked,
//            "is_option":document.getElementById('is_option').checked,
//            "file_url":document.getElementById("file_url"),
//            "image_url":document.getElementById("image_url"),
//            "category":category.options[category.selectedIndex].value,
//            "product_options": request_options
//        }
//
//        $('#form').addHiddenInputData({
//            'data':data
//        })
//
//    });

    function readURL(input, preview_id) {
      if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
          $(preview_id).attr('src', e.target.result);
        }
        document.getElementsByClassName("preview")[0].style.display="block"

        reader.readAsDataURL(input.files[0]);
      }
    }

    $("#img_main").change(function() {
      readURL(this,'#'+'preview_main');
    });


}