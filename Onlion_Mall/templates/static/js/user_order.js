function Pay(trade_id){
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			if(show == true){
				alert(xmlhttp.responseText);
			}
			
		}
	}
    xmlhttp.open('GET', '/trade/?type=change_state&trade_id='+trade_id+'&new_state=1', true);
    xmlhttp.send();
	alert("付款成功!");
	window.location.reload(); 
}
function Remind(){
	alert("已经收到您的提醒,我们会为您尽快安排发货！");
}

function Confirm(trade_id){
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			if(show == true){
				alert(xmlhttp.responseText);
			}
			
		}
	}
    xmlhttp.open('GET', '/trade/?type=change_state&trade_id='+trade_id+'&new_state=3', true);
    xmlhttp.send();
	alert("确认成功!");
	window.location.reload(); 
}

function Cancel(trade_id){
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			if(show == true){
				alert(xmlhttp.responseText);
			}
			
		}
	}
    xmlhttp.open('GET', '/trade/?type=change_state&trade_id='+trade_id+'&new_state=6', true);
    xmlhttp.send();
	alert("订单已关闭!");
	window.location.reload(); 
}
function Delete(trade_id){
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			if(show == true){
				alert(xmlhttp.responseText);
			}
			
		}
	}
    xmlhttp.open('GET', '/trade/?type=delete&trade_id='+trade_id, true);
    xmlhttp.send();
	alert("订单已删除!");
	window.location.reload(); 
}

function Comment_Management(){
	var account = localStorage.account;
	window.location.href='/comment/?type=view_comments&account='+account;    
}