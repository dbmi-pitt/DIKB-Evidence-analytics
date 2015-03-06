function adddrug()
{ 
	var druglist=[];
	var inputtag=document.getElementById("nope");
	druglist[druglist.length]=inputtag.value;
	inputtag.value="";
	var divlist=document.getElementById("druglist").getElementsByTagName("div");
	for(var i=0;i<divlist.length;i++)
	{
		if(divlist[i].getElementsByTagName("strong")[0].innerHTML!="")
		{
			druglist[druglist.length]=divlist[i].getElementsByTagName("strong")[0].innerHTML;
		}
	}
	updatelist(druglist);
}

function updatelist(druglist)
{ 
	var divlist=document.getElementById("druglist").getElementsByTagName("div");	
	for(var i=0;i<divlist.length;i++)
	{
		divlist[i].style.display="none";
		divlist[i].getElementsByTagName("strong")[0].innerHTML="";
	}
	for(var i=0;i<druglist.length;i++)
	{
		divlist[i].style.display="block";
		divlist[i].getElementsByTagName("strong")[0].innerHTML=druglist[i];
	}
	var ht=20;
	if(druglist.length>0)
	{
		ht=20+(druglist.length-1)*17;
	}
	document.getElementById("middle").style.height=ht+"px";
}

function cleandrug()
{
	var druglist=[];
	updatelist(druglist);
	document.getElementById("main").style.display="none";
}

function deldrug(divid)
{
	var druglist=[];
	var divlist=document.getElementById("druglist").getElementsByTagName("div");
	for(var i=0;i<divlist.length;i++)
	{
		if(divlist[i].id!=divid)
		{
			if(divlist[i].getElementsByTagName("strong")[0].innerHTML!="")
			{
				druglist[druglist.length]=divlist[i].getElementsByTagName("strong")[0].innerHTML;
			}
		}
	}
	updatelist(druglist);
	if(druglist.length==0)
	{
		document.getElementById("main").style.display="none";
	}
}
function showgeneric()
{
	var genericcheck=document.getElementById("genericbox");
	if(genericcheck.checked)
	{
		var x = document.getElementsByName("generic");
		for (var i = 0; i < x.length; i++) {
			x[i].style.display="inline";
		}
	}
	else
	{
		var x = document.getElementsByName("generic");
		for (var i = 0; i < x.length; i++) {
			x[i].style.display="none";
		}
	}
}
function showbrand()
{
	var genericcheck=document.getElementById("brandbox");
	if(genericcheck.checked)
	{
		var x = document.getElementsByName("brand");
		for (var i = 0; i < x.length; i++) {
			x[i].style.display="inline";
		}
	}
	else
	{
		var x = document.getElementsByName("brand");
		for (var i = 0; i < x.length; i++) {
			x[i].style.display="none";
		}
	}	
}