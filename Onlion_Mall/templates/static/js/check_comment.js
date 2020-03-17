function Comment_Management(){
	var account = localStorage.account;
	window.location.href='/comment/?type=view_comments&account='+account;    
}