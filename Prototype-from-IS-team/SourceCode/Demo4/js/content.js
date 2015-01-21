$(document).ready(function(){
  
   $("li#e1").click(function(){
	$("div#left").animate({scrollTop: $("div#evd1").offset().top}, 1000);
  });
  
   $("li#e2").click(function(){
	$("div#left").animate({scrollTop: $("div#evd2").offset().top},1000);
  });
  
   $("li#e3").click(function(){
	$("div#left").animate({scrollTop: $("div#evd3").offset().top}, 1000);
  });
  
   $("li#e4").click(function(){
	$("div#left").animate({scrollTop: $("div#evd4").offset().top}, 1000);
  });
  
   $("li#e5").click(function(){
	$("div#left").animate({scrollTop: $("div#evd5").offset().top}, 1000);
  });
  
   $("li#e6").click(function(){
	$("div#left").animate({scrollTop: $("div#evd6").offset().top}, 1000);
  });

  
  
   $("div#evd1,li#e1").mouseover(function(){
    $("div#evd1").css("background-color","E9E9E4");
    $("li#e1").css("background-color","E9E9E4");	
  });
   $("div#evd1,li#e1").mouseout(function(){
    $("div#evd1").css("background-color","#ffffff");
    $("li#e1").css("background-color","ffffff");	
  });
    
   $("div#evd2,li#e2").mouseover(function(){
    $("div#evd2").css("background-color","E9E9E4");
    $("li#e2").css("background-color","E9E9E4");	
  });
   $("div#evd2,li#e2").mouseout(function(){
    $("div#evd2").css("background-color","#ffffff");
    $("li#e2").css("background-color","ffffff");	
  });
    
   $("div#evd3,li#e3").mouseover(function(){
    $("div#evd3").css("background-color","E9E9E4");
    $("li#e3").css("background-color","E9E9E4");	
  });
   $("div#evd3,li#e3").mouseout(function(){
    $("div#evd3").css("background-color","#ffffff");
    $("li#e3").css("background-color","ffffff");	
  });
    
   $("div#evd4,li#e4").mouseover(function(){
    $("div#evd4").css("background-color","E9E9E4");
    $("li#e4").css("background-color","E9E9E4");	
  });
   $("div#evd4,li#e4").mouseout(function(){
    $("div#evd4").css("background-color","#ffffff");
    $("li#e4").css("background-color","ffffff");	
  });
 
   $("div#evd5,li#e5").mouseover(function(){
    $("div#evd5").css("background-color","E9E9E4");
    $("li#e5").css("background-color","E9E9E4");	
  });
   $("div#evd5,li#e5").mouseout(function(){
    $("div#evd5").css("background-color","#ffffff");
    $("li#e5").css("background-color","ffffff");	
  });
   $("div#evd6,li#e6").mouseover(function(){
    $("div#evd6").css("background-color","E9E9E4");
    $("li#e6").css("background-color","E9E9E4");	
  });
   $("div#evd6,li#e6").mouseout(function(){
    $("div#evd6").css("background-color","#ffffff");
    $("li#e6").css("background-color","ffffff");	
  });
});
