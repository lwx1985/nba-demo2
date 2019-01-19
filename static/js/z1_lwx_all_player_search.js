
    $(document).ready(function(){

        //获取GET
        (function ($) {
        $.getUrlParam = function (name) {
            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
            var r = window.location.search.substr(1).match(reg);
            if (r != null) return unescape(r[2]); return null;
                }
        })(jQuery);
        // 将url的get拆成字典
        function getQueryObject(url) {
            url = url == null ? window.location.href : url;
            var search = url.substring(url.lastIndexOf("?") + 1);
            var obj = {};
            var reg = /([^?&=]+)=([^?&=]*)/g;
            search.replace(reg, function (rs, $1, $2) {
                var name = decodeURIComponent($1);
                var val = decodeURIComponent($2);
                val = String(val);
                obj[name] = val;
                return rs;
            });
            return obj;
        }

        //控制排序时候给用户提示的那个上下箭头
        function icon_control(){          
            var order_method = $.getUrlParam('order');
            var sort = '';
            var icon_id = '';
            if(order_method !==null) {
                if (order_method[0] === '-') { //寻找要改变的标签id，并判断排序方式
                    sort = 'down';
                    icon_id = '#' + order_method.substr(1) + '_icon';
                }
                else {
                    sort = 'up';
                    icon_id = '#' + order_method + '_icon';
                }
            }
            else {
                    sort = 'up';
                    icon_id = '#' + order_method + '_icon';
                }
            $(icon_id).css("display","inline"); //将display属性现实出来
            
            if(sort === 'down'){
                $(icon_id).addClass("glyphicon glyphicon-arrow-down");
            }
            else if(sort === 'up'){
                $(icon_id).addClass("glyphicon glyphicon-arrow-up");
            }
            // console.log(order_method);
            // console.log(sort);
             console.log(icon_id);
        }

        
         //排序控制


        //给input加入已经输入过的search值便于用户查看
        function load_search_form_input_value(){
            // var player = $.getUrlParam('player');
            // var age_down = $.getUrlParam('age_down');
            // var age_up = $.getUrlParam('age_up');
            //
            // if(player !== ''){
            //     $("#player_search").attr("value",player);
            // }
            // if(age_down !== ''){
            //     $("#age_down_search").attr("value",age_down);
            // }
            // if(age_up !== ''){
            //     $("#age_up_search").attr("value",age_up);
            // }
            var json = getQueryObject();
            for(var key in json){
                if(key !== 'page' || key !== 'order'){
                    var temp_id = key+ '_search';
                    $('#'+temp_id).attr("value",json[key]);
                }
            }

        }



        load_search_form_input_value();
        icon_control();

        // $('html,body').animate({scrollTop: $("tr#"+"read_all").offset().top}, 500);



    });





