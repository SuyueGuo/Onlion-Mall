function Submit(commodity_id, trade_id){
	var content = document.getElementById('content').value;
	var account = localStorage.account;
	var score = document.getElementById('score').innerHTML;
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
				alert(xmlhttp.responseText);
				window.location.href='/trade/?type=view&account='+account;    
		}
	}
    xmlhttp.open('GET', '/comment/?type=create&commodity_id='+commodity_id+'&account='+account+'&content='+content+'&score='+score+'&trade_id='+trade_id, true);
    xmlhttp.send();
}

function Score(score){
	document.getElementById('score').innerHTML = score;
}

function Comment_Management(){
	var account = localStorage.account;
	window.location.href='/comment/?type=view_comments&account='+account;    
}