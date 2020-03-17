function Submit(){
	var search_text = document.getElementById('search_text').value;
    if (search_text.length == 0) {
        alert('搜索内容不能为空！');
        return;
    }
	var is_login = document.getElementById('is_login').innerHTML;
	var account = ''
    if (Number(is_login)) {
		account = localStorage.account;
	}    
    window.location.href='/commodity?type=search_name&search_text='+search_text+'&account='+account;    
}

function Search(){
	var commodity_list = document.getElementById('commodity_list'); 
	var childs = commodity_list.childNodes; 
	for(var i = childs.length - 1; i >= 0; i--) {
	  commodity_list.removeChild(childs[i]);
	}
	
	var search_text = document.getElementById('search_text').value;
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			return_text = xmlhttp.responseText;
			options = return_text.split(' ');
			var list = document.getElementById("commodity_list");
			for(var i = 0; i < options.length; i++){
				//alert(options[i]);
				var option_ = document.createElement("option");
				option_.value = options[i];
				list.appendChild(option_);
			}

		}
	}
    xmlhttp.open('GET', '/history/?type=get_history&search_text='+search_text, true);
    xmlhttp.send();
	
	
}

function View_By_Type(type){
	var account = '';
	var is_login = localStorage.is_login;
	if(Number(is_login)){
		account = localStorage.account;
	}
	window.location.href='/commodity/?type=search_type&commodity_type='+type+'&account='+account;    
}