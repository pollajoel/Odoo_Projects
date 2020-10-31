window.addEventListener('load', function () {


   



$('#invalidCheck2').change(function() {
	
	
        if(this.checked) {
		   $("#typenomentreprise").css("display","block");
		   $("#typecivilite").css("display","none");
        }else{
			$("#typenomentreprise").css("display","none");
		    $("#typecivilite").css("display","block")
		}
		
		
            
    });
	
	
	
	
	
	//gestion du bouton checkbox  ( pour accepter les conditions de confidentialités )
	$('#confidentialite_engagement').change(function() {
		
				if(this.checked){ 
				
				$('#sengagerid').removeAttr('disabled');  
						
				}else{
					
				$('#sengagerid').attr("disabled", "disabled");
						
				}
			
			
			
		});




	$('#customCheck9').change(function() {

				if(this.checked){

				$('#donnerId').removeAttr('disabled');

				}else{

				$('#donnerId').attr("disabled", "disabled");

				}



		});







		
		

	
	





});  