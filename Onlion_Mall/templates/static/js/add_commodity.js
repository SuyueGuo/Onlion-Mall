function Add_Type(){
	document.getElementById("type").value = "create";
	var name = document.getElementById("name").value;		//得到录入的商品信息，包括名字，商品id, 商品类型， 价格，版本等
	var commodity_id = document.getElementById('commodity_id').value;
	var commodity_type = document.getElementById('commodity_type').value;
	var price = document.getElementById('price').value;
	var edition = document.getElementById('edition').value;
	
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			alert(xmlhttp.responseText)
		}
	}
    xmlhttp.open('GET', '/commodity/?type=create&commodity_id='+commodity_id+'&name='+name+'&commodity_type='+commodity_type+'&price='+price+'&edition='+edition, true);	//向后台发送创建商品的请求
    xmlhttp.send();
}