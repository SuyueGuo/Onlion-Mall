function checkpost(){
	if(document.forms[0].account.value==""||document.forms[0].password.value==""){
		alert("账号或密码不能为空！");
		return false;
	}
	var pswd = document.getElementById("password").value;	//密码加密传输
	pswd = hex_md5(pswd);
	document.getElementById("password").value = pswd;
	document.getElementById("type").value = "login";
	return true;
}