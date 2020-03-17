function Change_Image1(){
	commodity_id = document.getElementById("commodity_id").innerHTML;
	document.getElementById("main_image").src="/static/images/single1_"+commodity_id+".png";
	document.getElementById("edition").innerHTML = document.getElementById("edition_1").innerHTML;
	document.getElementById("edition_id").innerHTML = '1';
}

function Change_Image2(){
	commodity_id = document.getElementById("commodity_id").innerHTML;
	document.getElementById("main_image").src="/static/images/single2_"+commodity_id+".png";
	document.getElementById("edition").innerHTML = document.getElementById("edition_2").innerHTML;
	document.getElementById("edition_id").innerHTML = '2';
}

function Change_Image3(){
	commodity_id = document.getElementById("commodity_id").innerHTML;
	document.getElementById("main_image").src="/static/images/single3_"+commodity_id+".png";
	document.getElementById("edition").innerHTML = document.getElementById("edition_3").innerHTML;
	document.getElementById("edition_id").innerHTML = '3';
}

function Change_Image4(){
	commodity_id = document.getElementById("commodity_id").innerHTML;
	document.getElementById("main_image").src="/static/images/single4_"+commodity_id+".png";
	document.getElementById("edition").innerHTML = document.getElementById("edition_4").innerHTML;
	document.getElementById("edition_id").innerHTML = '4';
}

function Change_Image5(){
	commodity_id = document.getElementById("commodity_id").innerHTML;
	document.getElementById("main_image").src="/static/images/single5_"+commodity_id+".png";
	document.getElementById("edition").innerHTML = document.getElementById("edition_5").innerHTML;
	document.getElementById("edition_id").innerHTML = '5';
}

function Add_to_Shopping_Cart(){
	var commodity_id = document.getElementById('commodity_id').innerHTML;
	var is_login = localStorage.is_login;
	if(!Number(is_login)){
		alert("请您先登录！");
		return;
	}
	
	var account = localStorage.account;
	var edition = document.getElementById("edition").innerHTML;			//得到添加购物车的版本版本id(版本id主要用于图片显示)
	var edition_id = document.getElementById("edition_id").innerHTML;
	
	// 创建一个http请求对象
    var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			alert(xmlhttp.responseText)
		}
	}
    xmlhttp.open('GET', '/shopping_cart/?type=create&commodity_id='+commodity_id+'&account='+account+'&edition='+edition+'&edition_id='+edition_id, true);
    xmlhttp.send();
}

function Buy(){
	var is_login = localStorage.is_login;			
	if(!Number(is_login)){
		alert("请您先登录！");
		return;
	}
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			alert(xmlhttp.responseText)
		}
	}
    
	var account = localStorage.account;
	
	var now = new Date();		//获取当前时间，用于订单号生成
	var commodity_id = document.getElementById('commodity_id').innerHTML;
	var edition_id = document.getElementById('edition_id').innerHTML;
	var edition = document.getElementById('edition').innerHTML;
	var trade_id = String(now.getFullYear()) + String(now.getMonth()+1) + String(now.getDate()) + String(now.getHours()) + String(now.getMinutes()) + String(now.getSeconds()) + commodity_id + edition_id;
	var get = '/trade/?type=create_2&commodity_id='+commodity_id+'&edition_id='+edition_id+'&edition='+edition+'&number=1&trade_id='+trade_id+'&account='+account;
	xmlhttp.open('GET', get, true);
	xmlhttp.send();
}
