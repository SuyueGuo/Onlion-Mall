function Check_Login(){
	var is_login = localStorage.is_login;
	if (Number(is_login)) {
		document.getElementById('name_shopping_cart').removeAttribute("hidden");
		document.getElementById('register_login').setAttribute("hidden","hidden");
		//接下来是把登录信息从localstorage取出
		document.getElementById('user_name').innerHTML = localStorage.name;
	}
}

function Logout(){
	alert("logout");
	document.getElementById('register_login').removeAttribute("hidden");
	document.getElementById('name_shopping_cart').setAttribute("hidden","hidden");
	localStorage.is_login = '0';
	window.location.href='/home/'; 
}

function View_Cart(){
	var account = localStorage.account;
	window.location.href='/shopping_cart/?type=view&account='+account;    
}
function View_Order(){
	var account = localStorage.account;
	window.location.href='/trade/?type=view&account='+account;    
}