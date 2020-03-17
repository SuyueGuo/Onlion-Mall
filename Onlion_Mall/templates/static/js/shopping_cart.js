function Check_Login_and_Total(){
	var is_login = localStorage.is_login;
	if (Number(is_login)) {
		document.getElementById('name_shopping_cart').removeAttribute("hidden");
		document.getElementById('register_login').setAttribute("hidden","hidden");
		//接下来是把登录信息从localstorage取出
		document.getElementById('user_name').innerHTML = localStorage.name;
	}
	else{
		alert("您还未登录，请您先登录！");
		window.location.href='/404/';
	}
}

function Change_Total(commodity_id, edition_id){
	var total_price = Number(document.getElementById(commodity_id+'_price').innerHTML) * document.getElementById(commodity_id+'_'+edition_id+'_number').value;
	document.getElementById(commodity_id+'_'+edition_id+'_total_price').innerHTML = String(total_price);
	document.getElementById(commodity_id+'_'+edition_id+'_checkbox').value = String(total_price);
}

function Calculate_Total(){
	var commodity_box = document.getElementsByName('commodity_box');
	var total_price = 0;
	for(i = 0; i < commodity_box.length; i++){
		if(commodity_box[i].checked){
			total_price = total_price + Number(commodity_box[i].value);
		}
	}
	document.getElementById('total_price').innerHTML = String(total_price);
}

function Number_Down(commodity_id, edition_id){
	var number = document.getElementById(commodity_id+'_'+edition_id+'_number').value;
	number = number - 1;
	if(number <= 0){
		Delete(commodity_id, edition_id, true);
	}
	document.getElementById(commodity_id+'_'+edition_id+'_number').value = number;
	Change_Total(commodity_id, edition_id);
	Calculate_Total();
}

function Number_Up(commodity_id, edition_id){
	var number = document.getElementById(commodity_id+'_'+edition_id+'_number').value;
	number = Number(number) + 1;
	document.getElementById(commodity_id+'_'+edition_id+'_number').value = number;
	Change_Total(commodity_id, edition_id);
	Calculate_Total();
}

function Delete(commodity_id, edition_id, show){
	var account = localStorage.account;
	// 创建一个http请求对象
    var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			if(show == true){
				alert(xmlhttp.responseText);
				window.location.href='/shopping_cart/?type=view&account='+account; 
			}
			
		}
	}
    xmlhttp.open('GET', '/shopping_cart/?type=delete&commodity_id='+commodity_id+'&account='+account+'&edition_id='+edition_id, true);
    xmlhttp.send();
}

function Choose(commodity_id, edition_id){
	var check_box = document.getElementById(commodity_id+'_'+edition_id+'_checkbox');
	if(check_box.checked == true){
		num_choose = document.getElementById('num_choose').innerHTML;
		num_choose = Number(num_choose) + 1;
		document.getElementById('num_choose').innerHTML = String(num_choose);
		
		total_price = document.getElementById('total_price').innerHTML;
		total_price = Number(total_price) + Number(document.getElementById(commodity_id+'_'+edition_id+'_total_price').innerHTML);
		document.getElementById('total_price').innerHTML = String(total_price);
	}
	else{
		num_choose = document.getElementById('num_choose').innerHTML;
		num_choose = Number(num_choose) - 1;
		document.getElementById('num_choose').innerHTML = String(num_choose);
		
		total_price = document.getElementById('total_price').innerHTML;
		total_price = Number(total_price) - Number(document.getElementById(commodity_id+'_'+edition_id+'_total_price').innerHTML);
		document.getElementById('total_price').innerHTML = String(total_price);
	}
}

function Choose_All(commodity_box_id){
	var check_box = document.getElementById(commodity_box_id);
	if(check_box.checked == true){
		var commodity_box = document.getElementsByName('commodity_box');
		var total_price = 0;
		for(i = 0; i < commodity_box.length; i++){
			commodity_box[i].checked = true;
		}
		Calculate_Total();
		document.getElementById('num_choose').innerHTML = String(commodity_box.length);	
	}
	else{
		var commodity_box = document.getElementsByName('commodity_box');
		var total_price = 0;
		for(i = 0; i < commodity_box.length; i++){
			commodity_box[i].checked = false;
		}
		Calculate_Total();
		document.getElementById('num_choose').innerHTML = String(0);	
	}
	
}

function Buy_All(){
	var is_login = localStorage.is_login;
	if(!Number(is_login)){
		alert("请您先登录！");
		return;
	}
	
    
	var account = localStorage.account;
	var commodity_box = document.getElementsByName('commodity_box');
	for(i = 0; i < commodity_box.length; i++){
		if(commodity_box[i].checked){			//查找被选中的商品，然后一个一个的生成订单
			var tmp = commodity_box[i].id.split('_');
			//alert(tmp);
			var commodity_id = tmp[0];
			var edition_id = tmp[1];
			var edition = document.getElementById(commodity_id+'_'+edition_id+'_edition').innerHTML;
			var number = document.getElementById(commodity_id+'_'+edition_id+'_number').value;
			var total_price = document.getElementById(commodity_id+'_'+edition_id+'_total_price').innerHTML;
			var now = new Date();
			var trade_id = String(now.getFullYear()) + String(now.getMonth()+1) + String(now.getDate()) + String(now.getHours()) + String(now.getMinutes()) + String(now.getSeconds()) + commodity_id + edition_id;
			//alert(now.getFullYear());
			var get = '/trade/?type=create&commodity_id='+commodity_id+'&edition_id='+edition_id+'&edition='+edition+'&number='+number+'&total_price='+total_price+'&trade_id='+trade_id+'&account='+account;
			var xmlhttp = new XMLHttpRequest();
			
			xmlhttp.open('GET', get, false);	//注意！这里第三个参数为false，表示取消异步，否则会出错
			xmlhttp.send();
			Delete(commodity_id, edition_id, false);
		}
	}
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			alert(xmlhttp.responseText)
			
		}
	}
	alert("购买成功！");
	//Calculate_Total()
	window.location.reload(); 
}
