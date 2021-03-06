function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getUserId(){
    var user_id = document.getElementById("user_account_id").innerHTML;
    return user_id;
}

function setAjaxCSRF(){
    var csrf_token = getCookie("csrftoken")
    $.ajaxSetup({
        headers: { "X-CSRFToken":csrf_token }
    });
}