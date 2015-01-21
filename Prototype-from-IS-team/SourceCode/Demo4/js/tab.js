function setTab(name,m,n){ 
	for( var i=1;i<=n;i++){ 
		var menu = document.getElementById(name+i); 
		var showDiv = document.getElementById("cont_"+name+"_"+i); 
		menu.className = i==m ?"on":""; 
		showDiv.style.display = i==m?"block":"none"; 
	} 
} 
function setSmallTab(name,m,n,z){ 
	for( var i=z;i<=n;i++){ 
		var menu = document.getElementById(name+i); 
		var showDiv = document.getElementById(name+i+"div"); 
		menu.className = i==m ?"on":""; 
		showDiv.style.display = i==m?"block":"none"; 
	} 
} 
function setVersion(name){ 
	var menu = document.getElementById(name); 
	if(menu.checked)
	{
		var showDiv = document.getElementById("prof");
		showDiv.style.display="block";
		showDiv = document.getElementById("unprof");
		showDiv.style.display="none";
		for(var i=1;i<=3;i++)
		{
			var tmp = document.getElementById("tow"+i); 
			if(tmp.className=="on")
			{
				setTab("tow",i+3,6);
			}
		}
	}
	else
	{
		var showDiv = document.getElementById("prof");
		showDiv.style.display="none";
		showDiv = document.getElementById("unprof");
		showDiv.style.display="block";
		for(var i=4;i<=6;i++)
		{
			var tmp = document.getElementById("tow"+i); 
			if(tmp.className=="on")
			{
				setTab("tow",i-3,6);
			}
		}
	}
}