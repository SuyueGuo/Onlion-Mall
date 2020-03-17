function checkpost(){
	if(document.forms[0].account.value==""||document.forms[0].password.value==""){
		alert("账号或密码不能为空！");
		return false;
	}
	if(document.forms[0].password.value!=document.forms[0].password2.value){
		alert("两次密码输入不一致！");
		return false;
	}
	if(document.getElementById("telephone").value.length != 11){
		alert("电话号码不符合格式！");
		alert(document.getElementById("telephone").value.length);
		return false;
	}
	var pswd = document.getElementById("password").value;	//获取密码
	pswd = hex_md5(pswd);	//把密码进行MD5加密
	document.getElementById("password").value = pswd;
	document.getElementById("password2").value = "0";
	document.getElementById("type").value = "create";
	return true;
}