function Submit(){
	var search_text = document.getElementById('search_text').value;
    if (search_text.length == 0) {
        alert('搜索内容不能为空！');
        return;
    }
	var is_login = localStorage.is_login;		//判断用户是否登录，如果登录还要把用户账号也发送到后台
	var account = ''
    if (Number(is_login)) {
		account = localStorage.account;
		//alert(account);
	}    
    window.location.href='/commodity?type=search_name&search_text='+search_text+'&account='+account;    
}

function Check_Login_Index(){
	var is_login = document.getElementById('is_login').innerHTML;
	if (Number(is_login)) {
		document.getElementById('name_shopping_cart').removeAttribute("hidden");
		document.getElementById('register_login').setAttribute("hidden","hidden");
		//接下来是把登录信息存入localstorage
		localStorage.is_login = '1';
		localStorage.account = document.getElementById('account').innerHTML;
		localStorage.name = document.getElementById('user_name').innerHTML;
		document.getElementById('account').innerHTML = '';
	}
	if (Number(is_login) == 0){
		is_login = localStorage.is_login;
		if(Number(is_login)){
			document.getElementById('name_shopping_cart').removeAttribute("hidden");
			document.getElementById('register_login').setAttribute("hidden","hidden");
			//接下来是把登录信息从localstorage取出
			document.getElementById('user_name').innerHTML = localStorage.name;
		}
	}
}

function Search(){
	var commodity_list = document.getElementById('commodity_list'); 
	var childs = commodity_list.childNodes; 
	for(var i = childs.length - 1; i >= 0; i--) {		//清空下拉框
	  commodity_list.removeChild(childs[i]);
	}
	
	var search_text = document.getElementById('search_text').value;	//把用户输入框里面的内容发送到后台，获取历史搜索记录
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			return_text = xmlhttp.responseText;
			options = return_text.split(' ');
			var list = document.getElementById("commodity_list");
			for(var i = 0; i < options.length; i++){		//把历史搜索结果加入下拉列表中
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